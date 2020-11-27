from flask import Flask
app = Flask(__name__)

@app.route('/')
def test_deployment():
    print("I am running")
    return "Hello,  app deployed on Kubernetes- welcome cloud native !!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
