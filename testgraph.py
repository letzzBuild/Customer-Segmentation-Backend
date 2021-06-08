
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from kmodes.kprototypes import KPrototypes
from rest_framework.response import Response
from config import PATH_TO_DATASET

# Create your views here.
def SegmentedCustomers():
    response = []
    series = [
        {"name":"cluster 0", "data" :[] },
        {"name":"cluster 1", "data" :[]},
        {"name":"cluster 2", "data" :[]},
        {"name":"cluster 3", "data" :[]},
        {"name":"cluster 4", "data" :[]}   
    ]
    df = pd.read_csv(PATH_TO_DATASET)
    df = df.drop(['CustomerID'],axis = 1)
    df = df.drop(['Profession'],axis = 1)
    df = df.drop(['location'],axis = 1)
    df = df.drop(['Family_Size'],axis = 1)
    df = df.drop(['Total'],axis = 1)
    df = df.drop(['email_id'],axis = 1)
    df_array = np.array(df)
    kproto = KPrototypes(n_clusters=5, verbose = 2, max_iter = 20)
    clusters = kproto.fit_predict(df_array, categorical =[0])
    cluster_dict = []
    for c in clusters:
       cluster_dict.append(c)
    df['cluster'] = cluster_dict
    temp_cordinate_list = []
    for index,data in df.iterrows():
        if data['cluster'] == 0:
            temp_cordinate_list.append(data['Age'])
            temp_cordinate_list.append(data['Spending Score (1-100)'])
            series[0]['data'].append(temp_cordinate_list)
            temp_cordinate_list = []
        elif data['cluster'] == 1:
            temp_cordinate_list.append(data['Age'])
            temp_cordinate_list.append(data['Spending Score (1-100)'])
            series[1]['data'].append(temp_cordinate_list)
            temp_cordinate_list = []   
        elif data['cluster'] == 2:
            temp_cordinate_list.append(data['Age'])
            temp_cordinate_list.append(data['Spending Score (1-100)'])
            series[2]['data'].append(temp_cordinate_list)
            temp_cordinate_list = []   
        elif data['cluster'] == 3:
            temp_cordinate_list.append(data['Age'])
            temp_cordinate_list.append(data['Spending Score (1-100)'])
            series[3]['data'].append(temp_cordinate_list)
            temp_cordinate_list = []
        else:
            temp_cordinate_list.append(data['Age'])
            temp_cordinate_list.append(data['Spending Score (1-100)'])
            series[4]['data'].append(temp_cordinate_list)
            temp_cordinate_list = []                  
    print(series)

SegmentedCustomers()
