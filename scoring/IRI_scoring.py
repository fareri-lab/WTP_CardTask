#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:53:21 2021

@author: mruiz
"""





#alldata = pd.read_excel("ALL_wtp_quesdata.xlsx" , index=False)
#%% 
import pandas as pd
alldata = pd.read_csv('new_pilot_quesdata.csv')
alldata.pop("attnchk")
alldata = alldata.sort_values(by=['dem_ID']) 
IRI_cols = [col for col in alldata.columns if 'IRI_' in col]
print(list(alldata.columns))
print(IRI_cols)

IRI_data = alldata.filter(regex='IRI_')
test= alldata.filter(regex='IRI_')
print(IRI_data)

IRI_score = pd.DataFrame(columns=IRI_cols, index=IRI_data.index)
#IRI_score.iloc[0] = IRI.iloc[0]

#%%
#reverse score: 2, 4, 5, 6, 7, 9, 12, 13, 16, 18, 19, 20, 21, 22, 23, 26, 33, 35, 39, 41, 42, 43, 45, and 46.
f_s= [1,5,7,12,16,23,26] #fantasy scale
e_c= [2,4,9,14,18,20,22]
p_t= [3,8,11,15,21,25,28]
p_d= [6,10,13,17,19,24,27]

reverse_score= [3,4,7,12,13,14,15,18,19]
resp_fs = pd.DataFrame()
resp_ec = pd.DataFrame()
resp_pt = pd.DataFrame()
resp_pd = pd.DataFrame()
#for i in len(range(1,17)): 
#%%


#for k,i in reverse_score:
#    if k in IRI_cols:
# print(i)
for k in range(0,len(IRI_data)):
    for i in range (1,len(IRI_data.columns)+1):
        
        #recode data to 0-4 scale
        if IRI_data.loc[k,'IRI_'+str(i)] == 1:
            IRI_score['IRI_' +str(i)][k] = 0
            test['IRI_' +str(i)][k] = 0
        elif IRI_data.loc[k,'IRI_'+str(i)] == 2:
            IRI_score['IRI_' +str(i)][k] = 1
            test['IRI_' +str(i)][k] = 1
        elif IRI_data.loc[k,'IRI_'+str(i)] == 3:
            IRI_score['IRI_' +str(i)][k] = 2
            test['IRI_' +str(i)][k] = 2
        elif IRI_data.loc[k,'IRI_'+str(i)] == 4:
            IRI_score['IRI_' +str(i)][k] = 3
            test['IRI_' +str(i)][k] = 3
        elif IRI_data.loc[k,'IRI_'+str(i)] == 5:
            IRI_score['IRI_' +str(i)][k] = 4
            test['IRI_' +str(i)][k] = 4 
        if i in reverse_score:
            if IRI_score.loc[k,'IRI_'+ str(i)] == 0:
                IRI_score['IRI_' +str(i)][k] = 4
            elif IRI_score.loc[k,'IRI_'+str(i)] == 1:
                IRI_score['IRI_' +str(i)][k] = 3
            elif IRI_score.loc[k,'IRI_'+str(i)] == 2:
                IRI_score['IRI_' +str(i)][k] = 2
            elif IRI_score.loc[k,'IRI_'+str(i)] == 3:
                IRI_score['IRI_' +str(i)][k] = 1
            elif IRI_score.loc[k,'IRI_'+str(i)] == 4:
                IRI_score['IRI_' +str(i)][k] = 0
#%%
for k in range(0,len(IRI_score)):
    for i in range (1,len(IRI_data.columns)+1):
        if i in f_s:
           resp_fs['IRI_' +str(i)] = IRI_score['IRI_' +str(i)]
        elif i in e_c:
           resp_ec['IRI_' +str(i)] = IRI_score['IRI_' +str(i)]
        elif i in p_t:
           resp_pt['IRI_' +str(i)] = IRI_score['IRI_' +str(i)]
        elif i in p_d:
           resp_pd['IRI_' +str(i)] = IRI_score['IRI_' +str(i)]
          
 

IRI_score["IRI_total"] = IRI_score.sum(axis=1)
IRI_score["IRI_FS"]= resp_fs.sum(axis=1)
IRI_score["IRI_EC"]= resp_ec.sum(axis=1)
IRI_score["IRI_PD"]= resp_pd.sum(axis=1)
IRI_score["IRI_PT"]= resp_pt.sum(axis=1)
IRI_score.insert (0, "prolific_ID", alldata["dem_ID"])       
IRI_score.to_csv("wtp_IRI_scores.csv" , index=False)
##
#
##Insert task data file here
##pd.read_excel(r'wtp_taskdata_NEW.xlsx')
complete_data = pd.read_csv(r'new_wtp_data.csv')
complete_data['IRI_total'] = IRI_score["IRI_total"]
complete_data["IRI_FS"]= IRI_score["IRI_FS"]
complete_data["IRI_EC"]= IRI_score["IRI_EC"]
complete_data["IRI_PD"]= IRI_score["IRI_PD"]
complete_data["IRI_PT"]= IRI_score["IRI_PT"]
complete_data.to_csv('new_wtp_data.csv', index=False)
#.to_excel("wtp_taskdata_NEW.xlsx" , index=False)
