from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello!</h1>"

@app.route("/two_sum/<x>/<y>")
def two_sum(x, y):
    return str(int(x) + int(y))

# /get_param?x=5&y=8
@app.route("/get_param")
def get_param():
    x = request.args.get("x")
    y = request.args.get("y")
    # return str(int(x) + int(y))
    return {"result": int(x) + int(y)}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")