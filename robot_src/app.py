import socket
import bot
from flask import Flask, render_template, request, redirect, url_for, make_response
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)


# Get server ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
server_ip = s.getsockname()[0]
s.close()

app = Flask(__name__)


@app.route('/')
def index():
    
    data = bot.dht()
    humid = data[0]
    temp = data[1]

    return render_template('index.html', server_ip=server_ip, temperature=temp, humidity=humid)


@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    bot.init()

    changePin = int(changepin)

    if changePin == 1:
        # motors.turnLeft()
        bot.left()
    elif changePin == 2:
        bot.forward()
        # motors.forward()
    elif changePin == 3:
        bot.right()
        # motors.turnRight()
    elif changePin == 4:
        bot.backward()
        # motors.backward()
    elif changePin == 5:
        gpio.cleanup()
    else:
        print("Wrong command")

    response = make_response(redirect(url_for('index')))
    return(response)


app.run(debug=True, host='0.0.0.0', port=8000)
