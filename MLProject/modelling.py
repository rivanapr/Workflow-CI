import mlflow

with mlflow.start_run():
    mlflow.log_param("model", "dummy")
    mlflow.log_metric("accuracy", 0.8)
