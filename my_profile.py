import streamlit as st
from PIL import Image
import base64
import requests
#import fitz
import io
from io import BytesIO
from bs4 import BeautifulSoup
from pdf2image import convert_from_bytes

def pdf_github_to_images(pdf_github_url):
    response = requests.get(pdf_github_url)
    pdf_bytes = BytesIO(response.content)

    images = convert_from_bytes(pdf_bytes)
    return images
#def pdf_github_to_images(pdf_github_url):
#    response = requests.get(pdf_github_url)
#    pdf_bytes = BytesIO(response.content)
#
#    images = []
#   pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
#    for page_num in range(pdf_document.page_count):
#        page = pdf_document.load_page(page_num)
#        image = page.get_pixmap(matrix=fitz.Matrix(3, 3))  # Increase the scale factor for larger images
#        pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
#        images.append(pil_image)
#    pdf_document.close()
#    return images
    
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

# Main app
def main():
    st.set_page_config(page_title="My Portfolio App", layout="wide")

    st.sidebar.title("Navigate Through My Profile")
    
    # Display links to different pages horizontally
    pages = ["Resume", "Courses and Certificates", "Blogs"]  # Add more pages as needed
    choice = st.sidebar.radio("Go to", pages, key="navigation")

    # Sections with anchors for navigation
    if choice == "Resume":
        pdf_github_url = "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/CV_Akshay_Bhasme.pdf"
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
        
    elif choice == "Blogs":
        blogs = [
            {
                "title": "Exploring Emotions with BERT -Transfer Learning: Your Guide to Sentiment Analysis",
                "read_more_link": "https://medium.com/@akshaybhasme30/exploring-emotions-with-bert-transfer-learning-your-guide-to-sentiment-analysis-6c260f9c1de5"
            },
            {
                "title": "Unleashing the Power of Deep Learning: Exploring LSTM on the Donors Choose Dataset",
                "read_more_link": "https://medium.com/@akshaybhasme30/unleashing-the-power-of-deep-learning-exploring-lstm-on-the-donors-choose-dataset-771951df6600"
            },
            {
                "title": "Common Mistakes to Avoid in Model Building: Insights from a Data Scientist’s Journey",
                "read_more_link": "https://medium.com/@akshaybhasme30/common-mistakes-to-avoid-in-model-building-insights-from-a-data-scientists-journey-dc3fbfb70925"
            },
            {
                "title": "Principal component analysis (PCA)",
                "read_more_link": "https://medium.com/@akshaybhasme30/principal-component-analysis-pca-d6de7a53efa7"
            },
            {
                "title": "How to create Jupyter Notebook instance on Google Cloud Platform (GCP)",
                "read_more_link": "https://medium.com/@akshaybhasme30/how-to-create-jupyter-notebook-instance-on-google-cloud-platform-gcp-3e74061dd869"
            },
            
            # Add more blogs
        ]
        for blog in blogs:
            title, image_url = fetch_medium_blog_info(blog['read_more_link'])
            blog['title'] = title
            blog['blog_image'] = Image.open(BytesIO(requests.get(image_url).content))
            
        st_display_blogs(blogs)

if __name__ == "__main__":
    main()
