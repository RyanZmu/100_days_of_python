# Automated Birthday Email Sender!

## How It Works
- Will check each day if the day and month matches an entry in birthday.csv
- Picks from the 3 possible letter templates and sends a happy birthday email

## How To Use
- In main.py replace my_email with your own email address
- Find your provider's stmp server address (smtp.gmail.com for example)
- Set up your account under security settings and get an App Password (Look online for info)
- Create a new file named .env in the main directory and place the password directly into it
- Edit the birthday.csv file with your own contacts
- Edit the letter templates to your liking and replace my name with your own
- For full effect sign up for PythonAnywhere.com or another cloud service and have it run the main.py everyday at 12am to check for birthdays
