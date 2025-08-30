import requests
import kagglehub
import os

# Download of datasets from open sources
# Source: UCI Machine Learning Repository - Diabetes 130-US hospitals for years 1999-2008 Data Set
# Source: CDC NHANES - Demographic Variables and Sample Weights 2021-2022
# Source: Kaggle - Hospital Admissions Dataset(India based)
dwnld_urls = [
    "https://archive.ics.uci.edu/static/public/296/diabetes+130-us+hospitals+for+years+1999-2008.zip",
    "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.xpt"
]

# Download of datasets from Kaggle hospital admissions data
path = kagglehub.dataset_download("ashishsahani/hospital-admissions-data")

# Download CSV files from the specified URLs
raw_data_dir = os.path.join(os.path.dirname(__file__), "/Projects/EHR-Project/data/00_raw") # ToDo: update the path so that it works on any system

for url in dwnld_urls:
    filename = url.split("/")[-1]
    file_path = os.path.join(raw_data_dir, filename)
    if os.path.exists(file_path):
        print(f"{filename} already exists in {raw_data_dir}, skipping download.")
        continue
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    with open(file_path, "wb") as f:
        f.write(response.content)
    print(f"Downloaded {filename} to {raw_data_dir}")


# Note: The downloaded file is a ZIP file. You may need to extract it to access the CSV files inside. Each file being downloaded is of different format. so need to handle them individually.