import threading
import requests
import time
from flask import Flask, render_template
from turbo_flask import Turbo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail():
    mail_content = '''Hello,
    This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
    Thank You'''

    # The mail addresses and password
    sender_address = '0a01b02@gmail.com'
    sender_pass = 'il6004760'
    receiver_address = 'iliavapnik@gmail.com'
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'  # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

app = Flask(__name__)
turbo: Turbo = Turbo(app)
current_result = "Good"
last_result = "Good"

@app.context_processor
def inject_load():
    global current_result
    global last_result
    try:
        if requests.get("http://10.2.3.233").status_code == 200:
            current_result = "Good"
    except:
        current_result = "Bad"
    if current_result != last_result:
        print("changed")
        last_result = current_result
        #send_mail()
    return {'load1': current_result}


@app.route('/')
def index():
    return render_template('base.html')


@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()


def update_load():
    global current_result
    with app.app_context():
        while True:
            time.sleep(2)
            if current_result == "Good":
                turbo.push(turbo.update(render_template('Good.html'), 'load'))
            else:
                turbo.push(turbo.update(render_template('BadR.html'), 'load'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
