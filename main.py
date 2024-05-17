from flask import Flask, render_template, Response, request, jsonify, session
from flask_cors import CORS
import cv2
import cvzone
import time
import numpy as np

import poseModules.bicepcurl_front_PoseModule as pm_bicep

app = Flask(__name__)
app.secret_key = "your-secret-key"
CORS(app)


exercise_mode = ""

    
def gen():
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        if not success:
            break
        else:
            if exercise_mode == "":
                img_with_faces = no_detect(img)
            if exercise_mode == "bicep_curl":
                img_with_faces = bicep_curl(img)
            if exercise_mode == "goblet_squat":
                img_with_faces = goblet_squat(img)


            ret, jpeg = cv2.imencode('.jpg', img_with_faces)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
               
@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def no_detect(img):
    img = cv2.resize(img, (1280, 720))
    return img

def bicep_curl(img):
    global start_exercise_bicep, countdown_before_exercise_bicep
    img = cv2.resize(img, (1280, 720))

    if start_exercise_bicep == True:
        countdown_elapsed_time = time.time() - countdown_before_exercise_bicep
        countdown_remaining_time = max(0, 10 - countdown_elapsed_time)

        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color
        timer_text = f"Starting B: {int(countdown_remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    return img

def goblet_squat(img):
    global start_exercise_goblet, countdown_before_exercise_goblet
    img = cv2.resize(img, (1280, 720))

    if start_exercise_goblet == True:
        countdown_elapsed_time = time.time() - countdown_before_exercise_goblet
        countdown_remaining_time = max(0, 10 - countdown_elapsed_time)

        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color
        timer_text = f"Starting G: {int(countdown_remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
    return img
    

@app.route('/register', methods=["POST"])
def register():
    fullname = request.json["fullname"]
    age = request.json["age"]
    injury1 = request.json["injury1"]
    injury2 = request.json["injury2"]
    #print(f"{fullname} {age} {injury1} {injury2}")
    if int(age) <= 13 or int(age) >= 41:
        print("not allowed")
        return jsonify({'failed': "Ages 14-60 are allowed to use the program. "}, {'more': 'Learn More'})
    elif injury1 == "yes" or injury2 == "yes":
        return jsonify({"injury": "Injuries are not allowed. "}, {'more':'Learn More'})
    else:
        session['age'] = age
        print("allowed")
        

    session['fullname'] = fullname
    
    
    return jsonify({'success':'success'})

exercise = ""
@app.route('/choose_exercise', methods=["POST"])
def choose_exercise():
    global exercise
    exercise = request.json['chooseExercise']
    #print(exercise)
    # if exercise == {'exercise': 'bicep_curl'}:
    #     print('tama')
    # else:
    #     print('mali')
    return jsonify({'success': exercise})

@app.route('/exercise_choosed', methods=['POST'])
def exercise_choosed():
    global exercise
    #print(exercise)
    return jsonify({"exercise": exercise})

getExercises = ""

countdown_before_exercise_bicep = time.time()
start_exercise_bicep = False

countdown_before_exercise_goblet = time.time()
start_exercise_goblet = False

@app.route('/start_exercise', methods=['POST'])
def start_exercise():
    global exercise_mode, countdown_before_exercise_bicep, start_exercise_bicep, countdown_before_exercise_goblet, start_exercise_goblet
    getExercises = request.json['getExercises']
    print(getExercises)

    if getExercises == "Bicep Curl":
        exercise_mode = "bicep_curl"
        start_exercise_bicep = True
        countdown_before_exercise_bicep = time.time()
    else:
        exercise_mode = "goblet_squat"
        countdown_before_exercise_goblet = time.time()
        start_exercise_goblet = True
       
    return jsonify({"Success":"Success Get Exercises"})


@app.route('/back_exercise', methods=['POST'])
def back_exercise():
    global getExercises, exercise_mode
    getExercises = ""

    if getExercises == "":
        exercise_mode = ""

    return jsonify({"Success": "Success Delete Exercise"})
    





if __name__ == '__main__':
    app.run(debug=True, threaded=True, use_reloader=True)