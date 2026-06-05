# Indian Startup Funding Analysis Web App

## Overview

The Indian Startup Funding Analysis Web App is an interactive dashboard built using Streamlit that helps users explore and understand startup funding trends in India.

The application provides insights into funding patterns, investor activities, startup performance, sector-wise investments, funding stages, and geographical distribution of investments. It transforms raw startup funding data into meaningful visualizations that make analysis simple and accessible.

This project was developed to practice data analysis, data visualization, and web application development using Python.

---

## Problem Statement

Startup funding data contains valuable information about investment trends, investor behavior, emerging sectors, and growing startups. However, analyzing thousands of funding records manually can be difficult and time-consuming.

This project addresses that problem by providing a user-friendly dashboard where users can quickly explore the data and gain insights through interactive charts and visualizations.

---

## Features

### Overall Analysis

Provides a high-level overview of the Indian startup ecosystem.

Key metrics include:

* Total funding amount
* Maximum funding received by a startup
* Average funding per startup
* Total number of funded startups

Additional insights:

* Monthly funding trends
* Number of startups funded each month
* Top investment locations
* Sector-wise investment analysis
* Funding stage analysis
* Investment heatmaps and trend visualizations

---

### Investor Insights

Allows users to analyze the activities of a particular investor.

Features include:

* Recent investments
* Biggest investments made
* Sector-wise investment distribution
* Stage-wise investment distribution
* City-wise investment distribution
* Year-on-year investment trends
* Top startups funded by the investor

---

### Startup Insights

Provides startup-specific information and analysis.

Users can:

* Select a startup
* View funding details
* Explore investor participation
* Analyze funding history
* Understand growth trends

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Streamlit

### Data Visualization

* Line Charts
* Bar Charts
* Pie Charts
* Heatmaps

---

## Project Structure

```text
Indian-Startup-Funding-Web-App/
│
├── app.py
│
├── data/
│   ├── raw/
│   │   └── startup_funding_raw.csv
│   │
│   └── processed/
│       └── startup_data.csv
│
├── notebooks/
│   └── startup_funding_eda.ipynb
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

---

## Data Processing

Before building the dashboard, the dataset was cleaned and prepared using Python.

The preprocessing steps included:

* Handling missing values
* Standardizing city names
* Cleaning investor names
* Removing duplicate records
* Converting funding amounts into a consistent format
* Correcting date formats
* Creating additional columns such as Year and Month for analysis

---

## Visualizations Included

### Funding Trend Analysis

Shows how startup funding changes over time.

### Startup Activity Analysis

Displays the number of startups receiving funding across different periods.

### Geographical Analysis

Highlights cities that attract the highest investment.

### Sector Analysis

Identifies sectors receiving the highest funding and sectors with the most startup activity.

### Funding Stage Analysis

Compares funding amounts and deal counts across different funding rounds.

### Investor Analysis

Tracks investor behavior, preferred sectors, and investment patterns.

---

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/indian-startup-funding-web-app.git
```

### Step 2: Move to the Project Directory

```bash
cd indian-startup-funding-web-app
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Data visualization
* Streamlit web application development
* Dashboard design
* Handling real-world datasets
* Creating interactive analytical applications

---

## Future Improvements

Some features that can be added in future versions include:

* Advanced filtering options
* Search functionality
* Startup comparison feature
* Investor comparison dashboard
* Predictive funding analysis
* Deployment on Streamlit Cloud or AWS
* Interactive visualizations using Plotly

---

## Conclusion
This project demonstrates how data analytics and visualization techniques can be used to extract meaningful insights from startup funding data. The dashboard simplifies complex datasets and enables users to explore trends, investors, sectors, and startup performance through an intuitive web interface.
