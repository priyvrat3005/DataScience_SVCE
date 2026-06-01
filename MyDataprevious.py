import numpy as np  # import statement for numpy library
arr=np.array([1,2,3,4,5]) 
type(arr)

twodarr=np.array([[75,8,9],[10,11,12]])
print(twodarr.shape) # shape is a tuple representing the dimensions of the array
print(twodarr.ndim) # ndim is the number of dimensions of the array
print(twodarr.size) # size is the total number of elements in the array
print(twodarr.itemsize) # itemsize is the size in bytes of each element in the array
print(twodarr.dtype) # dtype is the data type of the elements in the array
print(twodarr.nbytes) # nbytes is the total number of bytes consumed by the elements of the array
print(twodarr.strides) # strides is the number of bytes to step in each dimension when traversing an array
myarr=np.array([12,7,8,9,12],dtype='int64') 
myarr 
#### DataType Conversion in Numpy 
arr2=np.array([12.5,6.89,9.84,6.78],dtype='float32')


arr3=arr2.astype('int64')

arr3
### Creation of Array Using inbuilt Functions 
x=np.zeros([5,3,2])  # This will create a 3D array of shape (5, 3, 2) filled with zeros also called Tensor 
x2=np.ones(4)
x3=np.identity(4)
x4=np.eye(4,k=1)
x4
ar=np.arange(10,2,-1)
ar
#### Slicing in Arrays 
#### Boolean Indexing 
darr=np.array([15,22,30,8,45,12,60])

mask=darr>25

print(mask)
##### I want to print the items which are either  lesser than 20 or  greater than 50 
m2=(darr<20) | (darr>50)
print(darr[m2])
#### Conditional Statements 
narr=np.array([10,45,25,30,45,50])

res=np.where(narr<20,"Small",np.where(narr<40,"Medium","Large"))
print(res)

#### Numpy Select function
narr=np.array([10,45,25,30,45,50])

cons=[narr<20,
      (narr>=20)&(narr<40),
      narr>=40]

sel=["small","medium","Large"]
res=np.select(cons,sel,default="Unknown")
print(res)
### Arrays Reshape 
npar=np.arange(12)
rs=npar.reshape(4,-1)
print(rs)
npr=np.arange(2,20,2)

npr=npr.reshape(3,3)

print(npr.flatten())
#### Pandas Series 
###### Series is a smart dictionary that wears a mask of Numpy Array 

###### Series contains mainly three things 
 1. Value - The actual data ( this is soed as numpy array )
 2. index - The labels (This can be said as primary key )
 3. Name - The coumn heading 
 
import pandas as pd 
import numpy as np 
s=pd.Series([8,9,7,6,5],index=["Lko","vadodara","delhi","mumbai","kolkata"],name="City")

print(s)
print(s.name) 
print(s.index )
print(s.values)
print(s.dtype)
print(s.iloc[1])
print(s["delhi"])  
s2=pd.Series([1,2,3,4])
print(s2)
s2.iloc[0]=None
print(s2)
s3=pd.Series([1,2,3,4],dtype='Int64')
s3.iloc[0]=pd.NA
print(s3)
s4=pd.Series([10,20,30],index=['a','b','c'])
print(id(s4))
sdrop=s4.drop('b') # its creating a new series without 'b' and its value
print(sdrop)

print(s4)
## Vectorization
import numpy as np 
import time 
mylist=list(range(1000000))

start=time.time()
total=0
for i in mylist:
    total=total+i
print("Time taken by the list is ",time.time()-start)
nparr=np.arange(1000000)
start=time.time()
total=0
total=np.sum(nparr)
print("Time taken by the numpy array is ",time.time()-start)
#### Pandas 
import pandas as pd
import numpy as np

d ={
    "name":["Alice","Bob","Charlie","David","rohit","agastya","amar","joy"],
     "age":[25,30,35,40,50,21,43,45],
     "city":["New York","Los Angeles","Chicago","Houston","hongkong","delhi","mumbai","kolkata"],
     "sal":[50000,60000,70000,80000,30000,32000,45000,870000]
     }

df=pd.DataFrame(d)
df
for i in range(len(df)):
    df.loc[i,"sal"]=df.loc[i,"sal"]*1.0

df  
df["sal"]=df["sal"]*1.0
df

df.loc[df["sal"]>50000,"age"]-=5
df
data={
    "players":["virat","Rohit","sehwag","dhoni","virat","Rohit","sehwag","dhoni"],
    "matches":[100,200,300,400,100,200,300,400],
    "runs":[154,200,123,257,309,198,171,120],
    "Balls":[50,100,120,120,150,80,120,100]
}
ipl=pd.DataFrame(data)
ipl
## Task 
1. FInd the Strike rate of Each player    (run/ball*100)
2. Show only matches where virat has scored more than 150
3. show the total runs scored by the player and highest score by the player 

data={
    "players":["virat","Rohit","sehwag","dhoni","virat","Rohit","virat","dhoni"],
    "matches":[25,123,89,15,108,170,111,20],
    "runs":[154,200,123,257,309,198,171,54],
    "Balls":[50,100,120,120,150,80,120,100]
}
df=pd.DataFrame(data)
df
### GroupBy
grp=df.groupby("players" )["runs"].sum()
grp
### Aggregation
summ=df.groupby("players").agg(
    Total_runs=("runs", "sum"),
    Average_runs=("runs", "mean"),
    Matches_played=("matches","sum"),
    Highest_score=("runs","max"),
    Lowest_score=("runs","min"),
    Totals_balls=("Balls","sum")
).reset_index()

summ
summ=df.groupby("players").agg(
    Total_runs=("runs", "sum"),
    Average_runs=("runs", "mean"),
    Matches_played=("matches","sum"),
    Highest_score=("runs","max"),
    Lowest_score=("runs","min"),
    Totals_balls=("Balls","sum"),
    Fifties=("runs",lambda x:((x>=50) & (x<100)).sum())
).reset_index()
summ
#### Pandas In python 
# Date 28 May 2026 
import pandas as pd 
import numpy as np 
df=pd.DataFrame({
    "Name":["Rahul","Joy","Kumar","Mahi","Jhanvi","Shubham","Priya","Anit"],
     "age":[25,30,35,40,50,21,43,45],
     "city":["mumbai","delhi","Chicago","kolkata","hongkong","delhi","mumbai","kolkata"],
     "sal":[50000,60000,70000,80000,30000,32000,45000,870000],
     "Experience":[2,5,7,10,15,1,8,20],
     "Department":["IT","HR","Finance","IT","HR","Finance","IT","HR"]
})
df
df["Department"]   # Both will return the Same Thing a single columns data
df.Department # this will also return the same thing that is the single column data 

print(type(df["Name"]))  # This will return the Series 
print(type(df[["Name"]])) # This will return the DataFrame 
df.loc[:,["Name","sal"]] # This will return DataFrame 
# This is Column Access or can sal Label based Access 
df.iloc[:,[0,5]] # This will return Name and Department  
df.iloc[:,0:3] # This will three coluns Name age and City in dataFrame format 
### Now we are going to access rows Using .iloc method 
print(df.iloc[[4,2]])  
df.iloc[0:3,0:4]
##### I want to print 0th and 1st row and 0th and 3rd column what should i write to get it printed 
df.iloc[[0,1],[0,3]]
#### We are Going to Use .loc function to get the rows printed 
print(df.loc[[0,2,3]])
print("Second output")
print(df.loc[3])
df2=df.set_index("Name")
df2
df2.loc[["Jhanvi","Priya"]]
#### Here we are going to Use .loc function to get rows+columns together 

# Syntax  : df.loc[rows_selection,col_selection]

df.loc[3,"sal"]  # here we are accessing specific row and specific col

# Now multiple rows  and single column

df.loc[0:3,["Name","age","Department"]]

df.loc[df["age"]>25,["Name","sal","age","Department"]]# simple way 
mask=df["age"]>25
df.loc[mask,["Name","sal","age","Department"]] # here we are using Masking 
df[(df["age"]>25) & (df["sal"]>50000)],[["Name","sal","age","Department"]] # here we are using multiple conditions
# This is doubtful syntax but it is correct and it will work fine
#### Query method like sql 
df.query("age>25 and sal>50000 and Department=='IT'") # this is query method to filter the data based on conditions
df.query("age>25 and sal>30000 and city in ['Chicago','mumbai']")
@var way to write the queries 

con=30  # here we have taken a var and we will use this in query method by using @symbol to refer the var 
df.query("age>@con and sal>30000 and city in ['Chicago','mumbai']")
con=30  # here we have taken a var and we will use this in query method by using @symbol to refer the var 
df.query("age>@con and sal>30000 and city in ['Chicago','mumbai']")
#### isin() method   this is like membership method 
df[df["city"].isin(["delhi","mumbai"])]
### between() - Range Checking 
# Age should be greater than 30 and less than 40 

df[df["age"].between(30,40)][["Name","Department"]]
#### 1. to print only sal and Name cols 
#### 2. show the data whose age>40 
#### 3. display the row no 2 3 4 using .iloc()
#### 4. show only first 4 rows of Name and Department cols 
#### 5. Show all the names where the department is IT 
#### 6. Show the first two cols of last 3 rows 
#### 7. show the data where the sal is between 60k to 80k along with the name and city cols 

#### Goupby()
df.groupby("city")['sal'].mean()
df.groupby("Department")["sal"].agg(['min','max','mean','sum','count'])
df.agg({'age':['min','max','mean'],
        'sal':['min','max','std'],
        'Experience':['min','max','median']
        })
#### Sorting + EDA (Exploratory Data Analysis)
# sort_values() this is the functions to sort the things 
# it has multiple params like by,ascending,inplace etc

df.sort_values("Name",ascending=False)
df.sort_values(["Department","sal"],ascending=[True,False])
df['sal_rank']=df['sal'].rank(ascending=False)
df
#### EDA - its the process to understand the data without assumptions 
##### Responsibilty of Analyst is to:
1.  understand the data 
2. Find the pattern 
3. To find the problems in the data 

df.head() # it will show by default first 5 rows of the data 
df.tail() # it will show by default last 5 rows of the data

df.sample(3) # it will return random sample of the data by default it will return 1 row of the data
df.sample(frac=0.5) # it will return random sample of the data by default it will return 50% of the data because we have given frac=0.5
df.shape # it will return the shape of the data in tuple format (rows,columns)
df.info() # it will return the info of the data like number of non-null values in each column and data types of each column
df.dtypes
num_cols=df.select_dtypes(include=['int64','float64']).columns
num_cols
cat_col=df.select_dtypes(include=['object']).columns

print("Numerical columns:",len(list(num_cols)),"Categorical columns:",len(list(cat_col)))


df['age']=df['age']*1.0
df['age']=df['age'].astype('float64')

df
df.describe(include="all")

print(df['city'].value_counts(normalize=True)*100 )# it will return the count of each unique value in the city column and normalize=True will return the percentage of each unique value in the city column

print(df['city'].value_counts())# it will return the count of each unique value in the city column without normalizing it to percentage


import pandas as pd 
import numpy as np

df=pd.DataFrame({
    "Name":["Rahul","Joy","Kumar","Mahi","Jhanvi","Shubham","Priya","Anit"],
     "age":[25,np.nan,35,40,50,np.nan,43,45],
     "city":["mumbai","delhi","Chicago","kolkata","hongkong","delhi",np.nan,"kolkata"],
     "sal":[50000,60000,70000,80000,30000,32000,45000,870000],
     "Experience":[2,5,7,np.nan,15,1,8,np.nan],
     "Department":["IT","HR","Finance",np.nan,"HR","Finance","IT","HR"]
})

df
df.isna().sum() # it will return the count of missing values in each column of the data frame


df.notnull().sum()
df.isna().mean()*100
df[df.isna().all(axis=1)] # it will return the rows which have at least one missing value in any column
df[df.isna().any(axis=1)] # it will return the rows which have at least one missing value in any column
df[df["age"].isna()]
# df.dropna() this function drops the rows or cols from the data set 



df
df.dropna(axis=1) # it will drop the columns which have less than 6 non-null values
df.dropna(axis=0) # it will drop the rows which have less than 6 non-null values

df["Experience"].fillna(0)
df["city"].fillna("Unknown")

df.fillna({"Experience":0,"city":"Unknown"})
df

#### Filling the empty values Statistically 

df["Department"].fillna(df["Department"].mode()[0])

df.replace("Finance","FIna",inplace=True)
df
data=({
    "Student":["Alice","Bob","Charlie","David","rohit","agastya","amar","joy"],
     "maths":[85,90,np.nan,92,88,95,80,91],
     "science":[80,85,90,np.nan,88,92,np.nan,89],
     "English":[75,80,85,90,88,92,84,89],
     "Sanskrit":[70,75,np.nan,85,88,90,82,87],
     "Attendance":[90,85,95,80,88,np.nan,84,89]
})
## Task 
#### 1. Count the missing values 
#### 2. Fill all the missing values in maths with the mean value without using mean function 
#### 3. In english fill teh missing values with 0 
#### 4. verify whether your data is having any missing values or not 
#### 5. Fill the nan values in attendance column using mean value 
#### 6. remove that row which have more than 2 nan values 


df=pd.DataFrame({
    "StudentId":["S001","S002","S003","S004","S005","S006","S007","S008","S009","S010","S011","S012","S013","S014","S015"],
    "Name":["Alice","Bob","Charlie","David","rohit","agastya","amar","joy","Rohit","Mahi","Jhanvi","Shubham","Priya","Anit","Rahul"],
    "Maths":[85,90,np.nan,92,88,95,80,91,89,94,87,90,85,88,92],
    "Science":[80,85,90,np.nan,88,92,np.nan,89,90,40,56,78,85,90,30],
    "English":[75,80,85,90,88,92,84,89,90,40,56,78,85,90,30],
    "Attendance":[90,85,95,80,88,np.nan,84,89,90,40,56,78,85,90,30],
    "Grade":["A","A","B","A",np.nan,"A","C",np.nan,"A","C","B","B","B","A","A"],
    "Phone":["8989657890","9876543210","7654321098","6543210987","5432109876","4321098765","3210987654","2109876543","1098765432","0987654321","9876543210","8765432109","7654321098","6543210987","5432109876"],
    "Email":["alice@example.com","bob@example.com","charlie@example.com","david@example.com","rohit@example.com","agastya@example.com","amar@example.com","joy@example.com","rohit@example.com","mahi@example.com","jhanvi@example.com","shubham@example.com","priya@example.com","anit@example.com","rahul@example.com"],
    "Remarks":["Excellent","Excellent","Good","Excellent","Good","Excellent","Average","Good","Excellent","Average","Good","Good","Good","Excellent","Excellent"]

})
df
df.notnull().sum()
df.describe(include="all")
# i want to print all the rows which are having atleast on missing value in any column
df[df.isnull().any(axis=1)]
# i want to check if in a column there is any missing value or not
df["Maths"].isnull()

df.drop("Maths",axis=1)
df["Total"]=df["Maths"]+df["Science"]+df["English"]

df.fillna({"Attendance":df["Attendance"].mean(),"Total":df["Total"].mean()})

df["Grade"].fillna(df["Grade"].mode()[0],inplace=True)
df
df.drop("Total",axis=1)
df["Science"].fillna(df["Science"].mean(),inplace=True)

# i want to convert the Science column to int type after filling the missing values with mean

df["Science"]=df["Science"].astype("int64")

df["Maths"].fillna(df["Maths"].mean(),inplace=True)
df["Maths"]=df["Maths"].astype("int64")
df
#### Data Cleaning 
import pandas as pd
import numpy as np

from datetime import datetime # this is the module to work with date and time in python

df=pd.DataFrame({
    "CustomerName":["Priyvrat","Rahul Sharma             ","priya patel","AMIT KUMAR","neha gupta"," Vikas Jain","priya patel","sneha reddy"," rahul sharma ","Pooja Mehta",None,"Priyvrat"],
    "OrderDate":["2023-08-25","2023-01-15","2023/02/20","2023-03-10","20-04-2025","2023-05-25","2023-06-30","2023-07-15","2023-08-20","20-09-2010",None,"2023-08-25"],
    "ProductName":["Mouse","Laptop","Mobile","Keyboard","Headphones","Mouse","Mouse","Printer","Monitor","Keyboard","Mouse","Mouse"],
    "Quantity":["2",'1','2','koko','1','-3','2','1','1','2','200',"2"],
    "Price":[20000,50000,20000,1500,3000,800,800,5000,10000,1500,800,20000],
    "City":["Lucknow","Mumbai","Delhi","Chicago","Kolkata","Hongkong","Delhi","Mumbai","Kolkata","Delhi","Pune","Lucknow"],
    "DeliveryDate":["2023-08-25","2023-01-20","2023/02/25","2023-03-15","25-04-2025","2023-05-30","2023-07-05","2023-07-20","2023-08-25","2023-09-20","2023-08-25","2023-08-25"]
})
print(df)
df.info()
df.isna().sum()
print(df.duplicated().sum()) # it will return the count of duplicate rows in the data frame
df["CustomerName"]=df["CustomerName"].str.strip()# this will remove the leading and trailing spaces and convert the first letter of each word to uppercase and rest to lowercase in the CustomerName column
df["CustomerName"]=df["CustomerName"].str.capitalize() # this will convert the first letter of each word to uppercase and rest to lowercase in the CustomerName column
df.dropna(inplace=True) # this will drop the rows which have missing values in any column
print(df)
df["City"]=df["City"].replace({"Chicago":"Goa","Hongkong":"Hyderabad"})
df
def parseDate(datestr):
    if pd.isna(datestr):
        return pd.NaT
    
    datestr=str(datestr).strip()

    formats=['%Y-%m-%d','%Y/%m/%d','%d-%m-%Y','%Y-%d-%m',"%d/%m/%Y","%Y-%m-%d","%Y/%m/%d","%d-%m-%Y","%Y-%d-%m", "%d/%m/%Y"]

    for fmt in formats:
        try:
            return pd.to_datetime(datestr, format=fmt)
        except :
            continue
    return pd.NaT

df
df["OrderDate"]=df["OrderDate"].apply(parseDate)
df["DeliveryDate"]=df["DeliveryDate"].apply(parseDate)
df
df["Quantity"]=pd.to_numeric(df["Quantity"],errors="coerce")  ## here we have converted the Quantity column to numeric type and if there is any error in conversion it will be replaced with NaN
df
print("Now we are going to check for the negative vaues in Quantity column")

df[df["Quantity"]<0]

df["Quantity"]=df["Quantity"].abs() # this will convert the negative values in Quantity column to positive values
df
