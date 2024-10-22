# Adapted from the example on the Flask-Mail PyPI page at
# https://pypi.org/project/Flask-Mail/

from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com' # Assumes the sender account is a Gmail account
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'your_username'
app.config['MAIL_PASSWORD'] = 'your_password' # For Gmail this should be an app password, NOT the account password
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'

mail = Mail(app)
recipient = 'other_email@example.com'

@app.route("/")
def send_email():
    msg = Message(
        'App Engine Flask-Mail demo',
        recipients=[recipient],
        body='This is a test message sent from minimal_flaskmail.'
    )
    mail.send(msg)
    return 'Email sent!'

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)