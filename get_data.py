import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.utils import shuffle

def get_data():
    #read data
    data = pd.read_csv('data/train.csv')
    # print(data.shape)

    #parse pickup date
    pickup = data["pickup_datetime"].apply(lambda x:datetime.strptime(x,"%Y-%m-%d %H:%M:%S"))
    pickup_month = pickup.dt.month
    pickup_date = pickup.dt.date
    pickup_hour = pickup.dt.hour
    pickup_minute = pickup.dt.minute
    pickup_second = pickup.dt.second

    #prepare data
    input = {'month':pickup_month,'date':pickup_date,'hour':pickup_hour, 'minute':pickup_minute, 'second':pickup_second}
    input_data = pd.DataFrame(input)
    input_data = input_data.join(data.drop(['id','pickup_datetime','dropoff_datetime','store_and_fwd_flag'],axis=1))
    #
    input_data = shuffle(input_data)

    return input_data.drop(['trip_duration']), input_data['trip_duration']