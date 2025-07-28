# README.md

# EHR Readmission Risk Model

This project aims to develop a readmission risk model using the UCI Diabetes dataset and additional datasets from Kaggle. The model will analyze patient data to predict the likelihood of readmission within 30 days of discharge.

## Project Structure

- **data/**: Contains raw and processed datasets.
  - **raw/**: Original dataset from the UCI Machine Learning Repository.
  - **processed/**: Cleaned and processed dataset after data cleaning operations.
  
- **src/**: Source code for data acquisition, cleaning, and utility functions.
  - **data_acquisition/**: Functions to load data and perform database operations.
  - **data_cleaning/**: Functions for preprocessing and feature engineering.
  - **utils/**: Utility functions for logging and data validation.
  
- **sql/**: SQL scripts for database operations.
  - **create_tables.sql**: Commands to create necessary tables in the SQL database.
  - **data_import.sql**: Commands for importing cleaned data into the SQL database.
  - **queries.sql**: Various queries for data analysis and retrieval.
  
- **notebooks/**: Jupyter notebook for exploratory data analysis (EDA).
  
- **config/**: Configuration settings for the project.
  
- **requirements.txt**: Lists the Python dependencies required for the project.
  
- **.env**: Stores environment variables for sensitive information.
  
- **.gitignore**: Specifies files and directories to be ignored by Git.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ehr-readmission-risk
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the database configuration in the `config/database_config.py` file.

4. Run the data acquisition and cleaning scripts to prepare the dataset for analysis.

5. Use the Jupyter notebook in the `notebooks/` directory for exploratory data analysis.

## Usage Guidelines

- Ensure that the raw data is placed in the `data/raw/` directory.
- Follow the scripts in the `src/` directory to load and clean the data.
- Use the SQL scripts in the `sql/` directory for database operations.
- Explore the data and visualize insights using the Jupyter notebook.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.