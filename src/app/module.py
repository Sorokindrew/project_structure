import gzip
import json
import statistics
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, Tuple

__all__ = "parse_logs"


def parse_logs(config: Dict) -> None:
    """Parse logs folder and generate report."""

    log_folder = Path(config["LOG_DIR"]).absolute()
    report_folder = Path(config["REPORT_DIR"]).absolute()
    file, date = get_latest(log_folder)
    table_json = read_file(file, config)
    create_report(table_json, date, report_folder)


def get_latest(log_folder: Path) -> Tuple[str, datetime]:
    max_date = None
    file = None
    for el in log_folder.iterdir():
        if not el.stem.startswith("nginx"):
            continue
        year, month, day = el.stem[-8:-4], el.stem[-4:-2], el.stem[-2:]
        date = datetime(
            year=int(year),
            month=int(month if not month.startswith("0") else month[1:]),
            day=int(day if not day.startswith("0") else day[1:]),
        )
        if not max_date:
            max_date = date
            file = el
            continue
        if date > max_date:
            max_date = date
            file = el
    return file, date


def read_file(file: str, config):
    file_path = Path.joinpath(Path(config["LOG_DIR"]).absolute(), file)
    statistic = defaultdict(list)
    total_count = 0
    time_total = 0
    if file_path.suffix == ".gz":
        with gzip.open(file_path) as f:
            for line in f:
                data = line.decode().split()
                request_time = float(data[-1])
                total_count += 1
                time_total += request_time
                statistic[data[6]].append(request_time)
    else:
        with open(file_path) as f:
            for line in f:
                data = line.split()
                request_time = float(data[-1])
                total_count += 1
                time_total += request_time
                statistic[data[6]].append(request_time)
    return _calc_statistic(statistic, total_count, time_total, config["REPORT_SIZE"])


def create_report(table, date, report_folder):
    str_date = datetime.strftime(date, "%Y.%m.%d")
    with open(Path.joinpath(report_folder, "report.html"), "r") as f:
        report = f.read()
        new = report.replace("$table_json", table)
        with open(Path.joinpath(report_folder, f"report-{str_date}.html"), "w") as nf:
            nf.write(new)


def _calc_statistic(data: Dict, total_count: int, time_total: float, qty: int) -> str:
    result = []
    for k, v in data.items():
        count = len(v)
        time_sum = sum(v)
        result.append(
            {
                "url": k,
                "count": count,
                "count_perc": round(count / total_count * 100, 3),
                "time_perc": round(time_sum / time_total * 100, 3),
                "time_sum": time_sum,
                "time_avg": round(time_sum / count, 3),
                "time_max": max(v),
                "time_med": statistics.median(v),
            }
        )
    return json.dumps(sorted(result, key=lambda x: x["time_sum"], reverse=True)[:qty])
