import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st
from sklearn.preprocessing import LabelEncoder

model = pk.load(open('model.pkl','rb'))
cars_data = pd.read_csv('Cardetails.csv')
st.header("Find Estimated Price of Car")

# Add age column.
current_year=2025
cars_data['age']=current_year-cars_data["year"]

name = st.selectbox("Brand Name",cars_data['name'].unique())
year = st.selectbox("Year",cars_data['year'].unique())
km_driven = st.selectbox("Kilometer driven",cars_data['km_driven'].unique())
fuel = st.selectbox("Fuel type",cars_data['fuel'].unique())
seller_type = st.selectbox("Type of seller",cars_data['seller_type'].unique())
transmission = st.selectbox("Transmission Type",cars_data['transmission'].unique())
owner = st.selectbox("Owner",cars_data['owner'].unique())
mileage = st.selectbox("Mileage",cars_data['mileage'].unique())
engine = st.selectbox("Engine",cars_data['engine'].unique())
max_power = st.selectbox("Maximum power",cars_data['max_power'].unique())
seats = st.selectbox("Number of seats",cars_data['seats'].unique())
age = st.selectbox("How old car is",cars_data['age'].unique())

# function od data cleaning.
def clean_data(value):
    value = value.split(' ')[0]   
    value = value.strip()         
    if value == '':               
        value = 0
    return float(value)

if st.button("Estimated Price"):
    input_data_model = pd.DataFrame(
    [[name,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,seats,age]],
    columns=['name','year','km_driven','fuel','seller_type','transmission','owner','mileage','engine','max_power','seats','age'])
    
    input_data_model['mileage'] = input_data_model['mileage'].apply(clean_data)
    input_data_model['max_power'] = input_data_model['max_power'].apply(clean_data)
    input_data_model['engine'] = input_data_model['engine'].apply(clean_data)

    # Convert categorical columns.
    car_columns = ['name','fuel','seller_type','transmission','owner']
    label_encoder = LabelEncoder()
    for x in input_data_model[car_columns]:
        input_data_model[x]=label_encoder.fit_transform(input_data_model[x])

    st.write(input_data_model)
    car_price = model.predict(input_data_model)
    print(car_price)

    st.markdown('Car Price is going to be '+ str(car_price[0]))