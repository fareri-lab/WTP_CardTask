#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:45:56 2021

@author: melziur
"""


#scoring script for the Autism Quotient (AQ): scoring instrctions detailed here: https://www.queensu.ca/rarc/sites/webpublish.queensu.ca.rarcwww/files/files/services/ASDAssessmentTemplate/AAA/AQ_Scoring_Key.pdf


#subs= pd.read_csv('new_pilot_wtp.csv')
#
#subs= pd.DataFrame(subs['participant'])
#
#hello = pd.DataFrame()
#for i in range(0, len(new_alldata)):
#    if new_alldata.loc[i,'dem_ID'] in subs["participant"].values:
#        hello[i] = new_alldata.loc[i]
#        
#
#df = hello.transpose()
#
#df.to_csv('new_pilot_quesdata.csv')


import pandas as pd



#alldata = pd.read_excel("ALL_wtp_quesdata.xlsx" , index=False)
alldata = pd.read_csv('new_pilot_quesdata.csv')
alldata.pop("attnchk")
alldata = alldata.sort_values(by=['dem_ID']) 
aq_cols = [col for col in alldata.columns if 'AQ_' in col]
print(list(alldata.columns))
print(aq_cols)

aq = alldata.filter(regex='AQ_')
print(aq)

aq_score = pd.DataFrame(columns=aq_cols, index=aq.index)
aq_score.iloc[0] = aq.iloc[0]


#reverse score: 2, 4, 5, 6, 7, 9, 12, 13, 16, 18, 19, 20, 21, 22, 23, 26, 33, 35, 39, 41, 42, 43, 45, and 46.
reverse_score= [2, 4, 5, 6, 7, 9, 12, 13, 16, 18, 19, 20, 21, 22, 23, 26, 33, 35, 39, 41, 42, 43, 45, 46]
#for i in len(range(1,17)): 

#for k,i in reverse_score:
#    if k in aq_cols:
# print(i)
for k in range(0,len(aq)):
    for i in range (1,len(aq.columns)+1):
        if i in reverse_score:
            if aq.loc[k,'AQ_'+ str(i)] == 1 or aq.loc[k,'AQ_'+ str(i)] == 2:
                aq_score['AQ_' +str(i)][k] = 1
            else:
                aq_score['AQ_'+str(i)][k] = 0
        else:
            if aq.loc[k,'AQ_'+ str(i)] == 3 or aq.loc[k,'AQ_'+ str(i)] == 4:
                aq_score['AQ_' +str(i)][k] = 1
            else:
                aq_score['AQ_'+str(i)][k] = 0




aq_score["AQ_score"] = aq_score.sum(axis=1)


         
aq_score.insert (0, "prolific_ID", alldata["dem_ID"])       
aq_score.to_csv("wtp_aq_scores.csv" , index=False)

#ALLalldata = pd.read_excel(r'wtp_taskdata_NEW.xlsx')
#ALLalldata = pd.read_csv(r'new_pilot_wtp.csv')
ALLalldata = pd.read_csv(r'updated_allwtp.csv')
ALLalldata['AQ'] = aq_score["AQ_score"]
ALLalldata.to_csv("updated_allwtp.csv")
#ALLalldata.to_excel("wtp_taskdata_NEW.xlsx" , index=False)