import json

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def generate():
    X, y = make_classification(n_classes=2, n_samples=1000)

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    # extract probabilities of class 1
    probabilities = model.predict_proba(X_test)[:, 1].tolist()

    labels = y_test.tolist()

    results = [
        {"prediction": prediction, "label": label}
        for (prediction, label) in zip(probabilities, labels)
    ]

    with open("data/predictions.json", "w") as f:
        json.dump(results, f)
