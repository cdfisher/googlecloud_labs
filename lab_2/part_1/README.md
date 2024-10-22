### Part 1
#### Configuring main.py
- `MAIL_SERVER` should be `'smtp.gmail.com'` if the sender is a Gmail account.
- `MAIL_USERNAME` and `MAIL_DEFAULT_SENDER` should be the full email address of the sender.
- `MAIL_PASSWORD`: For Gmail accounts, this should be an app password, rather than the account password (see below).

#### Generating a Google app password
- Requires 2 factor authentication to be enabled.
- Go to Google account settings and search "App password". Generate one (what you name it doesn't matter) and then use 
it as the `MAIL_PASSWORD` value.

#### Deploying
- If continuing onwards from the steps in [the minimal_appengine repo](https://github.com/cdfisher/minimal_appengine),
make sure to add the line `Flask-Mail~=0.10.0` to  `requirements.txt` before deploying.
- In cmd, `cd` to the `/app/` directory and do `gcloud app deploy`.
- Once the app has deployed, `gcloud app browse` will open the application in a new browser tab and sends an email to 
the email set as `recipient` in `main.py`.
