INSERT INTO cleaned_data (column1, column2, column3, ..., readmitted)
SELECT column1, column2, column3, ..., 
       CASE 
           WHEN readmission_date IS NOT NULL AND DATEDIFF(day, admission_date, readmission_date) <= 30 THEN 1 
           ELSE 0 
       END AS readmitted
FROM [your_temp_table_name]; 

-- Replace [your_temp_table_name] with the actual name of the temporary table or staging area where the cleaned data is stored. 
-- Ensure that the column names match those in your cleaned_data table.