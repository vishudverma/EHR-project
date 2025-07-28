CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    race VARCHAR(50),
    time_in_hospital INT,
    num_lab_procedures INT,
    num_medications INT,
    number_emergency INT,
    number_inpatient INT,
    number_outpatient INT,
    readmitted BIT
);

CREATE TABLE admissions (
    admission_id INT PRIMARY KEY,
    patient_id INT,
    admission_date DATE,
    discharge_date DATE,
    readmission_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);