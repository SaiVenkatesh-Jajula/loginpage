from re import T
# from crypt import methods
from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)
#HOMEPAGE
@app.route("/")
def welco():
    return render_template("index.html")
#LOGIN SUCCESS ROUTE......RENDERING TEMPLATE OF HTML !
@app.route("/sucess/<id>")
def sucess(id):
    status=200
    lis=[id,status]
    return render_template("result.html",lis=lis)
#LOGIN FAILED ROUTE......!
@app.route("/fail/<id>")
def fail(id):
    status=400
    lis=[id,status]
    return render_template("result.html",lis=lis)

# @app.route("/results/<int:marks>")
# def results(marks):
#     if(marks>35):
#         result="sucess"
#     else:
#         result="fail"
#     return redirect(url_for(result,marks=marks))
#--------------------------------------------------------------------------------
#loginpage 
@app.route("/submit",methods=["POST","GET"])
def submit():
    if request.method=="POST":
        id = request.form.get("username")
        passs = request.form.get("password")       
        if id=="venkat" and passs=="sai":
            result="sucess"
        else:
            result="fail"
    return redirect(url_for(result,id=id))
    

if __name__=='__main__':
    app.run(debug=True)