# https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
# https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

user_id = ''

user_name = ''

@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user_name = request.form['user_name']
        print(f'ID: {user_id}\nName: {user_name}')
        return redirect(url_for('index'))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)