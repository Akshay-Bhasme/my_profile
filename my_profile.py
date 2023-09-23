import streamlit as st
from PIL import Image
import base64
import requests
import fitz
import io
from io import BytesIO
from bs4 import BeautifulSoup
from pdf2image import convert_from_bytes
import streamlit.components.v1 as components


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
    st.write(f"Download My Resume here [PDF](https://github.com/Akshay-Bhasme/my_profile/raw/main/CV_Akshay_Bhasme_ML.pdf)")
    st.write(f"Email: akshaybhasme30@gmail.com          ",f"        Mobile No: +91 7972014093")
    st.write(f"GitHub: https://github.com/Akshay-Bhasme ")
    st.write(f"LinkedIn: www.linkedin.com/in/akshaybhasme30 ")
    for i, image in enumerate(images):
        st.image(image, caption=f"Page {i+1}", use_column_width=True)
    st.write(f"Download My Resume here [PDF](https://github.com/Akshay-Bhasme/my_profile/raw/main/CV_Akshay_Bhasme_ML.pdf)")
    
def st_display_certificates(certificates, width=400, height=600):
    st.title("Courses and Certificates")
    for i, certificate in enumerate(certificates):
        st.write(f"## {certificate['course_name']}")
        st.image(certificate['certificate_image'], caption=f"Certificate for {certificate['course_name']}", use_column_width=None, width= 500)
        st.write(f"**Credentials**: {certificate['credentials']}")
        st.write("---")


# Function to display blogs
def st_display_blogs(blogs):
    st.title("My Blogs on Medium")
    for i, blog in enumerate(blogs):
        st.write(f"## {blog['title']}")
        st.image(blog['blog_image'], caption=f"Image for {blog['title']}", use_column_width=None, width= 500)
        st.write(f"[Read More]({blog['read_more_link']})")

def st_display_home():
    st.title("Welcome to My Portfolio")
    st.image("https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/dp.jpg", use_column_width=None,width= 400 )
    st.write("## About Me")
    st.write("""**Hey, I'm Akshay, a seasoned Data Scientist**.  
    What really gets me going is solving puzzles. From my early days,  I have always enjoyed to solve puzzles, and that's exactly how I approach those massive data sets. It's like one giant puzzle waiting for me to solve. My thrill comes from spotting patterns that others might overlook.
I've been doing this Data Scientist thing for over five years now, working in insurance, software, and media domain. My special talent is taking complicated stuff and turning it into simple, practical solutions with great user experience.  
Welcome to my area of expertise : Data Science and ML solutions.""")
    components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {box-sizing: border-box;}
body {font-family: Verdana, sans-serif;}
.mySlides {display: none;}
img {vertical-align: middle;}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/4 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 2s;
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .text {font-size: 11px}
}
</style>
</head>
<body>

<h3>Awards and Recognitions</h3>
<p>GroupM Choreos Awards 2022: Newbie In The Spotlight</p>

<div class="slideshow-container">

<div class="mySlides fade">
  <div class="numbertext">1 / 3</div>
  <img src="https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/EE2A4181.jpg" style="width:100%">
  <div class="text">Choreos'22 Newbie In The Spotlight</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">2 / 3</div>
  <img src="https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/EE2A4658.jpg" style="width:100%">
  <div class="text">Choreos'22 Newbie In The Spotlight</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">3 / 3</div>
  <img src="https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/Picsart_23-09-23_16-30-31-629.jpg" style="width:100%">
  <div class="text">Choreos'22 Newbie In The Spotlight</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">4 / 3</div>
  <img src="https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/IMG-20221212-WA0014.jpg" style="width:100%">
  <div class="text">Choreos'22 Newbie In The Spotlight</div>
</div>

</div>
<br>

<div style="text-align:center">
  <span class="dot"></span> 
  <span class="dot"></span> 
  <span class="dot"></span> 
  <span class="dot"></span>
</div>

<script>
let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}
</script>

</body>
</html> 

    """,
    height=600,
)

    

# Main app
def main():
    st.set_page_config(page_title="My Portfolio App", layout="wide",initial_sidebar_state='expanded')
    st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 200px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 200px;
        margin-left: -200px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
    
    st.sidebar.title("Navigate")
    
    # Display links to different pages horizontally
    pages = pages = ["About me", "Career Snapshot", "Courses and Certificates", "Blogs"]  # Add more pages as needed
    choice = st.sidebar.radio("Go to", pages, key="navigation")

    # Sections with anchors for navigation
    if choice == "About me":
        st_display_home()
    elif choice == "Career Snapshot":
        pdf_github_url = "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/CV_Akshay_Bhasme_ML.pdf"
        images = pdf_github_to_images(pdf_github_url)
        st_display_pdf(images)

    elif choice == "Courses and Certificates":
        certificates = [
            {
                "course_name": "Applied Machine Learning Course",
                "certificate_pdf": "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/Applie%20AI.pdf",
                "credentials": "https://www.appliedaicourse.com/certificate/902eadbdec",
                'certificate_image':"https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/cert_images/appliedai.jpeg"
            },
            {
                "course_name": "Python (Basic) Certificate",
                "certificate_pdf": "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/python_basic%20certificate.pdf",
                "credentials": "https://www.hackerrank.com/certificates/7ff0e9842ae8",
                'certificate_image':"https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/cert_images/python.jpeg"
            },
            {
                "course_name": "SQL (Basic) Certificate",
                "certificate_pdf": "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/sql_basic%20certificate.pdf",
                "credentials": "https://www.hackerrank.com/certificates/1aaf4b4e8057",
                'certificate_image':"https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/cert_images/sql.jpeg"
            },
            {
                "course_name": "Prompt Engineering for ChatGPT",
                "certificate_pdf": "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/PrompEngineeringForChatGPT.pdf",
                "credentials": "https://www.coursera.org/account/accomplishments/certificate/3U8XGSFYA74H",
                'certificate_image':"https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/cert_images/gpt.jpeg"
            },
            {
                "course_name": "Hands-on Machine Learning with AWS and NVIDIA",
                "certificate_pdf": "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/HandsOnMachineLearning.pdf",
                "credentials": "https://www.coursera.org/account/accomplishments/certificate/FYB8KV6CKWZH",
                'certificate_image':"https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/cert_images/aws.jpeg"
            },
            # Add more courses
        ]
        
        st_display_certificates(certificates)
        
    elif choice == "Blogs":
        blogs = [
            {
                "title": "Exploring Emotions with BERT -Transfer Learning: Your Guide to Sentiment Analysis",
                "read_more_link": "https://medium.com/@akshaybhasme30/exploring-emotions-with-bert-transfer-learning-your-guide-to-sentiment-analysis-6c260f9c1de5",
                "blog_image": "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/blog_images/Exploringemotions.jpeg"
            },
            {
                "title": "Unleashing the Power of Deep Learning: Exploring LSTM on the Donors Choose Dataset",
                "read_more_link": "https://medium.com/@akshaybhasme30/unleashing-the-power-of-deep-learning-exploring-lstm-on-the-donors-choose-dataset-771951df6600",
                "blog_image":"https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/blog_images/unleashingthepower.jpeg"
            },
            {
                "title": "Exploring Linear Regression-OLS: Clearing Misconceptions Surrounding It",
                "read_more_link": "https://medium.com/@akshaybhasme30/exploring-linear-regression-ols-clearing-misconceptions-surrounding-it-a5b21fe2c48a",
                "blog_image": "https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/blog_images/exploringlinearreg.jpeg"
            },
            {
                "title": "Common Mistakes to Avoid in Model Building: Insights from a Data Scientist’s Journey",
                "read_more_link": "https://medium.com/@akshaybhasme30/common-mistakes-to-avoid-in-model-building-insights-from-a-data-scientists-journey-dc3fbfb70925",
                "blog_image":"https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/blog_images/commonmistakes.jpeg"
            },
            {
                "title": "Principal component analysis (PCA)",
                "read_more_link": "https://medium.com/@akshaybhasme30/principal-component-analysis-pca-d6de7a53efa7",
                "blog_image":"https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/blog_images/pca.png"
            },
            {
                "title": "How to create Jupyter Notebook instance on Google Cloud Platform (GCP)",
                "read_more_link": "https://medium.com/@akshaybhasme30/how-to-create-jupyter-notebook-instance-on-google-cloud-platform-gcp-3e74061dd869",
                "blog_image":"https://raw.githubusercontent.com/Akshay-Bhasme/my_profile/main/blog_images/gcp.jpeg"
            },
            
            
            # Add more blogs
        ]
            
        st_display_blogs(blogs)

if __name__ == "__main__":
    main()
