# https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
# https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application
import pymysql
import sqlalchemy
from flask import Flask, render_template, request, url_for, redirect
from google.cloud.sql.connector import Connector  # pip install "cloud-sql-python-connector[pymysql]"

# Reference: https://pypi.org/project/cloud-sql-python-connector/

# initialize Connector object
connector = Connector()


# TODO set this up
# function to return the database connection
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "project:region:instance",
        "pymysql",
        user="my-user",
        password="my-password",
        db="my-db-name"
    )
    return conn


# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)


def insert(user_id, user_name):
    # insert statement
    insert_stmt = sqlalchemy.text(
        "INSERT INTO my_table (user_id, user_name) VALUES (:user_id, :user_name)",
    )

    with pool.connect() as db_conn:
        db_conn.execute(insert_stmt, parameters={"user_id": user_id, "user_name": user_name})

        db_conn.commit()


app = Flask(__name__)

user_id = ''

user_name = ''


# Connections using Automatic IAM database authentication are supported when using Postgres or MySQL drivers. First,
# make sure to configure your Cloud SQL Instance to allow IAM authentication and add an IAM database user.
#
# Now, you can connect using user or service account credentials instead of a password. In the call to connect, set the
# enable_iam_auth keyword argument to true and the user argument to the appropriately formatted IAM principal.
#
#     MySQL: For an IAM user account, this is the user's email address, without the @ or domain name. For example, for
#     test-user@gmail.com, set the user argument to test-user. For a service account, this is the service account's
#     email address without the @project-id.iam.gserviceaccount.com suffix.


@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        insert(request.form['user_id'], request.form['user_name'])
        return redirect(url_for('index'))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)