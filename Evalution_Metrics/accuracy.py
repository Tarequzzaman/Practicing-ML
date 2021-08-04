
from BasicMetrics import true_positive, true_negative, false_negative, false_positive


def accuracy(y_true, y_pred) -> float: 

    TP = true_positive(y_true, y_pred)
    TN = true_negative(y_true, y_pred)
    FP = false_positive(y_true, y_pred)
    FN = false_negative(y_true, y_pred)

    accuracy = (TP + TN)/(TP + TN + FP + FN)

    return accuracy




l1 = [0,1,1,1,0,0,0,1]
l2 = [0,1,0,1,0,1,0,0]

print(accuracy(l1, l2))
