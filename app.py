import nltk
import spacy
import wikipedia
from spacy import displacy
from flask import Flask, request, url_for, render_template

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

nlp = spacy.load('en_core_web_sm')

from flaskext.markdown import Markdown


app = Flask(__name__)
Markdown(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=="POST":

        info = request.form["rawtext"]
        rawtext = wikipedia.summary(info, auto_suggest=False)


        mydoc = nlp(rawtext)
        myhtmlval = displacy.render(mydoc,style='ent')
        myhtmlval = myhtmlval.replace("\n\n","\n")
        htmlval = HTML_WRAPPER.format(myhtmlval)


    return render_template('predict.html', rawtext=rawtext, htmlval=htmlval)

if __name__ == "__main__":
    app.run(debug=True)