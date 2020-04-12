import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def zapros(address):
    code = str(random.randint(1000, 9999))
    file = MIMEText(code)
    msg = MIMEMultipart()
    msg['From'] = ''  # Адресат
    msg['To'] = address  # Получатель
    msg.attach(file)
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login('', '')
        smtpObj.send_message(msg)
        smtpObj.quit()
        control(code,address)

    except:
        if err() == True:
            address = input("Адрес еще раз\n")
            zapros(address)
        else: exit(0)

def err():
    print("Что-то пошло не так")
    otvet = (input("Повторить попытку? y/n\n")).lower()
    if otvet == "y":
        return True
    elif otvet == "n":
        return False
    else:
        err()

def control(code,address):
    contr = input("Вам на почту пришел код, введите его сюда\n")
    if contr == code:
        f = open('file.txt', 'w')
        print("Проверка прошла успешно")
        f.write(address)
    else:
        if err() == True:
            address = input("Адрес еще раз\n")
            zapros(address)
        else:
            exit(0)

try:
    f = open("file.txt", 'r')
    address = str(f.read())
    print(address)
except:
    print("Укажите почту")
    address = input()
    zapros(address)
    f = open("file.txt", 'r')
    address = str(f.read())
    print(address)
