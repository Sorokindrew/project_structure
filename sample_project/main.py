import uvicorn
from fastapi import FastAPI, Depends
from starlette.responses import JSONResponse

from sample_project.infrastructure.di import get_statistic_service
from sample_project.services.statistic import StatisticService


app = FastAPI()


@app.get("/statistic")
def get_statistic(
    date: str,
    statistic_service: StatisticService = Depends(get_statistic_service),
) -> JSONResponse:
    """
    Get statistic of nginx logs.
    :param date: Required date
    :return: statistic of log
    """
    statistic = statistic_service.get_statistic_by_date(date)
    if statistic:
        return JSONResponse({"result": statistic}, status_code=200)
    return JSONResponse({"result": "nothing found"}, status_code=404)


if __name__ == "__main__":
    uvicorn.run(app)
