import os
import pandas as pd
import json

def extract_emails_in_batches(folder_path, email_column_name, name_column_name, output_folder):
    """
    Extracts email addresses and names from CSV, XLS, or XLSX files in a folder,
    filters out specific emails, and saves them in batches as JSON files.

    Args:
        folder_path (str): Path to the folder containing the files.
        email_column_name (str): Name of the column containing email addresses.
        name_column_name (str): Name of the column containing names.
        output_folder (str): Path to the folder where JSON output files will be saved.
    """

    email_entries = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.csv', '.xls', '.xlsx')):
            file_path = os.path.join(folder_path, file_name)
            try:
                if file_name.endswith('.csv'):
                    df = pd.read_csv(file_path)
                else:  # Handle .xls and .xlsx
                    df = pd.read_excel(file_path)

                if email_column_name in df.columns and name_column_name in df.columns:
                    # Use .loc to avoid SettingWithCopyWarning
                    for index, row in df.loc[:, [email_column_name, name_column_name]].dropna().iterrows():
                        email = row[email_column_name]
                        name = row[name_column_name]
                        # Filter out specific emails
                        if email not in ["No email", "vanshikaaggarwal@igdtuw.ac.in", "shivani.chopra@hp.com"]:
                            email_entries.append({"email": email, "name": name})
                else:
                    print(f"Column '{email_column_name}' or '{name_column_name}' not found in file {file_name}")
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

    batch_size = 200
    for i in range(0, len(email_entries), batch_size):
        batch = email_entries[i:i + batch_size]
        output_file = os.path.join(output_folder, f"emails_batch_{i // batch_size + 1}.json")

        with open(output_file, 'w') as f:
            json.dump(batch, f, indent=4)

    print(f"Emails have been successfully extracted in batches to {output_folder}")

# Usage example
folder_path = "/Volumes/PortableSSD/BulkEmailing/new_email"
email_column_name = "Email"  # Replace with the actual email column name
name_column_name = "Names" # Replace with the actual name column name
output_folder = "/Volumes/PortableSSD/BulkEmailing/Output3"

os.makedirs(output_folder, exist_ok=True)

extract_emails_in_batches(folder_path, email_column_name, name_column_name, output_folder)