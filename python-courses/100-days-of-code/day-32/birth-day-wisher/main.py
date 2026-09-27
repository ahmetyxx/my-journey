import datetime as dt
import pandas as pd
import smtplib 
from email.message import EmailMessage 
import random

EMAIL="cokgizliar@gmail.com"
PASSWORD="nvnh erdj jyro vxcz"

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address
#.

templates=[r"birth-day-wisher\letter_templates\letter_1.txt",
           r"birth-day-wisher\letter_templates\letter_2.txt",
           r"birth-day-wisher\letter_templates\letter_3.txt"]

bd=pd.read_csv(r"birth-day-wisher\birthdays.csv")
birthdays=[{"date":(month,day), "name":name,"email":email,} for name,email,month,day in  bd[["name","email","month","day"]].values]


now=dt.datetime.now().date()

if  (now.month,now.day) in [birthday["date"] for birthday in birthdays]:
    birthday_persons=[person for person in birthdays if (now.month,now.day)==person["date"]]
    
    for person in birthday_persons:
        path=random.choice(templates)
        
        with open(path,mode="r") as doc:
            template=doc.read()
            
        template=template.replace("[NAME]",person["name"])
        
        msg=EmailMessage()
        msg["From"]=EMAIL
        msg["To"]=person["email"]
        msg["Subject"]="Happy bırthday"
        
        msg.set_content(template)   
        with smtplib.SMTP("smtp.gmail.com") as connect:
            connect.starttls()
            connect.login(user=EMAIL,password=PASSWORD)
            connect.send_message(msg)
else:
    print("bugun kımsenın dogum gunu diil")

