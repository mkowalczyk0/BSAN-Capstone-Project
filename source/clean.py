import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

input = os.getenv('RAW_SOURCE_PATH')
output = os.getenv('CLEANED_OUTPUT_PATH')


def cleanLoans(input_path, output_path):
    print('START')
    loans_df = pd.read_csv(input_path, dtype=str)
    
    # transform 1 - nulls / columns
    try:
        print('TRANSFORM: Nulls & Columns')
        loans_df['Original_Loan_Balance'] = loans_df['Original_Loan_Balance'].fillna(loans_df['Credit_Limit'])
        loans_df.drop(columns=['Credit_Limit', 'No_Match', 'Activity_Designator', 'event_date'], inplace=True)
        loans_df.loc[loans_df['Loan_Type'] == 'Credit Cards', 'Loan_Term'] = 0
        loans_df.loc[loans_df['Loan_Type'] == 'Student Loans EFX', 'Loan_Type'] = 'Student Loans'
        loans_df['Is_Enabled'] = loans_df['Is_Enabled'].fillna('No')
        loans_df['Is_Linked'] = loans_df['Is_Linked'].fillna('No')
        loans_df['Current_Loan_Balance'] = loans_df['Current_Loan_Balance'].fillna(0)
        loans_df.dropna(subset=['Loan_Provider', 'Interest_Rate', 'Original_Loan_Balance', 'Minimum_Payment', 'Date_Linked', 'Loan_Term'], inplace=True)
    except Exception as e:
        print(f"\n\nERROR during transform 1 - nulls / columns: {str(e)}\n\n")

    # transform 2 - dtype conversion
    try:
        print('TRANSFORM: Data Types')
        loans_df['Interest_Rate'] = pd.to_numeric(loans_df['Interest_Rate']) / 100
        loans_df['Minimum_Payment'] = pd.to_numeric(loans_df['Minimum_Payment'])
        loans_df['Current_Loan_Balance'] = pd.to_numeric(loans_df['Current_Loan_Balance'])
        loans_df['Original_Loan_Balance'] = pd.to_numeric(loans_df['Original_Loan_Balance'])
        loans_df['Loan_Term'] = pd.to_numeric(loans_df['Loan_Term'])
        loans_df['Unique_Saved_In_Interest'] = pd.to_numeric(loans_df['Unique_Saved_In_Interest'])
        loans_df['Date_Issued'] = pd.to_datetime(loans_df['Date_Issued'], format='mixed', errors='coerce')
        loans_df['Date_Linked'] = pd.to_datetime(loans_df['Date_Linked'], format='mixed', errors='coerce')
        loans_df['Loan_Last_Payment'] = pd.to_datetime(loans_df['Loan_Last_Payment'], format='mixed', errors='coerce')
    except Exception as e:
        print(f"\n\nERROR during transform 2 - dtype conversion: {str(e)}\n\n")
        
    # transform 3 - remove negative link time cases
    try:
        print('TRANSFORM: Removing negative link time cases')
        # Drop loans where Date_Linked is before Date_Issued
        loans_df = loans_df[loans_df['Date_Linked'] >= loans_df['Date_Issued']]
    except Exception as e:
        print(f"\n\nERROR during transform 3 - negative link time removal: {str(e)}\n\n")
    
    # transform 4 - logical cleaning
    try:
        print('TRANSFORM: Logical')
        loans_df = loans_df[loans_df['Interest_Rate'].astype(float) <= 0.50]
        loans_df = loans_df[loans_df['Loan_Term'].astype(float) <= 480]
    except Exception as e:
        print(f"\n\nERROR during transform 4 - logical cleaning: {str(e)}\n\n")
    
    try:
        loans_df.to_csv(f'{output_path}/cleanedLoans.csv', index=False)
    except Exception as e:
        print(f"\n\nERROR during CSV export: {str(e)}\n\n")
    

def main():    
    try:
        print('-------------------Running Main-------------------')
        cleanLoans(input, output)
        print('-------------------SUCCESS-------------------')
    except Exception as e:
        print(f"\n\nERROR: {str(e)}\n\n")


if __name__ == "__main__":
    main()
