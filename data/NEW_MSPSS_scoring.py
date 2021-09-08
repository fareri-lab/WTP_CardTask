#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:02:45 2021

@author: melziur
"""



import pandas as pd

alldata = pd.read_csv('new_pilot_quesdata.csv')
alldata.pop("attnchk")
alldata = alldata.sort_values(by=['dem_ID'])
alldata = alldata.reset_index(drop=True)
MSPSS_cols = [col for col in alldata.columns if 'MSPSS_' in col]
print(list(alldata.columns))
print(MSPSS_cols)

mspss = alldata.filter(regex='MSPSS_')
print(mspss)

MSPSS_score = pd.DataFrame(columns=MSPSS_cols, index=mspss.index)
MSPSS_score.iloc[0] = mspss.iloc[0]


for k in range(0,len(mspss)):
    for i in range (1,len(mspss.columns)+1):

        MSPSS_score['MSPSS_' +str(i)][k] = mspss.loc[k,'MSPSS_'+ str(i)]

#MSPSS_score = MSPSS_score.drop(labels=[0], axis=0)
#MSPSS_score = MSPSS_score.reset_index(drop=True)
#MSPSS_score = MSPSS_score.astype(int)
#MSPSS_score = MSPSS_score.apply(pd.to_numeric, errors='ignore')
MSPSS_score["total_score"] = MSPSS_score.sum(axis=1)/12

#alldata = alldata.drop(labels=[0], axis=0)
#MSPSS_score.insert (0, "Random_ID", alldata['dem_ID'])  
#MSPSS_score["total_score"][0] = 'MSPSS Total'

         
    
MSPSS_score.to_csv("MSPSS_scores.csv" , index=False)

#pd.read_csv(r'new_pilot_wtp.csv')
complete_data = pd.read_csv(r'updated_allwtp.csv')
complete_data['MSPSS'] = MSPSS_score["total_score"]
complete_data.to_csv('updated_allwtp.csv', index=False)