from lib import *

def tts(X,Y,test_size):
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=test_size,random_state=42,stratify = Y)
    return x_train,x_test,y_train,y_test