##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import datetime as dt
import random
import smtplib

current_time = dt.datetime.now()
current_year = current_time.year
current_month = current_time.month
current_day = current_time.day

USERNAME = ""
PASSWORD = ""

def sendEmail(user_name, user_email):
    print(user_name)
    print(user_email)
    template_number = random.randint(1,3)
    with open(f"letter_templates/letter_{template_number}.txt") as f_ptr:
        template_msg = f_ptr.readlines()
    
    birthday_msg = ""
    for msg in template_msg:
        new_msg = msg.replace("[NAME]", user_name)
        birthday_msg += new_msg
    print(birthday_msg)

    with smtplib.SMTP("<your_email>") as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(
            from_addr=USERNAME,
            to_addrs=user_email,
            msg=f"Subject: Happy Birthday!\n\n {birthday_msg}"
        )



user_dict = []
data = pd.read_csv('birthdays.csv')

for index, row in data.iterrows():
    birth_month = row['month']
    birth_day = row['day']
    if current_day == birth_day and current_month == birth_month:
        new_dict = {
            "name": row['name'],
            "email":row['email']
        }
        user_dict.append(new_dict)

print(len(user_dict))
for user in user_dict:
    user_name = user.get('name')
    user_email = user.get('email')
    sendEmail(user_name, user_email)



