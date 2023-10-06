from flask import Flask,render_template

app =Flask (__name__)

@app.route("/index")
def index ():
    return render_template("index.html")

@app.route("/habitaciones")
def habitaciones ():
    return render_template("habitaciones.html")

@app.route("/login")
def login ():
    return render_template("login.html")

@app.route("/perfiles")
def perfiles ():
    return render_template("perfiles.html")

@app.route("/registroApr")
def registroApr ():
    return render_template("registroApr.html")

@app.route("/registro")
def registrolns ():
    return render_template("registrolns.html")




if (__name__ =="__main__"):
    app.run(port=5000,debug=True)