#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from PIL import Image
from PyPDF2 import PdfReader
import base64
import requests
import fitz 
import io
from io import BytesIO

def pdf_github_to_images(pdf_github_url):
    response = requests.get(pdf_github_url)
    pdf_bytes = BytesIO(response.content)

    images = []
    pdf = PdfReader(pdf_bytes)
    for page_num in range(pdf.getNumPages()):
        page = pdf.getPage(page_num)
        xObject = page['/Resources']['/XObject'].get_object()
        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                img = xObject[obj]
                data = img._data
                img = Image.open(BytesIO(data))
                images.append(img)
    return images
    
# Function to display the resume
def st_display_pdf(images,width=400, height=600):
    st.title("Career Snapshot")
    st.write(f"Download My Resume here [PDF](https://github.com/Akshay-Bhasme/my_profile/blob/main/CV_Akshay_Bhasme.pdf)")
    st.write(f"Email: akshaybhasme30@gmail.com          ",f"        Mobile No: +91 7972014093")
    st.write(f"GitHub: https://github.com/Akshay-Bhasme ")
    st.write(f"LinkedIn: www.linkedin.com/in/akshaybhasme30 ")
    for i, image in enumerate(images):
        st.image(image, caption=f"Page {i+1}", use_column_width=True)
    st.write(f"Download My Resume here [PDF](https://github.com/Akshay-Bhasme/my_profile/blob/main/CV_Akshay_Bhasme.pdf)")
    #response = requests.get(pdf_url)
    #pdf_data = response.content
    #pdf_b64 = base64.b64encode(pdf_data).decode("utf-8")
    
    # Use the iframe HTML tag to embed the PDF viewer
    #st.markdown(f'<iframe src="data:application/pdf;base64,{pdf_b64}" width="800" height="600"></iframe>', unsafe_allow_html=True)
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
        pdf_github_url = "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/raw/main/CV_Akshay_Bhasme.pdf"  # Replace with your GitHub PDF URL
        images = pdf_github_to_images(pdf_github_url)
        st_display_pdf(images)

if __name__ == "__main__":
    main()
