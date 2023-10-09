
##
setwd("/Users/dfareri/Dropbox/Dominic/Github/fareri-lab/WTP_CardTask/PCA")

data_ddm<-read.csv(file='WTP_3colsonly_allsubs.csv',header=TRUE,sep=',')
data_ddm2<-data_ddm
#recode choices, 1 = social 2 = non-social
data_ddm2$exp_chosen[data_ddm2$exp_chosen==0]<-2


colnames(data_ddm2)[2]="subjID"
colnames(data_ddm2)[3]="choice"
colnames(data_ddm2)[4]="RT"
data_ddm2[data_ddm2$RT>8,]
data_ddm2[data_ddm2$RT<0.3,]

mel_ddm<-choiceRT_ddm(data=data_ddm3,niter=5000,nwarmup=1000,nchain=4,ncore=6)



