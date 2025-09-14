# movies_tv_data_ingestion
End-to-end data engineering pipeline for Movies and TV Shows datasets using Databricks, Delta Lake, PySpark, DBT, and Streamlit. Implements Bronze-Silver-Gold medallion architecture, handles schema evolution, cleansing, enrichment, incremental loads, and provides interactive analytics-ready Gold tables and visualizations.

# Movies & TV Shows Data Engineering Project

## Project Overview

This repository demonstrates a full-fledged **end-to-end data engineering project** focused on ingesting, transforming, and visualizing Movies and TV Shows datasets using modern data engineering tools and best practices. The primary objective of this project is to simulate a real-world data pipeline workflow, showcasing skills in **data ingestion, storage optimization, transformation, and interactive visualization**, making it job-ready for data engineering roles.  

The project implements a **medallion architecture** using Databricks, dividing data into **Bronze, Silver, and Gold layers**. The Bronze layer ingests raw JSON and CSV files from open datasets, handling schema evolution, missing values, and duplicates. The Silver layer performs cleansing, enrichment, and integration of multiple sources to generate a more structured and analysis-ready dataset. Finally, the Gold layer provides aggregated, curated datasets optimized for analytics and downstream applications, supporting business intelligence and machine learning initiatives.  

To automate transformations and ensure a scalable and maintainable workflow, the project integrates **DBT (Data Build Tool)**. DBT models are implemented to standardize, validate, and transform Silver layer tables into Gold layer outputs, enforcing data quality through tests and documentation. This ensures reproducible, version-controlled transformations aligned with industry best practices.  

For data accessibility and presentation, a **Streamlit-based UI** is implemented, allowing end users to explore movie and TV show data interactively. Users can filter by genre, year, rating, and other attributes, view summaries and visualizations, and gain insights from the curated dataset without writing SQL queries. The UI demonstrates the capability to transform complex data pipelines into business-friendly interfaces.  

The project uses **Databricks for scalable data processing**, **DBT for transformation orchestration**, and **Streamlit for interactive visualization**, highlighting a complete skill set in modern data engineering. This end-to-end solution emphasizes **data ingestion, cleaning, transformation, and visualization**, replicating real-world enterprise pipelines. It is designed to be fully reproducible, well-documented, and modular, demonstrating the application of modern **data engineering principles**, making it an ideal showcase for prospective employers and a portfolio-ready project for aspiring data engineers.  

---

## Technologies Used

- **Databricks** – Scalable data processing and notebook environment  
- **DBT (Data Build Tool)** – Data transformation and orchestration  
- **Streamlit** – Interactive data visualization UI  
- **Python** – Data processing and scripting  
- **SQL & PySpark** – Data manipulation and transformation  

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movies-tv-data-engineering.git
   cd movies-tv-data-engineering
