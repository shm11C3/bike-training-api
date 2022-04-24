from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/')

def get_request():
    contents = request.args.get('value', '')
    return contents

if __name__ == "__main__":
    app.run(host='0.0.0.0')
