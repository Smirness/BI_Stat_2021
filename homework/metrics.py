import numpy as np


def binary_classification_metrics(y_pred, y_true):
    """
    Computes metrics for binary classification
    Arguments:
    y_pred, np array (num_samples) - model predictions
    y_true, np array (num_samples) - true labels
    Returns:
    precision, recall, f1, accuracy - classification metrics
    """

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score

    p = np.unique(y_true)[0]
    n = np.unique(y_true)[1]

    tp, fp, tn, fn = 0, 0, 0, 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            if y_true[i] == p:
                tp += 1
            elif y_true[i] == n:
                tn += 1
        elif y_true[i] != y_pred[i]:
            if y_true[i] == p:
                fn += 1
            elif y_true[i] == n:
                fp += 1

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = (2 * tp) / (2 * tp + fp + fn)
    accuracy = (tp + tn) / (tp + fp + tn + fn)

    return precision, recall, f1, accuracy
    pass


def multiclass_accuracy(y_pred, y_true):
    """
    Computes metrics for multiclass classification
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true labels
    Returns:
    accuracy - ratio of accurate predictions to total samples
    """
    p,f = 0, 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            p += 1

        elif y_true[i] != y_pred[i]:
            f += 1

    accuracy = p / (p + f)

    return accuracy
    pass


def r_squared(y_pred, y_true):
    """
    Computes r-squared for regression
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true values
    Returns:
    r2 - r-squared value
    """
    numerator = ((y_true - y_pred) ** 2).sum()
    denominator = ((y_true - np.average(y_true)) ** 2).sum()

    return 1 - numerator/denominator
    pass


def mse(y_pred, y_true):
    """
    Computes mean squared error
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true values
    Returns:
    mse - mean squared error
    """
    return np.average((y_true - y_pred) ** 2)
    pass


def mae(y_pred, y_true):
    """
    Computes mean absolut error
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true values
    Returns:
    mae - mean absolut error
    """
    return np.average(np.abs(y_pred - y_true))
    pass
    