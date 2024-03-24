## Flask Application Design for Creating a Web Page with ASCII Art

### HTML Files

- **index.html**: This file will be the main page of the application. It will include an HTML form that allows the user to enter text and submit it to the server. The form will have two fields:
  - **text**: A text field where the user can enter the text they want to be converted to ASCII art.
  - **submit**: A submit button that will send the text to the server.
- **result.html**: This file will display the ASCII art representation of the text entered by the user.

### Routes

- **route**: The route for the main page of the application. This route will render the index.html file.
- **result**: The route for the result page of the application. This route will take the text entered by the user and convert it to ASCII art using the ```ascii_art``` module. The resulting ASCII art will be displayed in the result.html file.

### Implementation

```python
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
```