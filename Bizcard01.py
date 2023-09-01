# ----------------------------------------------------- CLEAR CODE :
import easyocr
import re

# Create an EasyOCR reader object
reader = easyocr.Reader(['en'])  # Specify the list of languages you want to support

# image_path = '/content/1.jpeg'  # Load an image from file - 5 3 1 | C:\Users\DONMETHIL\Downloads\zOthers
image_path = r'C:\Users\DONMETHIL\Downloads\zOthers\5.jpeg'
results = reader.readtext(image_path)  # Perform OCR on the image

# ----------------------------------- # r'^[A-Za-z]{5,8}$'
name_pattern = r"Selva|KARTHICK|SANTHOSH"
job_pattern = r"DATA MANAGER|General Manager|Technical Manager|CEO|MD|Managing Director|Analyst|Specialist|Supervisor"
company_pattern = r"selva digitals|BORCELLE AIRLINES|Sun Electricals|selva |digitals"
phone_pattern = r"\+\d{3}[-\s]?\d{3}[-\s]?\d{4}"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
website_pattern = r"[www|WWW|wwW]+[\.|\s]+[a-zA-Z0-9]+[\.|\][a-zA-Z]+"
city_pattern = r"Chennai|Erode|Salem|HYDRABAD|Tirupur|Madurai|Trichy|coimbatore"
state_pattern = r"TamilNadu|Kerela|karnataka|Andhra|telangana"
pin_pattern = r"\b\d{6,7}\b"
# ----------------------------------- #
recognized_text = ' '.join(result[1] for result in results)
# ----------------------------------- #
recognized_name = re.findall(name_pattern, recognized_text)
recognized_job = re.findall(job_pattern, recognized_text)
recognized_company = re.findall(company_pattern, recognized_text)
recognized_phones = re.findall(phone_pattern, recognized_text)
recognized_email = re.findall(email_pattern, recognized_text)
recognized_web = re.findall(website_pattern, recognized_text)
recognized_city = re.findall(city_pattern, recognized_text)
recognized_state = re.findall(state_pattern, recognized_text)
recognized_pin = re.findall(pin_pattern, recognized_text)

# ----------------------------------- #
print(f"Name:",''.join(recognized_name))
print(f"Job Title:",''.join(recognized_job))
print(f"Company Name:",''.join(recognized_company))
print(f"Phone Number:",''.join(recognized_phones))
print(f"Email Address:",''.join(recognized_email))
print(f"Web Address:",''.join(recognized_web))
print(f"City:",''.join(recognized_city))
print(f"State:",''.join(recognized_state))
print(f"Pin Number:",''.join(recognized_pin))

# ----------------------------------- #
