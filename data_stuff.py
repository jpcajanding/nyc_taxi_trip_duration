import pandas as pd
import numpy as np
import datetime import datetime

#read data
data = pd.read_csv('data/train.csv')

pickup = data["pickup_datetime"].apply(lambda x:datetime.strptime(x,"%Y-%m-%d %H:%M:%S"))

