# import Flask, request, and json modules
from flask import Flask, request, render_template
import json

# create the Flask app
app = Flask(__name__)

# load the data.json file
with open("data.json", "r") as f:
    data = json.load(f)

# define a route for the home page
@app.route("/")
def home():
    # render the index.html template with the data
    return render_template("index.html", data=data)

# define a route for updating the data
@app.route("/update", methods=["POST"])
def update():
    # get the input value from the form
    input_value = request.form.get("input_value")
    # update the data with the input value
    data["value"] = input_value
    # save the data to the data.json file
    with open("data.json", "w") as f:
        json.dump(data, f)
    # redirect to the home page
    return home()

# run the app in debug mode on port 5000
if __name__ == "__main__":
    app.run(debug=True, port=5000)
