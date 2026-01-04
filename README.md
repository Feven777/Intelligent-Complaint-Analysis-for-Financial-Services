# Intelligent Complaint Analysis for Financial Services

## 📌 Project Overview
This project implements an **end-to-end intelligent complaint analysis pipeline** for large-scale financial consumer complaint data. It focuses on transforming unstructured complaint narratives into high-quality semantic embeddings and storing them in a vector database to enable advanced NLP tasks such as semantic search, clustering, and retrieval-augmented generation (RAG).

The project follows **industry-standard machine learning and software engineering practices**, emphasizing reproducibility, modular design, and evidence-based data preprocessing.

---

## 🎯 Objectives
- Clean and preprocess millions of real-world financial complaint records
- Perform exploratory data analysis (EDA) to understand narrative characteristics
- Generate semantic embeddings from complaint narratives using transformer models
- Chunk long complaint texts to preserve contextual meaning
- Store embeddings in a vector database for efficient similarity search
- Provide a scalable foundation for downstream intelligent analytics

---

## 📂 Dataset
The dataset consists of consumer complaints related to financial products such as credit reporting, debt collection, mortgages, and banking services.

### Key Characteristics
- **Raw size:** ~9.6 million records  
- **Cleaned size:** ~1.6 million records  
- **Text field:** Consumer complaint narrative  
- **Selected products:**
  - Credit reporting or other personal consumer reports
  - Debt collection
  - Checking or savings account
  - Mortgage
  - Credit card

Only complaints with sufficiently long narratives are retained to ensure high-quality semantic representations.

---

## 🧠 Methodology

### 1. Data Cleaning & Preprocessing
- Removal of records with missing complaint narratives
- Narrative length filtering (minimum word threshold)
- Product category filtering for relevance and data balance
- Feature engineering (narrative word count)

### 2. Exploratory Data Analysis (EDA)
- Distribution analysis of complaint narrative lengths
- Product-wise complaint distribution analysis

### 3. Text Chunking
To handle long complaint narratives:
- **Chunk size:** 400 characters
- **Chunk overlap:** 50 characters

This ensures semantic continuity and compatibility with transformer-based models.

### 4. Embedding Generation
- **Model:** `sentence-transformers/all-MiniLM-L6-v2`
- **Embedding dimension:** 384

The model provides a strong balance between semantic performance and computational efficiency.

### 5. Vector Store
- **Vector database:** Chroma
- **Stored objects:** Embedded text chunks  
- Enables fast semantic similarity search and retrieval

---

## 🏗️ Project Structure
Intelligent-Complaint-Analysis-for-Financial-Services/
│
├── data/
│ ├── raw/ # Raw complaint dataset
│ └── processed/ # Cleaned and processed data
│
├── notebooks/
│ └── eda_task1.ipynb # EDA and preprocessing evidence
│
├── src/
│ ├── data_loader.py # Data loading and cleaning logic
│ ├── chunking.py # Text chunking utilities
│ ├── embedding.py # Embedding model loader
│ ├── vector_store.py # Vector store interface
│ ├── build_embeddings.py # End-to-end embedding pipeline
│ └── config.py # Project configuration
│
├── README.md # Project documentation
└── requirements.txt # Python dependencies
# ⚙️ Setup & Installation

1. **Clone the repository**


git clone https://github.com/your-username/Intelligent-Complaint-Analysis-for-Financial-Services.git
cd Intelligent-Complaint-Analysis-for-Financial-Services

# Create a virtual environment

# Linux / macOS
python -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate

# Install dependencies

pip install -r requirements.txt

## 🚀 Usage
# 1. Run Exploratory Data Analysis (EDA)

notebooks/eda_task1.ipynb

# 2. Build Embeddings & Vector Store

python -m src.build_embeddings
