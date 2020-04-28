import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

import matplotlib as plt
from matplotlib import pyplot
import seaborn as sns

from datetime import datetime
from datetime import date


df=pd.read_csv('E:\Rohan\Datasets\SuperMarket Sales\supermarket sales - Copy.csv')


df=df.rename(columns={"cogs":"Cost Of Goods Sold",
                      'gross margin percentage':'Gross Margin Percentage',
                      'gross income':'Gross Income',
                      'Customer type':'Customer Type'})


#CHECK FOR UNIQUE VALUES IN GROSS MARGIN PERCENTAGE
s=list(df['Customer Type'].unique())
print(df.describe())

#MISSING  VALUES
missing_values = ["n/a", "na", "--","NA","N/A",'-']
df = pd.read_csv("supermarket sales - Copy.csv", na_values = missing_values)

# Detecting numbers in Branch
cnt=0
for row in df['Branch']:
    try:
        int(row)
        df.loc[cnt, 'Branch']=np.nan
    except ValueError:
        pass
    cnt+=1
missing_data=df.isnull()
print(missing_data.head(6))


#DISPLAYING THE MISSING/NOT MISSING DATA

for columns in missing_data.columns.values.tolist():
    print(columns)
    print(missing_data[columns].value_counts())
    print("")


#DROPPING MISSING VALUES
df.dropna(inplace=True)
df.dropna(how = 'all') #DROP THE OVERALL ROW
s=list(df['Customer type'].unique())

#CHECK NUMBER OF MISSING VALUES - SHOULD GIVE ZERO
#print(df.isnull().sum().sum())

#CHECKING UNIQUE VALUES
print("# unique values in Branch: {0}".format(len(df['Branch'].unique().tolist())))
print("# unique values in City: {0}".format(len(df['City'].unique().tolist())))
print("# unique values in Customer Type: {0}".format(len(df['Customer type'].unique().tolist())))
print("# unique values in Gender: {0}".format(len(df['Gender'].unique().tolist())))
print("# unique values in Product Line: {0}".format(len(df['Product line'].unique().tolist())))
print("# unique values in Payment: {0}".format(len(df['Payment'].unique().tolist())))


#DATA FORMATTING
df[['Quantity']]=df[['Quantity']].astype("int")
df['Date']=df['Date']+df['Time']
df['Date'] =  pd.to_datetime(df['Date'], format='%m/%d/%Y%H:%M')
df['Day'] = (df['Date']).dt.day
df['Month'] = (df['Date']).dt.month
df['Year'] = (df['Date']).dt.year
df['Hours'] = (df['Date']).dt.hour
df['Minutes'] = (df['Date']).dt.minute


#CHANGING THE TYPES OF COLUMNS 
df[['Day']]=df[['Day']].astype("int")
df[['Month']]=df[['Month']].astype("int")
df[['Year']]=df[['Year']].astype("int")
df[['Hours']]=df[['Hours']].astype("int")
df[['Minutes']]=df[['Minutes']].astype("int")

df=df.rename(columns={"Date":"DateTime"})
    

print (df.dtypes)

df=df.round({'Unit price': 2, 'Tax 5%': 2,'Total':2, 'cogs':2, 'gross margin percentage':2,
          'gross income':2,'rating':1})
print(df['Product line'].value_counts())
print(df['Payment'].value_counts())



#DATA STANDARDIZATION
#INSERT WRITTEN TEXT EVEN THOUGH WE DONT HAVE ANY STANDARDIZATION TO DO

#DATA NORMALIZATION
#THE ONLY FACTOR THAT CAN BE NORMALIZED IS THE RATING,WHICH IS ALREADY IN THE SCALE OF 1-10
#MENTION THAT

#BINNING
#s=[]
#for i in df["Product line"]:
#    s.append(i)

#COUNTING PRICE VARIATION
plt.pyplot.hist(df["Total"])
plt.pyplot.xlabel("Total Price")
plt.pyplot.ylabel("Count")
plt.pyplot.title("TOTAL PRICE VS COUNT")

#BINNING
bins = np.linspace(min(df["Total"]), max(df["Total"]), 4)
print(bins)

bin_names=['Low','Medium','High']
df['Price Category'] = pd.cut(df['Total'], bins, labels=bin_names, include_lowest=True)
print(df['Price Category','Total'].head(20))

def show_price_category():
    plt.pyplot.hist(df["Price Category"])
    plt.pyplot.xlabel("Price Category")
    plt.pyplot.ylabel("Count")
    plt.pyplot.title("PRICE CATEGORY VS COUNT")
    #ADD THE VALUES ON TOP OF THE BAR/HISTOGRAM


#GROUPING OF DATA
gk = df.groupby('Product line')
print(gk.get_group('Health and beauty')) 

#CREATE A FACTOR





#VISUALIZATIONS
genderCount  = sns.lineplot(x="Hours",  y = 'Quantity',data =df).set_title("Product Sales per Hour")

genderCount  = sns.relplot(x="Hours",  y = 'Quantity', col= 'Month' , row= 'Branch', kind="line", hue="Gender", style="Gender", data =df)
    