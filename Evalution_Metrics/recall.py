from BasicMetrics import true_positive, false_negative



def recall(y_true, y_pred) -> float: 

    TP = true_positive(y_true, y_pred)
    FN = false_negative(y_true, y_pred)

    recall = TP / (TP + FN)  #formulla

    return recall


l1 = [0,1,1,1,0,0,0,1]
l2 = [0,1,0,1,0,1,0,0]

print(recall(l1, l2))