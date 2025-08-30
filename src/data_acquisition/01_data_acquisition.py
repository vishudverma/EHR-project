import requests
import kagglehub
import os

# Download of datasets from open sources
# Source: UCI Machine Learning Repository - Diabetes 130-US hospitals for years 1999-2008 Data Set
# Source: CDC NHANES - Demographic Variables and Sample Weights 2021-2022
# Source: Kaggle - Hospital Admissions Dataset(India based)
# Source: Kaggle - Pima Indians Diabetes Database
dwnld_urls = [
    "https://archive.ics.uci.edu/static/public/296/diabetes+130-us+hospitals+for+years+1999-2008.zip",
    "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.xpt"
]
kaggle_urls = [
    "uciml/pima-indians-diabetes-database",
    "ashishsahani/hospital-admissions-data"
]

# Download CSV files from the specified URLs
raw_data_dir = os.path.abspath("data/00_raw")


# Download Kaggle datasets which bring in the Indian context
for url in kaggle_urls:
    # Download and extract to a temp directory
    dataset_path = kagglehub.dataset_download(url)
    # dataset_path is the extracted folder path
    for root, _, files in os.walk(dataset_path):
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(raw_data_dir, file)
            if os.path.exists(dest_file):
                print(f"{file} already exists in {raw_data_dir}, skipping copy.")
                continue
            os.makedirs(raw_data_dir, exist_ok=True)
            with open(src_file, "rb") as fsrc, open(dest_file, "wb") as fdst:
                fdst.write(fsrc.read())
            print(f"Copied {file} to {raw_data_dir}")

#Downloading the american datasets from UCI and CDC
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
# All the files are now getting downloaded after the execution of this script to the data/00_raw folder.
# This concludes the first step of the data pipeline - Data Acquisition.
# The next step is Data Cleaning and Preprocessing is within the 02_data_verfication.py script.