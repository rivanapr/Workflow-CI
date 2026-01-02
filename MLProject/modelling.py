import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

def main():
    X, y = load_iris(return_X_y=True)

    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=10)
        model.fit(X, y)

        mlflow.log_param("n_estimators", 10)
        mlflow.log_metric("accuracy", model.score(X, y))
        mlflow.sklearn.log_model(model, "model")

if __name__ == "__main__":
    main()
