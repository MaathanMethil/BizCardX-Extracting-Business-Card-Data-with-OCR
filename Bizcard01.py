# ----------------------------------EXTRACTING DATA FROM IMAGE AND STORING IT IN SQL------------------------------------------
#
import streamlit as st
from PIL import Image
import pytesseract
import re
import io
import mysql.connector
import pandas as pd
#
# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'M:\TesseractPy\tesseract.exe'
image_path = input("Enter the path to the image file: ")
# input("Enter the path to the image file: ")
# r'C:\Users\DONMETHIL\Downloads\zOthers\1.jpeg'
with open(image_path, 'rb') as image_file:
    image_data = image_file.read()
recognized_text = pytesseract.image_to_string(image_path)
# ----------------------------------------------------------------------------------------
# Define regular expression patterns
name_pattern = r"Selva|KARTHICK|SANTHOSH"
job_pattern = r"DATA MANAGER|General Manager|Technical Manager|CEO|MD|Managing Director|Analyst|Specialist|Supervisor"
company_pattern = r"selva digitals|BORCELLE AIRLINES|Sun Electricals|selva|digitals|Selvadigitals"
phone_pattern = r"\+\d{3}[-\s]?\d{3}[-\s]?\d{4}"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
website_pattern = r"www\.[a-zA-Z0-9]+\.[a-zA-Z]+"
street_pattern = r"123 ABC St\.|123ABCSt\.|123 XYZ St\.|999 MNO St\."
city_pattern = r"Chennai|Erode|Salem|HYDERABAD|Tirupur|Madurai|Trichy|Coimbatore"
state_pattern = r"TamilNadu|Kerala|Karnataka|Andhra|Telangana"
pin_pattern = r"\b\d{6,7}\b"

# Extract information using regular expressions
recognized_name = re.findall(name_pattern, recognized_text, re.IGNORECASE)
recognized_job = re.findall(job_pattern, recognized_text, re.IGNORECASE)
recognized_company = re.findall(company_pattern, recognized_text)
recognized_phones = re.findall(phone_pattern, recognized_text)
recognized_email = re.findall(email_pattern, recognized_text)
recognized_web = re.findall(website_pattern, recognized_text)
recognized_street = re.findall(street_pattern, recognized_text)
recognized_city = re.findall(city_pattern, recognized_text, re.IGNORECASE)
recognized_state = re.findall(state_pattern, recognized_text, re.IGNORECASE)
recognized_pin = re.findall(pin_pattern, recognized_text)

# Create a dictionary to hold the extracted data
data = {
    'name': ', '.join(recognized_name),
    'designation': ', '.join(recognized_job),
    'company': ', '.join(recognized_company),
    'contact': ', '.join(recognized_phones),
    'email': ', '.join(recognized_email),
    'website': ', '.join(recognized_web),
    'address': ', '.join(recognized_street),
    'city': ', '.join(recognized_city),
    'state': ', '.join(recognized_state),
    'pincode': ', '.join(recognized_pin),
    'image': image_data,  # Make sure you have defined 'imagesql' correctly
}

# ----------------------------------------------------------------------------------------
# MySQL connection details

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password="root123456789",
    port=3307,
    database="mydt01"
)

# Create a cursor
cursor = connection.cursor()

table_name = 'biximage_01'

create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        designation VARCHAR(255),
        company VARCHAR(255),
        contact VARCHAR(255),
        email VARCHAR(255),
        website VARCHAR(255),
        address VARCHAR(255),
        city VARCHAR(255),
        state VARCHAR(255),
        pincode VARCHAR(255),
        image LONGBLOB
    )
"""
cursor.execute(create_table_sql)
# ------------------------------------------

# Insert values into the new table
# Insert values into the new table
insert_query = f"""
    INSERT INTO {table_name} 
    (name, designation, company, contact, email, website, address, city, state, pincode, image)
    VALUES 
    (%(name)s, %(designation)s, %(company)s, %(contact)s, %(email)s, %(website)s, %(address)s, %(city)s, %(state)s, %(pincode)s, %(image)s)
"""
cursor.execute(insert_query, data)

connection.commit()
#
# ------------------------------------------
