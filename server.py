# TODO
# actually make web server to relay info

from cpu import *
from gpu import *
from ram import *
from flask import Flask, request

app = Flask(__name__)

@app.route("/cpu")
def cpu():
    return str(CPU().TotalPercent())

@app.route("/gpu")
def gpu():
    return str(GPU().LoadPercent())

@app.route("/ram")
def ram():
    return str(RAM().Percent())

@app.route("/color")
def color():
    option = request.args.get("o")
    option = option.lower()
    if option == "cpu":
        percentage = CPU().TotalPercent()
    elif option == "gpu":
        percentage = GPU().LoadPercent()
    elif option == "ram":
        percentage = RAM().Percent()
    else:
        percentage = CPU().TotalPercent()
        
    percentage = percentage / 100
    if percentage < 0.5:
        green = ((255 - 0) * (1 - percentage)) + 0
    else:
        green = ((0 - 255) * percentage) + 255

    red = ((255 - 0) * percentage) + 0
    return f"{str(red)},{str(green)}"


app.run("0.0.0.0", 5000)