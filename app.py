from flask import Flask, render_template, request
from googletrans import Translator
trans=Translator()
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def translate():
    if request.method=='POST':
        source_option=request.form['option']
        text = request.form['user_text']
        user_click=request.form['my_checkbox']
        translated=str(trans.translate(text, src=source_option, dest=user_click))
        translations=translated.partition('text=')[2]
        translated_text=translations.partition(',')[0]
        return render_template('index.html',translated_text=translated_text[:],source_text=text)
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
