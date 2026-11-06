import os
import json
import time
import redis
from flask import Flask

app = Flask(__name__)

r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "the-redis-server"),
    port=6379,
    decode_responses=True
)

def cached_page(key, html):
    data = r.get(key)

    if data is not None:
        data = json.loads(data)
        if time.time() - data["time"] <= 600:
            return data["html"]

    r.set(key, json.dumps({
    "html":html,
    "time":time.time()

    }))
    return html

@app.route("/")
def home():
    return cached_page("home", """
    <p>Welcome! this is another string</p>
    <p><a href="/about">about</a></p>
    <p><a href="/contact">Contact</a></p>
    """)

@app.route("/about")
def about():
    return cached_page("about", """
    <p>This application is on flask web framework</p>
    <p><a href="https://flask.palletsprojects.com/">Flask website</a></p>
    <p><a href="https://www.python.org/">Visit the python web</a></p>
    <p><a href="/">Home</a></p>
    """)

@app.route("/contact")
def contact():
    return cached_page("contact", """
    <p>Contact: maayan200510@gmail.com</p>
    <p><a href="/">Home</a></p>
    """)
