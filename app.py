from flask import Flask, render_template
import json
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)


@app.route('/')
def home():
    f = open("together.txt")
    return render_template('home.html', text=json.dumps(f.read()))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
