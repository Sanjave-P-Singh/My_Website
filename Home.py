import streamlit as st
import pandas

st.set_page_config(layout="wide")

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
   
    st.subheader("Contact me: ")
    email_address = "mailto:ssingh025@citymail.cuny.edu"
    linkedin_url = "https://www.linkedin.com/in/sanjave-singh-77043a162/"
    github_url = "https://github.com/Sanjave-P-Singh"


    # Email Address link
    st.markdown(
        f"<div style='text-align: center; margin-bottom: 28px;'><a href='{email_address}' style='font-size: 26px;'>Email Address</a></div>",
        unsafe_allow_html=True)

    # LinkedIn link
    st.markdown(
        f"<div style='text-align: center; margin-bottom: 28px;'><a href='{linkedin_url}' style='font-size: 26px;'>LinkedIn</a></div>",
        unsafe_allow_html=True)

    # GitHub link
    st.markdown(
        f"<div style='text-align: center; margin-bottom: 28px'><a href='{github_url}' style='font-size: 26px;'>Github</a></div>",
        unsafe_allow_html=True)
    
    content2 = """
Please don't hesitate to reach out to me using the email provided.\n
Below, you'll find a selection of Python applications I've created:
"""
st.write(content2)
    

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[0:3].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[3:5].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


