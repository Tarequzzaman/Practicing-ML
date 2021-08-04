
'''
You can remember TP(true_positive), TN(true_nagative), FP(False Positive), FN(False Negative) by a tchnics

             We assume that   the last word is Always Appair on the Prediction
                  positive -> 1
                  Negative -> 0 


And the First word (True/False) depend on the last word

True is same as the last word (Positive/ Negative)
False is the opposite of last word(Positive/ Negative)

so true positive means: since last word is positive so y_pred = 1 and the fast word is true so we keep y_true as same as te last word = 1

       y_pred = 1
       y_true = 1


   true negative 
       y_pred = 0
       y_ture = 1


   false negative 
      y_pred = 0 
      y_true = 1

   


'''



def true_positive(y_true, y_pred)-> int:
    count = 0
    for x, y in zip(y_true, y_pred):
        if x == 1 and y == 1:
            count = count  + 1 
    return count


def true_negative(y_true, y_pred) -> int: 
    count = 0 
    for x, y in zip(y_true, y_pred):
        if x == 0 and y == 0:
            count = count  + 1 
    return count

def false_positive(y_true, y_pred) -> int: 
    count = 0 
    for x, y in zip(y_true, y_pred):
        if x == 0 and y == 1:
            count = count  + 1 
    return count



def false_negative(y_true, y_pred) -> int: 
    count = 0 
    for x, y in zip(y_true, y_pred):
        if x == 1 and y == 0:
            count = count  + 1 
    return count




yt = [ 1, 0, 0, 1 , 1]
yp = [ 1, 1, 0, 0,  1]


print(true_positive(yt, yp))
