subs= pd.read_csv('new_wtp_data.csv')

 subs= pd.DataFrame(subs['participant'])
raw_data = pd.read_csv('wtp_qualtrics.csv')
raw_data = raw_data.sort_values(by=['dem_ID'])
hello = pd.DataFrame()
for i in range(0, len(raw_data)):
    if raw_data.loc[i,'dem_ID'] in subs["participant"].values:
        hello[i] = raw_data.loc[i]
#
#
df = hello.transpose()
df = df.sort_values(by=['dem_ID'])

df.to_csv('new_pilot_quesdata.csv')
