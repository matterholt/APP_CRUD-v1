# import dependancies
from flask import Flask, render_template

# initialize the Flask application
app = Flask(__name__)
# adding the routes to other parts of web
@app.route("/")
def index():
    my_list = ["apples", "oranges", "grapes", "pinapples"]
    return "render_template('index.html')"


@app.route("/testExp")
def exper():
    return "test experiances"


# run app behind an if quard
if __name__ == "__main__":
    # host to 0.0.0.0 allows websidte to be acecessible by all devices connected to the same network
    app.run(debug=True, host="0.0.0.0")

