#### Mean -> Mean is an Arithmetic Average of some data  

##### Ex mean=Sum of all values/ number of all values 

import pandas as pd
import numpy as np

sal=[110,70,86,65,70,80,90,100,5000] # sal is a list containing the salary data in list fomat 

def cal_mean(data):  # here we have created a function to calculate the mean of the data
    return sum(data)/len(data)  # here we have taken the sum of the data and divided it by the length of the data 



manual_mean=cal_mean(sal) # here we have called the function and pased the sal data and storing it in a var 
print("Manual Mean:",manual_mean) # Printing the output of the mean calculated manually

df =pd.DataFrame({"Salary":sal})

mean_sal=df["Salary"].mean()
print(mean_sal)

sal_num=[110,70,86,65,70,80,90,100] # here we have removed the skewed data or outlier  ie 5000
print(np.mean(sal_num))
print(np.mean(sal))
#### When to use Mean :
    1. When the data is distributed normally (bell curve)
    2. No extreme outliers or extreme values 
    3. The data should be continuous 
#### When you should'nt use Mean 
    1. When the data is Skewed
    2. When the outliers exist or extreme values exist 
#### Median - Median is the middle value when the data is sorted 
##### 1. sort the data 
##### 2. if odd count - middle value will be the median 
##### 3. if even count - average of the two middle values will be the median 
marks=[110,70,86,65,70,80,90,100,5000] # skewed data or outlier  ie 5000

mrk=[110,70,86,65,70,80,90,100] # cleaned data without outlier

def cal_median(data):
    srt_data=sorted(data) # here sorted will sort the list in ascending order and return a new list 
    n=len(srt_data)
    if n%2==0:
        median=(srt_data[n//2-1]+srt_data[n//2])/2
    else:
        median=srt_data[n//2]
    return median



manual_median=cal_median(marks)
print("Manual Median:",manual_median)
print("Numpy Median with outlier:",np.median(mrk))
# Calculating the median using Numpy 
print("Median with outlier:",np.median(marks))
print("Median without outlier:",np.median(mrk))
# Calculating the Median Using Pandas 

data=pd.DataFrame({"Marks":marks})
skwdmdn=data["Marks"].median()
print("Pandas Median with outlier:",skwdmdn)

normalmdn=pd.DataFrame({"Marks":mrk})
print("Pandas Median without outlier:",normalmdn["Marks"].median())
#####  When to use Median
#### 1. When the data is Skewed 
#### 2. when the outliers present in the data 
#### 3. used for income,house price,or any other monetary data 
#### 4. when you are working with ordinal Data 
#### 5. when you are unsure about the distribution of the data 

#### Mode 
##### Mode is the most frequent value in the data set.  its a measure of central tendency that works for the categoical data 
from scipy import stats
from collections import Counter

scores=[85,90,92,85,88,85,95,90,85,88,90,81,90,81,90,85]

def cal_mode(data):
    counter=Counter(data)
    maxdata=max(counter.values())
    modes=[k for k,v in counter.items() if v==maxdata]
    return modes,maxdata


manual_mode,frequency=cal_mode(scores)
print("Manual Mode:",manual_mode)
print("Frequency of Mode:",frequency)

# Scipy Way of MOde Calcuation 

mode_data=stats.mode(scores)
mode_data
# Pandas Way of Mode Calculation

data=pd.DataFrame({"Scores":scores})
mode_data=data["Scores"].mode()
print("Pandas Mode:",mode_data.tolist())
#### Types of Modes in Real Data 
##### Unimodal - Having only one mode value 
##### Bimodal  - Having two mode values 
##### MultiModal - Having more than two modes 
##### NoModeValue- Having no modes means each value is unique 

#### When to use Mode 
##### 1. This is best used with categorical data 
##### 2. Finding the most common category 
##### 3. Discrete data analysis
##### 4. To understand the data distribution peaks 
##### 5. Its not useful when the data with unique values 
##### 6. It becomes less informative with many modes 
### Label Encoding 
#### This is the way to teach Machines how to read categories 

# Below is list of colors and ML algos will not be able to read this 
data=["Red","Blue","Green","Red","Yellow","Blue","Red"]


enc_data=[0,1,2,0,3,1,0] # here we have encoded the data in numerical format so that ML algos can read this data and make predictions on it
#### Types of Categorical Data 
##### 1. Nominal Data  - No inherent order/ Unordered 
        color=["Red","Green","Yellow","Blue","Orange","Green"]
        countries=["India","Russia","USA","Nepal","SriLanka"]

##### 2. Ordinal Data - Has meaningful order 
        edu=["HighSchool","Graduation","PHD","Masters","Bachelors","Intermediate"]
        ratings=["Poor","Good","Average","VeryGood","Excellent"]
        

from sklearn.preprocessing import LabelEncoder
import pandas as pd
data=pd.DataFrame({"Colors":["Red","Blue","Green","Magenta","Yellow","Blue","Red","Orange","Purple","Magenta","Purple","Magenta"],
                })

print("The data That we are having ")
data 


ob=LabelEncoder() 

data["Encoded Colors"]=ob.fit_transform(data["Colors"])

print("After Label Encoding the data looks like this ")

print(dict(zip(ob.classes_,range(len(ob.classes_)))))
data
d1=["A","B","C","D"]
d2=[100,200,300,400]

print(dict(zip(d2,d1)))
fruits=["Apple","Banana","Orange"]

le=LabelEncoder()
enc_fruits=le.fit_transform(fruits)
print("Encoded Fruits:",enc_fruits.tolist())
#### OneHotEncoding 
One Hot Encoding Creates binary columns for each category 

myData=pd.DataFrame({"color":["Red","Blue","Green","Blue","Red","Magenta","Magenta","Yellow"],
                     "size":["Small","Medium","Large","Medium","Small","Large","Large","Medium"],
                     "price":[10,20,30,20,10,15,25,20]})
myData

#Pandas For OnHotENcoding 

datas=pd.get_dummies(myData,columns=["color","size"],prefix=["col","siz"])
datas

data=pd.DataFrame({
    "Fruits":["Apple","Banana","Orange","Apple","Banana"],
    "Size":["Small","Medium","Large","Small","Medium"],
    "Price":[10,20,30,10,20]
})
data

#### Price - Price is the numeric value that the ML Algo can understand 
#### Size  - That is in text format that cant be understood by the ML algo 
#### Fruits - That is in Text format that also cant be understood by the ML Algos 

encData=pd.get_dummies(data,columns=["Fruits"],prefix=["Frt"],dtype=int)
encData
encdata2=pd.get_dummies(data,columns=["Size"],prefix=["Sz"],dtype=int)
encdata2
encode_data=pd.get_dummies(data,columns=["Fruits","Size"],prefix=["Frt","Sz"],dtype=int)
encode_data
from sklearn.preprocessing import OneHotEncoder

obj=OneHotEncoder()
data=pd.DataFrame({
    "Fruits":["Apple","Banana","Orange","Apple","Banana"],
    "Size":["Small","Medium","Large","Small","Medium"],
    "Price":[10,20,30,10,20]
})


# Here we have encoded the data using Onehotencoder 
encoded_data=obj.fit_transform(data[["Fruits","Size"]])

encoded_data.toarray() # here we are getting an array in encoded format 


# here we are extratcing  the fearure names or the newly created columns after encoding the data
feature_names=obj.get_feature_names_out(["Fruits","Size"])
feature_names

final_data=pd.DataFrame(encoded_data.toarray(),columns=feature_names)
final_data["New Price"]=data["Price"]
final_data
