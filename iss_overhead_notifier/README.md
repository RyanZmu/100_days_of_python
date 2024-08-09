# ISS Notifier Applcation

## What It Does
- Checks the position of the ISS every 60 seconds to see if it's overhead
- Checks if it is nighttime as well so if it passes during the day no email will be sent
- Sends an email once the ISS is overhead and it is nighttime

## How To Use
- In main.py replace the MY_LONG and MY_LAT variable values with your own coordinates
- Replace MY_EMAIL with your own email and HOST with your email provider's SMTP server (Look online for server)
- Create a .env file in the main directory and inside of it enter your APP PASSWORD provided by your email provider (Look online for how to do this step - Usually under your email account's Security settings there will be an APP PASSWORD option)
- Open the iss_overhead_notifier folder and run the main.py file inside a Console - Keep your console open and every 60 seconds you will see the current ISS coords (long,lat) and text letting you know if the iSS is or is not overhead and if an email is being sent

# Sunset/Sunrise checker

## What It Does
- Using coords provided it will tell you when the sunrise and sunset will be
- Uses the Sunrise/Sunset API

## How To Use
- Open sunet_sunrise.py and edit the longitude and latitude values insider of parameters to your desired coords
- Run sunset_sunrise.py in a Console and it will output when the sunrise and sunset will happen
- Uncomment line 13 to see additional information such as when golden hour is and when twilight begins

# Kanye Quotes

## What It Does
- Generates a random Kanye quote
- Uses the Kanye Quotes API

## How To Use
- Run kanye_quotes.py and click on Kanye's head for a quote
- Shake your head at the ridicilousness