from flask import Flask , render_template, request
import pickle
app=Flask(__name__)

with open("trainedmodel.pkl", mode="rb") as file:
    Linreg=pickle.load(file)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pred" ,methods=["GET" , "POST"])
def prediction():
    c1=int(request.form.get("v1"))
    c2=int(request.form.get("v2"))
    c3=int(request.form.get("v3"))
    c4=int(request.form.get("v4"))
    c5=int(request.form.get("v5"))
    c6=int(request.form.get("v6"))
    c7=int(request.form.get("v7"))
    c8=int(request.form.get("v8"))
    c9=int(request.form.get("v9"))
    c10=int(request.form.get("v10"))
    c11=int(request.form.get("v11"))
    c12=int(request.form.get("v12"))
    c13=int(request.form.get("v13"))
    c14=int(request.form.get("v14"))
    c15=int(request.form.get("v15"))
    c16=int(request.form.get("v16"))
    c17=int(request.form.get("v17"))
    c18=int(request.form.get("v18"))
    c19=int(request.form.get("v19"))

    yp= Linreg.predict([[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19 ]])[0]
    if yp== 1:
        result = "The customer is likely to churn."
    else:
        result = "The customer is not likely to churn."


    return render_template("home.html" , sales=result)

if __name__ == "__main__" :
    app.run(debug=True)


