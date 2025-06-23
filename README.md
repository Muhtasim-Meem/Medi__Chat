# 💊 BD Medicine Chatbot (Powered by Gemini API)

A chatbot built with a Large Language Model (LLM) using the **Gemini API** to assist users with Bangladeshi medicine-related information. It intelligently processes and interacts with 6 structured CSV datasets to provide accurate, context-aware responses.

---

## 🚀 Features

- 🧠 AI-powered chatbot using Gemini LLM
- 📊 Uses 6 CSV files related to Bangladeshi medicine
- 🔍 Real-time Q&A and support based on structured medical data
- 🖥️ Easy to set up and run locally

---

## 📁 Dataset Overview

This project uses 6 CSV files for medicine-related information, such as:

1. **medicine.csv**
2. **dosage.csv**
3. **side_effects.csv**
4. **disease_mapping.csv**
5. **manufacturer.csv**
6. **alternative_medicine.csv**

> Make sure all CSV files are located in a `Data/` directory in the project root.

---

## 🛠️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/bd-medicine-chatbot.git
cd bd-medicine-chatbot
```
### Step 2: Install Requirements
It's recommended to use a virtual environment:

```bash
pip install -r requirements.txt
```
### Step 3: Add Your Gemini API Key
Create a .env file in the project root and add:

env
GEMINI_API_KEY=your_gemini_api_key_here
Or update directly in the config file if applicable.

### ▶️ Run the Chatbot
Start the chatbot by running:

```bash

python app.py
```
### 🧠 How It Works
The chatbot loads and processes data from the six CSV files.

It leverages the Gemini API to provide intelligent and context-aware answers.

It supports queries like:

“What is the dosage of Napa for adults?”

“List alternatives for Seclo.”

“What are the side effects of Monas?”
