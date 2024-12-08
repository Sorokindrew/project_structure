FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN python -m pip install poetry==1.8.4 \
    && poetry config virtualenvs.create false \
    && poetry install --without dev
CMD ["uvicorn", "sample_project.main:app", "--host", "0.0.0.0", "--port", "8000"]

