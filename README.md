# AI for Mineral Targeting - India AI Hackathon 2025

## Overview
This project leverages AI/ML to identify potential mineral-rich zones in Karnataka and Andhra Pradesh using multi-parametric data from the Geological Survey of India (GSI). It was developed for the IndiaAI Hackathon 2025, focused on accelerating mineral exploration in India through technology.

## Problem Statement
Traditional mineral exploration methods are costly, slow, and often fail to detect deep or hidden deposits. The goal was to develop a data-driven solution to:
- Automate geoscience data analysis
- Predict mineral zones for REE, copper, and gold
- Provide interpretable and scalable results for future use

## Solution Highlights
- Supervised learning (Random Forest, Neural Networks) for classification
- Unsupervised learning (K-Means, DBSCAN) for anomaly detection
- Feature engineering with lithology, magnetic anomalies, REE concentrations
- Visualization with heatmaps and 3D subsurface models (QGIS/ArcGIS)
- One-hot encoding and missing value imputation in preprocessing pipeline

## Tech Stack
- Python, pandas, scikit-learn, seaborn
- QGIS, ArcGIS for visualization
- Jupyter Notebooks for EDA
- GitHub for collaboration and version control

## Setup Instructions
```bash
# Clone the repository
git clone https://github.com/gnaaneswaran/ai-mineral-targeting.git
cd ai-mineral-targeting

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python preprocess.py
python model.py
python visualize.py
