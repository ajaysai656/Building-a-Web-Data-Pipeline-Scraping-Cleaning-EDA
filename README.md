#📱 Flipkart Smartphone Market Analysis
## End-to-End Web Data Pipeline: Scraping → Cleaning → Feature Engineering → EDA
🚀 Project Overview

This project builds a complete web data pipeline to analyze smartphone listings from Flipkart.

Instead of using a pre-collected dataset, I:

Scraped raw smartphone listing data using Python

Handled pagination across 40+ pages per brand group

Extracted structured information from messy HTML

Cleaned and standardized inconsistent data

Performed feature engineering using regular expressions (regex)

Merged multiple brand datasets into one analysis-ready dataset

Conducted Exploratory Data Analysis (EDA)

Generated business insights on pricing, availability, and brand strategies

This project demonstrates strong practical skills in:

Web Scraping

Data Cleaning

Feature Engineering

Data Integration

Exploratory Data Analysis

Analytical Thinking

🛠 Tech Stack

Python

requests

BeautifulSoup

pandas

numpy

matplotlib

seaborn

Regular Expressions (regex)

## 🌐 Data Source

Platform: Flipkart (public smartphone listings)

Data Type: Product listing information

Access Method: HTTP requests + HTML parsing

Ethical Note: Only publicly visible data was collected

## 🕷 Web Scraping Implementation

Implemented inside:

Key Capabilities:

Dynamic pagination handling

Brand-wise URL filtering

Structured extraction of:

Product Name

Price

Availability Status

Ratings & Reviews

Processor

Storage (RAM & ROM)

Camera Specifications

Battery Capacity

Warranty

The script automatically merges all brand datasets into a final dataset.

Final dataset:

https://github.com/ajaysai656/Building-a-Web-Data-Pipeline-Scraping-Cleaning-EDA/blob/main/flipkart_smartphones_cleaned_merged.csv.csv
## 🧹 Data Cleaning & Feature Engineering

Performed in:

notebooks/data_preprocessing_and_eda.ipynb
Data Cleaning:

Removed currency symbols and commas from price

Standardized availability labels

Handled missing values

Dropped irrelevant columns

## Feature Engineering:

Extracted numeric RAM and ROM values using regex

Extracted numeric camera megapixel values

Extracted battery capacity values

Converted text-based specifications into structured numeric columns

Prepared a fully analysis-ready dataset

## 📊 Exploratory Data Analysis (EDA)
Analyses Performed:

Brand-wise availability comparison

Price distribution analysis (right-skewed market structure)

Availability vs Price relationship

Brand pricing strategy comparison

Correlation analysis between price and technical features

## 🔍 Key Insights

“Coming Soon” models are typically priced higher, reflecting launch-phase premium positioning.

“Currently Unavailable” models are often older and priced lower.

RAM and ROM show stronger correlation with price than camera megapixels.

Premium brands operate across wider pricing segments.

Budget brands maintain narrower and more consistent pricing strategies.

The smartphone market shows clear segmentation into budget, mid-range, and premium tiers.

## 📂 Repository Structure
scraping_scripts/
    scrape_flipkart_smartphones.py

data/
    flipkart_smartphones_analysis_ready.csv

notebooks/
    data_preprocessing_and_eda.ipynb

README.md
requirements.txt
## 💡 What This Project Demonstrates

Ability to scrape real-world messy websites

Handling unstructured HTML data

Applying regex for structured feature extraction

Building an end-to-end data pipeline

Performing meaningful business-driven analysis

Converting raw web data into actionable insights
