from flask import Flask, render_template, Response, request, jsonify, session
from flask_cors import CORS
import cv2
import cvzone
import time
import numpy as np
import concurrent.futures

import poseModules.bicepcurl_front_PoseModule as pm_bicep
import poseModules.gobletsquat_front_PoseModule as pm_goblet




# -------------- BICEP CURL SET 1 ------------------
detector_bicep = pm_bicep.poseDetector()


dir_bicep_left = 0
dir_bicep_right = 0

 # starts time
display_info_bicep = False # display features

bar_left_bicep = 0
bar_right_bicep = 0
per_left_bicep = 0
per_right_bicep = 0
angle_left_bicep = 0
angle_right_bicep = 0

color_right_bicep = (0, 0, 255)
color_left_bicep = (0, 0, 255)

success_threshold_bicep = 100

atrest_value_bicep = 0

unsuccessful_reps_count_left_bicep = 0
successful_reps_count_left_bicep = 0

unsuccessful_reps_count_right_bicep = 0
successful_reps_count_right_bicep = 0

dir_bicep_left_unsuccessful_bicep = 0
dir_bicep_right_unsuccessful_bicep = 0

#timer
start_time1_bicep = time.time()
start_time2_bicep = time.time()
start_time3_bicep = time.time()
start_time4_bicep = time.time()
time_threshold_bicep = 5 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_bicep = 0
within_range_time2_bicep = 0
within_range_time3_bicep = 0

# gen feedback success
general_feedback = ""
general_feedback_unsuccessful = ""

gen_feedback_unsuccessful = ""
gen_feedback_unsuccessful_left = ""
gen_feedback_unsuccessful_right = ""

live_feedback_left_bicep = ""
live_feedback_right_bicep = ""

# gen feedback unsuccess
dir_gen_feedback_bicep = 0
dir_gen_feedback_unsuccessful_bicep = 0

sound_correct = r'D:\CPEDES\Fittology-Flask\audio\correct_final.WAV'
sound_incorrect = r'D:\CPEDES\Fittology-Flask\audio\wrong_final.WAV'

sound_gen_correct = r'D:\CPEDES\Fittology-Flask\audio\SUCCESFUL_MARIO.WAV'
sound_gen_incorrect = r'D:\CPEDES\Fittology-Flask\audio\UNSUCCESSFUL_MARIO.WAV'

tts_correct_left = "Correct left form!"
tts_correct_right = "Correct right form!"
tts_correct_both = "correct both form"

tts_incorrect_left = "incorrect left form"
tts_incorrect_right = "incorrect right form"
tts_incorrect_both = "incorrect both form"

total_successful_count_bicep = 0
total_unsuccessful_count_bicep = 0



rest_bicep_start_time = time.time()

executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)

text_correction = ""
live_feedback = ""
go_result_page = False
feedback_for_results = ""
feedback_for_unsuccessful_result = ""

# -------------- END BICEP CURL SET 1 --------------

# -------------- BICEP CURL SET 2 ------------------

dir_bicep_left_set2 = 0
dir_bicep_right_set2 = 0

 # starts time

display_info_bicep_set2 = True # display features

bar_left_bicep_set2 = 0
bar_right_bicep_set2 = 0
per_left_bicep_set2 = 0
per_right_bicep_set2 = 0
angle_left_bicep_set2 = 0
angle_right_bicep_set2 = 0

color_right_bicep_set2 = (0, 0, 255)
color_left_bicep_set2 = (0, 0, 255)

success_threshold_bicep_set2 = 100

atrest_value_bicep_set2 = 0

unsuccessful_reps_count_left_bicep_set2 = 0
successful_reps_count_left_bicep_set2 = 0

unsuccessful_reps_count_right_bicep_set2 = 0
successful_reps_count_right_bicep_set2 = 0

dir_bicep_left_unsuccessful_bicep_set2 = 0
dir_bicep_right_unsuccessful_bicep_set2 = 0

#timer
start_time1_bicep_set2 = time.time()
start_time2_bicep_set2 = time.time()
start_time3_bicep_set2 = time.time()
start_time4_bicep_set2 = time.time()
time_threshold_bicep_set2 = 5 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_bicep_set2 = 0
within_range_time2_bicep_set2 = 0
within_range_time3_bicep_set2 = 0

# gen feedback success
general_feedback_set2 = ""
general_feedback_unsuccessful_set2 = ""

gen_feedback_unsuccessful_set2 = ""
gen_feedback_unsuccessful_left_set2 = ""
gen_feedback_unsuccessful_right_set2 = ""

live_feedback_left_bicep_set2 = ""
live_feedback_right_bicep_set2 = ""

# gen feedback unsuccess
dir_gen_feedback_bicep_set2 = 0
dir_gen_feedback_unsuccessful_bicep_set2 = 0

sound_correct = r'D:\CPEDES\Fittology-Flask\audio\correct_final.WAV'
sound_incorrect = r'D:\CPEDES\Fittology-Flask\audio\wrong_final.WAV'

sound_gen_correct = r'D:\CPEDES\Fittology-Flask\audio\SUCCESFUL_MARIO.WAV'
sound_gen_incorrect = r'D:\CPEDES\Fittology-Flask\audio\UNSUCCESSFUL_MARIO.WAV'

tts_correct_left = "Correct left form!"
tts_correct_right = "Correct right form!"
tts_correct_both = "correct both form"

tts_incorrect_left = "incorrect left form"
tts_incorrect_right = "incorrect right form"
tts_incorrect_both = "incorrect both form"

total_successful_count_bicep_set2 = 0
total_unsuccessful_count_bicep_set2 = 0



rest_bicep_start_time_set2 = time.time()

feedback_for_results_set2 = ""
feedback_for_unsuccessful_result_set2 = ""

# -------------- END BICEP CURL SET 2 --------------

# -------------- BICEP CURL SET 3 ------------------

dir_bicep_left_set3 = 0
dir_bicep_right_set3 = 0

 # starts time

display_info_bicep_set3 = True # display features

bar_left_bicep_set3 = 0
bar_right_bicep_set3 = 0
per_left_bicep_set3 = 0
per_right_bicep_set3 = 0
angle_left_bicep_set3 = 0
angle_right_bicep_set3 = 0

color_right_bicep_set3 = (0, 0, 255)
color_left_bicep_set3 = (0, 0, 255)

success_threshold_bicep_set3 = 100

atrest_value_bicep_set3 = 0

unsuccessful_reps_count_left_bicep_set3 = 0
successful_reps_count_left_bicep_set3 = 0

unsuccessful_reps_count_right_bicep_set3 = 0
successful_reps_count_right_bicep_set3 = 0

dir_bicep_left_unsuccessful_bicep_set3 = 0
dir_bicep_right_unsuccessful_bicep_set3 = 0

#timer
start_time1_bicep_set3 = time.time()
start_time2_bicep_set3 = time.time()
start_time3_bicep_set3 = time.time()
start_time4_bicep_set3 = time.time()
time_threshold_bicep_set3 = 5 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time1_bicep_set3 = 0
within_range_time2_bicep_set3 = 0
within_range_time3_bicep_set3 = 0

# gen feedback success
general_feedback_set3 = ""
general_feedback_unsuccessful_set3 = ""

gen_feedback_unsuccessful_set3 = ""
gen_feedback_unsuccessful_left_set3 = ""
gen_feedback_unsuccessful_right_set3 = ""

live_feedback_left_bicep_set3 = ""
live_feedback_right_bicep_set3 = ""

# gen feedback unsuccess
dir_gen_feedback_bicep_set3 = 0
dir_gen_feedback_unsuccessful_bicep_set3 = 0

sound_correct = r'D:\CPEDES\Fittology-Flask\audio\correct_final.WAV'
sound_incorrect = r'D:\CPEDES\Fittology-Flask\audio\wrong_final.WAV'

sound_gen_correct = r'D:\CPEDES\Fittology-Flask\audio\SUCCESFUL_MARIO.WAV'
sound_gen_incorrect = r'D:\CPEDES\Fittology-Flask\audio\UNSUCCESSFUL_MARIO.WAV'

tts_correct_left = "Correct left form!"
tts_correct_right = "Correct right form!"
tts_correct_both = "correct both form"

tts_incorrect_left = "incorrect left form"
tts_incorrect_right = "incorrect right form"
tts_incorrect_both = "incorrect both form"

total_successful_count_bicep_set3 = 0
total_unsuccessful_count_bicep_set3 = 0



rest_bicep_start_time_set3 = time.time()


feedback_for_results_set3 = ""
feedback_for_unsuccessful_result_set3 = ""

# -------------- END BICEP CURL SET 3 --------------

# -------------- GOBLET SQUAT SET 1 ----------------
detector_gobletsquat = pm_goblet.poseDetectorGobletSquat()

dir_gobletsquat_left = 0
dir_gobletsquat_right = 0

repetition_time_gobletsquat = 60  # Repetition time

# Display info
display_info_gobletsquat = False

per_right_gobletsquat = 0
per_left_gobletsquat = 0
bar_left_gobletsquat = 0
bar_right_gobletsquat = 0 


color_right_gobletsquat = (0, 0, 255)
color_left_gobletsquat = (0, 0, 255)


success_threshold_gobletsquat = 100

atrest_value_gobletsquat = 0

unsuccessful_reps_count_left_gobletsquat = 0
successful_reps_count_left_gobletsquat = 0

unsuccessful_reps_count_right_gobletsquat = 0
successful_reps_count_right_gobletsquat = 0

dir_left_unsuccessful_gobletsquat = 0
dir_right_unsuccessful_gobletsquat = 0

start_time1_gobletsquat = time.time()
start_time4_gobletsquat = time.time()
time_threshold_gobletsquat = 5 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time3_gobletsquat = 0

# gen feedback success

# general_feedback = ""
general_feedback_left_gobletsquat = ""

# gen_feedback_unsuccessful = ""

# gen feedback unsuccess
dir_gen_feedback_gobletsquat = 0
dir_gen_feedback_unsuccessful_gobletsquat = 0

cooldown_timer_gobletsquat = 0

sound_correct_both = r'D:\CPEDES\Fittology-Flask\audio\correct_final.WAV'
sound_incorrect_both = r'D:\CPEDES\Fittology-Flask\audio\wrong_final.WAV'

# sound_gen_correct = r'D:\CPEDES\Fittology-Flask\audio\SUCCESFUL_MARIO.WAV'
# sound_gen_incorrect = r'D:\CPEDES\Fittology-Flask\audio\UNSUCCESSFUL_MARIO.WAV'

# tts_correct_both = "correct both form"
# tts_incorrect_both = "incorrect both form"

# executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)




live_gen_feedback_gobletsquat = ""

rest_goblet_start_time = time.time()

# -------------- END GOBLET SQUAT SET 1 ------------

# -------------- GOBLET SQUAT SET 2 ----------------
dir_gobletsquat_left_set2 = 0
dir_gobletsquat_right_set2 = 0


# Display info
display_info_gobletsquat_set2 = True

per_right_gobletsquat_set2 = 0
per_left_gobletsquat_set2 = 0
bar_left_gobletsquat_set2 = 0
bar_right_gobletsquat_set2 = 0 


color_right_gobletsquat_set2 = (0, 0, 255)
color_left_gobletsquat_set2 = (0, 0, 255)


success_threshold_gobletsquat_set2 = 100

atrest_value_gobletsquat_set2 = 0

unsuccessful_reps_count_left_gobletsquat_set2 = 0
successful_reps_count_left_gobletsquat_set2 = 0

unsuccessful_reps_count_right_gobletsquat_set2 = 0
successful_reps_count_right_gobletsquat_set2 = 0

dir_left_unsuccessful_gobletsquat_set2 = 0
dir_right_unsuccessful_gobletsquat_set2 = 0

start_time1_gobletsquat_set2 = time.time()
start_time4_gobletsquat_set2 = time.time()
time_threshold_gobletsquat_set2 = 5 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time3_gobletsquat_set2 = 0

# gen feedback success

general_feedback_set2 = ""
general_feedback_left_gobletsquat_set2 = ""

gen_feedback_unsuccessful_set2 = ""

# gen feedback unsuccess
dir_gen_feedback_gobletsquat_set2 = 0
dir_gen_feedback_unsuccessful_gobletsquat_set2 = 0

cooldown_timer_gobletsquat_set2 = 0

sound_correct_both = r'D:\CPEDES\Fittology-Flask\audio\correct_final.WAV'
sound_incorrect_both = r'D:\CPEDES\Fittology-Flask\audio\wrong_final.WAV'

# sound_gen_correct = r'D:\CPEDES\Fittology-Flask\audio\SUCCESFUL_MARIO.WAV'
# sound_gen_incorrect = r'D:\CPEDES\Fittology-Flask\audio\UNSUCCESSFUL_MARIO.WAV'

# tts_correct_both = "correct both form"
# tts_incorrect_both = "incorrect both form"

# executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)

live_gen_feedback_gobletsquat_set2 = ""

rest_goblet_start_time_set2 = time.time()

# -------------- END GOBLET SQUAT SET 2 ------------

# -------------- GOBLET SQUAT SET 2 ----------------
dir_gobletsquat_left_set3 = 0
dir_gobletsquat_right_set3 = 0


# Display info
display_info_gobletsquat_set3 = True

per_right_gobletsquat_set3 = 0
per_left_gobletsquat_set3 = 0
bar_left_gobletsquat_set3 = 0
bar_right_gobletsquat_set3 = 0 


color_right_gobletsquat_set3 = (0, 0, 255)
color_left_gobletsquat_set3 = (0, 0, 255)


success_threshold_gobletsquat_set3 = 100

atrest_value_gobletsquat_set3 = 0

unsuccessful_reps_count_left_gobletsquat_set3 = 0
successful_reps_count_left_gobletsquat_set3 = 0

unsuccessful_reps_count_right_gobletsquat_set3 = 0
successful_reps_count_right_gobletsquat_set3 = 0

dir_left_unsuccessful_gobletsquat_set3 = 0
dir_right_unsuccessful_gobletsquat_set3 = 0

start_time1_gobletsquat_set3 = time.time()
start_time4_gobletsquat_set3 = time.time()
time_threshold_gobletsquat_set3 = 5 # Specify the time threshold in seconds # can be changed for testing but default should be 1, 0.2 is for testing
within_range_time3_gobletsquat_set3 = 0

# gen feedback success

general_feedback_set3 = ""
general_feedback_left_gobletsquat_set3 = ""

gen_feedback_unsuccessful_set3 = ""

# gen feedback unsuccess
dir_gen_feedback_gobletsquat_set3 = 0
dir_gen_feedback_unsuccessful_gobletsquat_set3 = 0

cooldown_timer_gobletsquat_set3 = 0

sound_correct_both = r'D:\CPEDES\Fittology-Flask\audio\correct_final.WAV'
sound_incorrect_both = r'D:\CPEDES\Fittology-Flask\audio\wrong_final.WAV'

# sound_gen_correct = r'D:\CPEDES\Fittology-Flask\audio\SUCCESFUL_MARIO.WAV'
# sound_gen_incorrect = r'D:\CPEDES\Fittology-Flask\audio\UNSUCCESSFUL_MARIO.WAV'

# tts_correct_both = "correct both form"
# tts_incorrect_both = "incorrect both form"

# executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)

live_gen_feedback_gobletsquat_set3 = ""

rest_goblet_start_time_set3 = time.time()

# -------------- END GOBLET SQUAT SET 2 ------------

total_successful_count = 0 
total_unsuccessful_count = 0

total_successful_count_set2 = 0 
total_unsuccessful_count_set2 = 0

total_successful_count_set3 = 0 
total_unsuccessful_count_set3 = 0

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
            elif exercise_mode == "rest_bicep":
                img_with_faces = rest_bicep(img)
            elif exercise_mode == "bicep_curl_set2":
                img_with_faces = bicep_curl_set2(img)
            elif exercise_mode == "rest_bicep_set2":
                img_with_faces = rest_bicep_set2(img)
            elif exercise_mode == "bicep_curl_set3":
                img_with_faces = bicep_curl_set3(img)
            elif exercise_mode == "rest_bicep_set3":
                img_with_faces = rest_bicep_set3(img)


            if exercise_mode == "goblet_squat":
                img_with_faces = goblet_squat(img)
            elif exercise_mode == "rest_goblet":
                img_with_faces = rest_goblet(img)
            elif exercise_mode == "goblet_squat_set2":
                img_with_faces = goblet_squat_set2(img)
            elif exercise_mode == "rest_goblet_set2":
                img_with_faces =  rest_goblet_set2(img)
            elif exercise_mode == "goblet_squat_set3":
                img_with_faces = goblet_squat_set3(img)
            elif exercise_mode == "rest_goblet_set3":
                img_with_faces = rest_goblet_set3(img)
            


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
    global start_exercise_bicep, countdown_before_exercise_bicep, display_info_bicep, dir_bicep_left, dir_bicep_right, bar_left_bicep, bar_right_bicep, per_left_bicep, per_right_bicep, angle_left_bicep, angle_right_bicep, color_right_bicep, color_left_bicep, success_threshold_bicep, atrest_value_bicep, unsuccessful_reps_count_left_bicep, successful_reps_count_left_bicep, unsuccessful_reps_count_right_bicep, successful_reps_count_right_bicep, dir_bicep_left_unsuccessful_bicep, dir_bicep_right_unsuccessful_bicep, start_time1_bicep, start_time2_bicep, start_time3_bicep, start_time4_bicep, time_threshold_bicep, within_range_time1_bicep, within_range_time2_bicep, within_range_time3_bicep, general_feedback, gen_feedback_unsuccessful, gen_feedback_unsuccessful_left, gen_feedback_unsuccessful_right, live_feedback_left_bicep, live_feedback_right_bicep, dir_gen_feedback_bicep, dir_gen_feedback_unsuccessful_bicep, sound_correct, sound_incorrect, sound_gen_correct, sound_gen_incorrect, tts_correct_left, tts_correct_right, tts_correct_both, tts_incorrect_left, tts_incorrect_right, tts_incorrect_both, executor, total_successful_count_bicep, total_unsuccessful_count_bicep, exercise_mode, rest_bicep_start_time, text_correction, live_feedback, feedback_for_results, general_feedback_unsuccessful, feedback_for_unsuccessful_result, total_successful_count, total_unsuccessful_count



    img = cv2.resize(img, (1280, 720))

    if start_exercise_bicep == True:
        countdown_elapsed_time = time.time() - countdown_before_exercise_bicep
        countdown_remaining_time = max(0, 10 - countdown_elapsed_time)

        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color
        timer_text = f"Starting: {int(countdown_remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        if countdown_remaining_time <= 0:
            start_exercise_bicep = False
            display_info_bicep = True
    
    # Timer - starts timer based on set duration
    elapsed_time_bicep = time.time() - start_time1_bicep
    remaining_time_bicep = max(0, 70 - elapsed_time_bicep)

    if display_info_bicep:  # Check if to display counter, bar, and percentage
        img = detector_bicep.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_bicep.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:

            angle_left_bicep = detector_bicep.BicepCurl(img, 11 ,13, 15, True)
            angle_right_bicep = detector_bicep.BicepCurl(img, 12, 14 ,16, True)

            per_left_bicep = np.interp(angle_left_bicep, (30, 130), (100, 0)) 
            bar_left_bicep = np.interp(angle_left_bicep, (30, 140), (200, 400)) 

            per_right_bicep = np.interp(angle_right_bicep, (200, 340), (0, 100)) 
            bar_right_bicep = np.interp(angle_right_bicep, (200, 340), (400, 200)) 

            
            # color changer for the bar
            if int(per_left_bicep) == 100:
                color_left_bicep = (0, 255, 0)  # Change color of left leg bar to green
            elif int(per_right_bicep) == 100:
                color_right_bicep = (0, 255, 0)
            else:
                color_left_bicep = (0, 0, 255)  # Keep color of left leg bar as red
                color_right_bicep = (0, 0, 255)

            #both
            if 40 <= per_left_bicep <= 95 and 40 <= per_right_bicep <= 95:
                within_range_time3_bicep += time.time() - start_time4_bicep

                if within_range_time3_bicep >= time_threshold_bicep:
                    if dir_bicep_left_unsuccessful_bicep == 0 and dir_bicep_right_unsuccessful_bicep == 0:
                        unsuccessful_reps_count_left_bicep += 0.5
                        unsuccessful_reps_count_right_bicep += 0.5
                        executor.submit(detector_bicep.play_sound, sound_incorrect)
                        executor.submit(detector_bicep.tts_sound, tts_incorrect_both)
                        dir_bicep_left_unsuccessful_bicep = 1
                        dir_bicep_right_unsuccessful_bicep = 1
            else:
                within_range_time3_bicep = 0
                # Update the start time to the current time
                start_time4_bicep = time.time()

            if 1 <= per_left_bicep <= 10 and 1 <= per_right_bicep <= 10:
                if dir_bicep_left_unsuccessful_bicep == 1 and dir_bicep_right_unsuccessful_bicep == 1:
                    unsuccessful_reps_count_left_bicep += 0.5
                    unsuccessful_reps_count_right_bicep += 0.5
                    dir_bicep_left_unsuccessful_bicep = 0
                    dir_bicep_right_unsuccessful_bicep = 0
            
            if per_left_bicep == success_threshold_bicep and per_right_bicep == success_threshold_bicep:
                if dir_bicep_left == 0 and dir_bicep_right == 0:
                    successful_reps_count_left_bicep += 0.5
                    successful_reps_count_right_bicep += 0.5
                    dir_bicep_left = 1
                    dir_bicep_right = 1
                    executor.submit(detector_bicep.play_sound, sound_correct)
                    executor.submit(detector_bicep.tts_sound, tts_correct_both)

            elif per_left_bicep == atrest_value_bicep and per_right_bicep == atrest_value_bicep:
                if dir_bicep_left == 1 and dir_bicep_right == 1:
                    successful_reps_count_left_bicep += 0.5
                    successful_reps_count_right_bicep += 0.5
                    if successful_reps_count_left_bicep == successful_reps_count_right_bicep and 1 <= successful_reps_count_left_bicep <= 10:
                        live_feedback_left_bicep = detector_bicep.left_arm_feedback(successful_reps_count_left_bicep)
                        live_feedback_right_bicep = detector_bicep.right_arm_feedback(successful_reps_count_right_bicep)
                    dir_bicep_left = 0
                    dir_bicep_right = 0
                     
            #left
            if 40 <= per_left_bicep <= 95:
                # Increment the time within range
                within_range_time1_bicep += time.time() - start_time2_bicep

                # Check if peak value has been within range for the specified time
                if within_range_time1_bicep >= time_threshold_bicep:
                    if dir_bicep_left_unsuccessful_bicep == 0:
                        unsuccessful_reps_count_left_bicep += 0.5
                        executor.submit(detector_bicep.play_sound, sound_incorrect)
                        executor.submit(detector_bicep.tts_sound, tts_incorrect_left)
                        text_correction = "INCORRECT LEFT"
                        dir_bicep_left_unsuccessful_bicep = 1

            else:
                within_range_time1_bicep = 0
                # Update the start time to the current time
                start_time2_bicep = time.time()

            if 1 <= per_left_bicep <= 10:
                if dir_bicep_left_unsuccessful_bicep == 1:
                    unsuccessful_reps_count_left_bicep += 0.5
                    dir_bicep_left_unsuccessful_bicep = 0
                    text_correction = "ATREST"

            if per_left_bicep == success_threshold_bicep:
                if dir_bicep_left == 0:
                    successful_reps_count_left_bicep += 0.5
                    executor.submit(detector_bicep.play_sound, sound_correct)
                    executor.submit(detector_bicep.tts_sound, tts_correct_left)
                    text_correction = "CORRECT LEFT"
                    dir_bicep_left = 1
                
            elif per_left_bicep == atrest_value_bicep:
                if dir_bicep_left == 1:
                    successful_reps_count_left_bicep += 0.5
                    text_correction = "ATREST"
                    if 1 <= successful_reps_count_left_bicep <= 10:
                        live_feedback_left_bicep = detector_bicep.left_arm_feedback(successful_reps_count_left_bicep)
                        live_feedback = live_feedback_left_bicep
                    dir_bicep_left = 0

            # right
            if 40 <= per_right_bicep <= 95:
                # Increment the time within range
                within_range_time2_bicep += time.time() - start_time3_bicep

                # Check if peak value has been within range for the specified time
                if within_range_time2_bicep >= time_threshold_bicep:
                    if dir_bicep_right_unsuccessful_bicep == 0:
                        unsuccessful_reps_count_right_bicep += 0.5
                        dir_bicep_right_unsuccessful_bicep = 1
                        executor.submit(detector_bicep.play_sound, sound_incorrect)
                        executor.submit(detector_bicep.tts_sound, tts_incorrect_right)
                        text_correction = "INCORRECT RIGHT"
                        
            else:
                within_range_time2_bicep = 0
                # Update the start time to the current time
                start_time3_bicep = time.time()

            if 1 <= per_right_bicep <= 10:
                if dir_bicep_right_unsuccessful_bicep == 1:
                    unsuccessful_reps_count_right_bicep += 0.5
                    dir_bicep_right_unsuccessful_bicep = 0
                    text_correction = "ATREST"

            if per_right_bicep == success_threshold_bicep:
                if dir_bicep_right == 0:
                    successful_reps_count_right_bicep += 0.5
                    executor.submit(detector_bicep.play_sound, sound_correct)
                    executor.submit(detector_bicep.tts_sound, tts_correct_right)
                    text_correction = "CORRECT RIGHT"
                    dir_bicep_right = 1
         
                
            elif per_right_bicep == atrest_value_bicep:
                if dir_bicep_right == 1:
                    successful_reps_count_right_bicep += 0.5
                    text_correction = "ATREST"
                    if 1 <= successful_reps_count_right_bicep <= 10:
                        live_feedback_right_bicep = detector_bicep.right_arm_feedback(successful_reps_count_right_bicep)
                        live_feedback = live_feedback_right_bicep
                    dir_bicep_right = 0

        # label
        cvzone.putTextRect(img, 'Front Facing Bicep Curl Tracker', [440, 30], thickness=2, border=2, scale=1.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_bicep)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_bicep)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (8, int(bar_right_bicep)), (50, 400), color_right_bicep, -1)

        cv2.putText(img, f"L {int(per_left_bicep)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (952, int(bar_left_bicep)), (995, 400), color_left_bicep, -1)

    #counter in display
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_bicep)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_bicep)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # To check if time is still running
    if remaining_time_bicep <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bicep = False
        rest_bicep_start_time = time.time()
        exercise_mode = "rest_bicep"
        feedback_for_results = "You didn't complete the bicep curl in time. Keep practicing!"
        feedback_for_unsuccessful_result = ""


    # To be Fetched for total successful an unsuccessful count
    total_successful_count_bicep = successful_reps_count_right_bicep + successful_reps_count_left_bicep
    total_unsuccessful_count_bicep = unsuccessful_reps_count_left_bicep + unsuccessful_reps_count_right_bicep    

    total_successful_count = total_successful_count_bicep
    total_unsuccessful_count = total_unsuccessful_count_bicep


    if successful_reps_count_right_bicep >= 5 and successful_reps_count_left_bicep >= 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bicep = False

        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_bicep == 0:
            if 0 <= unsuccessful_reps_count_left_bicep <= 10:
                general_feedback = detector_bicep.gen_feedback_successful_count(total_successful_count_bicep)
                general_feedback_unsuccessful = detector_bicep.gen_feedback_unsuccessful(total_unsuccessful_count_bicep)
                executor.submit(detector_bicep.play_sound, sound_gen_correct)
                feedback_for_results = general_feedback
                feedback_for_unsuccessful_result = general_feedback_unsuccessful
                exercise_mode = "rest_bicep"
                rest_bicep_start_time = time.time()
            dir_gen_feedback_bicep = 1

    # # To check for unsuccessful arm rep counter # CHANGED
    if unsuccessful_reps_count_left_bicep == 3 and unsuccessful_reps_count_right_bicep == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for both arms. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep = False

        if dir_gen_feedback_unsuccessful_bicep == 0:
            gen_feedback_unsuccessful = detector_bicep.gen_feedback_unsuccessful(unsuccessful_reps_count_left_bicep, unsuccessful_reps_count_right_bicep)
            executor.submit(detector_bicep.play_sound, sound_gen_incorrect)
            exercise_mode = "rest_bicep"
            rest_bicep_start_time = time.time()
            dir_gen_feedback_unsuccessful_bicep = 1

    if unsuccessful_reps_count_left_bicep == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep = False

        if dir_gen_feedback_unsuccessful_bicep == 0:
            gen_feedback_unsuccessful_left = detector_bicep.left_arm_unsuccessful_feedback(unsuccessful_reps_count_left_bicep)
            executor.submit(detector_bicep.play_sound, sound_gen_incorrect)
            exercise_mode = "rest_bicep"
            rest_bicep_start_time = time.time()
            dir_gen_feedback_unsuccessful_bicep = 1
            feedback_for_results = ""
            feedback_for_unsuccessful_result = gen_feedback_unsuccessful_left

    if unsuccessful_reps_count_right_bicep == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep = False

        if dir_gen_feedback_unsuccessful_bicep == 0:
            gen_feedback_unsuccessful_right = detector_bicep.right_arm_unsuccessful_feedback(unsuccessful_reps_count_right_bicep)
            executor.submit(detector_bicep.play_sound, sound_gen_incorrect)
            exercise_mode = "rest_bicep"
            rest_bicep_start_time = time.time()
            dir_gen_feedback_unsuccessful_bicep = 1
            feedback_for_results = ""
            feedback_for_unsuccessful_result = gen_feedback_unsuccessful_right

    return img

def rest_bicep(img):
    global exercise_mode, rest_bicep_start_time, start_time1_bicep_set2 #go_result_page
    img = cv2.resize(img, (1280, 720))
    rest_elapsed_time = time.time() - rest_bicep_start_time
    #print(rest_elapsed_time)
    rest_remaining_time = max(0, 10 - int(rest_elapsed_time))
    

    # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        # go_result_page = True
        exercise_mode = "bicep_curl_set2"
        start_time1_bicep_set2 = time.time()

    return img

def bicep_curl_set2(img):
    global dir_bicep_left_set2, dir_bicep_right_set2, display_info_bicep_set2, bar_left_bicep_set2, bar_right_bicep_set2, per_left_bicep_set2, per_right_bicep_set2, angle_left_bicep_set2, angle_right_bicep_set2, color_right_bicep_set2, color_left_bicep_set2, success_threshold_bicep_set2, atrest_value_bicep_set2, unsuccessful_reps_count_left_bicep_set2, successful_reps_count_left_bicep_set2, unsuccessful_reps_count_right_bicep_set2, successful_reps_count_right_bicep_set2, dir_bicep_left_unsuccessful_bicep_set2, dir_bicep_right_unsuccessful_bicep_set2, start_time1_bicep_set2, start_time2_bicep_set2, start_time3_bicep_set2, start_time4_bicep_set2, time_threshold_bicep_set2, within_range_time1_bicep_set2, within_range_time2_bicep_set2, within_range_time3_bicep_set2, general_feedback_set2, general_feedback_unsuccessful_set2, gen_feedback_unsuccessful_set2, gen_feedback_unsuccessful_left_set2, gen_feedback_unsuccessful_right_set2, live_feedback_left_bicep_set2, live_feedback_right_bicep_set2, dir_gen_feedback_bicep_set2, dir_gen_feedback_unsuccessful_bicep_set2, sound_correct, sound_incorrect, sound_gen_correct, sound_gen_incorrect, tts_correct_left, tts_correct_right, tts_correct_both, tts_incorrect_left, tts_incorrect_right, tts_incorrect_both, total_successful_count_bicep_set2, total_unsuccessful_count_bicep_set2, rest_bicep_start_time_set2, text_correction, live_feedback, executor, feedback_for_results_set2, feedback_for_unsuccessful_result_set2, exercise_mode, total_successful_count_set2, total_unsuccessful_count_set2


    img = cv2.resize(img, (1280, 720))

    elapsed_time_bicep = time.time() - start_time1_bicep_set2
    remaining_time_bicep = max(0, 60 - elapsed_time_bicep)

    if display_info_bicep_set2:  # Check if to display counter, bar, and percentage
        img = detector_bicep.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_bicep.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:

            angle_left_bicep_set2 = detector_bicep.BicepCurl(img, 11 ,13, 15, True)
            angle_right_bicep_set2 = detector_bicep.BicepCurl(img, 12, 14 ,16, True)

            per_left_bicep_set2 = np.interp(angle_left_bicep_set2, (30, 130), (100, 0)) 
            bar_left_bicep_set2 = np.interp(angle_left_bicep_set2, (30, 140), (200, 400)) 

            per_right_bicep_set2 = np.interp(angle_right_bicep_set2, (200, 340), (0, 100)) 
            bar_right_bicep_set2 = np.interp(angle_right_bicep_set2, (200, 340), (400, 200)) 

            
            # color changer for the bar
            if int(per_left_bicep_set2) == 100:
                color_left_bicep_set2 = (0, 255, 0)  # Change color of left leg bar to green
            elif int(per_right_bicep_set2) == 100:
                color_right_bicep_set2 = (0, 255, 0)
            else:
                color_left_bicep_set2 = (0, 0, 255)  # Keep color of left leg bar as red
                color_right_bicep_set2 = (0, 0, 255)

            #both
            if 40 <= per_left_bicep_set2 <= 95 and 40 <= per_right_bicep_set2 <= 95:
                within_range_time3_bicep_set2 += time.time() - start_time4_bicep_set2

                if within_range_time3_bicep_set2 >= time_threshold_bicep_set2:
                    if dir_bicep_left_unsuccessful_bicep_set2 == 0 and dir_bicep_right_unsuccessful_bicep_set2 == 0:
                        unsuccessful_reps_count_left_bicep_set2 += 0.5
                        unsuccessful_reps_count_right_bicep_set2 += 0.5
                        executor.submit(detector_bicep.play_sound, sound_incorrect)
                        executor.submit(detector_bicep.tts_sound, tts_incorrect_both)
                        dir_bicep_left_unsuccessful_bicep_set2 = 1
                        dir_bicep_right_unsuccessful_bicep_set2 = 1
            else:
                within_range_time3_bicep_set2 = 0
                # Update the start time to the current time
                start_time4_bicep_set2 = time.time()

            if 1 <= per_left_bicep_set2 <= 10 and 1 <= per_right_bicep_set2 <= 10:
                if dir_bicep_left_unsuccessful_bicep_set2 == 1 and dir_bicep_right_unsuccessful_bicep_set2 == 1:
                    unsuccessful_reps_count_left_bicep_set2 += 0.5
                    unsuccessful_reps_count_right_bicep_set2 += 0.5
                    dir_bicep_left_unsuccessful_bicep_set2 = 0
                    dir_bicep_right_unsuccessful_bicep_set2 = 0
            
            if per_left_bicep_set2 == success_threshold_bicep_set2 and per_right_bicep_set2 == success_threshold_bicep_set2:
                if dir_bicep_left_set2 == 0 and dir_bicep_right_set2 == 0:
                    successful_reps_count_left_bicep_set2 += 0.5
                    successful_reps_count_right_bicep_set2 += 0.5
                    dir_bicep_left_set2 = 1
                    dir_bicep_right_set2 = 1
                    executor.submit(detector_bicep.play_sound, sound_correct)
                    executor.submit(detector_bicep.tts_sound, tts_correct_both)

            elif per_left_bicep_set2 == atrest_value_bicep_set2 and per_right_bicep_set2 == atrest_value_bicep_set2:
                if dir_bicep_left_set2 == 1 and dir_bicep_right_set2 == 1:
                    successful_reps_count_left_bicep_set2 += 0.5
                    successful_reps_count_right_bicep_set2 += 0.5
                    if successful_reps_count_left_bicep_set2 == successful_reps_count_right_bicep_set2 and 1 <= successful_reps_count_left_bicep_set2 <= 10:
                        live_feedback_left_bicep_set2 = detector_bicep.left_arm_feedback(successful_reps_count_left_bicep_set2)
                        live_feedback_right_bicep_set2 = detector_bicep.right_arm_feedback(successful_reps_count_right_bicep_set2)
                    dir_bicep_left_set2 = 0
                    dir_bicep_right_set2 = 0
                     
            #left
            if 40 <= per_left_bicep_set2 <= 95:
                # Increment the time within range
                within_range_time1_bicep_set2 += time.time() - start_time2_bicep_set2

                # Check if peak value has been within range for the specified time
                if within_range_time1_bicep_set2 >= time_threshold_bicep_set2:
                    if dir_bicep_left_unsuccessful_bicep_set2 == 0:
                        unsuccessful_reps_count_left_bicep_set2 += 0.5
                        executor.submit(detector_bicep.play_sound, sound_incorrect)
                        executor.submit(detector_bicep.tts_sound, tts_incorrect_left)
                        text_correction = "INCORRECT LEFT"
                        dir_bicep_left_unsuccessful_bicep_set2 = 1

            else:
                within_range_time1_bicep_set2 = 0
                # Update the start time to the current time
                start_time2_bicep_set2 = time.time()

            if 1 <= per_left_bicep_set2 <= 10:
                if dir_bicep_left_unsuccessful_bicep_set2 == 1:
                    unsuccessful_reps_count_left_bicep_set2 += 0.5
                    dir_bicep_left_unsuccessful_bicep_set2 = 0
                    text_correction = "ATREST"

            if per_left_bicep_set2 == success_threshold_bicep_set2:
                if dir_bicep_left_set2 == 0:
                    successful_reps_count_left_bicep_set2 += 0.5
                    executor.submit(detector_bicep.play_sound, sound_correct)
                    executor.submit(detector_bicep.tts_sound, tts_correct_left)
                    text_correction = "CORRECT LEFT"
                    dir_bicep_left_set2 = 1
                
            elif per_left_bicep_set2 == atrest_value_bicep_set2:
                if dir_bicep_left_set2 == 1:
                    successful_reps_count_left_bicep_set2 += 0.5
                    text_correction = "ATREST"
                    if 1 <= successful_reps_count_left_bicep_set2 <= 10:
                        live_feedback_left_bicep_set2 = detector_bicep.left_arm_feedback(successful_reps_count_left_bicep_set2)
                        live_feedback = live_feedback_left_bicep_set2
                    dir_bicep_left_set2 = 0

            # right
            if 40 <= per_right_bicep_set2 <= 95:
                # Increment the time within range
                within_range_time2_bicep_set2 += time.time() - start_time3_bicep_set2

                # Check if peak value has been within range for the specified time
                if within_range_time2_bicep_set2 >= time_threshold_bicep_set2:
                    if dir_bicep_right_unsuccessful_bicep_set2 == 0:
                        unsuccessful_reps_count_right_bicep_set2 += 0.5
                        dir_bicep_right_unsuccessful_bicep_set2 = 1
                        executor.submit(detector_bicep.play_sound, sound_incorrect)
                        executor.submit(detector_bicep.tts_sound, tts_incorrect_right)
                        text_correction = "INCORRECT RIGHT"
                        
            else:
                within_range_time2_bicep_set2 = 0
                # Update the start time to the current time
                start_time3_bicep_set2 = time.time()

            if 1 <= per_right_bicep_set2 <= 10:
                if dir_bicep_right_unsuccessful_bicep_set2 == 1:
                    unsuccessful_reps_count_right_bicep_set2 += 0.5
                    dir_bicep_right_unsuccessful_bicep_set2 = 0
                    text_correction = "ATREST"

            if per_right_bicep_set2 == success_threshold_bicep_set2:
                if dir_bicep_right_set2 == 0:
                    successful_reps_count_right_bicep_set2 += 0.5
                    executor.submit(detector_bicep.play_sound, sound_correct)
                    executor.submit(detector_bicep.tts_sound, tts_correct_right)
                    text_correction = "CORRECT RIGHT"
                    dir_bicep_right_set2 = 1
         
                
            elif per_right_bicep_set2 == atrest_value_bicep_set2:
                if dir_bicep_right_set2 == 1:
                    successful_reps_count_right_bicep_set2 += 0.5
                    text_correction = "ATREST"
                    if 1 <= successful_reps_count_right_bicep_set2 <= 10:
                        live_feedback_right_bicep_set2 = detector_bicep.right_arm_feedback(successful_reps_count_right_bicep_set2)
                        live_feedback = live_feedback_right_bicep_set2
                    dir_bicep_right_set2 = 0

        # label
        cvzone.putTextRect(img, 'Front Facing Bicep Curl SET 2', [440, 30], thickness=2, border=2, scale=1.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_bicep)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_bicep_set2)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (8, int(bar_right_bicep_set2)), (50, 400), color_right_bicep_set2, -1)

        cv2.putText(img, f"L {int(per_left_bicep_set2)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (952, int(bar_left_bicep_set2)), (995, 400), color_left_bicep_set2, -1)

    #counter in display
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_bicep_set2)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_bicep_set2)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # To check if time is still running
    if remaining_time_bicep <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bicep_set2 = False
        rest_bicep_start_time_set2 = time.time()
        exercise_mode = "rest_bicep_set2"
        feedback_for_results_set2 = "You didn't complete the bicep curl in time. Keep practicing!"
        feedback_for_unsuccessful_result_set2 = ""


    # To be Fetched for total successful an unsuccessful count
    total_successful_count_bicep_set2 = successful_reps_count_right_bicep_set2 + successful_reps_count_left_bicep_set2
    total_unsuccessful_count_bicep_set2 = unsuccessful_reps_count_left_bicep_set2 + unsuccessful_reps_count_right_bicep_set2    

    total_successful_count_set2 = total_successful_count_bicep_set2
    total_unsuccessful_count_set2 = total_unsuccessful_count_bicep_set2


    if successful_reps_count_right_bicep_set2 >= 5 and successful_reps_count_left_bicep_set2 >= 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bicep_set2 = False

        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_bicep_set2 == 0:
            if 0 <= unsuccessful_reps_count_left_bicep_set2 <= 10:
                general_feedback_set2 = detector_bicep.gen_feedback_successful_count(total_successful_count_bicep_set2)
                general_feedback_unsuccessful_set2 = detector_bicep.gen_feedback_unsuccessful(total_unsuccessful_count_bicep_set2)
                executor.submit(detector_bicep.play_sound, sound_gen_correct)
                feedback_for_results_set2 = general_feedback_set2
                feedback_for_unsuccessful_result_set2 = general_feedback_unsuccessful_set2
                exercise_mode = "rest_bicep_set2"
                rest_bicep_start_time_set2 = time.time()
            dir_gen_feedback_bicep_set2 = 1

    # # To check for unsuccessful arm rep counter # CHANGED
    if unsuccessful_reps_count_left_bicep_set2 == 3 and unsuccessful_reps_count_right_bicep_set2 == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for both arms. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep_set2 = False

        if dir_gen_feedback_unsuccessful_bicep_set2 == 0:
            gen_feedback_unsuccessful_set2 = detector_bicep.gen_feedback_unsuccessful(unsuccessful_reps_count_left_bicep_set2, unsuccessful_reps_count_right_bicep_set2)
            executor.submit(detector_bicep.play_sound, sound_gen_incorrect)
            exercise_mode = "rest_bicep_set2"
            rest_bicep_start_time_set2 = time.time()
            dir_gen_feedback_unsuccessful_bicep_set2 = 1


    if unsuccessful_reps_count_left_bicep_set2 == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep_set2 = False

        if dir_gen_feedback_unsuccessful_bicep_set2 == 0:
            gen_feedback_unsuccessful_left_set2 = detector_bicep.left_arm_unsuccessful_feedback(unsuccessful_reps_count_left_bicep_set2)
            executor.submit(detector_bicep.play_sound, sound_gen_incorrect)
            exercise_mode = "rest_bicep_set2"
            rest_bicep_start_time_set2 = time.time()
            dir_gen_feedback_unsuccessful_bicep_set2 = 1
            feedback_for_results_set2 = ""
            feedback_for_unsuccessful_result_set2 = gen_feedback_unsuccessful_left_set2

    if unsuccessful_reps_count_right_bicep_set2 == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep_set2 = False

        if dir_gen_feedback_unsuccessful_bicep_set2 == 0:
            gen_feedback_unsuccessful_right_set2 = detector_bicep.right_arm_unsuccessful_feedback(unsuccessful_reps_count_right_bicep_set2)
            executor.submit(detector_bicep.play_sound, sound_gen_incorrect)
            exercise_mode = "rest_bicep_set2"
            rest_bicep_start_time_set2 = time.time()
            dir_gen_feedback_unsuccessful_bicep_set2 = 1
            feedback_for_results_set2 = ""
            feedback_for_unsuccessful_result_set2 = gen_feedback_unsuccessful_right_set2
    return img


def rest_bicep_set2(img):
    global exercise_mode, rest_bicep_start_time_set2, start_time1_bicep_set3 #go_result_page
    img = cv2.resize(img, (1280, 720))
    rest_elapsed_time = time.time() - rest_bicep_start_time_set2
    #print(rest_elapsed_time)
    rest_remaining_time = max(0, 10 - int(rest_elapsed_time))
    

    # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        # go_result_page = True
        exercise_mode = "bicep_curl_set3"
        start_time1_bicep_set3 = time.time()
    return img

def bicep_curl_set3(img):
    global dir_bicep_left_set3, dir_bicep_right_set3, display_info_bicep_set3, bar_left_bicep_set3, bar_right_bicep_set3, per_left_bicep_set3, per_right_bicep_set3, angle_left_bicep_set3, angle_right_bicep_set3, color_right_bicep_set3, color_left_bicep_set3, success_threshold_bicep_set3, atrest_value_bicep_set3, unsuccessful_reps_count_left_bicep_set3, successful_reps_count_left_bicep_set3, unsuccessful_reps_count_right_bicep_set3, successful_reps_count_right_bicep_set3, dir_bicep_left_unsuccessful_bicep_set3, dir_bicep_right_unsuccessful_bicep_set3, start_time1_bicep_set3, start_time2_bicep_set3, start_time3_bicep_set3, start_time4_bicep_set3, time_threshold_bicep_set3, within_range_time1_bicep_set3, within_range_time2_bicep_set3, within_range_time3_bicep_set3, general_feedback_set3, general_feedback_unsuccessful_set3, gen_feedback_unsuccessful_set3, gen_feedback_unsuccessful_left_set3, gen_feedback_unsuccessful_right_set3, live_feedback_left_bicep_set3, live_feedback_right_bicep_set3, dir_gen_feedback_bicep_set3, dir_gen_feedback_unsuccessful_bicep_set3, sound_correct, sound_incorrect, sound_gen_correct, sound_gen_incorrect, tts_correct_left, tts_correct_right, tts_correct_both, tts_incorrect_left, tts_incorrect_right, tts_incorrect_both, total_successful_count_bicep_set3, total_unsuccessful_count_bicep_set3, rest_bicep_start_time_set3, text_correction, live_feedback, executor, feedback_for_results_set3, feedback_for_unsuccessful_result_set3, exercise_mode, total_successful_count_set3, total_unsuccessful_count_set3


    img = cv2.resize(img, (1280, 720))

    elapsed_time_bicep = time.time() - start_time1_bicep_set3
    remaining_time_bicep = max(0, 60 - elapsed_time_bicep)

    if display_info_bicep_set3:  # Check if to display counter, bar, and percentage
        img = detector_bicep.findPose(img, False) # initializes img as variable for findpose function
        lmList_bicep = detector_bicep.findPosition(img, False) # initializes lmList_bicep as variable for findPosition function

        # Define hand angles outside the if statement
        if len(lmList_bicep) != 0:

            angle_left_bicep_set3 = detector_bicep.BicepCurl(img, 11 ,13, 15, True)
            angle_right_bicep_set3 = detector_bicep.BicepCurl(img, 12, 14 ,16, True)

            per_left_bicep_set3 = np.interp(angle_left_bicep_set3, (30, 130), (100, 0)) 
            bar_left_bicep_set3 = np.interp(angle_left_bicep_set3, (30, 140), (200, 400)) 

            per_right_bicep_set3 = np.interp(angle_right_bicep_set3, (200, 340), (0, 100)) 
            bar_right_bicep_set3 = np.interp(angle_right_bicep_set3, (200, 340), (400, 200)) 

            
            # color changer for the bar
            if int(per_left_bicep_set3) == 100:
                color_left_bicep_set3 = (0, 255, 0)  # Change color of left leg bar to green
            elif int(per_right_bicep_set3) == 100:
                color_right_bicep_set3 = (0, 255, 0)
            else:
                color_left_bicep_set3 = (0, 0, 255)  # Keep color of left leg bar as red
                color_right_bicep_set3 = (0, 0, 255)

            #both
            if 40 <= per_left_bicep_set3 <= 95 and 40 <= per_right_bicep_set3 <= 95:
                within_range_time3_bicep_set3 += time.time() - start_time4_bicep_set3

                if within_range_time3_bicep_set3 >= time_threshold_bicep_set3:
                    if dir_bicep_left_unsuccessful_bicep_set3 == 0 and dir_bicep_right_unsuccessful_bicep_set3 == 0:
                        unsuccessful_reps_count_left_bicep_set3 += 0.5
                        unsuccessful_reps_count_right_bicep_set3 += 0.5
                        executor.submit(detector_bicep.play_sound, sound_incorrect)
                        executor.submit(detector_bicep.tts_sound, tts_incorrect_both)
                        dir_bicep_left_unsuccessful_bicep_set3 = 1
                        dir_bicep_right_unsuccessful_bicep_set3 = 1
            else:
                within_range_time3_bicep_set3 = 0
                # Update the start time to the current time
                start_time4_bicep_set3 = time.time()

            if 1 <= per_left_bicep_set3 <= 10 and 1 <= per_right_bicep_set3 <= 10:
                if dir_bicep_left_unsuccessful_bicep_set3 == 1 and dir_bicep_right_unsuccessful_bicep_set3 == 1:
                    unsuccessful_reps_count_left_bicep_set3 += 0.5
                    unsuccessful_reps_count_right_bicep_set3 += 0.5
                    dir_bicep_left_unsuccessful_bicep_set3 = 0
                    dir_bicep_right_unsuccessful_bicep_set3 = 0
            
            if per_left_bicep_set3 == success_threshold_bicep_set3 and per_right_bicep_set3 == success_threshold_bicep_set3:
                if dir_bicep_left_set3 == 0 and dir_bicep_right_set3 == 0:
                    successful_reps_count_left_bicep_set3 += 0.5
                    successful_reps_count_right_bicep_set3 += 0.5
                    dir_bicep_left_set3 = 1
                    dir_bicep_right_set3 = 1
                    executor.submit(detector_bicep.play_sound, sound_correct)
                    executor.submit(detector_bicep.tts_sound, tts_correct_both)

            elif per_left_bicep_set3 == atrest_value_bicep_set3 and per_right_bicep_set3 == atrest_value_bicep_set3:
                if dir_bicep_left_set3 == 1 and dir_bicep_right_set3 == 1:
                    successful_reps_count_left_bicep_set3 += 0.5
                    successful_reps_count_right_bicep_set3 += 0.5
                    if successful_reps_count_left_bicep_set3 == successful_reps_count_right_bicep_set3 and 1 <= successful_reps_count_left_bicep_set3 <= 10:
                        live_feedback_left_bicep_set3 = detector_bicep.left_arm_feedback(successful_reps_count_left_bicep_set3)
                        live_feedback_right_bicep_set3 = detector_bicep.right_arm_feedback(successful_reps_count_right_bicep_set3)
                    dir_bicep_left_set3 = 0
                    dir_bicep_right_set3 = 0
                     
            #left
            if 40 <= per_left_bicep_set3 <= 95:
                # Increment the time within range
                within_range_time1_bicep_set3 += time.time() - start_time2_bicep_set3

                # Check if peak value has been within range for the specified time
                if within_range_time1_bicep_set3 >= time_threshold_bicep_set3:
                    if dir_bicep_left_unsuccessful_bicep_set3 == 0:
                        unsuccessful_reps_count_left_bicep_set3 += 0.5
                        executor.submit(detector_bicep.play_sound, sound_incorrect)
                        executor.submit(detector_bicep.tts_sound, tts_incorrect_left)
                        text_correction = "INCORRECT LEFT"
                        dir_bicep_left_unsuccessful_bicep_set3 = 1

            else:
                within_range_time1_bicep_set3 = 0
                # Update the start time to the current time
                start_time2_bicep_set3 = time.time()

            if 1 <= per_left_bicep_set3 <= 10:
                if dir_bicep_left_unsuccessful_bicep_set3 == 1:
                    unsuccessful_reps_count_left_bicep_set3 += 0.5
                    dir_bicep_left_unsuccessful_bicep_set3 = 0
                    text_correction = "ATREST"

            if per_left_bicep_set3 == success_threshold_bicep_set3:
                if dir_bicep_left_set3 == 0:
                    successful_reps_count_left_bicep_set3 += 0.5
                    executor.submit(detector_bicep.play_sound, sound_correct)
                    executor.submit(detector_bicep.tts_sound, tts_correct_left)
                    text_correction = "CORRECT LEFT"
                    dir_bicep_left_set3 = 1
                
            elif per_left_bicep_set3 == atrest_value_bicep_set3:
                if dir_bicep_left_set3 == 1:
                    successful_reps_count_left_bicep_set3 += 0.5
                    text_correction = "ATREST"
                    if 1 <= successful_reps_count_left_bicep_set3 <= 10:
                        live_feedback_left_bicep_set3 = detector_bicep.left_arm_feedback(successful_reps_count_left_bicep_set3)
                        live_feedback = live_feedback_left_bicep_set3
                    dir_bicep_left_set3 = 0

            # right
            if 40 <= per_right_bicep_set3 <= 95:
                # Increment the time within range
                within_range_time2_bicep_set3 += time.time() - start_time3_bicep_set3

                # Check if peak value has been within range for the specified time
                if within_range_time2_bicep_set3 >= time_threshold_bicep_set3:
                    if dir_bicep_right_unsuccessful_bicep_set3 == 0:
                        unsuccessful_reps_count_right_bicep_set3 += 0.5
                        dir_bicep_right_unsuccessful_bicep_set3 = 1
                        executor.submit(detector_bicep.play_sound, sound_incorrect)
                        executor.submit(detector_bicep.tts_sound, tts_incorrect_right)
                        text_correction = "INCORRECT RIGHT"
                        
            else:
                within_range_time2_bicep_set3 = 0
                # Update the start time to the current time
                start_time3_bicep_set3 = time.time()

            if 1 <= per_right_bicep_set3 <= 10:
                if dir_bicep_right_unsuccessful_bicep_set3 == 1:
                    unsuccessful_reps_count_right_bicep_set3 += 0.5
                    dir_bicep_right_unsuccessful_bicep_set3 = 0
                    text_correction = "ATREST"

            if per_right_bicep_set3 == success_threshold_bicep_set3:
                if dir_bicep_right_set3 == 0:
                    successful_reps_count_right_bicep_set3 += 0.5
                    executor.submit(detector_bicep.play_sound, sound_correct)
                    executor.submit(detector_bicep.tts_sound, tts_correct_right)
                    text_correction = "CORRECT RIGHT"
                    dir_bicep_right_set3 = 1
         
                
            elif per_right_bicep_set3 == atrest_value_bicep_set3:
                if dir_bicep_right_set3 == 1:
                    successful_reps_count_right_bicep_set3 += 0.5
                    text_correction = "ATREST"
                    if 1 <= successful_reps_count_right_bicep_set3 <= 10:
                        live_feedback_right_bicep_set3 = detector_bicep.right_arm_feedback(successful_reps_count_right_bicep_set3)
                        live_feedback = live_feedback_right_bicep_set3
                    dir_bicep_right_set3 = 0

        # label
        cvzone.putTextRect(img, 'Front Facing Bicep Curl SET 3', [440, 30], thickness=2, border=2, scale=1.5) 

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_bicep)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        # bar
        cv2.putText(img, f"R {int(per_right_bicep_set3)}%" , (24, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 200), (50, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (8, int(bar_right_bicep_set3)), (50, 400), color_right_bicep_set3, -1)

        cv2.putText(img, f"L {int(per_left_bicep_set3)}%", (962, 195), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 200), (995, 400), (255, 255, 255), 5)
        cv2.rectangle(img, (952, int(bar_left_bicep_set3)), (995, 400), color_left_bicep_set3, -1)

    #counter in display
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_bicep_set3)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_bicep_set3)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    # To check if time is still running
    if remaining_time_bicep <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bicep_set3 = False
        rest_bicep_start_time_set3 = time.time()
        exercise_mode = "rest_bicep_set3"
        feedback_for_results_set3 = "You didn't complete the bicep curl in time. Keep practicing!"
        feedback_for_unsuccessful_result_set3 = ""


    # To be Fetched for total successful an unsuccessful count
    total_successful_count_bicep_set3 = successful_reps_count_right_bicep_set3 + successful_reps_count_left_bicep_set3
    total_unsuccessful_count_bicep_set3 = unsuccessful_reps_count_left_bicep_set3 + unsuccessful_reps_count_right_bicep_set3    

    total_successful_count_set3 = total_successful_count_bicep_set3
    total_unsuccessful_count_set3 = total_unsuccessful_count_bicep_set3


    if successful_reps_count_right_bicep_set3 >= 5 and successful_reps_count_left_bicep_set3 >= 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_bicep_set3 = False

        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_bicep_set3 == 0:
            if 0 <= unsuccessful_reps_count_left_bicep_set3 <= 10:
                general_feedback_set3 = detector_bicep.gen_feedback_successful_count(total_successful_count_bicep_set3)
                general_feedback_unsuccessful_set3 = detector_bicep.gen_feedback_unsuccessful(total_unsuccessful_count_bicep_set3)
                executor.submit(detector_bicep.play_sound, sound_gen_correct)
                feedback_for_results_set3 = general_feedback_set3
                feedback_for_unsuccessful_result_set3 = general_feedback_unsuccessful_set3
                exercise_mode = "rest_bicep_set3"
                rest_bicep_start_time_set3 = time.time()
            dir_gen_feedback_bicep_set3 = 1

    # # To check for unsuccessful arm rep counter # CHANGED
    if unsuccessful_reps_count_left_bicep_set3 == 3 and unsuccessful_reps_count_right_bicep_set3 == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for both arms. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep_set3 = False

        if dir_gen_feedback_unsuccessful_bicep_set3 == 0:
            gen_feedback_unsuccessful_set3 = detector_bicep.gen_feedback_unsuccessful(unsuccessful_reps_count_left_bicep_set3, unsuccessful_reps_count_right_bicep_set3)
            executor.submit(detector_bicep.play_sound, sound_gen_incorrect)
            exercise_mode = "rest_bicep_set3"
            rest_bicep_start_time_set3 = time.time()
            dir_gen_feedback_unsuccessful_bicep_set3 = 1

    if unsuccessful_reps_count_left_bicep_set3 == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for left arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep_set3 = False

        if dir_gen_feedback_unsuccessful_bicep_set3 == 0:
            gen_feedback_unsuccessful_left_set3 = detector_bicep.left_arm_unsuccessful_feedback(unsuccessful_reps_count_left_bicep_set3)
            executor.submit(detector_bicep.play_sound, sound_gen_incorrect)
            exercise_mode = "rest_bicep_set3"
            rest_bicep_start_time_set3 = time.time()
            dir_gen_feedback_unsuccessful_bicep_set3 = 1
            feedback_for_results_set3 = ""
            feedback_for_unsuccessful_result_set3 = gen_feedback_unsuccessful_left_set3

    if unsuccessful_reps_count_right_bicep_set3 == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for right arm. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_bicep_set3 = False

        if dir_gen_feedback_unsuccessful_bicep_set3 == 0:
            gen_feedback_unsuccessful_right_set3 = detector_bicep.right_arm_unsuccessful_feedback(unsuccessful_reps_count_right_bicep_set3)
            executor.submit(detector_bicep.play_sound, sound_gen_incorrect)
            exercise_mode = "rest_bicep_set3"
            rest_bicep_start_time_set3 = time.time()
            dir_gen_feedback_unsuccessful_bicep_set3 = 1
            feedback_for_results_set3 = ""
            feedback_for_unsuccessful_result_set3 = gen_feedback_unsuccessful_right_set3
    return img

def rest_bicep_set3(img):
    global exercise_mode, rest_bicep_start_time_set3, go_result_page
    img = cv2.resize(img, (1280, 720))
    rest_elapsed_time = time.time() - rest_bicep_start_time_set3
    #print(rest_elapsed_time)
    rest_remaining_time = max(0, 10 - int(rest_elapsed_time))
    

    # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        go_result_page = True
    return img


def goblet_squat(img):
    global start_exercise_goblet, countdown_before_exercise_goblet, display_info_gobletsquat, start_time1_gobletsquat, dir_gobletsquat_left, dir_gobletsquat_right, per_right_gobletsquat, per_left_gobletsquat, bar_left_gobletsquat, bar_right_gobletsquat, color_right_gobletsquat, color_left_gobletsquat, success_threshold_gobletsquat, atrest_value_gobletsquat, unsuccessful_reps_count_left_gobletsquat, successful_reps_count_left_gobletsquat, unsuccessful_reps_count_right_gobletsquat, successful_reps_count_right_gobletsquat, dir_left_unsuccessful_gobletsquat, dir_right_unsuccessful_gobletsquat, start_time4_gobletsquat, time_threshold_gobletsquat, within_range_time3_gobletsquat, general_feedback, general_feedback_left_gobletsquat, gen_feedback_unsuccessful, dir_gen_feedback_gobletsquat, dir_gen_feedback_unsuccessful_gobletsquat, cooldown_timer_gobletsquat, sound_correct_both, sound_incorrect_both, sound_gen_correct, sound_gen_incorrect, tts_correct_both, tts_incorrect_both, rest_goblet_start_time, executor, total_successful_count, total_unsuccessful_count, live_gen_feedback_gobletsquat, exercise_mode, text_correction, live_feedback, feedback_for_results, feedback_for_unsuccessful_result, general_feedback_unsuccessful
    img = cv2.resize(img, (1280, 720))

    if start_exercise_goblet == True:
        countdown_elapsed_time = time.time() - countdown_before_exercise_goblet
        countdown_remaining_time = max(0, 10 - countdown_elapsed_time)

        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color
        timer_text = f"Starting: {int(countdown_remaining_time)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

        if countdown_remaining_time <= 0:
            start_exercise_goblet = False
            display_info_gobletsquat = True

    elapsed_time_gobletsquat = time.time() - start_time1_gobletsquat
    remaining_time_gobletsquat = max(0, 70 - elapsed_time_gobletsquat)

    if display_info_gobletsquat:  # Check if to display counter, bar, and percentage
        img = detector_gobletsquat.findPose(img, False)
        lmList_gobletsquat = detector_gobletsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_gobletsquat) != 0:

            # Right and Left keypoints
            rightleg_gobletsquat = detector_gobletsquat.GobletSquat(img, 24, 26, 28, True)
            leftleg_gobletsquat = detector_gobletsquat.GobletSquat(img, 23, 25, 27, True)

            if cooldown_timer_gobletsquat > 0:
                cooldown_timer_gobletsquat -= 1

            per_right_gobletsquat = np.interp(rightleg_gobletsquat, (160, 240), (100, 0))
            bar_right_gobletsquat = np.interp(rightleg_gobletsquat, (160, 240), (480, 680))
            per_left_gobletsquat = np.interp(leftleg_gobletsquat, (160, 240), (100, 0))
            bar_left_gobletsquat = np.interp(leftleg_gobletsquat, (160, 240), (480, 680))


            if int(per_left_gobletsquat) == 100:
                color_left_gobletsquat = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_gobletsquat = (0, 0, 255)
            
            if int(per_right_gobletsquat) == 100:
                color_right_gobletsquat = (0, 255, 0)
            else:
                color_right_gobletsquat = (0, 0, 255)

            #both
            if 40 <= per_left_gobletsquat <= 95 and 40 <= per_right_gobletsquat <= 95:
                within_range_time3_gobletsquat += time.time() - start_time4_gobletsquat
                #start_time4_gobletsquat = time.time() 

                if within_range_time3_gobletsquat >= time_threshold_gobletsquat:
                    if dir_left_unsuccessful_gobletsquat == 0 and dir_right_unsuccessful_gobletsquat == 0:
                        unsuccessful_reps_count_left_gobletsquat += 0.5
                        unsuccessful_reps_count_right_gobletsquat += 0.5
                        executor.submit(detector_gobletsquat.play_sound, sound_incorrect_both)
                        executor.submit(detector_gobletsquat.tts_sound, tts_incorrect_both)
                        text_correction = "INCORRECT BOTH"
                        dir_left_unsuccessful_gobletsquat = 1
                        dir_right_unsuccessful_gobletsquat = 1
                        
            else:
                within_range_time3_gobletsquat = 0
                # Update the start time to the current time
                start_time4_gobletsquat = time.time()

            if 1 <= per_left_gobletsquat <= 10 and 1 <= per_right_gobletsquat <= 10:
                if dir_left_unsuccessful_gobletsquat == 1 and dir_right_unsuccessful_gobletsquat == 1:
                    unsuccessful_reps_count_left_gobletsquat += 0.5
                    unsuccessful_reps_count_right_gobletsquat += 0.5
                    dir_left_unsuccessful_gobletsquat = 0
                    dir_right_unsuccessful_gobletsquat = 0
                    text_correction = "ATREST"

            if per_left_gobletsquat == success_threshold_gobletsquat and per_right_gobletsquat == success_threshold_gobletsquat:
                if dir_gobletsquat_left == 0 and dir_gobletsquat_right == 0:
                    successful_reps_count_left_gobletsquat += 0.5
                    successful_reps_count_right_gobletsquat += 0.5
                    dir_gobletsquat_left = 1
                    dir_gobletsquat_right = 1
                    executor.submit(detector_gobletsquat.play_sound, sound_correct_both)
                    executor.submit(detector_gobletsquat.tts_sound, tts_correct_both)
                    text_correction = "CORRECT BOTH"

            elif per_left_gobletsquat == atrest_value_gobletsquat and per_right_gobletsquat == atrest_value_gobletsquat:
                if dir_gobletsquat_left == 1 and dir_gobletsquat_right == 1:
                    successful_reps_count_left_gobletsquat += 0.5
                    successful_reps_count_right_gobletsquat += 0.5
                    text_correction = "ATREST"
                    if successful_reps_count_left_gobletsquat == successful_reps_count_right_gobletsquat and 1 <= successful_reps_count_left_gobletsquat <= 10:
                        live_gen_feedback_gobletsquat = detector_gobletsquat.leg_feedback(successful_reps_count_left_gobletsquat, successful_reps_count_right_gobletsquat)
                        live_feedback = live_gen_feedback_gobletsquat
                    dir_gobletsquat_left = 0
                    dir_gobletsquat_right = 0


        cvzone.putTextRect(img, 'Front Goblet Squat Tracker', [450, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_gobletsquat)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_gobletsquat)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_gobletsquat)), (50, 680), color_right_gobletsquat, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_gobletsquat)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_gobletsquat)), (995, 680), color_left_gobletsquat, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_gobletsquat)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_gobletsquat)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)


    #Timer
    if remaining_time_gobletsquat <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_gobletsquat = False
        rest_goblet_start_time = time.time()
        exercise_mode = "rest_goblet"
        feedback_for_results = "You didn't complete the goblet squat in time. Keep practicing!"
        feedback_for_unsuccessful_result = ""

    total_successful_count = successful_reps_count_right_gobletsquat + successful_reps_count_left_gobletsquat
    total_unsuccessful_count = unsuccessful_reps_count_left_gobletsquat + unsuccessful_reps_count_right_gobletsquat    

    if successful_reps_count_right_gobletsquat == 5 and successful_reps_count_left_gobletsquat == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_gobletsquat = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_gobletsquat == 0:
            if 0 <= unsuccessful_reps_count_left_gobletsquat <= 10:
                general_feedback = detector_gobletsquat.gen_feedback_successful_count(total_successful_count)
                executor.submit(detector_gobletsquat.play_sound, sound_gen_correct)
                general_feedback_unsuccessful = detector_gobletsquat.gen_feedback_unsuccessful_count(total_unsuccessful_count)
                feedback_for_results = general_feedback
                feedback_for_unsuccessful_result = general_feedback_unsuccessful
                rest_goblet_start_time = time.time()
                exercise_mode = "rest_goblet"
            dir_gen_feedback_gobletsquat = 1

    # # To check for unsuccessful arm rep counter # CHANGED
    if unsuccessful_reps_count_left_gobletsquat == 3 and unsuccessful_reps_count_right_gobletsquat == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for both arms. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat = False

        if dir_gen_feedback_unsuccessful_gobletsquat == 0:
            gen_feedback_unsuccessful = detector_gobletsquat.gen_feedback_unsuccessful(unsuccessful_reps_count_left_gobletsquat, unsuccessful_reps_count_right_gobletsquat)
            rest_goblet_start_time = time.time()
            exercise_mode = "rest_goblet"
            feedback_for_results = ""
            feedback_for_unsuccessful_result = gen_feedback_unsuccessful
            dir_gen_feedback_unsuccessful_gobletsquat = 1
            executor.submit(detector_gobletsquat.play_sound, sound_gen_incorrect)
    return img

def rest_goblet(img):
    global exercise_mode, rest_goblet_start_time, start_time1_gobletsquat_set2 #go_result_page
    img = cv2.resize(img, (1280, 720))
    rest_elapsed_time = time.time() - rest_goblet_start_time
    #print(rest_elapsed_time)
    rest_remaining_time = max(0, 10 - int(rest_elapsed_time))
    

    # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        #go_result_page = True
        exercise_mode = "goblet_squat_set2"
        start_time1_gobletsquat_set2 = time.time()

    return img

def goblet_squat_set2(img):
    global display_info_gobletsquat_set2, start_time1_gobletsquat_set2, dir_gobletsquat_left_set2, dir_gobletsquat_right_set2, per_right_gobletsquat_set2, per_left_gobletsquat_set2, bar_left_gobletsquat_set2, bar_right_gobletsquat_set2, color_right_gobletsquat_set2, color_left_gobletsquat_set2, success_threshold_gobletsquat_set2, atrest_value_gobletsquat_set2, unsuccessful_reps_count_left_gobletsquat_set2, successful_reps_count_left_gobletsquat_set2, unsuccessful_reps_count_right_gobletsquat_set2, successful_reps_count_right_gobletsquat_set2, dir_left_unsuccessful_gobletsquat_set2, dir_right_unsuccessful_gobletsquat_set2, start_time4_gobletsquat_set2, time_threshold_gobletsquat_set2, within_range_time3_gobletsquat_set2, general_feedback_set2, general_feedback_left_gobletsquat_set2, gen_feedback_unsuccessful_set2, dir_gen_feedback_gobletsquat_set2, dir_gen_feedback_unsuccessful_gobletsquat_set2, cooldown_timer_gobletsquat_set2, sound_correct_both, sound_incorrect_both, sound_gen_correct, sound_gen_incorrect, tts_correct_both, tts_incorrect_both, rest_goblet_start_time_set2, executor, total_successful_count_set2, total_unsuccessful_count_set2, live_gen_feedback_gobletsquat_set2, exercise_mode, text_correction, live_feedback, feedback_for_results_set2, feedback_for_unsuccessful_result_set2, general_feedback_unsuccessful_set2

    img = cv2.resize(img, (1280, 720))

    elapsed_time_gobletsquat = time.time() - start_time1_gobletsquat_set2
    remaining_time_gobletsquat = max(0, 60 - elapsed_time_gobletsquat)

    if display_info_gobletsquat_set2:  # Check if to display counter, bar, and percentage
        img = detector_gobletsquat.findPose(img, False)
        lmList_gobletsquat = detector_gobletsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_gobletsquat) != 0:

            # Right and Left keypoints
            rightleg_gobletsquat_set2 = detector_gobletsquat.GobletSquat(img, 24, 26, 28, True)
            leftleg_gobletsquat_set2 = detector_gobletsquat.GobletSquat(img, 23, 25, 27, True)

            if cooldown_timer_gobletsquat_set2 > 0:
                cooldown_timer_gobletsquat_set2 -= 1

            per_right_gobletsquat_set2 = np.interp(rightleg_gobletsquat_set2, (160, 240), (100, 0))
            bar_right_gobletsquat_set2 = np.interp(rightleg_gobletsquat_set2, (160, 240), (480, 680))
            per_left_gobletsquat_set2 = np.interp(leftleg_gobletsquat_set2, (160, 240), (100, 0))
            bar_left_gobletsquat_set2 = np.interp(leftleg_gobletsquat_set2, (160, 240), (480, 680))


            if int(per_left_gobletsquat_set2) == 100:
                color_left_gobletsquat_set2 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_gobletsquat_set2 = (0, 0, 255)
            
            if int(per_right_gobletsquat_set2) == 100:
                color_right_gobletsquat_set2 = (0, 255, 0)
            else:
                color_right_gobletsquat_set2 = (0, 0, 255)

            #both
            if 40 <= per_left_gobletsquat_set2 <= 95 and 40 <= per_right_gobletsquat_set2 <= 95:
                within_range_time3_gobletsquat_set2 += time.time() - start_time4_gobletsquat_set2
                #start_time4_gobletsquat = time.time() 

                if within_range_time3_gobletsquat_set2 >= time_threshold_gobletsquat_set2:
                    if dir_left_unsuccessful_gobletsquat_set2 == 0 and dir_right_unsuccessful_gobletsquat_set2 == 0:
                        unsuccessful_reps_count_left_gobletsquat_set2 += 0.5
                        unsuccessful_reps_count_right_gobletsquat_set2 += 0.5
                        executor.submit(detector_gobletsquat.play_sound, sound_incorrect_both)
                        executor.submit(detector_gobletsquat.tts_sound, tts_incorrect_both)
                        text_correction = "INCORRECT BOTH"
                        dir_left_unsuccessful_gobletsquat_set2 = 1
                        dir_right_unsuccessful_gobletsquat_set2 = 1
                        
            else:
                within_range_time3_gobletsquat_set2 = 0
                # Update the start time to the current time
                start_time4_gobletsquat_set2 = time.time()

            if 1 <= per_left_gobletsquat_set2 <= 10 and 1 <= per_right_gobletsquat_set2 <= 10:
                if dir_left_unsuccessful_gobletsquat_set2 == 1 and dir_right_unsuccessful_gobletsquat_set2 == 1:
                    unsuccessful_reps_count_left_gobletsquat_set2 += 0.5
                    unsuccessful_reps_count_right_gobletsquat_set2 += 0.5
                    dir_left_unsuccessful_gobletsquat_set2 = 0
                    dir_right_unsuccessful_gobletsquat_set2 = 0
                    text_correction = "ATREST"

            if per_left_gobletsquat_set2 == success_threshold_gobletsquat_set2 and per_right_gobletsquat_set2 == success_threshold_gobletsquat_set2:
                if dir_gobletsquat_left_set2 == 0 and dir_gobletsquat_right_set2 == 0:
                    successful_reps_count_left_gobletsquat_set2 += 0.5
                    successful_reps_count_right_gobletsquat_set2 += 0.5
                    dir_gobletsquat_left_set2 = 1
                    dir_gobletsquat_right_set2 = 1
                    executor.submit(detector_gobletsquat.play_sound, sound_correct_both)
                    executor.submit(detector_gobletsquat.tts_sound, tts_correct_both)
                    text_correction = "CORRECT BOTH"

            elif per_left_gobletsquat_set2 == atrest_value_gobletsquat_set2 and per_right_gobletsquat_set2 == atrest_value_gobletsquat_set2:
                if dir_gobletsquat_left_set2 == 1 and dir_gobletsquat_right_set2 == 1:
                    successful_reps_count_left_gobletsquat_set2 += 0.5
                    successful_reps_count_right_gobletsquat_set2 += 0.5
                    text_correction = "ATREST"
                    if successful_reps_count_left_gobletsquat_set2 == successful_reps_count_right_gobletsquat_set2 and 1 <= successful_reps_count_left_gobletsquat_set2 <= 10:
                        live_gen_feedback_gobletsquat_set2 = detector_gobletsquat.leg_feedback(successful_reps_count_left_gobletsquat_set2, successful_reps_count_right_gobletsquat_set2)
                        live_feedback = live_gen_feedback_gobletsquat_set2
                    dir_gobletsquat_left_set2 = 0
                    dir_gobletsquat_right_set2 = 0


        cvzone.putTextRect(img, 'Front Goblet Squat SET 2', [450, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_gobletsquat)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_gobletsquat_set2)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_gobletsquat_set2)), (50, 680), color_right_gobletsquat_set2, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_gobletsquat_set2)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_gobletsquat_set2)), (995, 680), color_left_gobletsquat_set2, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_gobletsquat_set2)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_gobletsquat_set2)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)


    #Timer
    if remaining_time_gobletsquat <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_gobletsquat_set2 = False
        rest_goblet_start_time_set2 = time.time()
        exercise_mode = "rest_goblet_set2"
        feedback_for_results_set2 = "You didn't complete the goblet squat in time. Keep practicing!"
        feedback_for_unsuccessful_result_set2 = ""

    total_successful_count_set2 = successful_reps_count_right_gobletsquat_set2 + successful_reps_count_left_gobletsquat_set2
    total_unsuccessful_count_set2 = unsuccessful_reps_count_left_gobletsquat_set2 + unsuccessful_reps_count_right_gobletsquat_set2    

    if successful_reps_count_right_gobletsquat_set2 == 5 and successful_reps_count_left_gobletsquat_set2 == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_gobletsquat_set2 = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_gobletsquat_set2 == 0:
            if 0 <= unsuccessful_reps_count_left_gobletsquat_set2 <= 10:
                general_feedback_set2 = detector_gobletsquat.gen_feedback_successful_count(total_successful_count_set2)
                executor.submit(detector_gobletsquat.play_sound, sound_gen_correct)
                general_feedback_unsuccessful_set2 = detector_gobletsquat.gen_feedback_unsuccessful_count(total_unsuccessful_count_set2)
                feedback_for_results_set2 = general_feedback_set2
                feedback_for_unsuccessful_result_set2 = general_feedback_unsuccessful_set2
                rest_goblet_start_time_set2 = time.time()
                exercise_mode = "rest_goblet_set2"
            dir_gen_feedback_gobletsquat_set2 = 1

    # # To check for unsuccessful arm rep counter # CHANGED
    if unsuccessful_reps_count_left_gobletsquat_set2 == 3 and unsuccessful_reps_count_right_gobletsquat_set2 == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for both arms. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat_set2 = False

        if dir_gen_feedback_unsuccessful_gobletsquat_set2 == 0:
            gen_feedback_unsuccessful_set2 = detector_gobletsquat.gen_feedback_unsuccessful(unsuccessful_reps_count_left_gobletsquat_set2, unsuccessful_reps_count_right_gobletsquat_set2)
            rest_goblet_start_time_set2 = time.time()
            exercise_mode = "rest_goblet_set2"
            feedback_for_results_set2 = ""
            feedback_for_unsuccessful_result_set2 = gen_feedback_unsuccessful_set2
            dir_gen_feedback_unsuccessful_gobletsquat_set2 = 1
            executor.submit(detector_gobletsquat.play_sound, sound_gen_incorrect)

    return img

def rest_goblet_set2(img):
    global exercise_mode, rest_goblet_start_time_set2, start_time1_gobletsquat_set3 #go_result_page
    img = cv2.resize(img, (1280, 720))
    rest_elapsed_time = time.time() - rest_goblet_start_time_set2
    #print(rest_elapsed_time)
    rest_remaining_time = max(0, 10 - int(rest_elapsed_time))
    

    # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        #go_result_page = True
        exercise_mode = "goblet_squat_set3"
        start_time1_gobletsquat_set3 = time.time()
    return img

def goblet_squat_set3(img):
    global display_info_gobletsquat_set3, start_time1_gobletsquat_set3, dir_gobletsquat_left_set3, dir_gobletsquat_right_set3, per_right_gobletsquat_set3, per_left_gobletsquat_set3, bar_left_gobletsquat_set3, bar_right_gobletsquat_set3, color_right_gobletsquat_set3, color_left_gobletsquat_set3, success_threshold_gobletsquat_set3, atrest_value_gobletsquat_set3, unsuccessful_reps_count_left_gobletsquat_set3, successful_reps_count_left_gobletsquat_set3, unsuccessful_reps_count_right_gobletsquat_set3, successful_reps_count_right_gobletsquat_set3, dir_left_unsuccessful_gobletsquat_set3, dir_right_unsuccessful_gobletsquat_set3, start_time4_gobletsquat_set3, time_threshold_gobletsquat_set3, within_range_time3_gobletsquat_set3, general_feedback_set3, general_feedback_left_gobletsquat_set3, gen_feedback_unsuccessful_set3, dir_gen_feedback_gobletsquat_set3, dir_gen_feedback_unsuccessful_gobletsquat_set3, cooldown_timer_gobletsquat_set3, sound_correct_both, sound_incorrect_both, sound_gen_correct, sound_gen_incorrect, tts_correct_both, tts_incorrect_both, rest_goblet_start_time_set3, executor, total_successful_count_set3, total_unsuccessful_count_set3, live_gen_feedback_gobletsquat_set3, exercise_mode, text_correction, live_feedback, feedback_for_results_set3, feedback_for_unsuccessful_result_set3, general_feedback_unsuccessful_set3

    img = cv2.resize(img, (1280, 720))

    elapsed_time_gobletsquat = time.time() - start_time1_gobletsquat_set3
    remaining_time_gobletsquat = max(0, 60 - elapsed_time_gobletsquat)

    if display_info_gobletsquat_set3:  # Check if to display counter, bar, and percentage
        img = detector_gobletsquat.findPose(img, False)
        lmList_gobletsquat = detector_gobletsquat.findPosition(img, False)

        # Define angles for jumping jacks outside the if statement
        if len(lmList_gobletsquat) != 0:

            # Right and Left keypoints
            rightleg_gobletsquat_set3 = detector_gobletsquat.GobletSquat(img, 24, 26, 28, True)
            leftleg_gobletsquat_set3 = detector_gobletsquat.GobletSquat(img, 23, 25, 27, True)

            if cooldown_timer_gobletsquat_set3 > 0:
                cooldown_timer_gobletsquat_set3 -= 1

            per_right_gobletsquat_set3 = np.interp(rightleg_gobletsquat_set3, (160, 240), (100, 0))
            bar_right_gobletsquat_set3 = np.interp(rightleg_gobletsquat_set3, (160, 240), (480, 680))
            per_left_gobletsquat_set3 = np.interp(leftleg_gobletsquat_set3, (160, 240), (100, 0))
            bar_left_gobletsquat_set3 = np.interp(leftleg_gobletsquat_set3, (160, 240), (480, 680))


            if int(per_left_gobletsquat_set3) == 100:
                color_left_gobletsquat_set3 = (0, 255, 0)  # Change color of left leg bar to green
            else:
                color_left_gobletsquat_set3 = (0, 0, 255)
            
            if int(per_right_gobletsquat_set3) == 100:
                color_right_gobletsquat_set3 = (0, 255, 0)
            else:
                color_right_gobletsquat_set3 = (0, 0, 255)

            #both
            if 40 <= per_left_gobletsquat_set3 <= 95 and 40 <= per_right_gobletsquat_set3 <= 95:
                within_range_time3_gobletsquat_set3 += time.time() - start_time4_gobletsquat_set3
                #start_time4_gobletsquat = time.time() 

                if within_range_time3_gobletsquat_set3 >= time_threshold_gobletsquat_set3:
                    if dir_left_unsuccessful_gobletsquat_set3 == 0 and dir_right_unsuccessful_gobletsquat_set3 == 0:
                        unsuccessful_reps_count_left_gobletsquat_set3 += 0.5
                        unsuccessful_reps_count_right_gobletsquat_set3 += 0.5
                        executor.submit(detector_gobletsquat.play_sound, sound_incorrect_both)
                        executor.submit(detector_gobletsquat.tts_sound, tts_incorrect_both)
                        text_correction = "INCORRECT BOTH"
                        dir_left_unsuccessful_gobletsquat_set3 = 1
                        dir_right_unsuccessful_gobletsquat_set3 = 1
                        
            else:
                within_range_time3_gobletsquat_set3 = 0
                # Update the start time to the current time
                start_time4_gobletsquat_set3 = time.time()

            if 1 <= per_left_gobletsquat_set3 <= 10 and 1 <= per_right_gobletsquat_set3 <= 10:
                if dir_left_unsuccessful_gobletsquat_set3 == 1 and dir_right_unsuccessful_gobletsquat_set3 == 1:
                    unsuccessful_reps_count_left_gobletsquat_set3 += 0.5
                    unsuccessful_reps_count_right_gobletsquat_set3 += 0.5
                    dir_left_unsuccessful_gobletsquat_set3 = 0
                    dir_right_unsuccessful_gobletsquat_set3 = 0
                    text_correction = "ATREST"

            if per_left_gobletsquat_set3 == success_threshold_gobletsquat_set2 and per_right_gobletsquat_set3 == success_threshold_gobletsquat_set3:
                if dir_gobletsquat_left_set3 == 0 and dir_gobletsquat_right_set3 == 0:
                    successful_reps_count_left_gobletsquat_set3 += 0.5
                    successful_reps_count_right_gobletsquat_set3 += 0.5
                    dir_gobletsquat_left_set3 = 1
                    dir_gobletsquat_right_set3 = 1
                    executor.submit(detector_gobletsquat.play_sound, sound_correct_both)
                    executor.submit(detector_gobletsquat.tts_sound, tts_correct_both)
                    text_correction = "CORRECT BOTH"

            elif per_left_gobletsquat_set3 == atrest_value_gobletsquat_set3 and per_right_gobletsquat_set3 == atrest_value_gobletsquat_set3:
                if dir_gobletsquat_left_set3 == 1 and dir_gobletsquat_right_set3 == 1:
                    successful_reps_count_left_gobletsquat_set3 += 0.5
                    successful_reps_count_right_gobletsquat_set3 += 0.5
                    text_correction = "ATREST"
                    if successful_reps_count_left_gobletsquat_set3 == successful_reps_count_right_gobletsquat_set3 and 1 <= successful_reps_count_left_gobletsquat_set3 <= 10:
                        live_gen_feedback_gobletsquat_set3 = detector_gobletsquat.leg_feedback(successful_reps_count_left_gobletsquat_set3, successful_reps_count_right_gobletsquat_set3)
                        live_feedback = live_gen_feedback_gobletsquat_set3
                    dir_gobletsquat_left_set3 = 0
                    dir_gobletsquat_right_set3 = 0


        cvzone.putTextRect(img, 'Front Goblet Squat SET 3', [450, 30], thickness=2, border=2, scale=1.5)

        # Draw rectangle behind the timer text
        cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

        # Draw timer text above the rectangle
        timer_text = f"Time left: {int(remaining_time_gobletsquat)}s"
        cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)
        # RIGHT LEG
        cv2.putText(img, f"R {int(per_right_gobletsquat_set3)}%", (24, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (8, 480), (50, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (8, int(bar_right_gobletsquat_set3)), (50, 680), color_right_gobletsquat_set3, -1)

        # LEFT LEG
        cv2.putText(img, f"L {int(per_left_gobletsquat_set3)}%", (962, 470), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 255), 7)
        cv2.rectangle(img, (952, 480), (995, 680), (0, 255, 0), 5)
        cv2.rectangle(img, (952, int(bar_left_gobletsquat_set3)), (995, 680), color_left_gobletsquat_set3, -1)

    # Counter 
    cv2.rectangle(img, (20, 20), (200, 130), (0, 0, 255), -1)
    cv2.putText(img, f"{int(successful_reps_count_right_gobletsquat_set3)}/5", (30, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)

    cv2.rectangle(img, (210, 20), (390, 130), (255, 0, 0), -1)
    cv2.putText(img, f"{int(successful_reps_count_left_gobletsquat_set3)}/5", (220, 90), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.6, (255, 255, 255), 7)


    #Timer
    if remaining_time_gobletsquat <= 0:
        cvzone.putTextRect(img, "Time's Up", [420, 30], thickness=2, border=2, scale=2.5)
        display_info_gobletsquat_set3 = False
        rest_goblet_start_time_set3 = time.time()
        exercise_mode = "rest_goblet_set3"
        feedback_for_results_set3 = "You didn't complete the goblet squat in time. Keep practicing!"
        feedback_for_unsuccessful_result_set3 = ""

    total_successful_count_set3 = successful_reps_count_right_gobletsquat_set3 + successful_reps_count_left_gobletsquat_set3
    total_unsuccessful_count_set3 = unsuccessful_reps_count_left_gobletsquat_set3 + unsuccessful_reps_count_right_gobletsquat_set3    

    if successful_reps_count_right_gobletsquat_set3 == 5 and successful_reps_count_left_gobletsquat_set3 == 5:
        cvzone.putTextRect(img, 'All Repetitions Completed', [420, 30], thickness=2, border=2, scale=2.5)
        display_info_gobletsquat_set3 = False
        # General feedback after finishing the exercise # TO BE FETCHED
        if dir_gen_feedback_gobletsquat_set3 == 0:
            if 0 <= unsuccessful_reps_count_left_gobletsquat_set3 <= 10:
                general_feedback_set3 = detector_gobletsquat.gen_feedback_successful_count(total_successful_count_set3)
                executor.submit(detector_gobletsquat.play_sound, sound_gen_correct)
                general_feedback_unsuccessful_set3 = detector_gobletsquat.gen_feedback_unsuccessful_count(total_unsuccessful_count_set3)
                feedback_for_results_set3 = general_feedback_set3
                feedback_for_unsuccessful_result_set3 = general_feedback_unsuccessful_set3
                rest_goblet_start_time_set3 = time.time()
                exercise_mode = "rest_goblet_set3"
            dir_gen_feedback_gobletsquat_set3 = 1

    # # To check for unsuccessful arm rep counter # CHANGED
    if unsuccessful_reps_count_left_gobletsquat_set3 == 3 and unsuccessful_reps_count_right_gobletsquat_set3 == 3:
        cvzone.putTextRect(img, 'You have made 3 unsuccessful tries for both arms. Please retry again', [420, 30], thickness=2, border=2, scale=1)
        display_info_gobletsquat_set3 = False

        if dir_gen_feedback_unsuccessful_gobletsquat_set3 == 0:
            gen_feedback_unsuccessful_set3 = detector_gobletsquat.gen_feedback_unsuccessful(unsuccessful_reps_count_left_gobletsquat_set3, unsuccessful_reps_count_right_gobletsquat_set3)
            rest_goblet_start_time_set3 = time.time()
            exercise_mode = "rest_goblet_set3"
            feedback_for_results_set3 = ""
            feedback_for_unsuccessful_result_set3 = gen_feedback_unsuccessful_set3
            dir_gen_feedback_unsuccessful_gobletsquat_set3 = 1
            executor.submit(detector_gobletsquat.play_sound, sound_gen_incorrect)
    return img

def rest_goblet_set3(img):
    global exercise_mode, rest_goblet_start_time_set3, go_result_page
    img = cv2.resize(img, (1280, 720))
    rest_elapsed_time = time.time() - rest_goblet_start_time_set3
    #print(rest_elapsed_time)
    rest_remaining_time = max(0, 10 - int(rest_elapsed_time))
    

    # Draw rectangle behind the timer text
    cv2.rectangle(img, (890, 10), (1260, 80), (255, 0, 0), -2)  # Rectangle position and color

    # Draw timer text above the rectangle
    timer_text = f"Rest: {int(rest_remaining_time)}s"
    cv2.putText(img, timer_text, (900, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 0, 255), 3)

    if rest_remaining_time <= 0:
        go_result_page = True

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
    global exercise_mode, countdown_before_exercise_bicep, start_exercise_bicep, countdown_before_exercise_goblet, start_exercise_goblet, start_time1_bicep, start_time1_gobletsquat
    getExercises = request.json['getExercises']
    print(getExercises)

    if getExercises == "Bicep Curl":
        exercise_mode = "bicep_curl"
        start_exercise_bicep = True
        countdown_before_exercise_bicep = time.time()
        start_time1_bicep = time.time()
    else:
        exercise_mode = "goblet_squat"
        countdown_before_exercise_goblet = time.time()
        start_exercise_goblet = True
        start_time1_gobletsquat = time.time()
       
    return jsonify({"Success":"Success Get Exercises"})


@app.route('/back_exercise', methods=['POST'])
def back_exercise():
    global getExercises, exercise_mode
    getExercises = ""

    if getExercises == "":
        exercise_mode = ""

    return jsonify({"Success": "Success Delete Exercise"})
    

@app.route('/correct_bicep', methods=['POST'])
def correct_bicep():
    global text_correction, live_feedback, go_result_page
    #print(text_correction)

    return jsonify({"Correct": text_correction}, {"livefeedback" : live_feedback}, {"goResult": go_result_page})

@app.route('/result', methods=['POST'])
def result():
    global total_successful_count, total_unsuccessful_count, feedback_for_results, feedback_for_unsuccessful_result, total_successful_count_set2, total_unsuccessful_count_set2, feedback_for_results_set2, feedback_for_unsuccessful_result_set2, total_successful_count_set3, total_unsuccessful_count_set3, feedback_for_results_set3, feedback_for_unsuccessful_result_set3

    return jsonify({"total_successful":total_successful_count}, {"total_unsuccessful":total_unsuccessful_count}, {"general_feedback" : feedback_for_results}, {"general_feedback_unsuccessful" : feedback_for_unsuccessful_result}, {"total_successful_set2":total_successful_count_set2}, {"total_unsuccessful_set2":total_unsuccessful_count_set2}, {"general_feedback_set2" : feedback_for_results_set2}, {"general_feedback_unsuccessful_set2" : feedback_for_unsuccessful_result_set2}, {"total_successful_set3":total_successful_count_set3}, {"total_unsuccessful_set3":total_unsuccessful_count_set3}, {"general_feedback_set3" : feedback_for_results_set3}, {"general_feedback_unsuccessful_set3" : feedback_for_unsuccessful_result_set3})


@app.route('/get_feedback', methods=['POST'])
def get_feedback():
    feedbackForResult = request.json['feedbackForResult']
    feedbackForUnsuccessfulResult = request.json['feedbackForUnsuccessfulResult']
    total_feedback_for_results = f"{feedbackForResult}{feedbackForUnsuccessfulResult}"
    print(total_feedback_for_results)
    executor.submit(detector_bicep.tts_sound, total_feedback_for_results)

    return jsonify({"success" : "success getting feedback"})


@app.route('/get_feedback_set2', methods=['POST'])
def get_feedback_set2():
    feedbackForResultset2 = request.json['feedbackForResultset2']
    feedbackForUnsuccessfulResultset2 = request.json['feedbackForUnsuccessfulResultset2']
    total_feedback_for_results_set2 = f"{feedbackForResultset2}{feedbackForUnsuccessfulResultset2}"
    executor.submit(detector_bicep.tts_sound, total_feedback_for_results_set2)

    return jsonify({"success": "success getting feedback for set 2"})

@app.route('/get_feedback_set3', methods=['POST'])
def get_feedback_set3():
    feedbackForResultset3 = request.json['feedbackForResultset3']
    feedbackForUnsuccessfulResultset3 = request.json['feedbackForUnsuccessfulResultset3']
    total_feedback_for_results_set3 = f"{feedbackForResultset3}{feedbackForUnsuccessfulResultset3}"
    executor.submit(detector_bicep.tts_sound, total_feedback_for_results_set3)

    return jsonify({"success": "success getting feedback for set 3"})
    





if __name__ == '__main__':
    app.run(debug=True, threaded=True, use_reloader=True)