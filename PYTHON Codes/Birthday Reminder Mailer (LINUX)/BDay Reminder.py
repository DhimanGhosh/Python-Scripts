def checkTodaysBirthdays():
    global birthdayFile
    fileName = open(birthdayFile, 'r')
    today = time.strftime('%d%m%Y')
    flag = 0
    for line in fileName:
        if today[:4] == line[:4]:
            line = line.split(' ')
	    flag = 1
            birthday = datetime.strptime(line[0], '%d%m%Y')
            if '@' in line[-1]:
                age = (datetime.today() - birthday).days/365
                to_mail_id = line[-1].strip()
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                from_mail_id = 'dgkiitcsedual@gmail.com'
                from_mail_idPWD = 'kovarcsbmqxmtvds'
                s.login(from_mail_id, from_mail_idPWD)
                
                msg = MIMEMultipart()
                msg['From'] = from_mail_id
                msg['To'] = to_mail_id
                msg['Subject'] = "Happy Birthday!"
                body = 'Many Happy Returns of the Day!\nAge: ' + str(age)
                msg.attach(MIMEText(body, 'plain'))
                attachment = open(os.getcwd() + '/Birthday_Wish.pdf', 'rb')
                p = MIMEBase('application', 'octet-stream')
                p.set_payload((attachment).read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', "attachment; filename= %s" % fileName)
                msg.attach(p)

                s.sendmail(from_mail_id, to_mail_id, msg.as_string())
                s.quit()
                os.system('notify-send "Birthdays Today: ' + ' '.join(line[1:-1]) + ' Mail Sent to: ' + to_mail_id + ' successfully!"')
            else:
                os.system('notify-send "Birthdays Today: ' + ' '.join(line[1:]) + ' No Mail ID Found! Enter a Mail ID!"')
    if flag == 0:
        os.system('notify-send "No Birthdays Today!"')

def run():
    checkTodaysBirthdays()

if __name__ == '__main__':
    import time, os, smtplib
    from datetime import datetime
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    birthdayFile = os.getcwd() + '/birthdays.txt'
    run()
