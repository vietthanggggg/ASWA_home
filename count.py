import pandas as pd

def count(file_path, state):
    done_count = 0
    # Load the Excel file
    excel_data = pd.ExcelFile(file_path)
    # Check each sheet
    for sheet_name in excel_data.sheet_names:
        sheet_df = pd.read_excel(file_path, sheet_name=sheet_name)
        
        # Search for the column containing "Số tiền"
        for col in sheet_df.columns:
            if sheet_df[col].astype(str).str.contains(state).any():
                # Count occurrences of "done" in the found column
                done_count = sheet_df[col].astype(str).str.lower().str.count('done').sum()
                print(f'"done" found {done_count} times in the column with "Số tiền" in sheet: {sheet_name}')
                break

    if done_count == 0:
        print('"Số tiền" not found or "done" not present in the same column in the Excel file.')

