# Gold Price Prediction in Pakistan

## Overview
This project predicts gold prices in Pakistan using classical machine learning algorithms. The data consists of global gold prices scraped from the LBMA (24-karat), USD to PKR exchange rates, and local petrol prices. Multiple regression models (Linear Regression, Decision Tree, Random Forest, Gradient Boosting, and Support Vector Regressor) are trained and evaluated using metrics such as MSE, RMSE, MAE, and R². The best performing model is deployed in a Streamlit application that accepts user inputs and displays gold price predictions in various units (ounce, troy ounce, tola, or gram).

## Features
- **Data Collection & Preprocessing**: 
  - Scraping gold prices from LBMA.
  - Gathering exchange rates and petrol prices.
  - Standardizing date formats and merging datasets (262 rows of business-day data).
- **Modeling & Evaluation**:
  - Training multiple regression models.
  - Evaluating using Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R² score.
  - Comparison table to identify the best performing model.
- **Deployment**:
  - A Streamlit app for real-time predictions.
  - Unit conversion for output (ounce, troy ounce, tola, gram).

## Data
The dataset includes:
- **Date**: Business days in the format MM/DD/YYYY.
- **USD to PKR**: The exchange rate.
- **Global Gold Price (USD)**: Price per troy ounce.
- **24 Karat**: Local gold prices.
- **Petrol Price**: Local petrol prices.

## Models
The following regression models were evaluated:
- **Linear Regression**: Excellent performance (R² = 0.99).
- **Decision Tree Regression**
- **Random Forest Regression**
- **Gradient Boosting Regression**
- **Support Vector Regression**: Underperformed (R² = 0.00).

Based on evaluation metrics (MSE, RMSE, MAE, R²), **Linear Regression**, **Random Forest**, and **Gradient Boosting** performed best. For this project, the best model is saved and deployed for predictions.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gold-price-prediction.git
   cd gold-price-prediction
