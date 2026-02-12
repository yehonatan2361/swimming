import requests
import os
import glob
import json
import pdf

pdf_folder = "C:/Users/yehon/OneDrive/Dokumenter/tamar_swimming/pdf_swimming"
os.makedirs(pdf_folder, exist_ok=True)

USER_KEY = "CHIZYhnxgFf5vjl8G6dK"
SECRET = "ff97d3fc-7052-4bcd-8cb6-7d94ef19b4cf"

url = "https://api.yeshinvoice.co.il/api/v1/addCustomer"


def create_customer(customer_data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": json.dumps({
            "secret": SECRET,
            "userkey": USER_KEY
        })
    }
    response = requests.post(url, headers=headers, json=customer_data)
    if response.status_code == 200:
        result = response.json()
        if result.get("Success"):
            securekey = result["ReturnValue"]["securekey"]
            print(f"✔ לקוח/חשבונית נוצר בהצלחה: {customer_data['nameOnInvoice']} | securekey: {securekey}")
            return securekey
        else:
            print(" שגיאה ביצירת לקוח:", result.get("ErrorMessage"))
            return None
    else:
        print(" שגיאה ביצירת לקוח:", response.status_code, response.text)
        return None


def nnn():
    pdf_files = glob.glob(os.path.join(pdf_folder, "*.pdf"))

    if not pdf_files:
        print("אין קבצי PDF בתיקייה.")
    else:
        for pdf_file in pdf_files:
            customer_data = pdf.d()
            print(customer_data)
            create_customer(customer_data)
