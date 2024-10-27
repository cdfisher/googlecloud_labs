# https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
# https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application
import pymysql
import sqlalchemy
from flask import Flask, render_template, request, url_for, redirect
from google.cloud.sql.connector import Connector  # pip install "cloud-sql-python-connector[pymysql]"

# Reference: https://pypi.org/project/cloud-sql-python-connector/

# initialize Connector object
connector = Connector(enable_iam_auth=True)

def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "exam-project-439721:northamerica-northeast1:exam-demo", # This is "Connection name" under "Connect to this instance" on the Cloud SQL Instance details page.
        "pymysql",
        # If running locally, use your Google account as the user
        user='exam-project-439721',     # If running from App Engine, use the App Engine service account as the user
        db="students",
        enable_iam_auth=True
    )
    return conn


# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)


def insert(user_id, user_name):
    print(f"Insert called with id {user_id} and name {user_name}")
    # insert statement
    insert_stmt = sqlalchemy.text(
        "INSERT INTO studentRecords (studentID, studentName) VALUES (:user_id, :user_name)",
    )

    with pool.connect() as db_conn:
        db_conn.execute(insert_stmt, parameters={"user_id": user_id, "user_name": user_name})

        db_conn.commit()


app = Flask(__name__)

user_id = ''

user_name = ''


@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        print("0")
        user_id = request.form['user_id']
        user_name = request.form['user_name']
        if not (user_id == '' and user_name == ''):
            print("1")
            insert(user_id, user_name)
            return redirect(url_for('index'))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)