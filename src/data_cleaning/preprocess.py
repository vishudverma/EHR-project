def handle_missing_data(df):
    """
    Handle missing data in the DataFrame.
    - Remove features with more than 40% missing values.
    - Impute remaining missing values using mean for numerical features and mode for categorical features.
    """
    # Remove features with >40% missing values
    threshold = 0.4 * len(df)
    df = df.loc[:, df.isnull().sum() < threshold]

    # Impute remaining missing values
    for column in df.columns:
        if df[column].dtype == 'object':  # Categorical features
            df[column].fillna(df[column].mode()[0], inplace=True)
        else:  # Numerical features
            df[column].fillna(df[column].mean(), inplace=True)

    return df


def remove_duplicates(df):
    """
    Remove duplicate rows from the DataFrame.
    """
    return df.drop_duplicates()


def preprocess_data(file_path):
    """
    Main function to preprocess the data.
    - Load data from CSV
    - Handle missing data
    - Remove duplicates
    - Return cleaned DataFrame
    """
    import pandas as pd

    # Load data
    df = pd.read_csv(file_path)

    # Handle missing data
    df = handle_missing_data(df)

    # Remove duplicates
    df = remove_duplicates(df)

    return df