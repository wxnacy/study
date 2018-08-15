from flask import Flask
import os

# Connect to Redis

app = Flask(__name__)

@app.route("/")
def hello():

    html = "<h3>Hello {name}!</h3>"
    return html.format(name=os.getenv("NAME", "world"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8006)
