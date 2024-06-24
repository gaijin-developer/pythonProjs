import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "<enter email>"
    password = "<enter generated email password>"
    context = ssl.create_default_context()
    receiver = "<receiver> email"
#     message = """\
# Subject:Joe
# How are you doing"""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
