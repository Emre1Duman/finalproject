from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return ("<h1>Welcome...</h1>")



if __name__ == '__main__': 
    app.run() 