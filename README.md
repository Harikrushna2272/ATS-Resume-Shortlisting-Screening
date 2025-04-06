# 📄 ATS (Applicant Tracking System) Project

This repository contains an **Applicant Tracking System (ATS)** designed for HR managers to screen and rank resumes based on job descriptions. The system integrates a **Streamlit-based dashboard** with an **n8n workflow** to process resumes stored in Google Drive folders.

> 🛠️ Developed as a technical task for Step AI.

---

## 🚀 Overview

- **Front-End**: A Streamlit application (`app.py`) allows HR managers to input job descriptions (Text, HTML, or PDF) and select a job category, triggering the ATS workflow via a webhook.
- **Back-End**: An n8n workflow retrieves resumes from Google Drive, applies cutting-edge ranking algorithms, and returns detailed results, optimized for scalability and accuracy.
- **Goal**: Screen and rank data from a specified Google Drive folder and after process through AI agents give result in terms of score and rank of person.

---

## ✅ Prerequisites

### 📦 Streamlit
- **Python**: Version 3.8+

#### Required Python Libraries
- `streamlit`
- `requests`
- `json`
- `pandas`
- `beautifulsoup4`
- `pypdf`

Install with:

```bash
pip install streamlit requests pandas beautifulsoup4 pypdf
# ATS-Resume-Shortlisting-Screening
