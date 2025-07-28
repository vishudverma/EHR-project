def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def validate_data(data):
    """Validates the input data for expected formats and values."""
    if data is None or len(data) == 0:
        log_message("Data is empty or None.")
        return False
    # Add more validation checks as needed
    return True

def save_to_csv(data, file_path):
    """Saves the given data to a CSV file."""
    import pandas as pd
    try:
        data.to_csv(file_path, index=False)
        log_message(f"Data saved to {file_path}")
    except Exception as e:
        log_message(f"Error saving data to CSV: {e}")