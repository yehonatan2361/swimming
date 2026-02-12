import glob
import os
from aaa import extract_customer_data
import shutil

destination_path = "C:/Users/yehon/OneDrive/Dokumenter/tamar_swimming/up"
os.makedirs("C:/Users/yehon/OneDrive/Dokumenter/tamar_swimming/up", exist_ok=True)
source_path = "C:/Users/yehon/OneDrive/Dokumenter/tamar_swimming/pdf_swimming"
pdf_files = glob.glob(os.path.join(source_path, "*.pdf"))
os.path.join(source_path, )



def d():
    file_path=""
    for filename in os.listdir(source_path):
        file_path = os.path.join(source_path, filename)
        if True:
            print(1)

            customer_data = extract_customer_data(file_path)
            shutil.move(file_path, destination_path)
            print(f"--- {os.path.basename(file_path)} ---")
            return customer_data
        else:
            pass
    return None
