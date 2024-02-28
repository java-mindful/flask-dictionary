from flask import Flask, render_template, request
from nltk.corpus import wordnet

app = Flask(__name__)

def get_word_definition(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets[0].definition()
    else:
        return "Word not found in the dictionary"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    word = request.form['word'].lower()
    definition = get_word_definition(word)
    return render_template('result.html', word=word, definition=definition)

if __name__ == '__main__':
    app.run(debug=True)