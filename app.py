import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data=pd.read_csv("data//Salary_Data.csv")
lr=LinearRegression()
x = np.array(data['YearsExperience']).reshape(-1,1)
lr.fit(x,np.array(data['Salary']))
st.title("Salary Predictor")

nav= st.sidebar.radio("Navigation",['Home' , 'Prediction' , 'Contribute'])
if nav=='Home':
    st.image("data//salary.jpj")
    if st.checkbox("Show Table"):
        st.table(data)
    graph= st.selectbox("select graph",["Non-interactive","Interactive"])
    val= st.slider('Filter data ',0,20,value=5)
    data=data.loc[data['YearsExperience']>val]
    if graph =="Non-interactive" :
        fig,ax =plt.subplots()
        plt.figure(figsize=(10,5))
        ax.scatter(data['YearsExperience'],data['Salary'])
        plt.xlabel('years of experience')
        plt.ylabel('Salary')
        plt.title('Scatter plt')
        st.pyplot(fig)

    if graph =="Interactive" :
        fig, ax = plt.subplots()
        plt.figure(figsize=(10, 5))
        ax.scatter(data['YearsExperience'], data['Salary'])
        plt.xlabel('years of experience')
        plt.ylabel('Salary')
        plt.title('Scatter plt')
        st.pyplot_chart(fig)

if nav == "Prediction":
    st.image("data//salary.jpj")
    st.header("Know your Salary")
    val = st.number_input("Enter you exp",0.00,20.00,step=0.25)
    val = np.array(val).reshape(1,-1)
    pred =lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your predicted salary is {round(pred)}")
if nav == "Contribute":
    st.image("data//salary.jpj")
    st.header("Contribute to our dataset")
    ex = st.number_input("Enter your Experience",0.0,20.0)
    sal = st.number_input("Enter your Salary",0.00,1000000.00,step = 1000.0)
    if st.button("submit"):
        to_add = {"YearsExperience":[ex],"Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("data//Salary_Data.csv",mode='a',header = False,index= False)
        st.success("Submitted")




