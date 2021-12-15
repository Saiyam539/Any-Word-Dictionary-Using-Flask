from flask import Flask, render_template, request, flash
import PyDictionary

app = Flask(__name__)
app.secret_key = 'dictionary'

@app.route('/')
def main_page():
    return render_template('main_page.html')

    
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/dictionary', methods=['GET', 'POST'])
def main_func():
    words = request.form['word']
    Dictionary = PyDictionary.PyDictionary()
    if words:
        try:
            definition = Dictionary.meaning(words)
            flash(f'The meaning of "{words}" is: {definition}')
            return render_template('index.html', word=words, definition=definition)
        except:
            messages = 'Word not found'
            return render_template('index.html', word=words, definition=messages)
    else:
        messages = 'Word not found'
        return render_template('index.html',definition=messages)
if __name__ == '__main__':
    app.run(debug=True)