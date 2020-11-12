from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    
    <html>
        <head>
            <title>Hello, CI/CD Pypeline</title>
        </head>
    </html>
    <body>
    <h1>Hi from CircleCI</h1>
<div style="width:100%;height:0;padding-bottom:56%;position:relative;"><iframe src="https://giphy.com/embed/3oKIPsx2VAYAgEHC12" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/DNCE-3oKIPsx2VAYAgEHC12">via GIPHY</a></p>    </body>
    '''