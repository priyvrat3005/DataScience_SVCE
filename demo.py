##### We are goint to Analyse the Netflix userbase Data and will deepdive on some Stats concepts 
#### Link of the dataset - https://www.kaggle.com/datasets/riturajsingh99/netflix-userbase/discussion?sort=hotness

##### We have taken the data set from kaggle 
import numpy as np 
import pandas as pd 
df=pd.read_csv("netflix.csv")
df.head()
df.shape
df.describe()
df["Monthly Revenue"].count()
mean_val=df["Monthly Revenue"].mean()
mean_val
# from this mean value we can say the on an avg 12.5$ is paid by per user to netflix each month 
median_val=df["Monthly Revenue"].median()
median_val
mode_val=df["Monthly Revenue"].mode()

mode_val
range_of_revnue=df["Monthly Revenue"].max()-df["Monthly Revenue"].min()
range_of_revnue
variance_of_rev=df["Monthly Revenue"].var()
variance_of_rev

std_dev_of_rev=df["Monthly Revenue"].std()
std_dev_of_rev
Q1=df["Monthly Revenue"].quantile(0.25)
Q2=df["Monthly Revenue"].quantile(0.50)
Q3=df["Monthly Revenue"].quantile(0.75)



print("25% Users pay ",Q1,"$ permonth")
print("50% Users pay ",Q2,"$ permonth")
print("75% Users pay ",Q3,"$ permonth")
#InterQuartile Range  - It tell us the Spread of middle 50% of the data 

# Interquartile range = Q3-Q1

IQR=df["Monthly Revenue"].quantile(0.75)-df["Monthly Revenue"].quantile(0.25)
IQR
# The middle of the 50% user have revenues spread accross $3 range 
# Skew 
skew=df["Monthly Revenue"].skew()
skew

# Skew=0 - Perefectly symmetric - bell curve 
# skew >0 positive : Long tail on right side 
# skew <0 negative : Long tail on left side 


frqncy_of_revenue=df["Monthly Revenue"].value_counts()
frqncy_of_revenue
tot_user=df["Monthly Revenue"].count()
prem_user=df[df["Monthly Revenue"]==15]["Monthly Revenue"].count()
prob=prem_user/tot_user
print(prob*100," % Chances that the user will be premium ")

df.groupby("Subscription Type")["Monthly Revenue"].mean().sort_values()

df.groupby("Subscription Type")["Monthly Revenue"].agg(["count","mean","std","median"])