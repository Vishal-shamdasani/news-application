from flask import Flask,render_template,request
import requests
import json
import os 

app=Flask(__name__,template_folder="template",static_folder="static")

@app.route("/")
def home():
    return render_template("index.html",N=refresh("top news"),I=refresh("india"),S=refresh("tesla"))


@app.route("/refresh")
def refresh(q):
    apikey=os.environ.get('api_key')
    news=requests.get(f"https://newsapi.org/v2/everything?q={q}&sortBy=publishedAt&apiKey={apikey}")
    b=(json.loads(news.text))

    values=""
    keys=["title","author","source","date","img","content","description"]
    article={}

    # print(b)
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
        article[i]["url"]=b["articles"][i]["url"]
        article[i]["img"]=b["articles"][i]["urlToImage"]
        article[i]["content"]=b["articles"][i]["content"]
        article[i]["description"]=b["articles"][i]["description"]
# print(article[0])
    return article

if __name__=="__main__":
    app.run()
    pass

# print(refresh("us"))