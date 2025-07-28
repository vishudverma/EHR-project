def create_binary_target(data):
    """
    Create a binary target variable for readmission within 30 days.
    
    Parameters:
    data (DataFrame): The input DataFrame containing patient data.
    
    Returns:
    DataFrame: The DataFrame with the new binary target variable added.
    """
    data['readmitted'] = data['readmitted'].apply(lambda x: 1 if x == '<30' else 0)
    return data

def create_feature_interactions(data):
    """
    Create interaction features for the dataset.
    
    Parameters:
    data (DataFrame): The input DataFrame containing patient data.
    
    Returns:
    DataFrame: The DataFrame with new interaction features added.
    """
    data['insulin_bmi_interaction'] = data['insulin'] * data['body_mass_index']
    return data

def feature_engineering(data):
    """
    Perform feature engineering on the dataset.
    
    Parameters:
    data (DataFrame): The input DataFrame containing patient data.
    
    Returns:
    DataFrame: The DataFrame with engineered features.
    """
    data = create_binary_target(data)
    data = create_feature_interactions(data)
    return data