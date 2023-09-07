#
import streamlit as st
from PIL import Image
import pytesseract
import re
import mysql.connector
import pandas as pd
# ----------------------------------------------------------------------------
image = r'C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone\91.jpg'
# ----------------------------------------------------------------------------
# Upload the file: 

st.sidebar.title("BIZCARD : Extracting Business Card Data")
uploaded_files = st.sidebar.file_uploader("Choose an image file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    image = Image.open(uploaded_file)
    st.image(image, caption=f"Uploaded Image: {uploaded_file.name}", use_column_width=True)
    if image is None:
        st.write("Please Upload the Image")

# ----------------------------------------------------------------------------
# Path to the Tesseract executable: 

pytesseract.pytesseract.tesseract_cmd = r'M:\TesseractPy\tesseract.exe'  #image_path = r'C:\Users\DONMETHIL\Downloads\zOthers\1.jpeg'
image_path = image

recognized_text = pytesseract.image_to_string(image_path)

# ----------------------------------------------------------------------------
# Define regular expression patterns: 

name_pattern = r"Selva|KARTHICK|SANTHOSH|Amit kumar|REVANTH"
job_pattern = r"Marketing Executive|DATA MANAGER|General Manager|Technical Manager|CEO & FOUNDER|MD|Managing Director|Marketing|Executive"
company_pattern = r"BORCELLE AIRLINES|Sun Electricals|selva digitals|selvadigitals|GLOBAL|INSURANCE|Family Restaurant"
phone_pattern = r"\+\d{2,3}[-\s]?\d{3}[-\s]?\d{4}"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
website_pattern = r"www\.[a-zA-Z0-9]+\.[a-zA-Z]+"
street_pattern = r"123 ABC St\.|123ABCSt\.|123 XYZ St\.|999 MNO St\.|123 global St\."
city_pattern = r"Chennai|Erode|Salem|HYDRABAD|Tirupur|Madurai|Trichy|Coimbatore"
state_pattern = r"TamilNadu|Kerala|Karnataka|Andhra|Telangana"
pin_pattern = r"\b\d{6,7}\b"

# Extract information using regular expressions:
recognized_name = re.findall(name_pattern, recognized_text, re.IGNORECASE)
recognized_job = re.findall(job_pattern, recognized_text)
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
    'image': 'image_path'
}

# ----------------------------------------------------------------------------
#st.image(image)
#st.write(data)
# ----------------------------------------------------------------------------
# MySQL connection details: 

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password="root123456789",
    port=3307,
    database="mydt01"
)

# Create a cursor
cursor = connection.cursor()

table_name = 'bixtable03'

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
if st.sidebar.button("Save Data in SQL"):
    insert_query = f"""
    INSERT INTO {table_name} (name, designation, company, contact, email, website, address, city, state, pincode, image)
    VALUES (%(name)s, %(designation)s, %(company)s, %(contact)s, %(email)s, %(website)s, %(address)s, %(city)s, %(state)s, %(pincode)s,%(image)s)
    """
    cursor.execute(insert_query, data)
    connection.commit()
# ------------------------------------------
# ------------------------------------------

if st.sidebar.button("MySql Table"):
    select_query = f"SELECT * FROM {table_name}" #  Show Table
    cursor.execute(select_query)
    result = cursor.fetchall()
    st.table(result)

if st.sidebar.button("User Details"):
    st.table(data)

# ------------------------------------------
if st.sidebar.button("Reset Table"):
    reset_query = f"TRUNCATE TABLE {table_name};" #  Show Table
    cursor.execute(reset_query)
    result01 = cursor.fetchall()
    st.table(result01)
# ------------------------------------------
#
