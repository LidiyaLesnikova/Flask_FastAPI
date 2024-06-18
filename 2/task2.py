from flask import Flask, redirect, render_template, request, url_for, make_response

app = Flask(__name__)

#app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/autorization/', methods=['GET', 'POST'])
def autorization():
    if request.method == 'POST':
        response = make_response(redirect(url_for('welcome')))
        response.set_cookie('username', request.form['name'])
        return response
    return render_template("base.html")

@app.route('/welcome/', methods=['GET', 'POST'])
def welcome():
    context = {'title': 'Приветствие',
               'message': f'Приветствуем Вас, {request.cookies.get('username')}'}
    if request.method == 'POST':
        return redirect(url_for('logout'))
    return render_template("welcome.html", **context)

@app.route("/logout/")
def logout():
    res = make_response(redirect(url_for('base')))
    res.set_cookie("username", "", 0)
    return res

if __name__ == '__main__':
    app.run(debug=True)