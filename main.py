from flask import Flask,request,jsonify


knjige = {
    "1":{
                    "title": "Professional JavaScript",
                    "authors": [
                        "Nicholas C. Zakas"
                    ],
                    "edition": 3,
                    "year": 2011
                },
    "2":
                {
                    "title": "Professional Python",
                    "authors": [
                        "Andrej C.Zakas"
                    ],
                    "edition": 4,
                    "year": 2012
                },
    "3":        {
                    "title": "Professional Ajax",
                    "authors": [
                        "Nicholas C. Zakas",
                        "Jeremy McPeak",
                        "Joe Fawcett"
                    ],
                    "edition": 2,
                    "year": 2008
                }
}

app = Flask(__name__)

@app.route("/books")
def books():
    data = jsonify(knjige)
    return data

@app.route("/books/<id>")
def books_by_id(id):
    if(id in knjige):
        return knjige[id]  
    return "<h1>NOT FOUND ERROR 404</h1>"

@app.route("/add",methods=["GET","POST"])
def add():
    if(request.method == "GET"):
        return "<h1>dodaj</h1>"
    elif(request.method == "POST"):
        data = request.get_json()
        knjige.update(data)
        return "dodano"


