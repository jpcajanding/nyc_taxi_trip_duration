import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

from get_data import get_data

data, labels = get_data()

train_data, test_data, train_labels, test_labels = train_test_split(data,labels,train_size=0.7,shuffle=True)

