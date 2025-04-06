# 📄 ATS (Applicant Tracking System) Project

This repository contains an **Applicant Tracking System (ATS)** designed for HR managers to screen and rank resumes based on job descriptions. The system integrates a **Streamlit-based dashboard** with an **n8n workflow** to process resumes stored in Google Drive folders.

> 🛠️ Developed as a technical task for Step AI.

---

## 🚀 Overview

- **Front-End**: A Streamlit application (`app.py`) allows HR managers to input job descriptions (Text, HTML, or PDF) and select a job category, triggering the ATS workflow via a webhook.
- **Back-End**: An n8n workflow retrieves resumes from Google Drive, applies cutting-edge ranking algorithms, and returns detailed results, optimized for scalability and accuracy.
+ One standout innovation is the "Google Gemini Chat" node, integrating AI-powered scoring into the ATS process. This node likely uses Google’s generative AI for NLP, analyzing resume text and job descriptions to assess context and relevance beyond simple keywords. This enhances scoring accuracy and could generate interview questions, setting your workflow apart as a modern HR tool.
  
+ The dual-loop architecture, with two "Loop Over Items" nodes, is another creative feature. The first loop downloads all 50+ PDFs, fixing the 1-PDF issue, while the second refines scores post-merge, addressing the 10-PDF limit. This two-phase strategy ensures comprehensive processing and adaptability for large datasets.

The use of multiple "Code" nodes before and after "Merge" introduces a dynamic scoring system. The first node might handle initial keyword matching, while the second refines scores with AI insights, creating a hybrid model. This flexibility adapts to diverse job descriptions and supports future enhancements.

The "Merge" node, enhanced by "Switch" and "Code" nodes, offers a smart aggregation technique. The "Switch" filters low-scoring resumes, and the "Code" optimizes the merge, resolving the 10-PDF limit. This “smart merge” prioritizes top candidates, improving HR efficiency.

The "Google Gemini Chat" node enables real-time text extraction and scoring from PDF binaries. It parses content on-the-fly, aligning it with the job description, eliminating manual extraction. This scalable AI integration handles unstructured data, adding a unique efficiency to the workflow.

The "Switch" and "Replace" nodes optimize data flow management. "Switch" routes data based on score thresholds, while "Replace" standardizes or enriches it, adapting to 50+ PDFs. This self-regulating design enhances robustness and flexibility for large-scale use.

Parallel processing and error handling, implied by the structure and "Switch" nodes, boost resilience. Parallel execution speeds up 50+ PDF processing, while "Switch" offers fallback paths for errors. This proactive design ensures reliability for enterprise-level deployments.

The final "Merge," "Edit Fields," and "Respond to Webhook" nodes optimize output. "Edit Fields" formats the ranked list (e.g., rank, totalScore) for Streamlit, ensuring efficiency. This presentation intelligence enhances user experience, making it a thoughtful innovation.
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
