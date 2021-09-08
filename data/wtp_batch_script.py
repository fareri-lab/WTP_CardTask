#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:11:00 2021

@author: melziur
"""

#import libraries

from pathlib import Path
from collections import namedtuple
import pandas as pd 

#create file namedtuple


File = namedtuple('File', 'participant avg_spent_social avg_spent_nonsocial total_spent_social total_spent_nonsocial prop_social prop_nonsocial moresocial prop_moresocial')


#create empty list


files = []

#create starting path
p = Path('/Users/mruiz/Desktop/new_wtp_data/data')

for item in p.glob("**/*"):
    if item.suffix in ['.csv']:
        subfile = item.name
        sub = pd.read_csv('data/%s' %subfile,encoding='latin1')
        exp_sheet = pd.read_csv('/Users/mruiz/Desktop/wtp_data/experiences.csv')
        nonsoc_exp= pd.DataFrame(exp_sheet['nonsocial_exp'])
        soc_exp = pd.DataFrame(exp_sheet['social_exp'])
        cols= ['participant','responses.keys', 'Left','Right', 'leftmoney', 'rightmoney', 'social_left', 'decision_price']
        new_df = sub[cols]
        new_df = new_df.dropna()
        new_df = new_df.reset_index()
        del new_df['index']
        
        
        
        
        new_df['avg_spent_social'] = ''
        new_df['avg_spent_nonsocial']= ''
        new_df['total_spent_social'] = ''
        new_df['total_spent_nonsocial']= ''
        new_df['prop_social'] = ''
        new_df['prop_nonsocial'] = ''
        new_df['exp_type2'] = 0
        new_df['choicespent'] = ''
        new_df['moresocial'] = ''
        new_df['prop_moresocial'] = ''
        
        social_choice = []
        nonsocial_choice= []
        social_exptype= []
        nonsocial_exptype= []
        
        for i in range(0,len(new_df)):
            if new_df.loc[i,'responses.keys'] == 2 and new_df.loc[i,'social_left'] == 0:
                new_df['exp_type2'][i] = 1
            elif new_df.loc[i,'responses.keys'] == 1 and new_df.loc[i,'social_left'] == 1:
                new_df['exp_type2'][i] = 1
            elif new_df.loc[i,'responses.keys'] == 1 and new_df.loc[i,'social_left'] == 0:
                new_df['exp_type2'][i] = 0
            elif new_df.loc[i,'responses.keys'] == 2 and new_df.loc[i,'social_left'] == 1:
                new_df['exp_type2'][i] = 0
        new_df['total_soc'] = sum(new_df['exp_type2'])

        for i in range(0,len(new_df)):

            if new_df.loc[i,'exp_type2'] == 1:
                social_choice.append(new_df.loc[i,'decision_price'])
                social_exptype.append(soc_exp.loc[i,'social_exp'])
            elif new_df.loc[i,'exp_type2'] == 0:
                nonsocial_choice.append(new_df.loc[i,'decision_price'])
                nonsocial_exptype.append(nonsoc_exp.loc[i,'nonsocial_exp'])

        for i in range(0,len(new_df)):
            if new_df.loc[i,'prop_social'] > new_df.loc[i,'prop_nonsocial']:
                new_df['prop_moresocial'][i] = 1
            else:
                new_df['prop_moresocial'][i] = 0 
                 
                
        print(new_df['participant'])
        new_df['avg_spent_social'] = sum(social_choice)/len(social_choice)
        new_df['avg_spent_nonsocial'] = sum(nonsocial_choice)/len(nonsocial_choice)
        new_df['total_spent_social'] = sum(social_choice)
        new_df['total_spent_nonsocial'] = sum(nonsocial_choice)
        new_df['prop_social'] = len(social_choice)/len(new_df)
        new_df['prop_nonsocial'] = len(nonsocial_choice)/len(new_df)
         
           
        for i in range(0,len(new_df)):
            if new_df.loc[i,'avg_spent_social'] > new_df.loc[i,'avg_spent_nonsocial']:
                new_df['moresocial'][i] = 1
            else:
                new_df['moresocial'][i] = 0
                
        for i in range(0,len(new_df)):
            if new_df.loc[i,'prop_social'] > new_df.loc[i,'prop_nonsocial']:
                new_df['prop_moresocial'][i] = 1
            else:
                new_df['prop_moresocial'][i] = 0
        
        #prop_allmoresocials = pd.DataFrame()
        #for i in range(0,len(newsubs)):
        #    if newsubs.loc[i,'moresocial'] ==1:
        #       prop_allmoresocials[i] = newsubs.loc[i]
        
        participant = new_df['participant'][1]
        avg_spent_social = new_df['avg_spent_social'][1]
        avg_spent_nonsocial = new_df['avg_spent_nonsocial'][1]
        total_spent_social = new_df['total_spent_social'][1]
        total_spent_nonsocial = new_df['total_spent_nonsocial'][1]
        prop_social = new_df['prop_social'][1]
        prop_nonsocial = new_df['prop_nonsocial'][1]
        moresocial = new_df['moresocial'][1]
        prop_moresocial = new_df['prop_moresocial'][1]
        files.append(File(participant,avg_spent_social,avg_spent_nonsocial,total_spent_social,total_spent_nonsocial,prop_social,prop_nonsocial, moresocial, prop_moresocial))


df= pd.DataFrame(files)
df = df.sort_values(by=['participant'])
df.to_csv('updated_allwtp.csv', index=False)



#prop_allmoresocials = pd.DataFrame()
#for i in range(0,len(newsubs)):
#    if newsubs.loc[i,'moresocial'] ==1:
#        prop_allmoresocials[i] = newsubs.loc[i]
#prop_allmoresocials = prop_allmoresocials.transpose()#
##
#prop_allmoresocials.to_csv('prop_allmoresocials.csv')