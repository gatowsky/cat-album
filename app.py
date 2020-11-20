from flask import Flask
app = Flask(__name__)

@app.route('/')
def test_deployment():
    return "app succesfully deployed to Kubernetes"
