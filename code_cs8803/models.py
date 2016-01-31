import numpy as np
from sklearn.datasets import load_svmlight_file
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import *

import utils


# input: X_train, Y_train and X_test
# output: Y_pred
def logistic_regression_pred(X_train, Y_train, X_test):
    # TODO: train a logistic regression classifier using X_train and Y_train. Use this to predict labels of X_test
    # use default params for the classifier
    lr_model = LogisticRegression(random_state=545510477)
    lr_model.fit(X_train, Y_train)
    Y_pred = lr_model.predict(X_test)
    return Y_pred


# input: X_train, Y_train and X_test
# output: Y_pred
def svm_pred(X_train, Y_train, X_test):
    # TODO:train a SVM classifier using X_train and Y_train. Use this to predict labels of X_test
    # use default params for the classifier
    svm_model = LinearSVC(random_state=545510477)
    svm_model.fit(X_train, Y_train)
    Y_pred = svm_model.predict(X_test)
    return Y_pred


# input: X_train, Y_train and X_test
# output: Y_pred
def decisionTree_pred(X_train, Y_train, X_test):
    # TODO:train a logistic regression classifier using X_train and Y_train. Use this to predict labels of X_test
    # IMPORTANT: use max_depth as 5. Else your test cases might fail.
    dt_model = DecisionTreeClassifier(max_depth=5, random_state=545510477)
    dt_model.fit(X_train, Y_train)
    Y_pred = dt_model.predict(X_test)
    return Y_pred


# input: Y_pred,Y_true
# output: accuracy, auc, precision, recall, f1-score
def classification_metrics(Y_pred, Y_true):
    # TODO: Calculate the above mentioned metrics
    # NOTE: It is important to provide the output in the same order
    accuracy = accuracy_score(Y_true, Y_pred)
    auc_score = roc_auc_score(Y_true, Y_pred)
    precision = precision_score(Y_true, Y_pred)
    recall = recall_score(Y_true, Y_pred)
    f1 = f1_score(Y_true, Y_pred)
    return accuracy, auc_score, precision, recall, f1


# input: Name of classifier, predicted labels, actual labels
def display_metrics(classifierName, Y_pred, Y_true):
    print "______________________________________________"
    print "Classifier: " + classifierName
    acc, auc_, precision, recall, f1score = classification_metrics(Y_pred, Y_true)
    print "Accuracy: " + str(acc)
    print "AUC: " + str(auc_)
    print "Precision: " + str(precision)
    print "Recall: " + str(recall)
    print "F1-score: " + str(f1score)
    print "______________________________________________"
    print ""


def main():
    X_train, Y_train = utils.get_data_from_svmlight("../deliverables/features_svmlight.train")
    X_test, Y_test = utils.get_data_from_svmlight("../data/features_svmlight.validate")

    display_metrics("Logistic Regression", logistic_regression_pred(X_train, Y_train, X_test), Y_test)
    display_metrics("SVM", svm_pred(X_train, Y_train, X_test), Y_test)
    display_metrics("Decision Tree", decisionTree_pred(X_train, Y_train, X_test), Y_test)


if __name__ == "__main__":
    main()
