import streamlit as st
import pandas

st.set_page_config(layout = "wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/me.png")

with col2:
    st.title("Sanjave P. Singh")
    content = """
    "Hello my name is Sanjave Pritipaul Singh, a senior computer engineering student at the City 
    College of New York. I'm deeply passionate about technology and its transformative impact. 
    I'm also intrigued by electrical engineering. As I approach graduation, I'm excited to contribute to the world of engineering."
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


