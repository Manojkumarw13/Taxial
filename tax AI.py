import pandas as pd


file_path = 'Tax.csv'
synthetic_tax_data = pd.read_csv(file_path)


user_phone_number = input("Enter a phone number: ")


user_phone_number = int(user_phone_number)


if user_phone_number in synthetic_tax_data['PHONE NUMBER'].values:
    
    user_data = synthetic_tax_data[synthetic_tax_data['PHONE NUMBER'] == user_phone_number]

    
    print("Phone number found in the data.")
    print(user_data[['NAME','ADDRESS','PAN NUMBER','AADHAR NUMBER','ACCOUNT NUMBER','ANNUAL INCOME','DATE OF BIRTH','AGE','TAX AMOUNT']])
    
else:
    print("Phone number not found in the data.")
    
