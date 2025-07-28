-- SQL queries for data analysis and retrieval

-- Query to retrieve the count of readmissions
SELECT COUNT(*) AS readmission_count
FROM patient_data
WHERE readmitted = 1;

-- Query to get the average length of stay for readmitted patients
SELECT AVG(length_of_stay) AS avg_length_of_stay
FROM patient_data
WHERE readmitted = 1;

-- Query to find the distribution of readmissions by age group
SELECT age_group, COUNT(*) AS count
FROM (
    SELECT CASE 
        WHEN age < 30 THEN 'Under 30'
        WHEN age BETWEEN 30 AND 39 THEN '30-39'
        WHEN age BETWEEN 40 AND 49 THEN '40-49'
        WHEN age BETWEEN 50 AND 59 THEN '50-59'
        WHEN age BETWEEN 60 AND 69 THEN '60-69'
        ELSE '70 and above'
    END AS age_group
    FROM patient_data
) AS age_distribution
GROUP BY age_group;

-- Query to get the average glucose level for readmitted patients
SELECT AVG(glucose_level) AS avg_glucose_level
FROM patient_data
WHERE readmitted = 1;

-- Query to retrieve the top 5 most common diagnoses for readmitted patients
SELECT TOP 5 diagnosis, COUNT(*) AS count
FROM patient_data
WHERE readmitted = 1
GROUP BY diagnosis
ORDER BY count DESC;