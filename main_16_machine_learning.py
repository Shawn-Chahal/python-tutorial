import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, matthews_corrcoef
from sklearn.model_selection import train_test_split


def train_test_model(dataset, classifier):
    df = pd.read_csv(f"Dataset_{dataset}.csv")
    col_groups = df.columns[0]
    features = df.columns[1:]

    x = df.loc[:, features].to_numpy()  # Input data
    y = df.loc[:, col_groups].to_numpy()  # Output data

    # It is important to ensure a machine learning model is not trained and tested on the same data
    # This function will take 1/3 of the data to be the test set and the remaining 2/3 will be the training set.
    # stratify=y means that both sets will have a similar distribution of the groups as the vector y
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=(1 / 3), stratify=y, random_state=0)

    print(f"x_train.shape = {x_train.shape}")
    print(f"y_train.shape = {y_train.shape}")
    print(f"x_test.shape = {x_test.shape}")
    print(f"y_test.shape = {y_test.shape}")

    # Fit (i.e., train) a machine learning classifier model on the training set
    classifier.fit(x_train, y_train)

    # Use the model to predict the label of samples in the test set
    y_pred = classifier.predict(x_test)

    # Evaluate the accuracy and MCC score
    accuracy = accuracy_score(y_test, y_pred)
    mcc = matthews_corrcoef(y_test, y_pred)

    print(50 * "-")
    print(dataset)
    print(classifier)
    print(f"Accuracy: {accuracy:.1%}")
    print(f"MCC:      {mcc:.3f}")
    print(50 * "-")


# In this example, a Random forest model will be trained and tested.
train_test_model("Iris", RandomForestClassifier(n_estimators=5, random_state=0))
train_test_model("Wine", RandomForestClassifier(n_estimators=100, random_state=0))
