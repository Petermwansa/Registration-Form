from flask import Flask, render_template, request 

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

    # here we have the code to validate the submission 
    if not request.form.get("name") or request.form.get("sport") not in ["Football", "Baseball", "Basketball", "Netball", "Volleyball"]:
        return render_template("failure.html")
        

    #here we are confirming the registration
        return render_template("success.html")


