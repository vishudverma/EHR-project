import requests
import kagglehub

# Download of datasets from open sources
# Source: UCI Machine Learning Repository - Diabetes 130-US hospitals for years 1999-2008 Data Set
csv_urls = [
    "https://archive.ics.uci.edu/static/public/296/diabetes+130-us+hospitals+for+years+1999-2008.zip"
]

# Download of datasets from Kaggle
path = kagglehub.dataset_download("ashishsahani/hospital-admissions-data")

# Download CSV files from the specified URLs
for url in csv_urls:
    filename = url.split("/")[-1]
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Downloaded {filename}")


# Note: The downloaded file is a ZIP file. You may need to extract it to access the CSV files inside.
# Todo: Add additional sources for more comprehensive and robust data acquisition; refer to notes for the required sources.