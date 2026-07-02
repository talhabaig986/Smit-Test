from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/adminlogin")
def adminlogin():
    return render_template("adminlogin.html")

@app.route("/adminpage",methods=["post"])
def adminpg():
      email = request.form['email']
      password = request.form['password']
      return render_template("adminpage.html")

app.run(debug=True)
