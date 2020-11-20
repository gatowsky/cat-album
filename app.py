from flask import Flask
app = Flask(__name__)

@app.route('/')
def test_deployment():
    print("I am running")
    return "app succesfully deployed to Kubernetes"
