import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, empty_col,col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("images/photo.png",width=400)

with col2:
    st.title("Frank Entsie")
    content = """
    As a dedicated and versatile Full-Stack Developer based in Naha, Okinawa, Japan, 
    I specialize in creating and maintaining web products using a range of 
    modern technologies including ReactJs, VueJs, Tailwind, TypeScript, NodeJs, PHP, Python, 
    Golang, and cloud platforms like AWS. My experience spans frontend development, 
    backend architecture, database management, and infrastructure, 
    ensuring I deliver comprehensive and optimized solutions.

With a strong focus on performance optimization, 
user experience, and secure application design, 
I have successfully implemented features that significantly enhance functionality and user satisfaction. 
My collaborative approach and passion for continuous 
learning enable me to stay at the forefront of technological advancements, 
solving real-world challenges with innovative solutions.
     """
    st.info(content)



col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
       
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        
