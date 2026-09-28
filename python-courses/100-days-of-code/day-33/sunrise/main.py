import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
my_email="cokgizliar@gmail.com"
password="nvnh erdj jyro vxcz"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
    if time_now.hour<sunrise or time_now.hour>sunset:
        with smtplib.SMTP("smtp.gmail.com") as connetcion:
            connetcion.starttls()
            connetcion.login(user=my_email,password=password)
            connetcion.send_message("Subject:look up!\n\n look up ",from_addr=my_email,to_addrs="ahmetcanisik375@gmail.com")
else: 
        with smtplib.SMTP("smtp.gmail.com") as connetcion:
                    connetcion.starttls()
                    connetcion.login(user=my_email,password=password)
                    connetcion.sendmail(from_addr=my_email,to_addrs="ahmetcanisik375@gmail.com",msg="Subject:loook up!\n\n look up ",)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



