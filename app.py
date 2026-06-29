import streamlit as st  
import pandas as pd 
import pickle as pkl
import math

pipe = pkl.load(open("CPP.pkl","rb+"))
st.title('Car Price Prediction Project')
df = pd.read_csv(r"C:\Users\tejas\Downloads\carpr\clean_data.csv")
arr = sorted(df['company'].unique())
company =  st.selectbox("Enter company",arr)
names = sorted(df[df['company']==company]['name'].unique())
name = st.selectbox("Enter Car name",names)
year = st.number_input("Enter year",min_value=2005,max_value=2026)
kms_driven = st.number_input("Enter kilometers",min_value=500)
fuel_types = sorted(df[df['name']==name]['fuel_type'].unique())
fuel_type = st.selectbox("Enter Fuel type",fuel_types)
if(st.button("Submit")):
    
    inputdata = pd.DataFrame(data=[[name,company,year,kms_driven,fuel_type]],columns=['name','company','year','kms_driven','fuel_type'])
    result = pipe.predict(inputdata)
    result = result[0,0]
    value = math.ceil(result)
    # st.write(value)
    st.text(f"₹{value:,}")