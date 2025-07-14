from flask import Flask,render_template
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import json
import os

load_dotenv()
with open("new_page_firebase_api_key.json", "w") as f:
    f.write(os.getenv("new_page_firebase_api_key"))
cred = credentials.Certificate("new_page_firebase_api_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': f"{os.getenv('firebase_url')}"
})


app=Flask(__name__,template_folder="template",static_folder="static")



@app.route("/")
def home():
    search_query = get_data("Top Stories")
    if search_query:
        return render_template("Clean-News-Article-Hub (1).html",articles=search_query)
    else:
        return render_template("error.html")


def update_data():
    for i in ["Politics","Science","Health","Entertainment","Sports","Business","Technology","Top Stories"]:
        print(f"Updating data for {i}")
        format_and_store_date(i)  # Fetch and store data for each category



def format_and_store_date(query:str):
    apikey=os.getenv("api_key")
    query = query.lower()
    print("🔥 Fetching data for:", query)
    news=requests.get(f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={apikey}")
    raw_api_data=(json.loads(news.text))

    values=""
    keys=["title","author","source","date","img","content","description"]
    article={}
    if raw_api_data['status'] not in [200,"ok"]:
        return raw_api_data
    
    for i in range(20):
        if raw_api_data["articles"][i]["title"]=='[Removed]' or not raw_api_data["articles"][i]["urlToImage"]:
            continue
        article[i]=article.get(i,dict.fromkeys(keys,values))
        article[i]["title"]=raw_api_data["articles"][i]["title"]
        article[i]["author"]=raw_api_data["articles"][i]["author"]
        article[i]["source"]=raw_api_data["articles"][i]["source"]["name"]
        article[i]["date"]=raw_api_data["articles"][i]["publishedAt"].split("T")[0]
        article[i]["url"]=raw_api_data["articles"][i]["url"]
        article[i]["img"]=raw_api_data["articles"][i]["urlToImage"]
        article[i]["content"]=raw_api_data["articles"][i]["content"]
        article[i]["description"]=raw_api_data["articles"][i]["description"]
    ref = db.reference('users')
    ref.child(query.lower()).set(article)
    
    return article

def get_data(query:str):
    query = query.lower()
    ref = db.reference('users')
    print("🔥 Searching for:", query)
    data = ref.child(query).get()
    if not data:
        print("data collected from api")
        return list(format_and_store_date(query).values())
    print("data found")
    # print(data)
    return data

@app.route("/<string:query>")
def search(query:str):
    print("🔥 Route hit with query:", query)
    print(f"searching for {query}")
    search_query = get_data(query)
    if search_query:
        return render_template("Clean-News-Article-Hub (1).html", articles=search_query)
    else:
        return render_template("error.html")

@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content, no crash

scheduler = BackgroundScheduler()
scheduler.add_job(update_data, 'interval', minutes=30)
scheduler.start()

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    pass