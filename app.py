from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Halo! Pipeline CI/CD Self-Hosted berhasil jalan!"

if __name__ == '__main__':
    # Jangan pakai debug=True di production, nanti kena scan security!
    app.run(host='0.0.0.0', port=5000) # nosec B104
