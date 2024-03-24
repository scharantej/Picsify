
from flask import Flask, render_template, request
import ascii_art

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
  text = request.form["text"]
  art = ascii_art.text2art(text)
  return render_template('result.html', art=art)

if __name__ == "__main__":
  app.run()
