from flask import Flask, redirect, render_template, request
import mysql.connector
import os

conn = mysql.connector.connect(host="localhost", username = "root", password="1234", database = "mywebsite")
curser = conn.cursor()

web=Flask(__name__)


@web.route("/")
def home():
    return render_template("home.html")

@web.route("/contact")
def contact():
    return render_template("contact.html")

@web.route("/about")
def about():
    return render_template("about.html")

@web.route("/bookings")
def bookings():
    return render_template("bookings.html")

@web.route("/topdest")
def topdest():
    return render_template("topdest.html")

@web.route("/feedback")
def feedback():
    return render_template("feedback.html")

@web.route("/savedata", methods = ["POST"])
def savedata():
    if request.method == "POST":
        Name = request.form.get("Name")
        email = request.form.get("Email")
        dep_date = request.form.get("Departure")
        ret_date = request.form.get("Return")
        destination = request.form.get("Destination")
        p_num = request.form.get("Phonenumber")
        image = request.files.get("img")
        print(image, "jggg")
    
    if image:
            image.save(os.path.join("static/images", image.filename))
            img = os.path.join(os.path.join("static/images/", image.filename))

    curser.execute(f"insert into mytravel values ('{Name}',  '{email}','{dep_date}',  '{ret_date}','{destination}','{p_num}','{img}') ")
    conn.commit() 
    
    return redirect("/showdata")
    
@web.route("/showdata")
def showdata():
    curser.execute("select * from mytravel;")
    data = curser.fetchall()
    return render_template("showdata.html", alldata = data)
    


if __name__ == "__main__":
    web.run(debug = True)