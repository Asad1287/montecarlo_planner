import openpyxl
import pandas as pd
def read_excel_table(file_name: str, sheet_name: str, table_name: str) -> pd.DataFrame:
    """
    Read an Excel table into a pandas DataFrame

    Parameters
    ----------
    file_name : str

    sheet_name : str

    table_name : str

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame containing the table data
    """

    # Load the workbook and worksheet
    wb = openpyxl.load_workbook(file_name)
    ws = wb[sheet_name]
    
    # Locate the named table
    table = ws.tables[table_name]
    
    # Determine the cell range of the table
    cell_range = table.ref
    print(f"Reading cell range: {cell_range}")

    # Parse the cell range string to get starting and ending cells
    start_cell, end_cell = cell_range.split(":")
    
    # Get the starting and ending rows and columns
    start_row = int(''.join(filter(str.isdigit, start_cell)))
    end_row = int(''.join(filter(str.isdigit, end_cell)))
    start_col = ''.join(filter(str.isalpha, start_cell))
    end_col = ''.join(filter(str.isalpha, end_cell))

    # Generate the column range string for pandas
    col_range = f"{start_col}:{end_col}"

    # Read the table into a pandas DataFrame
    df = pd.read_excel(file_name, sheet_name=sheet_name, skiprows=start_row-1, nrows=end_row-start_row+1, usecols=col_range)
    
    return df

