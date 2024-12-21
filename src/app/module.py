import gzip
import time
import json
from datetime import datetime
from pathlib import Path


def get_latest():
    max_date = None
    file = None
    for el in Path.joinpath(Path.cwd(), 'src', 'log_dir').iterdir():
        year, month, day = el.stem[-8:-4],el.stem[-4:-2],el.stem[-2:]
        date = datetime(year=int(year),
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
    return file


def read_file(file):
    file_path = Path.joinpath(Path.cwd(), 'src', 'log_dir', file)
    if file_path.suffix == ".gz":
        with gzip.open(file_path) as f:
            line = f.readline()
            print(line)
    else:
        with open(file_path) as f:
            line = f.readline()
            print(line)
