# Python Tutorial

## About

This is a quick tutorial I made to showcase the basics of Python and some core data science libraries.

Start by running `main_00_generate_datasets.py` to download the datasets used in this tutorial.

The actual tutorial starts with `main_01_data_types.py`. I highly recommend following the tutorial in order.

## Requirements

This tutorial uses Python 3.10.14 and the following libraries:

```requirements
matplotlib==3.8.0
numpy==1.26.4
pandas==2.2.1
scikit-learn==1.3.0
scipy==1.12.0
statsmodels==0.14.0
```

# Additional Resources

## numpy

* [Statistics (E.g., mean, standard deviation, etc)](https://numpy.org/doc/stable/reference/routines.statistics.html)
* [Mathematical functions](https://numpy.org/doc/stable/reference/routines.math.html)

## pandas

* [Import a csv file](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
* [Export a csv file](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html)
* [Access a single value from a DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html)
* [Access a group of rows and columns from a DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)
* [Perform stats or math on a DataFrame by groups](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)
* [Create a DataFrame from a dictionary](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html)

## scipy

* [Statistical tests (E.g., one-way ANOVA, Tukey's HSD test, etc.)](https://docs.scipy.org/doc/scipy/reference/stats.html#independent-sample-tests)

## statsmodels

* [Two-way ANOVA](https://www.statsmodels.org/dev/examples/notebooks/generated/interactions_anova.html#Two-way-ANOVA)

## matplotlib

* [Examples](https://matplotlib.org/stable/gallery/index.html)
* [Scatter plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)
* [Line plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
* [Colors](https://matplotlib.org/stable/gallery/color/named_colors.html)
* [Markers](https://matplotlib.org/stable/api/markers_api.html)

## scikit-learn

* [Examples](https://scikit-learn.org/stable/auto_examples/index.html)

* Preprocessing:
    * [Standardization](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

* Dimensionality reduction:
    * [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
    * [t-SNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)

* Machine learning classifiers:
    * [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
    * [Support Vector Machine](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
    * [k-Nearest Neighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
    * [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

* Hyperparameter optimization:
    * [Grid Search CV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
    * [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html)

* Model validation:
    * [Train-Test-Split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
    * [Metrics (E.g., Accuracy, MCC, etc.)](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics)



