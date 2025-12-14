from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '''
    <html>
        <head><title>Hola Mundo</title></head>
        <body style="text-align: center; padding-top: 50px; font-family: Arial;">
            <h1>¡Hola Mundo desde Docker! 🐳</h1>
            <p>Esta es mi aplicación DevOps</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
