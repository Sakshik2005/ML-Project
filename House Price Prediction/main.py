from flask import Flask , render_template, request
import pickle


app=Flask(__name__)

with open("house_price.pkl", mode="rb") as file:
    Linreg=pickle.load(file)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pred" ,methods=["GET" , "POST"])
def prediction():
    aai  = int(request.form.get("v1"))
    aaha = int(request.form.get("v2"))
    aanr = int(request.form.get("v3"))
    aanb = int(request.form.get("v4"))
    ap = int(request.form.get("v5"))

    yp= int(Linreg.predict([[aai, aaha, aanr, aanb, ap]])[0])
    

    return render_template("home.html" , price=yp)

if __name__ == "__main__" :
    app.run(debug=True)


