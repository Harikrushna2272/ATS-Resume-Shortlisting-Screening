# 📄 ATS (Applicant Tracking System) Project

This repository contains an **Applicant Tracking System (ATS)** designed for HR managers to screen and rank resumes based on job descriptions. The system integrates a **Streamlit-based dashboard** with an **n8n workflow** to process resumes stored in Google Drive folders.

> 🛠️ Developed as a technical task for Step AI.

---

🚀 Key Enhancements
Feature	Description
🤖 AI Integration	Leverages Google Gemini Chat to perform intelligent and context-aware resume scoring based on the job description.
🔁 Dual-Loop Efficiency	Two-phase looping mechanism: one for downloading all files and another for refining scoring with contextual feedback.
📊 Dynamic Scoring	Uses multiple Code nodes for progressive scoring logic, enriched with Gemini Chat for enhanced ranking.
🧠 Smart Merging	Applies contextual filters before merging resumes, ensuring only relevant files are included in the output.
⚡ Real-Time Processing	Extracts text, formats data, and applies scoring logic in real-time as files are streamed from Google Drive.
🚀 Optimized Flow	Conditional branches and routing streamline processing paths for PDFs, HTML, or text files dynamically.
🛡️ Robustness	Implements parallel execution and error-handling nodes for stable processing, even with corrupted or unsupported files.
📦 Output Excellence	Responses are tailored and compressed, reducing size while preserving ranking insights and metadata.

---

## 🚀 Overview

- **Front-End**: A Streamlit application (`app.py`) allows HR managers to input job descriptions (Text, HTML, or PDF) and select a job category, triggering the ATS workflow via a webhook.
<img width="1470" alt="Screenshot 2025-04-06 at 5 16 49 PM" src="https://github.com/user-attachments/assets/84e813fc-8261-4dd1-bf1e-34187d89ec49" />

- **Back-End**: An n8n workflow retrieves resumes from Google Drive, applies cutting-edge ranking algorithms, and returns detailed results, optimized for scalability and accuracy:
 beyond simple keywords. This enhances scoring accuracy and could generate interview questions, setting your workflow apart as a modern HR tool.
<img width="1265" alt="Screenshot 2025-04-06 at 5 13 56 PM" src="https://github.com/user-attachments/assets/768c2f1f-dbe6-490d-a1ba-f913e2e1e1ed" />


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
