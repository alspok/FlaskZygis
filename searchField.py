from flask import Flask, redirect, url_for, request, render_template
from Classes.SearchFile import SearchFile
from Classes.InitValues import InitValues as iv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', file_list = iv.file_list)

# @app.route('/', methods = ['GET', 'POST'])
@app.route('/searchField', methods = ['POST'])
def searchField():
    select_file = request.form.get('select_file')
    search_field = request.form.get('search_field')
    search_value = request.form.get('search_value')
    dict_list = SearchFile().searchFile(select_file, search_field, search_value)
    if len(dict_list) > 0:
        bool = True
    else:
        bool = False
    return render_template('index.html',
                           file_list = iv.file_list,
                           select_file = select_file,
                           field = search_field,
                           value = search_value,
                           dict_list = dict_list,
                           bool = bool)

if __name__ == '__main__':
    #app.run(host='localhost', port=5000, debug=True)
    app.run()