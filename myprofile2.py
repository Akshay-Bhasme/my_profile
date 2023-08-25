import streamlit as st
from PIL import Image
import base64
import requests
import fitz
import io
from io import BytesIO
from bs4 import BeautifulSoup
from pdf2image import convert_from_bytes

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

def convert_medium_url(url):
    return url.replace("https://medium.com", "https://medium.com/@mediumusername")

# Function to fetch blog information from Medium URL
def fetch_medium_blog_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("title").text
    image_url = soup.find("meta", {"property": "og:image"})["content"]
    return title, image_url

# Function to display blogs
def st_display_blogs(blogs):
    st.title("My Blogs on Medium")
    for i, blog in enumerate(blogs):
        st.write(f"## {blog['title']}")
        st.image(blog['blog_image'], caption=f"Image for {blog['title']}", use_column_width=True)
        st.write(f"[Read More]({blog['read_more_link']})")


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
