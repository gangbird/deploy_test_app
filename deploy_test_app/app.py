from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template_string('''
    <!doctype html>
    <html lang="ko">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <style>
          body, html {
            height: 100%;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: Arial, sans-serif;
          }
          .centered {
            text-align: center;
            font-size: 2em;
          }
        </style>
        <title>안녕하세요!</title>
      </head>
      <body>
        <div class="centered">안녕하세요!</div>
      </body>
    </html>
    ''')

