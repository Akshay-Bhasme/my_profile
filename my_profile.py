#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from PIL import Image
import base64
import requests
import fitz 
import io
from io import BytesIO

def pdf_github_to_images(pdf_github_url):
    response = requests.get(pdf_github_url)
    pdf_bytes = BytesIO(response.content)

    images = []
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        image = page.get_pixmap(matrix=fitz.Matrix(3, 3))  # Increase the scale factor for larger images
        pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
        images.append(pil_image)
    pdf_document.close()
    return images
    
# Function to display the resume
def st_display_pdf(images,width=400, height=600):
    st.title("Career Snapshot")
    st.write(f"Download My Resume here [PDF](https://github.com/Akshay-Bhasme/my_profile/raw/main/CV_Akshay_Bhasme.pdf)")
    st.write(f"Email: akshaybhasme30@gmail.com          ",f"        Mobile No: +91 7972014093")
    st.write(f"GitHub: https://github.com/Akshay-Bhasme ")
    st.write(f"LinkedIn: www.linkedin.com/in/akshaybhasme30 ")
    for i, image in enumerate(images):
        st.image(image, caption=f"Page {i+1}", use_column_width=True)
    st.write(f"Download My Resume here [PDF](https://github.com/Akshay-Bhasme/my_profile/raw/main/CV_Akshay_Bhasme.pdf)")
    
def st_display_certificates(certificates, width=400, height=600):
    st.title("Courses and Certificates")
    for i, certificate in enumerate(certificates):
        st.write(f"## {certificate['course_name']}")
        st.image(certificate['certificate_image'], caption=f"Certificate for {certificate['course_name']}", use_column_width=True)
        st.write(f"**Credentials**: {certificate['credentials']}")
        st.write("---")

# Main app
def main():
    st.set_page_config(page_title="My Portfolio App", layout="wide")

    st.sidebar.title("My Portfolio App")

    st.markdown(
        """
        <style>
        .navigation-option {
            display: inline-block;
            padding: 10px 20px;
            margin: 5px;
            background-color: #f0f0f0;
            border: 2px solid #333;
            border-radius: 5px;
            cursor: pointer;
        }
        .navigation-option:hover {
            background-color: #ccc;
        }
        .selected-option {
            background-color: #333;
            color: #fff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Display links to different pages
    pages = ["Resume","Courses and Certificates"]  # Add more pages as needed
    choice = st.radio("Go to", pages, key="navigation")

    if choice == "Resume":
        pdf_github_url = "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/CV_Akshay_Bhasme.pdf"  # Replace with your GitHub PDF URL
        images = pdf_github_to_images(pdf_github_url)
        st_display_pdf(images)

    elif choice == "Courses and Certificates":
        certificates = [
            {
                "course_name": "Applied Machine Learning Course",
                "certificate_pdf": "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/Applie%20AI.pdf",
                "credentials": "https://www.appliedaicourse.com/certificate/902eadbdec"
            },
            {
                "course_name": "Python (Basic) Certificate",
                "certificate_pdf": "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/python_basic%20certificate.pdf",
                "credentials": "https://www.hackerrank.com/certificates/7ff0e9842ae8"
            },
            {
                "course_name": "SQL (Basic) Certificate",
                "certificate_pdf": "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/sql_basic%20certificate.pdf",
                "credentials": "https://www.hackerrank.com/certificates/1aaf4b4e8057"
            },
            {
                "course_name": "Prompt Engineering for ChatGPT",
                "certificate_pdf": "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/PrompEngineeringForChatGPT.pdf",
                "credentials": "https://www.coursera.org/account/accomplishments/certificate/3U8XGSFYA74H"
            },
            {
                "course_name": "Hands-on Machine Learning with AWS and NVIDIA",
                "certificate_pdf": "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/HandsOnMachineLearning.pdf",
                "credentials": "https://www.coursera.org/account/accomplishments/certificate/FYB8KV6CKWZH"
            },
            # Add more courses
        ]
        
        for certificate in certificates:
            certificate_pdf_url = certificate['certificate_pdf']
            certificate_images = pdf_github_to_images(certificate_pdf_url)
            if certificate_images:
                certificate['certificate_image'] = certificate_images[0]  # Display only the first page as an image
            else:
                certificate['certificate_image'] = None
        
        st_display_certificates(certificates)

if __name__ == "__main__":
    main()
