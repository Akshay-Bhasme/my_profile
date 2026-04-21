from pathlib import Path

import fitz
import streamlit as st
from PIL import Image


BASE_DIR = Path(__file__).resolve().parent
RESUME_PATH = BASE_DIR / "CV_Akshay_Bhasme_ML.pdf"
PROFILE_IMAGE_PATH = BASE_DIR / "dp1.jpg"

AWARD_IMAGES = [
  {
    "path": BASE_DIR / "EE2A4181.jpg",
    "caption": "Choreos'22 Newbie In The Spotlight",
  },
  {
    "path": BASE_DIR / "EE2A4658.jpg",
    "caption": "Choreos'22 Newbie In The Spotlight",
  },
  {
    "path": BASE_DIR / "Picsart_23-09-23_16-30-31-629.jpg",
    "caption": "Choreos'22 Newbie In The Spotlight",
  },
  {
    "path": BASE_DIR / "IMG-20221212-WA0014.jpg",
    "caption": "Choreos'22 Newbie In The Spotlight",
  },
]

CERTIFICATES = [
  {
    "course_name": "Applied Machine Learning Course",
    "certificate_pdf": BASE_DIR / "Applie AI.pdf",
    "credentials": "https://www.appliedaicourse.com/certificate/902eadbdec",
    "certificate_image": BASE_DIR / "cert_images" / "appliedai.jpeg",
  },
  {
    "course_name": "Python (Basic) Certificate",
    "certificate_pdf": BASE_DIR / "python_basic certificate.pdf",
    "credentials": "https://www.hackerrank.com/certificates/7ff0e9842ae8",
    "certificate_image": BASE_DIR / "cert_images" / "python.jpeg",
  },
  {
    "course_name": "SQL (Basic) Certificate",
    "certificate_pdf": BASE_DIR / "sql_basic certificate.pdf",
    "credentials": "https://www.hackerrank.com/certificates/1aaf4b4e8057",
    "certificate_image": BASE_DIR / "cert_images" / "sql.jpeg",
  },
  {
    "course_name": "Prompt Engineering for ChatGPT",
    "certificate_pdf": BASE_DIR / "PrompEngineeringForChatGPT.pdf",
    "credentials": "https://www.coursera.org/account/accomplishments/certificate/3U8XGSFYA74H",
    "certificate_image": BASE_DIR / "cert_images" / "gpt.jpeg",
  },
  {
    "course_name": "Hands-on Machine Learning with AWS and NVIDIA",
    "certificate_pdf": BASE_DIR / "HandsOnMachineLearning.pdf",
    "credentials": "https://www.coursera.org/account/accomplishments/certificate/FYB8KV6CKWZH",
    "certificate_image": BASE_DIR / "cert_images" / "aws.jpeg",
  },
]
# For the blogs, you can add more entries to the BLOGS list as needed.
BLOGS = [
  {
    "title": "Exploring Emotions with BERT -Transfer Learning: Your Guide to Sentiment Analysis",
    "read_more_link": "https://medium.com/@akshaybhasme30/exploring-emotions-with-bert-transfer-learning-your-guide-to-sentiment-analysis-6c260f9c1de5",
    "blog_image": BASE_DIR / "blog_images" / "Exploringemotions.jpeg",
  },
  {
    "title": "Unleashing the Power of Deep Learning: Exploring LSTM on the Donors Choose Dataset",
    "read_more_link": "https://medium.com/@akshaybhasme30/unleashing-the-power-of-deep-learning-exploring-lstm-on-the-donors-choose-dataset-771951df6600",
    "blog_image": BASE_DIR / "blog_images" / "unleashingthepower.jpeg",
  },
  {
    "title": "Exploring Linear Regression-OLS: Clearing Misconceptions Surrounding It",
    "read_more_link": "https://medium.com/@akshaybhasme30/exploring-linear-regression-ols-clearing-misconceptions-surrounding-it-a5b21fe2c48a",
    "blog_image": BASE_DIR / "blog_images" / "exploringlinearreg.jpeg",
  },
  {
    "title": "Common Mistakes to Avoid in Model Building: Insights from a Data Scientist’s Journey",
    "read_more_link": "https://medium.com/@akshaybhasme30/common-mistakes-to-avoid-in-model-building-insights-from-a-data-scientists-journey-dc3fbfb70925",
    "blog_image": BASE_DIR / "blog_images" / "commonmistakes.jpeg",
  },
  {
    "title": "Principal component analysis (PCA)",
    "read_more_link": "https://medium.com/@akshaybhasme30/principal-component-analysis-pca-d6de7a53efa7",
    "blog_image": BASE_DIR / "blog_images" / "pca.png",
  },
  {
    "title": "How to create Jupyter Notebook instance on Google Cloud Platform (GCP)",
    "read_more_link": "https://medium.com/@akshaybhasme30/how-to-create-jupyter-notebook-instance-on-google-cloud-platform-gcp-3e74061dd869",
    "blog_image": BASE_DIR / "blog_images" / "gcp.jpeg",
  },
]


@st.cache_data(show_spinner=False)
def pdf_to_images(pdf_path: Path):
  images = []
  pdf_document = fitz.open(pdf_path)
  try:
    for page_num in range(pdf_document.page_count):
      page = pdf_document.load_page(page_num)
      image = page.get_pixmap(matrix=fitz.Matrix(2, 2))
      pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
      images.append(pil_image)
  finally:
    pdf_document.close()
  return images


def file_bytes(file_path: Path) -> bytes:
  return file_path.read_bytes()


def st_display_pdf(images):
  st.title("Career Snapshot")
  st.download_button(
    "Download Resume PDF",
    data=file_bytes(RESUME_PATH),
    file_name=RESUME_PATH.name,
    mime="application/pdf",
  )
  st.write("Email: akshaybhasme30@gmail.com")
  st.write("Mobile No: +91 7972014093")
  st.write("GitHub: https://github.com/Akshay-Bhasme")
  st.write("LinkedIn: www.linkedin.com/in/akshaybhasme30")
  for index, image in enumerate(images, start=1):
    st.image(image, caption=f"Page {index}", use_container_width=True)
  st.download_button(
    "Download Resume PDF Again",
    data=file_bytes(RESUME_PATH),
    file_name=RESUME_PATH.name,
    mime="application/pdf",
    key="resume_download_bottom",
  )


def st_display_certificates(certificates):
  st.title("Courses and Certificates")
  for certificate in certificates:
    st.write(f"## {certificate['course_name']}")
    st.image(
      str(certificate["certificate_image"]),
      caption=f"Certificate for {certificate['course_name']}",
      width=400,
    )
    st.write(f"**Credentials**: {certificate['credentials']}")
    st.download_button(
      f"Download {certificate['course_name']} PDF",
      data=file_bytes(certificate["certificate_pdf"]),
      file_name=certificate["certificate_pdf"].name,
      mime="application/pdf",
      key=f"cert_{certificate['course_name']}",
    )
    st.write("---")


def st_display_blogs(blogs):
  st.title("My Blogs on Medium")
  for blog in blogs:
    st.write(f"## {blog['title']}")
    st.image(str(blog["blog_image"]), caption=f"Image for {blog['title']}", width=300)
    st.write(f"[Read More]({blog['read_more_link']})")


def st_display_home():
  st.title("Welcome to My Portfolio")
  st.image(str(PROFILE_IMAGE_PATH), width=150)
  st.write("## About Me")
  st.write(
    """**Hey, I'm Akshay, a seasoned Data Scientist**.
What really gets me going is solving puzzles. From my early days, I have always enjoyed solving puzzles, and that's exactly how I approach large data sets. It's one giant puzzle waiting to be solved. My thrill comes from spotting patterns that others might overlook.
I've been doing data science work for over five years across insurance, software, and media. My strength is taking complicated problems and turning them into practical solutions with a strong user experience.
Welcome to my area of expertise: Data Science and ML solutions."""
  )
  st.subheader("Awards and Recognitions")
  st.write("GroupM Choreos Awards 2022: Newbie In The Spotlight")
  award_tabs = st.tabs([f"Award {index}" for index in range(1, len(AWARD_IMAGES) + 1)])
  for tab, award in zip(award_tabs, AWARD_IMAGES):
    with tab:
      st.image(str(award["path"]), caption=award["caption"], use_container_width=True)


def main():
  st.set_page_config(
    page_title="My Portfolio App",
    layout="wide",
    initial_sidebar_state="expanded",
  )
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
  pages = ["About me", "Career Snapshot", "Courses and Certificates", "Blogs"]
  choice = st.sidebar.radio("Go to", pages, key="navigation")

  if choice == "About me":
    st_display_home()
  elif choice == "Career Snapshot":
    images = pdf_to_images(RESUME_PATH)
    st_display_pdf(images)
  elif choice == "Courses and Certificates":
    st_display_certificates(CERTIFICATES)
  elif choice == "Blogs":
    st_display_blogs(BLOGS)


if __name__ == "__main__":
  main()
