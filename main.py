from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo


import openai



openai.api_key = "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"

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/chatgpt"
mongo = PyMongo(app)

@app.route('/')
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats= myChats)

@app.route("/api", methods=["GET","POST"])
def qa(): 
    if request.method == "POST":
         print(request.json)
         question = request.json.get("question")
         chat= mongo.db.chats.find_one({"question": question})
         print(chat)
         if chat:
             data = {"question": question, "answer" : f"{chat['answer']}"}
             return jsonify(data)
         else:
            response = openai.completions.create(
                model="davinci-002",
                prompt=question,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
)
            print(response)
            
            
            ans = response.choices[0].text
            data = {"question": question, "answer": ans}
            mongo.db.chats.insert_one(data)
            dta= {"answer" : ans}
            return jsonify(dta)
            #data = {"question": question, "answer": response["choices"][0]["text"]}
            #mongo.db.chats.insert_one({"question": question, "answer": response["choices"][0]["text"]})
            #return jsonify(data)
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss? "}
    return jsonify(data)
app.run(debug=True)