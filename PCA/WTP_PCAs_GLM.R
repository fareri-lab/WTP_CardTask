#set working directory

data <- read.csv(file = '/Users/melanieruiz/Google Drive/My Drive/WTP_data/WTP_LONG_ALL.csv')

# load LMER libraries
library(lme4)
library(lmerTest)

# PC1 LMER model in R
PC1<-lmer('exp_chosen ~ PC1  + (1|subid)', data=data)
summary(PC1)



# PC1/PC2 LMER model in R
PC1_2<-lmer('exp_chosen ~ PC1 + PC2 + (1|subid)', data=data)
summary(PC1_2)

# PC1/PC2/PC3 LMER model in R
PC1_2_3<-lmer('exp_chosen ~ PC1 + PC2 + PC3 + (1|subid)', data=data)
summary(PC1_2_3)

