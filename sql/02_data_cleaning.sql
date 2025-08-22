-- SQL queries for data cleaning

-- Remove duplicate patient records
WITH duplicate_patients AS (
    SELECT patient_id,
           ROW_NUMBER() OVER (PARTITION BY birth_date, gender, zip_code ORDER BY patient_id) as rn
    FROM patient_demographics
)
DELETE FROM patient_demographics
WHERE patient_id IN (
    SELECT patient_id 
    FROM duplicate_patients 
    WHERE rn > 1
);

-- Clean admission dates
UPDATE hospital_admissions
SET discharge_date = NULL
WHERE discharge_date < admission_date;

-- Standardize diagnosis codes
UPDATE diagnoses
SET icd_code = UPPER(TRIM(icd_code));

-- Remove invalid lab results
DELETE FROM lab_results
WHERE result_value IS NULL
   OR result_value < 0
   OR test_name IS NULL;

-- Fix medication date ranges
UPDATE medications
SET end_date = start_date
WHERE end_date < start_date;

-- Validate readmission records
DELETE FROM readmissions
WHERE days_to_readmission < 0
   OR days_to_readmission > 365;
