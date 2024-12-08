from pathlib import Path


class StatisticService:
    def get_statistic_by_date(self, date: str) -> str:
        data = Path.cwd().absolute().joinpath(
            "sample_project", "data"
        )
        statistic = None
        for el in data.iterdir():
            if el.stem == date:
                with open(el, "r") as f:
                    statistic = f.read()
        return statistic
