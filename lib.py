from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import cv2
import pickle
import numpy as np
import h5py
import tensorflow as tf
import time

import warnings
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout, Flatten,Activation
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from tqdm import tqdm
import tensorflow as ts 
from tensorflow.keras.callbacks import ReduceLROnPlateau
import random as rn
from tensorflow.keras.optimizers import Adam,SGD,Adagrad,Adadelta,RMSprop
print(tf.__version__)
from tensorflow.keras.callbacks import *
import glob
np.random.seed(42)
rn.seed(42)
tf.random.set_seed(42)