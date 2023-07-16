from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)



def fetchDetails():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return str(host_name), str(host_ip)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health/")
def health():
    return jsonify(
        status = "Up"
    )

@app.route("/details")
def details():
    host_name, host_ip = fetchDetails()
    return render_template('index.html', host_name=host_name, host_ip = host_ip)



if __name__=="__main__":
    app.run()