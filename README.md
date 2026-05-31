# 🍔 AI Restaurant Concept Builder

A modern, dynamic web application powered by **Streamlit** and **LangChain** that helps culinary entrepreneurs build a complete brand identity in seconds. By analyzing selected user preferences, the application leverages **ChatGroq** and cloud generation pipelines to deliver instant restaurant names and curated menus.

---

## ✨ Features

*   **Custom Sidebar Parameters**: Tailor your brand concept using three distinct interactive controls:
    *   **Cuisine Selection**: Choose from popular global food profiles.
    *   **Price Point Filters**: Set tier levels ranging from budget-friendly bistros to high-end fine dining.
    *   **Design Ambiance Themes**: Define the visual layout aesthetic (e.g., Minimalist, Vintage, Neon).
*   **Intelligent Brand Copywriting**: Generates a unified restaurant title and a custom 5-course menu 
*   **Modern LCEL Architecture**: Built using the latest **LangChain Expression Language (LCEL)** pipe (`|`) syntax to minimize execution latency.

---

## 🚀 Tech Stack

*   **Frontend Interface**: Streamlit
*   **LLM Orchestration**: LangChain Core / LangChain Groq
*   **Inference Engine**: ChatGroq (`llama3-70b-8192`)
*   **Image Generation**: Pollinations API Engine (No-Auth CDN wrapper)

---

## 🛠️ Local Setup Instructions

Follow these step-by-step instructions to clone and deploy this project locally on your machine.

### 1. Prerequisites
Ensure you have Python 3.10+ installed on your computer.

### 2. Clone the Repository
```bash
git clone https://github.com
cd Restaurant_Concept_Builder
```

### 3. Initialize and Activate Virtual Environment
```powershell
# Create environment
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
*(If you do not have a requirements.txt file, manually run: `pip install streamlit langchain-core langchain-groq python-dotenv`)*

### 5. Configure Your API Secrets
Create a file named exactly `SecretKey.env` in the root folder directory and add your active Groq access token credentials:
```text
GROQ_API_KEY=gsk_your_actual_groq_key_here
```

### 6. Launch the Server Application
```powershell
streamlit run RestaurantConceptBuilder.py
```

---

## 📌 Usage Flow Demonstration

1. Open the sidebar configuration interface on the left-hand screen panel.
2. Select your desired target **Cuisine Type**, **Price Category**, and **Ambiance Theme**.
3. Review your newly created brand typography and detailed menu side-by-side!
