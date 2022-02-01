#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request, send_from_directory
from camera import VideoCamera
import time
import threading
import os
import gopigo

pi_camera = VideoCamera(flip=True) # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

@app.route("/fwd")
def fwd():
    gopigo.fwd()
    return "{ 'gopigo': 'fwd' }"

@app.route("/halt")
def halt():
    gopigo.stop()
    return "{ 'gopigo': 'stop' }"

@app.route("/bwd")
def bwd():
    gopigo.bwd()
    return "{ 'gopigo': 'bwd' }"

@app.route("/left")
def left():
    gopigo.left()
    return "{ 'gopigo': 'left' }"

@app.route("/right")
def right():
    gopigo.right()
    return "{ 'gopigo': 'right' }"

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
    


