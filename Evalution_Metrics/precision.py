
from BasicMetrics import true_positive, false_positive


def precision(y_true, y_pred) -> float: 

    TP = true_positive(y_true, y_pred)
    FP = false_positive(y_true, y_pred)

    precision = TP / (TP+FP)  #formulla

    return precision




l1 = [0,1,1,1,0,0,0,1]
l2 = [0,1,0,1,0,1,0,0]

print(precision(l1, l2))
