from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_data")
def get_data():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return jsonify(cpu_percent=cpu, mem_percent=mem)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
