import streamlit as st 
import requests # requests is used for making HTTP requests
import json # json is used for handling JSON data
import pandas as pd
from bs4 import BeautifulSoup # BeautifulSoup is used for parsing HTML
import pypdf as PyPDF2 # PyPDF2 is used for reading PDF files and extracting text

# n8n webhook URL through which the ATS will send job descriptions and receive ranked resumes
N8N_WEBHOOK_URL = "https://workforce2272.app.n8n.cloud/webhook-test/ats-trigger"

# Predefined job categories and their Google Drive folder IDs
JOB_CATEGORIES = {
    "INFORMATION-TECHNOLOGY": "1a-kJI6aOWSuv_Ll93UjWWeoLqtqzYgli",
    # "INFORMATION-TECHNOLOGY": "INFORMATION-TECHNOLOGY",
    "Marketing": "Marketing"
}

st.set_page_config(page_title="ATS Dashboard", layout="wide")
st.title("ATS Dashboard for HR Managers")
st.markdown("Screen resumes based on job requirements and category.")

# Step 1: Job description input
st.subheader("Step 1: Input Job Description")
input_type = st.radio("Choose Input Format", ["Text", "HTML", "PDF"], key="input_type")
job_desc = None

# if input_type == "Text":
if input_type == "Text":
    job_desc = st.text_area(
        "Enter Job Description",
        placeholder="e.g., Seeking an accountant with 3+ years of experience...",
        height=150,
        key="text_input"
    )
# if input_type == "HTML":
elif input_type == "HTML":
    html_file = st.file_uploader("Upload HTML Job Description", type=["html"], key="html_upload")
    if html_file:
        soup = BeautifulSoup(html_file.read(), "html.parser")
        job_desc = soup.get_text(separator=" ").strip()
        st.success("HTML processed!")
# if input_type == "PDF":
elif input_type == "PDF":
    pdf_file = st.file_uploader("Upload PDF Job Description", type=["pdf"], key="pdf_upload")
    if pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        job_desc = " ".join(page.extract_text() for page in pdf_reader.pages if page.extract_text()).strip()
        st.success("PDF processed!")

# Step 2: Select job category
st.subheader("Step 2: Select Job Category")
job_category = st.selectbox("Choose a Job Category", list(JOB_CATEGORIES.keys()), key="category_select")

# Step 3: Trigger screening
if st.button("Screen Resumes", key="screen_button", disabled=not (job_desc and job_category)):
    with st.spinner("Processing resumes from {} folder...".format(job_category)):
        # Prepare the payload for n8n webhook, including job description and folder ID
        payload = {
            "jobDescription": job_desc,
            "folderId": JOB_CATEGORIES[job_category]
        }
        
        try:
            
            response = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=120)
            response.raise_for_status()
            results = response.json()

            # Check if the response contains a list of results
            if isinstance(results, list) and results:
                df = pd.DataFrame(results)
                st.subheader("Step 3: Ranked Resumes")
                st.markdown(f"Top candidates for {job_category} role:")
                # Display the top 10 candidates
                st.dataframe(
                    df[["rank", "filename", "totalScore"]].style.format({"totalScore": "{:.1f}"}),
                    use_container_width=True
                )
                
                st.subheader("Detailed Breakdown")
                # Display detailed breakdown for each candidate
                for _, row in df.iterrows():
                    with st.expander(f"Rank {row['rank']}: {row['filename']} (Score: {row['totalScore']})"):
                        st.json(row["breakdown"])
            else:
                st.warning("No resumes found or processed.")
        except Exception as e:
            st.error(f"Error: {e}")

# Slidebar information
st.sidebar.header("HR Guide")
st.sidebar.markdown("""
1. **Enter Job Description**: Use text, HTML, or PDF.
2. **Select Category**: Choose Accounting or Marketing.
3. **Screen Resumes**: Click to rank candidates from the selected folder.
""")