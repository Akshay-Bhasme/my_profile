import streamlit as st
from PIL import Image
import base64
import requests
import fitz
import io
from io import BytesIO
from bs4 import BeautifulSoup
from pdf2image import convert_from_bytes



def st_display_intro():
    st.title("Howdy! I am Akshay Bhasme")
    st.write("Welcome to my portfolio app.")
    st.write("I am a Data Scientist with a passion for Machine Learning and AI.")
    st.write("Feel free to explore my resume, certificates, and blogs.")
    st.write("Click on the icons below to navigate:")

def st_display_navigation_buttons():
    col1, col2, col3 = st.beta_columns(3)

    with col1:
        st.image("https://image.flaticon.com/icons/png/512/135/135760.png", width=100)
        st.write("Resume")
        if st.button("Go to Resume"):
            main("Resume")

    with col2:
        st.image("https://image.flaticon.com/icons/png/512/25/25694.png", width=100)
        st.write("Courses and Certificates")
        if st.button("Go to Courses and Certificates"):
            main("Courses and Certificates")

    with col3:
        st.image("https://image.flaticon.com/icons/png/512/25/25618.png", width=100)
        st.write("Blogs")
        if st.button("Go to Blogs"):
            main("Blogs")

def main(page=None):
    st.set_page_config(page_title="My Portfolio App", layout="wide")

    if page is None:
        st_display_intro()
        st_display_navigation_buttons()
    elif page == "Resume":
        pdf_github_url = "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/CV_Akshay_Bhasme.pdf"
        images = pdf_github_to_images(pdf_github_url)
        st_display_pdf(images)
    elif page == "Courses and Certificates":
        # ... (your existing code)
    elif page == "Blogs":
        # ... (your existing code)

if __name__ == "__main__":
    main()
