# House Price Prediction Web Application

This is a web application built using Flask for predicting house prices based on user-inputted features. The application leverages machine learning models to provide accurate price predictions based on a dataset of house attributes.


# Exploratory Data Analysis (EDA) Pipeline

![EDA Pipeline](https://github.com/MUSTAKIMSHAIKH2942/Exploratory-Insight-Generator-/blob/main/EDA.png)  <!-- Add an image illustrating the EDA process -->

## Overview

The **Exploratory Data Analysis (EDA) Pipeline** is a comprehensive Python-based framework designed to facilitate the analysis of datasets. This pipeline automates the process of generating insightful summaries, visualizations, and reports that aid in understanding the underlying patterns and anomalies in the data.

## Key Features

- **Summary Statistics**: Automatically generates statistical summaries of the dataset.
- **Missing Values Analysis**: Identifies and visualizes missing data points.
- **Distribution Visualization**: Plots the distributions of numerical features for better insights.
- **Correlation Analysis**: Calculates and visualizes the correlation matrix of numerical variables.
- **Categorical Features Analysis**: Visualizes the distribution of categorical variables.

## Directory Structure   
"The project directory is organized as follows:"


![Directory Structure Pic](https://github.com/MUSTAKIMSHAIKH2942/House-Price-Prediction/blob/main/HPP-Leftpannel.PNG)



## Installation

To get started with the EDA Pipeline, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

   pip install -r requirements.txt
Usage
To run the EDA pipeline, execute the following command in your terminal:


python eda/eda_main.py "data/target/titanic"
Example
Assuming your project folder is structured correctly and contains the train.csv file, simply run:


python eda/eda_main.py "C:/Users/user/Desktop/ML - Code/Base/data"
Output
Upon successful execution, the following files will be generated in the data/eda_results directory:

report.md: A Markdown report summarizing the EDA findings.
Various PNG files corresponding to generated visualizations (e.g., distribution plots, correlation matrices).

<!-- Add a screenshot of the report or example visualizations -->

## Code Explanation
## 1. Main Script: eda_main.py
The main script controls the EDA process and performs the following tasks:

Imports Necessary Modules: This includes functions from various analysis modules.
Sets Up Logging: Configures logging to provide insights into the EDA process.
Generates Report: Collects results from various analyses and writes them into a Markdown report.
Key Functions
generate_report:

Creates a Markdown report that includes the summary, missing values, distributions, correlations, and categorical feature analysis.
Writes the report to data/eda_results/report.md.
run_all_eda:

Executes the EDA functions in sequence:
Calls run_summary for statistical analysis.
Calls run_missing_values_analysis to assess data completeness.
Calls run_distribution_visualization to create distribution plots.
Calls run_correlation_analysis for correlation matrix visualizations.
Calls run_categorical_analysis for categorical data insights.
Logging Information
The script utilizes Python's logging module to log the execution steps, making it easier to debug and track the process.

## 2. Individual Modules
data_summary.py:

Contains functions to calculate summary statistics of the dataset, such as mean, median, and standard deviation.
missing_values_analysis.py:

Analyzes the dataset for missing values and returns a structured summary.
distribution_visualization.py:

Generates visualizations (e.g., histograms, density plots) for each numerical feature to understand their distributions.
correlation_analysis.py:

Computes the correlation matrix and visualizes it using heatmaps to reveal relationships between numerical variables.
categorical_analysis.py:

Analyzes categorical features and produces count plots to visualize their distribution.
Contribution
Contributions to the EDA Pipeline are welcome! If you have suggestions or improvements, please create a pull request or open an issue.

## Acknowledgements
Inspired by various data analysis frameworks and the Python data science community.
Thanks to the libraries used: Pandas, NumPy, Matplotlib, and Seaborn for their invaluable contributions to data analysis and visualization.
Conclusion
This EDA pipeline provides a structured and automated approach to exploratory data analysis, making it easier to derive insights from datasets. By following the outlined steps, you can efficiently analyze your data and generate comprehensive reports.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Features

- User-friendly web interface for inputting house details.
- Model selection between Linear Regression, Random Forest, and XGBoost.
- Dynamic input fields based on the dataset.
- Missing value handling using median imputation.
- Real-time house price predictions based on user input.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Machine Learning**: Scikit-learn
- **Data Processing**: Pandas
- **Environment**: Virtualenv

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction
   
## Create a virtual environment (optional but recommended):


python -m venv .venv
Activate the virtual environment:

On Windows:

.venv\Scripts\activate
On macOS/Linux:

source .venv/bin/activate
Install required packages:

pip install -r requirements.txt
## Download the dataset:

Place the dataset (e.g., train.csv) in the appropriate directory as specified in the code.
Usage
Run the application:


python app.py
Access the web app: Open your web browser and navigate to http://127.0.0.1:5000/.

Input House Details:

Select the model type.
Fill in the required house features (e.g., LotFrontage, LotArea, MSSubClass).
Click on "Predict Price" to get the predicted house price.
How It Works
User Input: Users input house attributes via a web form.
Data Imputation: Missing values in the dataset are handled using median imputation.
Model Selection: The user selects a machine learning model for prediction.
Model Training: The chosen model is trained on the dataset.
Prediction: The model predicts the house price based on the input provided.
Display Result: The predicted price is displayed on the same web page.
Contributing
Contributions are welcome! If you want to contribute, please follow these steps:

![Directory Structure Pic](https://github.com/MUSTAKIMSHAIKH2942/House-Price-Prediction/blob/main/H_P_P.PNG

## Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.


### Instructions to Use:

1. **Create a file named `README.md`** in the root of your repository.
2. **Copy and paste the above code** into the `README.md` file.
3. **Replace the placeholder URL** (`https://github.com/yourusername/house-price-prediction.git`) with the actual URL of your GitHub repository.

Feel free to modify any sections to better reflect your project's specifics!
