# Python File:
import pytesseract
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image
import requests
import re
import io
import mysql.connector
import pandas as pd
# # #
st.set_page_config(page_title="My Webpage", page_icon=":cyclone:", layout="wide")
# C:\Users\DONMETHIL\Downloads\Xudemy\GUVI\CapeStone



with st.sidebar:
    selected = option_menu("BIZCARDX", ["Home","Upload", 'Modify'], icons=['bank' ,'cloud-upload', 'list-task'], menu_icon="aspect-ratio", default_index=0)
    #selected
    def load_lottieurl1(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
    #
    lottie_coding1 = load_lottieurl1("https://lottie.host/03542bbe-bc4c-4a43-bdb1-1033ab4728d4/Itqo1d2Ua1.json")
    st_lottie(lottie_coding1, height=200, key="coding01")
    #
    

def get_home():
    st.title("BizCardX: Extracting Business Card Data with OCR")

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_coding = load_lottieurl("https://lottie.host/43317a9d-ba10-49b3-b927-d1a12b21157b/YsfA2e6UHq.json")
            
    text = """The Streamlit application that allows users to upload an image of a business card and 
                extract relevant information from it using
                easyOCR. The extracted information should include the company name, card holder
                name, designation, mobile number, email address, website URL, area, city, state,
                and pin code. The extracted information should then be displayed in the application's
                graphical user interface (GUI)."""
    
    text1 = """In addition, the application should allow users to save the extracted information into
                a database along with the uploaded business card image. The database should be
                able to store multiple entries, each with its own business card image and extracted
                information."""
                    
    text2 = """To achieve this, you will need to use Python, Streamlit, easyOCR, and a database
                management system like SQLite or MySQL. The application should have a simple
                and intuitive user interface that guides users through the process of uploading the
                business card image and extracting its information. The extracted information should
                be displayed in a clean and organized manner, and users should be able to easily
                add it to the database with the click of a button. And Allow the user to Read the data,
                Update the data and Allow the user to delete the data through the streamlit UI
                This project will require skills in image processing, OCR, GUI development, and
                database management. It will also require you to carefully design and plan the
                application architecture to ensure that it is scalable, maintainable, and extensible.
                Good documentation and code organization will also be important for this project.
                """
    st.write(" ")
    # * * * #
    with st.container():
        #st.write("---")
        img_left_col, right_col = st.columns((1,2))

        with img_left_col:
            st.write("---")
            st_lottie(lottie_coding, height=200, key="coding")
            # ------------------------------------------------------> lottie_coding

        with right_col:
            st.write("---")
            st.write(text)
    st.write("---")
    st.write(text1)
    st.write(text2)
    st.write("---")
    
# # #

def get_upload():
    uploaded_files = st.file_uploader("", key="newuploader01", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        image_file = Image.open(uploaded_file)
    pytesseract.pytesseract.tesseract_cmd = r'M:\TesseractPy\tesseract.exe'
    recognized_text = pytesseract.image_to_string(image_file)

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

    # Create a dictionary to hold the extracted data:
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
    'image': image_file  # Make sure you have defined 'imagesql' correctly
    }

    with st.container():
        st.write("---")
        up_left_column, up_right_column = st.columns(2)
        st.table(data)

        with up_left_column:
            st.title("UPLOADED IMAGE:")
            st.write("---")
            st.image(image_file, caption=f"Uploaded Image: {uploaded_file.name}", use_column_width=True)

        with up_right_column:
            st.title("EXTRACTED DATA:")
            st.write("---")
            st.write(recognized_text)

    with st.container():
        st.write("---")
        img_left_column, img_right_column = st.columns(2)

        with img_left_column:
            #st.write("Left:")
            st.write("---")
            input_name = st.text_input("Name",data['name'])
            input_designation = st.text_input("designation",data['designation'])
            input_company = st.text_input("company",data['company'])
            input_contact = st.text_input("contact",data['contact'])
            input_email = st.text_input("email",data['email'])

        with img_right_column:
            #st.write("Right:")
            st.write("---")
            input_website = st.text_input("website",data['website'])
            input_address = st.text_input("address",data['address'])
            input_city = st.text_input("city",data['city'])
            input_state = st.text_input("state",data['state'])
            input_pincode = st.text_input("pincode",data['pincode'])
            #input_image = st.text_input("Image",data['image'])

            

    with st.container():
        st.write("---")
        col1, col2 = st.columns(2)
        #__________________________________________________________________#
        connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password="root123456789",
        port=3307,
        database="mydt01"
        )

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

        if col1.button("Save to DB",use_container_width=True): # if selected2 == "Save to DB":
            insert_query = f"""INSERT INTO {table_name} (name, designation, company, contact, email, website, address, city, state, pincode, image)
            VALUES (%(input_name)s, %(input_designation)s, %(input_company)s, %(input_contact)s, %(input_email)s, %(input_website)s, %(input_address)s, %(input_city)s, %(input_state)s, %(input_pincode)s, NULL)
            """

            insert_data = {
                'input_name': input_name,
                'input_designation': input_designation,
                'input_company': input_company,
                'input_contact': input_contact,
                'input_email': input_email,
                'input_website': input_website,
                'input_address': input_address,
                'input_city': input_city,
                'input_state': input_state,
                'input_pincode': input_pincode
                }
            
            cursor.execute(insert_query, insert_data)
            connection.commit()
        
        if col2.button("Update",use_container_width=True):
            insert_query = f"""INSERT INTO {table_name} (name, designation, company, contact, email, website, address, city, state, pincode)
            VALUES (%(input_name)s, %(input_designation)s, %(input_company)s, %(input_contact)s, %(input_email)s, %(input_website)s, %(input_address)s, %(input_city)s, %(input_state)s, %(input_pincode)s)
            """

            insert_data = {
                'input_name': input_name,
                'input_designation': input_designation,
                'input_company': input_company,
                'input_contact': input_contact,
                'input_email': input_email,
                'input_website': input_website,
                'input_address': input_address,
                'input_city': input_city,
                'input_state': input_state,
                'input_pincode': input_pincode
                }
            
            cursor.execute(insert_query, insert_data)
            connection.commit()
           
# # #   

def update_sql():
    connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password="root123456789",
    port=3307,
    database="mydt01"
    )
    cursor = connection.cursor()

    table_name = 'bixtable03'

    Show_table = f"""SELECT * FROM {table_name}"""
    cursor.execute(Show_table)
    results = cursor.fetchall() # important cmd.
    #st.table(results)
    df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description]) # 
    st.dataframe(df) # ------------------- SHOW DATA FRAME:

    # --------------------------------------------------------------------------- #
    #st.write("---")
    #df1 = pd.DataFrame(results)
    #st.dataframe(df1)
    # --------------------------------------------------------------------------- #

    input_get_name = st.text_input("Name", value="Selva",  key = 'newinput0') # result1[0],
    input_get_id = st.text_input("ID", value="1",  key = 'newinput11') # result1[0],
    
    #st.write(input_get_id)
    #

    Show_Name = f"""SELECT * FROM {table_name} WHERE ID = {input_get_id}"""
    cursor.execute(Show_Name)
    result1 = cursor.fetchone()

    # --------------------------------------------------------------------------- #

    mdata = {
    'mname': result1[1],
    'mdesignation': result1[2],
    'mcompany': result1[3],
    'mcontact': result1[4],
    'memail': result1[5],
    'mwebsite': result1[6],
    'maddress': result1[7],
    'mcity': result1[8],
    'mstate': result1[9],
    'mpincode': result1[10],
    }

    # #
    with st.container():
        st.write("---")
        
        modify_left, modify_right = st.columns(2)

        with modify_left:
            st.write("---")
            #st.write("LeFt")
            input_texts1 = st.text_input("Name", mdata['mname'],key = 'newinput01')
            input_designation1 = st.text_input("Designation", mdata['mdesignation'], key = 'newinput02')
            input_company1 = st.text_input("Company", mdata['mcompany'],key = 'newinput03')
            input_contact1 = st.text_input("Contact", mdata['mcontact'],key = 'newinput04')
            input_email1 = st.text_input("Email", mdata['memail'],key = 'newinput05')

        with modify_right:
            st.write("---")
            #st.write("RiGht")
            input_website1 = st.text_input("Website", mdata['mwebsite'],key = 'newinput06')
            input_address1 = st.text_input("Address", mdata['maddress'],key = 'newinput07')
            input_city1 = st.text_input("City", mdata['mcity'],key = 'newinput08')
            input_state1 = st.text_input("State", mdata['mstate'],key = 'newinput09')
            input_pincode1 = st.text_input("Pincode", mdata['mpincode'],key = 'newinput10')


    # #
    with st.container():
        st.write("---")
        if st.button("Modify Content", use_container_width=True):
            modify_query_01 = f"""UPDATE {table_name}
            SET
            name = %s, designation = %s, company = %s, contact = %s, email = %s, website = %s, address = %s, city = %s, state = %s, pincode = %s
            WHERE ID = {input_get_id}
            """
            cursor.execute(modify_query_01,(input_texts1, input_designation1, input_company1, input_contact1, input_email1, input_website1, input_address1, input_city1, input_state1, input_pincode1))
            connection.commit()
            st.write("---")
            st.write("Content Modified")
    # #      
    with st.container():
        st.write("---")
        input_get_id01 = st.text_input("Enter the ID of the User To be Deleted:", key = 'delinput11')
        if st.button("Delete Data", use_container_width=True):
            delete_query_01 = f"""DELETE FROM {table_name} WHERE ID = {input_get_id01}"""
            cursor.execute(delete_query_01)
            connection.commit()
            st.write("---")
            st.write("User Data Deleted")


# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ #
if selected == "Home":
    get_home()

elif selected == "Upload":
    get_upload()

elif selected == "Modify":
    update_sql()
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ #
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ #


