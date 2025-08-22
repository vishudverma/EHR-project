"""
Data Dictionary for EHR Readmission Risk Model

This document provides detailed descriptions of all features used in the model.
"""

# Data Dictionary

## Patient Demographics
| Feature | Description | Type | Source |
|---------|------------|------|--------|
| patient_id | Unique identifier for patient | string | EHR |
| age | Patient age at admission | integer | EHR |
| gender | Patient gender | categorical | EHR |
| race | Patient race | categorical | EHR |
| zip_code | Patient residence ZIP code | string | EHR |

## Admission Details
| Feature | Description | Type | Source |
|---------|------------|------|--------|
| admission_id | Unique identifier for admission | string | EHR |
| admission_date | Date of admission | date | EHR |
| length_of_stay | Duration of hospital stay | integer | Derived |
| admission_type | Type of admission (emergency/elective) | categorical | EHR |

## Clinical Features
| Feature | Description | Type | Source |
|---------|------------|------|--------|
| diagnosis_count | Number of diagnoses | integer | Derived |
| primary_diagnosis | Primary ICD-10 code | categorical | EHR |
| comorbidity_score | Charlson comorbidity index | float | Derived |
| medication_count | Number of medications | integer | Derived |

## Lab Results
| Feature | Description | Type | Source |
|---------|------------|------|--------|
| glucose_level | Blood glucose level | float | EHR |
| hemoglobin | Hemoglobin level | float | EHR |
| creatinine | Serum creatinine | float | EHR |
| sodium | Serum sodium | float | EHR |

## Derived Features
| Feature | Description | Type | Source |
|---------|------------|------|--------|
| prev_admissions | Number of previous admissions | integer | Derived |
| days_since_last | Days since last admission | integer | Derived |
| readmission_history | Previous readmission flag | boolean | Derived |
| risk_score | Computed risk score | float | Model |

## Target Variable
| Feature | Description | Type | Source |
|---------|------------|------|--------|
| readmitted_30 | 30-day readmission flag | boolean | Derived |
