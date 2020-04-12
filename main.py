from PIL import Image, ImageGrab
import smtplib
from _datetime import datetime
import regist

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import win32gui, win32con

def screen_message():
    scren = ImageGrab.grab()
    a = datetime.now()
    dat = str(a.date()) + "_" + str(a.hour) + "_" + str(a.minute) + "_" + str(a.second)
    name = "screen\\screen" + dat + '.png'
    print(name)
    scren.save(name, "PNG")
    with open(name, 'rb') as fp:
        file = MIMEImage(fp.read())
        fp.close()

    msg = MIMEMultipart()
    msg['From'] = 'EMAIL_SANDLER'  # Адресат
    msg['To'] = regist.address  # Получатель
    msg['Subject'] = dat
    msg.attach(file)

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login('EMAIL_SANDLER', 'PASSWORD')
        smtpObj.send_message(msg)
        smtpObj.quit()
        print("ok")
    except:
        print("error")

# The_program_to_hide = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)
import keyboard
keyboard.add_hotkey('Ctrl + `', screen_message)
keyboard.wait()
