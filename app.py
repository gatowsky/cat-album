from flask import Flask
app = Flask(__name__)

@app.route('/')
def test_deployment():
    print("I am running")
    return "Hello, 世界,  app deployed on Kubernetes- welcome cloud native !!"

@app.route('/helm')
def helm_hi():
    return "Hello Helm wrapper"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
