from lib import *

def normalize(X,Z):
    le=LabelEncoder()
    Y=le.fit_transform(Z)
    Y=to_categorical(Y,2)
    X=np.array(X)
    X=X/255.0
    return X,Y