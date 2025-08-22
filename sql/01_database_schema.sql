-- Create database schema for EHR readmission risk model

-- Patient demographics table
CREATE TABLE patient_demographics (
    patient_id VARCHAR(50) PRIMARY KEY,
    birth_date DATE,
    gender VARCHAR(10),
    race VARCHAR(50),
    ethnicity VARCHAR(50),
    zip_code VARCHAR(10)
);

-- Hospital admissions table
CREATE TABLE hospital_admissions (
    admission_id VARCHAR(50) PRIMARY KEY,
    patient_id VARCHAR(50),
    admission_date DATE,
    discharge_date DATE,
    length_of_stay INT,
    admission_type VARCHAR(50),
    discharge_disposition VARCHAR(50),
    FOREIGN KEY (patient_id) REFERENCES patient_demographics(patient_id)
);

-- Diagnoses table
CREATE TABLE diagnoses (
    diagnosis_id VARCHAR(50) PRIMARY KEY,
    admission_id VARCHAR(50),
    icd_code VARCHAR(20),
    diagnosis_type VARCHAR(50),
    FOREIGN KEY (admission_id) REFERENCES hospital_admissions(admission_id)
);

-- Lab results table
CREATE TABLE lab_results (
    lab_id VARCHAR(50) PRIMARY KEY,
    admission_id VARCHAR(50),
    test_name VARCHAR(100),
    result_value FLOAT,
    result_unit VARCHAR(20),
    test_date DATE,
    FOREIGN KEY (admission_id) REFERENCES hospital_admissions(admission_id)
);

-- Medications table
CREATE TABLE medications (
    medication_id VARCHAR(50) PRIMARY KEY,
    admission_id VARCHAR(50),
    medication_name VARCHAR(100),
    dosage VARCHAR(50),
    frequency VARCHAR(50),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (admission_id) REFERENCES hospital_admissions(admission_id)
);

-- Readmissions table
CREATE TABLE readmissions (
    readmission_id VARCHAR(50) PRIMARY KEY,
    initial_admission_id VARCHAR(50),
    readmission_date DATE,
    days_to_readmission INT,
    readmission_reason VARCHAR(100),
    FOREIGN KEY (initial_admission_id) REFERENCES hospital_admissions(admission_id)
);
