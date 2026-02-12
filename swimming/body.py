
import pdfplumber
import re




def extract_customer_data(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()


            lines = text.splitlines()

            for line in lines:
                if "םירוגמ תבותכ" in line:
                    address = line.replace("םירוגמ תבותכ", "").strip()
                    if '\u0590' <= address <= '\u05FF':
                        address = address[::-1]




    name_match = re.search(r"([A-Za-zא-ת]+(?:\s+[A-Za-zא-ת]+)?)\s*\*\s*" r"(?:הרוהה םש|יטרפ םש|החפשמ םש)", text)
    name = name_match.group(1) if name_match else ""
    if '\u0590' <= name <= '\u05FF':
        name = name[::-1]

    email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    email = email_match.group(0) if email_match else ""


    id_match = re.search(r"\b\d{5,10}\b", text)  # מספר בן 5-10 ספרות
    id_number = id_match.group(0) if id_match else ""


    phone_match = re.findall(r"\+?\d{2,3}[-\s]?\d{7,10}", text)
    phone = phone_match[1] if len(phone_match) > 1 else ""
    phone2 = phone_match[2] if len(phone_match) > 2 else ""

    return {
        "name": name,
        "nameOnInvoice": name,
        "email": email,
        "numberid": id_number,
        "address": address,
        "city": "בית שמש",
        "zipcode": "",
        "phone": phone,
        "phone2": phone2,
        "customkey": id_number,
        "fax": "",
        "namecontact": name,
        "balance": 0,
        "website": "",
        "taxnumberid": "",
        "vatnumberid": "",
        "tags": "",
        "invoiceCurrency": 2,
        "bankcode": "",
        "bankbranch": "",
        "bankaccount": ""
    }
