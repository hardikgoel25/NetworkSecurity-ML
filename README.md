
# Phishing-URL Detector – API + Streamlit Frontend

🌐 **Live Demo:** [Streamlit App (Frontend + Real-Time Prediction UI)](https://networksecurity-ml-ndqg2eobfmuehsnzyufhzm.streamlit.app/)

---

## 📖 Project Overview

**Phishing-URL Detector** is a full-stack Machine Learning project designed to **detect whether a website URL is phishing or legitimate**. It integrates end-to-end ML pipelines, robust preprocessing, model training, evaluation, and a user-friendly frontend for real-time URL analysis.

**Key Highlights:**

- **End-to-End ML Pipelines:** URL feature extraction, preprocessing, model training, and evaluation.  
- **Real-Time Prediction UI:** Streamlit interface for live phishing URL detection.  
- **Reusable Utilities:** Tools for data validation, model saving/loading, and evaluation metrics.  
- **Deployment Ready:** Supports local execution, Docker, or Streamlit Cloud deployment.

---

## ⚙️ Tech Stack

- **Backend & Pipelines:** Python 3.12+, custom ML pipelines for URL analysis  
- **Frontend:** Streamlit (Hosted on Streamlit Cloud)  
- **Modeling:** Scikit-learn, Pandas, NumPy  
- **Deployment:** Streamlit Cloud for frontend and live predictions

---

## 📂 Project Structure

```
NetworkSecurity-ML/
├── .github/                   # GitHub Actions workflows
│   └── workflows/             # CI/CD pipeline configurations
├── NetworkSec/                # Core machine learning and utility modules
│   ├── entity/                # Configuration & artifact entities
│   ├── exception/             # Custom exception handling
│   ├── logging/               # Logging utilities
│   ├── pipeline/              # End-to-end ML pipeline scripts
│   ├── components/            # Data transformation,validation,ingestion and model training
│   └── constants/             # Configuration constants
├── Network_Data/              # Raw network traffic data
├── data_schema/               # Schema for data validation
├── final_model/               # Trained ML model artifacts
├── prediction_output/         # Output predictions from the model
├── templates/                 # HTML templates for the web app
├── valid_data/                # Cleaned and validated data for the model
├── .gitignore                 # Git ignore file
├── DockerFile                 # Dockerfile for containerized deployment
├── README.md                  # Project documentation
├── api_app.py                 # Flask backend for API access
├── app.py                     # Main application script
├── main.py                    # Main script for running the ETL and model training pipeline
├── push_data.py               # Script for inserting data into MongoDB
├── requirements.txt           # Python dependencies
├── setup.py                   # Installation script for the project
└── test_mongodb.py            # Tests for MongoDB integration
└── services/                  # Demo Implementations for phishing Url detector         

```

---

## 🔑 Environment Variables

For local development, create a `.env` file (not committed) with:

```
MODEL_PATH=final_model/network_model.pkl
LOG_LEVEL=INFO
```

- `MODEL_PATH`: Path to the trained ML model.  
- `LOG_LEVEL`: Logging level for pipeline runs (e.g., INFO, DEBUG).

---

## ▶️ Running Locally

**Clone the Repository:**

```bash
git clone https://github.com/hardikgoel25/NetworkSecurity-ML.git
cd NetworkSecurity-ML
```

**Install Dependencies:**

```bash
pip install -r requirements.txt
```

**Run the Streamlit App:**

```bash
streamlit run app/ui_app.py
```

The app will launch at [http://localhost:8501](http://localhost:8501).

**Optional:** Run the ML Pipeline manually:

```bash
python -m NetworkSec.pipeline.run_pipeline
```

---

## 🚀 Deployment Notes

- **Streamlit App:** Deployed at [Live Demo](https://networksecurity-ml-ndqg2eobfmuehsnzyufhzm.streamlit.app/)  
- **Pipelines:** Modular design, easily integrated with backend or API systems.  
- **Docker Deployment:**

```bash
docker build -t phishing-url-detector .
docker run -p 8501:8501 phishing-url-detector
```

---

## 🧪 Usage

1. **Input URL:** Enter a website URL via the Streamlit UI.  
2. **Model Prediction:** System predicts whether the URL is phishing or legitimate in real-time.  
3. **Explore Pipelines:** Review intermediate artifacts like feature-engineered data, evaluation metrics, and saved models.  
4. **API Access:** Leverage backend utilities for integration with other services.

---

## 📊 Key Components

| Component      | Purpose                                           |
|----------------|--------------------------------------------------|
| `ui_app.py`     | Streamlit interface for real-time URL predictions |
| `pipeline/`     | End-to-end ML pipelines for training & deployment |
| `services/`     | URL feature extraction, preprocessing & ML utilities |
| `final_model/`  | Trained ML model artifacts                       |
| `entity/`       | Configuration and artifact entity definitions  |
| `exception/`    | Custom exception handling                       |
| `logging/`      | Centralized logging for pipelines and utilities|

---

## 👤 Author

Developed by **Hardik Goel**
