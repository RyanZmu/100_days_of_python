# ISS Notifier Applcation

## How It Works
- Checks the position of the ISS every 60 seconds to see if it overhead
- Checks if it is nighttime as well so if it passes during the day no email will be sent
- Sends an email when the ISS is overhead and it is nighttime

## How To Use
- In main.py replace the MY_LONG and MY_LAT vars with your own coordinates
- Replace MY_EMAIL with your own email and HOST with your email provider's SMTP server (look online)
- Create a .env file in the main directory and inside of it enter your APP PASSWORD provided by your email provider (Look online for how to do this step - Usually under your email account's Security settings)
- Open the iss_overhead_notifier folder and run the main.py file inside in a Console - Keep your console open and every 60 seconds you will see the current ISS coords (long,lat) and text letting you know if the iSS is or is not overhead and if an email is being sent