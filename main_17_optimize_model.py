import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, matthews_corrcoef
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC


# In practice, you will want to optimize the model's hyperparameters automatically
# For example, how many estimators should you use in a Random Forest model?
# Instead of trying different values manually, automate the process

def optimize_model(dataset, classifier, parameters):
    df = pd.read_csv(f"Dataset_{dataset}.csv")
    col_groups = df.columns[0]
    features = df.columns[1:]

    x = df.loc[:, features].to_numpy()
    y = df.loc[:, col_groups].to_numpy()

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=(1 / 3), stratify=y, random_state=0)

    # Standard Scaler will make sure the features are on the same scale
    # GridSearch CV will try every combination of parameters and find the best set
    pipe = make_pipeline(StandardScaler(), GridSearchCV(classifier, parameters))

    # The rest of the process is the same
    pipe.fit(x_train, y_train)
    y_pred = pipe.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    mcc = matthews_corrcoef(y_test, y_pred)

    print(50 * "-")
    print(dataset)
    print(classifier)
    # The best parameters found by GridSearchCV will be printed.
    print(f"Best parameters = {pipe['gridsearchcv'].best_params_}")
    print(f"Accuracy: {accuracy:.1%}")
    print(f"MCC:      {mcc:.3f}")
    print(50 * "-")


# This process is shown for both datasets and
# several different types of models with different hyperparameters to be optimized.

# It is important to remember here that the final model
# should not be tested on samples that were involved in the hyperparameter optimization process

# That is why we use StandardScaler and GridSearchCV in a pipeline and only train the pipeline on the training set

for dataset_ in ["Iris", "Wine"]:
    optimize_model(dataset=dataset_,
                   classifier=RandomForestClassifier(),
                   parameters={"n_estimators": [2, 4, 8, 16, 32, 64, 128],
                               "random_state": [0]})

    optimize_model(dataset=dataset_,
                   classifier=KNeighborsClassifier(),
                   parameters={"n_neighbors": [2, 4, 8, 16, 32],
                               "weights": ["uniform", "distance"]})

    optimize_model(dataset=dataset_,
                   classifier=SVC(),
                   parameters={"C": [10 ** i for i in range(-4, 5)],
                               "kernel": ['linear', 'rbf'],
                               "random_state": [0]})

    optimize_model(dataset=dataset_,
                   classifier=LogisticRegression(),
                   parameters={"C": [10 ** i for i in range(-4, 5)],
                               "max_iter": [1000],
                               "random_state": [0]})
