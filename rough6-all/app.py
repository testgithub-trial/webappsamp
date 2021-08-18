from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy, Model
app = Flask(__name__)


# @app.route("/", methods=["GET", "POST"])



@app.route("/vm", methods=["GET", "POST"])
def vm():
    if request.method == "POST":
        print("Hii")
        uname = request.form["uname"]
        zone = request.form["zone"]
        machine_type = request.form["machine_type"]
        OS_image = request.form["OS_image"]
        print(uname)
        print(machine_type)
        print(OS_image)
        with open("terraform.tfvars", "w") as fo:
            fo.write("name = " + '"'+uname+'"'+ "\n")
            fo.write("zone = "+'"'+zone+'"'+ "\n")
            fo.write("machine_type = " + '"' + machine_type + '"' + "\n")
            fo.write("image = " + '"'+OS_image+'"'+ "\n")


        return "hellooo ok"
    return render_template('vm.html')


@app.route("/vpc", methods=["GET", "POST"])
def vpc():
    if request.method == "POST":
        print("Hii")
        uname = request.form["uname"]
        region = request.form["region"]
        subnetname = request.form["subnetname"]
        subnetname0 = request.form["subnetname0"]
        subnetname00 = request.form["subnetname00"]
        region0 = request.form["region0"]
        region00 = request.form["region00"]

        # machine_type = request.form["machine_type"]
        # OS_image = request.form["OS_image"]
        # print(uname)
        # print(machine_type)
        # print(OS_image)
        with open("testing.tfvars", "w") as fo:
            fo.write("name = " + '"'+uname+'"'+ "\n")
            fo.write("subnetname = " + '"' + subnetname + '"' + "\n")
            fo.write("region = " + '"' + region + '"' + "\n")
            fo.write("subnetname0 = " + '"' + subnetname0 + '"' + "\n")
            fo.write("region0 = " + '"' + region0 + '"' + "\n")
            fo.write("subnetname00 = " + '"' + subnetname00 + '"' + "\n")
            fo.write("region00 = " + '"' + region00 + '"' + "\n")
            # fo.write("machine_type = " + '"' + machine_type + '"' + "\n")
            # fo.write("image = " + '"'+OS_image+'"'+ "\n")
            # fo.write("jj = kk \n")

        return render_template('Ok.html')
    return render_template('vpc.html')





@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True, port=5031)