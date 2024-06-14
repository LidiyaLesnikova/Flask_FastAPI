from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/clothes/')
def clothes():
    context = {'section': "Обувь",
               'level':'/'}
    return render_template('clothes.html', **context)

@app.route('/shoes/')
def shoes():
    context = {'section': "Обувь",
               'level':'/'}
    return section_not_fill(context)

@app.route('/clothes/jacket/')
def jacket():
    context = {'section': "Куртки",
               'level':'/clothes/',
               'assortment': [{'name': 'Куртка летняя серая',
                               'link': "https://swg.style/images/detailed/4/374A-P154-55-DSCF8189_xee7-p8.jpg"},
                              {'name': 'Куртка летняя синяя',
                               'link': "https://tis-tex.ru/images/detailed/10/4391-71-15.jpg"}]}
    return render_template('assortment.html', **context)

@app.route('/clothes/dress/')
def dress():
    context = {'section': "Платья",
               'level':'/clothes/'}
    return section_not_fill(context)

@app.route('/clothes/trousers/')
def trousers():
    context = {'section': "Брюки",
               'level':'/clothes/'}
    return section_not_fill(context)

def section_not_fill(context):
    return render_template('section_not_fill.html', **context)

if __name__ == '__main__':
    app.run(debug=True)