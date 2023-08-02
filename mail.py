import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

email = 'Enter your email id here'
password = 'Enter password here'


def sendmail(receiver):
    server.login(email, password)

    """ take the receiver's email id as input"""
    print("Enter the email id of the receiver: ")

    print("Please write the email you want to send: \n")
    content = input()
    server.sendmail(email, receiver, content)
    print("Mail Sent!")
    return
