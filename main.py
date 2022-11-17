# importing the Yagmail library
import yagmail

my_email = "testpythonmailer1@gmail.com"
password = "foanjireptgrxvox"


try:
    # initializing the server connection
    yag = yagmail.SMTP(user=my_email, password=password)
    # sending the email
    yag.send(to='testpythonmailer2@yahoo.com', subject='Testing Yagmail', contents='<h1>Hurray, Second Email '
                                                                                   'worked!</h1> '
             '<p>Just Running multiple tests</p>')
    print("Email sent successfully")
except:
    print("Error, email was not sent")
