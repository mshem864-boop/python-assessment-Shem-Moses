

Task 10: Machine Learning with Scikit-Learn - KNN & Naive Bayes

Dataset: Iris (built into scikit-learn, no download needed).
"""

# a. Install scikit-learn first, from the terminal:
#       pip install scikit-learn
import sklearn
print("a. scikit-learn version:", sklearn.__version__)

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

# b. Load dataset with Pandas, show first 5 rows
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target
print("\nb. First 5 rows of the Iris dataset:")
print(df.head())

# c. Features (X) and labels (y), train/test split
X = df.drop(columns=["target"])
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# d. KNN: instantiate, fit, predict
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
knn_predictions = knn.predict(X_test)

# e. KNN: accuracy and classification report
print("\ne. KNN accuracy:", accuracy_score(y_test, knn_predictions))
print("KNN classification report:\n",
      classification_report(y_test, knn_predictions))

# f. Mathematics behind KNN (written explanation)
"""
f. How KNN works:

KNN classifies a new point by looking at the 'k' closest points in the
training data and taking a majority vote of their labels.

"Closest" is usually measured using the Euclidean distance between two
points p = (p1, p2, ..., pn) and q = (q1, q2, ..., qn):

    distance(p, q) = sqrt( (p1-q1)^2 + (p2-q2)^2 + ... + (pn-qn)^2 )

Choosing k:
- A small k (e.g. k=1) is sensitive to noise/outliers (overfitting).
- A large k smooths out predictions but can blur the boundary between
  classes (underfitting), and can be biased toward the majority class.
- k is often chosen by testing a range of odd values (to avoid ties in
  binary classification) and picking the one with the best validation
  accuracy. Here we used k=3 as a reasonable starting point.
"""

# g. Naive Bayes: instantiate, fit, predict
nb = GaussianNB()
nb.fit(X_train, y_train)
nb_predictions = nb.predict(X_test)

# h. Naive Bayes: accuracy and confusion matrix
print("\nh. Naive Bayes accuracy:", accuracy_score(y_test, nb_predictions))
print("Naive Bayes confusion matrix:\n",
      confusion_matrix(y_test, nb_predictions))

# i. Mathematics behind Naive Bayes (written explanation)
"""
i. How Naive Bayes works:

Naive Bayes uses Bayes' theorem to compute the probability of each class
given the observed features, and picks the class with the highest
probability.

Bayes' theorem:

    P(class | features) = ( P(features | class) * P(class) ) / P(features)

It is called "naive" because it assumes the features are conditionally
independent of each other given the class - i.e.

    P(features | class) = P(feature_1 | class) * P(feature_2 | class)
                           * ... * P(feature_n | class)

Since P(features) is the same for every class when comparing them, the
model simply picks the class that maximises:

    P(class) * P(feature_1 | class) * P(feature_2 | class) * ...

GaussianNB assumes each feature follows a normal (Gaussian) distribution
within each class, and uses that to estimate P(feature_i | class).
"""

if __name__ == "__main__":
    print("\nTask 10 complete: KNN and Naive Bayes both trained and "
          "evaluated on the Iris dataset.")
