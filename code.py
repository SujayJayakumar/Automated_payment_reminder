
import os

from twilio.rest import Client

import keys

import pandas as pd


def process_excel_sheet(file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path, engine='openpyxl')

        # Iterate through each row in the DataFrame
        for index, row in df.iterrows():
            # Get the value of the I column (column index 8)
            status = row.iloc[8]

            # Check if the value in the I column is " Unpaid "
            if status == "Unpaid":
                # Get the value in the H column (column index 7)
                if row.iloc[7]=="-":
                    target_no = "number not available"
                    
                else:
                    target_no = "+91"+str(int(row.iloc[7]))

                    #twilio code to send msg
                    ct = Client(keys.account_sid, keys.auth_token)
                    ct.messages.create(body= " You have a pending payment towards layout mantainance,\n Make sure to complete the same within the end of this month.\n -RWA",from_=keys.twilio_number,to=target_no)


                print(f"Unpaid: {target_no}")
            else:
                continue

    except Exception as e:
        print("Error:", e)


# Replace 'path/to/your/excel_file.xlsx' with the actual path to your Excel file
excel_file_path = "D:\SUJAY\Daily Coding Problems\RoyalSheltersProject\RWA-PaidMemberListAsOnApril23.xlsx"
process_excel_sheet(excel_file_path)
