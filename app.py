from flask import Flask,render_template,request
import requests
import json

app=Flask(__name__,template_folder="template",static_folder="static")

@app.route("/")
def home():
    return render_template("index.html",N=refresh("us"),S=refresh("tesla"))


@app.route("/refresh")
def refresh(q):
        
    header={
        "country":f"{q}",
        "apikey":"you api key",
        
    }
    news=requests.get("https://newsapi.org/v2/top-headlines",params=header)
    b=(json.loads(news.text))

    values=""
    keys=["title","author","source","date","img","content","description"]
    article={}

    print(q,b,"\n\n")
    if b['totalResults']==0:
        return {}
    for i in range(20):
        if b["articles"][i]["title"]=='[Removed]':
            continue
        article[i]=article.get(i,dict.fromkeys(keys,values))
        article[i]["title"]=b["articles"][i]["title"]
        article[i]["author"]=b["articles"][i]["author"]
        article[i]["source"]=b["articles"][i]["source"]["name"]
        article[i]["date"]=b["articles"][i]["publishedAt"].split("T")[0]
        article[i]["img"]=b["articles"][i]["urlToImage"]
        article[i]["content"]=b["articles"][i]["content"]
        article[i]["description"]=b["articles"][i]["description"]
# print(article[0])
    return article

if __name__=="__main__":
    app.run(debug=True)
    pass