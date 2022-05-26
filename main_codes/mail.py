import cv2
import time
import smtplib
import os
import os.path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email = 'xxxxxxxxx@gmail.com'
password = 'xxxxxxxx'
send_to_email = 'xxxxxxxxxx@gmail.com'
subject = 'Over speed Detected'
message = 'This vehicle crossed speed limit'
file_location = 'vehicle.jpg'
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['subject'] = subject

p = 0

def main():
    global p
    cam = cv2.VideoCapture(0)
    for i in range(1, 5):
        ret, frame = cam.read()
        print(ret)
        cv2.imwrite('vehicle.jpg', frame)
    msg.attach(MIMEText(message,'plain'))
    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= %s"%filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    print("sending mail")
    server.starttls()
    server.login(email,password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    print("mail sent")
    server.quit()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
