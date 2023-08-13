#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from PIL import Image
import base64

# Function to display the resume
def st_display_pdf(pdf_url):
    st.title("My Resume")
    st.markdown(f"Download [PDF](https://github.com/Akshay-Bhasme/my_profile/blob/main/CV_Akshay_Bhasme.pdf)")
    
    pdf_data = open(pdf_url, "rb").read()
    st.write(f'<embed src="data:application/pdf;base64,{base64.b64encode(pdf_data).decode("utf-8")}" width="800" height="600" type="application/pdf">')
    #with open(pdf_file,"rb") as f:
    #    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    #pdf_display = F'<embed src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    #st.markdown(pdf_display, unsafe_allow_html=True)
    
# Function to display your work/projects
#def display_work():
#    st.title("My Work")
#    # Display your work here, e.g., images, descriptions, links, etc.
#    # You can create a grid of images and descriptions for each project
#    project_data = [
#        {"image_path": "project1.jpg", "description": "Project 1 description"},
#        {"image_path": "project2.jpg", "description": "Project 2 description"},
#        # Add more projects as needed
#    ]
#    for project in project_data:
#        image = Image.open(project["image_path"])
#        st.image(image, caption=project["description"], use_column_width=True)

# Main app
def main():
    st.set_page_config(page_title="My Portfolio App", layout="wide")
    
    st.sidebar.title("Navigation")
    pages = ["Resume"]
    choice = st.sidebar.radio("Go to", pages)
    
    if choice == "Resume":
        st_display_pdf("https://github.com/Akshay-Bhasme/my_profile/blob/main/CV_Akshay_Bhasme.pdf")

if __name__ == "__main__":
    main()







