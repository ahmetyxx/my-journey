
import smtplib
import datetime as dt
import random

my_email="cokgizliar@gmail.com"
password="nvnh erdj jyro vxcz"

def send_mail(subject,body,to_mail="ahmetcanisik375@yahoo.com"):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_mail,
            msg=f"Subject:{subject}\n\n{body}"
            )

if dt.datetime.now().weekday() == 5:
    with open(file="quotes.txt",mode="r") as file:
        quotes=file.readlines()
        quote=random.choice(quotes)
        send_mail(subject="motivation",body=f"{quote}\n gun sonu projesiydi pardon")
