import cv2
import mediapipe as mp
import math
import numpy as np

import os
import pygame
import pyttsx3

class poseDetectorGobletSquat():

    def __init__(self, mode=False, upBody=False, smooth=True):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList

    def GobletSquat(self, img, p1, p2, p3, drawpoints):
        if len(self.lmList) != 0:

            x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
            x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
            x3, y3 = self.lmList[p3][1], self.lmList[p3][2]

            measure = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
            midpoint_x = int((x1 + x3) / 2)
            midpoint_y = int((y1 + y3) / 2)

            if drawpoints:
                cv2.circle(img, (x1, y1), 10, (255, 0, 255), 5)
                cv2.circle(img, (x1, y1), 15, (0, 255, 0), 5)
                cv2.circle(img, (x2, y2), 10, (255, 0, 255), 5)
                cv2.circle(img, (x2, y2), 15, (0, 255, 0), 5)
                cv2.circle(img, (x3, y3), 10, (255, 0, 255), 5)
                cv2.circle(img, (x3, y3), 15, (0, 255, 0), 5)

                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 6)
                cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 6)

                cv2.putText(img, f"{int(measure)}", (midpoint_x, midpoint_y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                return int(measure)

    def left_leg_feedback(self, count):
        if count == 10:
            return "Congratulations! You've completed all 10 goblet squats. Celebrate your accomplishment and take pride in your hard work."
        elif count == 9:
            return "Only one more to go, you're at 9 goblet squats. Keep pushing! Maintain proper form and breathe rhythmically."
        elif count == 8:
            return "You've accomplished 8 goblet squats. Great job! Focus on keeping your back straight and your movements controlled."
        elif count == 7:
            return "Well done on completing 7 goblet squats. Keep up the good work! Focus on steady breathing and engaging your core."
        elif count == 6: 
            return "You're now at 6 goblet squats. Stay focused and maintain a steady pace. Remember to keep your chest up and knees aligned with your toes."
        elif count == 5:
            return "You're halfway there with 5 goblet squats completed. Keep going strong! Focus on maintaining proper depth and pushing through your heels."
        elif count == 4:
            return "Great progress! You've reached 4 goblet squats. Focus on maintaining a smooth and controlled motion."
        elif count == 3:
            return "You've completed 3 goblet squats. Keep it up! Remember to engage your core and drive through your heels as you stand."
        elif count == 2:
            return "Well done on completing 2 goblet squats. You're doing great! Focus on maintaining control and keeping your chest lifted."
        elif count == 1:
            return "You've executed 1 goblet squat. Keep pushing forward! Focus on form and consistency."
        elif count == 0:
            return "You haven't completed a single goblet squat. Don't give up! Take a moment to rest, then try again with determination."
        else:
            return "The count has exceeded the limit. Please reset the program."

    def right_leg_feedback(self, count):
        if count == 10:
            return "Congratulations! You've completed all 10 goblet squats with your right arm. Celebrate your accomplishment and take pride in your hard work."
        elif count == 9:
            return "Only one more to go, you're at 9 goblet squats with your right arm. Keep pushing! Maintain proper form and breathe rhythmically."
        elif count == 8:
            return "You've accomplished 8 goblet squats with your right arm. Great job! Focus on keeping your arm steady and your movements controlled."
        elif count == 7:
            return "Well done on completing 7 goblet squats with your right arm. Keep up the good work! Focus on steady breathing and engaging your shoulder muscles."
        elif count == 6: 
            return "You're now at 6 goblet squats with your right arm. Stay focused and maintain a steady pace. Remember to keep your core stable throughout."
        elif count == 5:
            return "You're halfway there with 5 goblet squats completed with your right arm. Keep going strong! Focus on squatting with control and maintaining proper form."
        elif count == 4:
            return "Great progress! You've reached 4 goblet squats with your right arm. Focus on maintaining a smooth and controlled motion."
        elif count == 3:
            return "You've completed 3 goblet squats with your right arm. Keep it up! Remember to breathe and engage your shoulder and arm muscles."
        elif count == 2:
            return "Well done on completing 2 goblet squats with your right arm. You're doing great! Focus on maintaining control and squatting with your shoulder."
        elif count == 1:
            return "You've executed 1 goblet squat with your right arm. Keep pushing forward! Focus on form and consistency."
        elif count == 0:
            return "You haven't completed a single goblet squat with your right arm. Don't give up! Take a moment to rest, then try again with determination."
        else:
            return "The count has exceeded the limit. Please reset the program."

    def leg_feedback(self, count1, count2):

        if count1 == 10 and count2 == 10:
            return f"Congratulations! You've completed all 10 goblet squats with both your legs. Celebrate your accomplishment and take pride in your hard work."
        elif count1 == 9 and count2 == 9:
            return f"Only one more to go, you're at 9 goblet squats with both your legs. Keep pushing! Maintain proper form and breathe rhythmically."
        elif count1 == 8 and count2 == 8:
            return f"You've accomplished 8 goblet squats with both your legs. Great job! Focus on keeping your back steady and your movements controlled."
        elif count1 == 7 and count2 == 7:
            return f"Well done on completing 7 goblet squats with both your legs. Keep up the good work! Focus on steady breathing and engaging your core shoulder muscles."
        elif count1 == 6 and count2 == 6:
            return f"You're now at 6 goblet squats with both your legs. Stay focused and maintain a steady pace. Remember to keep your chest up and knees aligned with your toes."
        elif count1 == 5 and count2 == 5:
            return f"You're halfway there with 5 goblet squats completed with both your legs. Keep going strong! Focus on maintaining proper depth and pushing through your heels."
        elif count1 == 4 and count2 == 3:
            return f"Great progress! You've reached 4 goblet squats with both your legs. Focus on maintaining a smooth and controlled motion."
        elif count1 == 3 and count2 == 3:
            return f"You've completed 3 goblet squats with both your legs. Keep it up! Remember to engage your core and drive through your heels as you stand."
        elif count1 == 2 and count2 == 2:
            return f"Well done on completing 2 goblet squats with both your legs. You're doing great! Focus on maintaining control and keeping your chest lifted."
        elif count1 == 1 and count2 == 1:
            return f"You've executed 1 goblet squat with both your legs. Keep pushing forward! Focus on form and consistency."
        elif count1 == 0 and count2 == 0:
            return f"You haven't completed a single goblet squat with both your legs. Don't give up! Take a moment to rest, then try again with determination."
        else:
            return "The count has exceeded the limit. Please reset the program."


    def left_leg_unsuccessful_feedback(self, count):
        if count == 5:
            return "You've reached 5 attempted goblet squats with your left arm. Keep pushing! Each attempt is a step closer to your goal."
        elif count == 4:
            return "You've attempted 4 goblet squats with your left arm. Don't get discouraged! Use each attempt as a learning experience to improve."
        elif count == 3:
            return "You've attempted 3 goblet squats with your left arm. Keep trying! Persistence and practice will lead to progress."
        elif count == 2:
            return "You've attempted 2 goblet squats with your left arm. Stay focused! Consistency is key to mastering the movement."
        elif count == 1:
            return "You've attempted 1 goblet squat with your left arm, but faced some challenges. Don't give up! Take a moment to rest, then try again."
        elif count == 0:
            return "You haven't successfully completed a single goblet squat with your left arm. It's okay! Take it as a chance to learn and grow. Keep practicing!"



    def gen_feedback_unsuccessful_count(self, count_unsuccessful):
        if count_unsuccessful == 0:
            return "Great job! You haven't had any unsuccessful goblet squats. Keep up the good work! Maintaining consistent form and focus is key to continued success."
        elif count_unsuccessful == 1:
            return "You had 1 unsuccessful goblet squat. Ensure your form is correct and keep your chest up and back straight. Paying attention to each rep will help you improve."
        elif count_unsuccessful == 2:
            return "You had 2 unsuccessful goblet squats. Focus on keeping your knees tracking over your toes and avoid letting them collapse inward. This helps maximize engagement and effectiveness."
        elif count_unsuccessful == 3:
            return "You had 3 unsuccessful goblet squats. Concentrate on controlling the movement during both the descent and ascent. Control is crucial for muscle development."
        elif count_unsuccessful == 4:
            return "You had 4 unsuccessful goblet squats. Make sure your grip on the weight is firm but relaxed, and keep it close to your chest. Proper grip helps prevent unnecessary strain."
        elif count_unsuccessful == 5:
            return "You had 5 unsuccessful goblet squats. Remember to breathe properly – inhale as you squat down and exhale as you stand up. Proper breathing supports better performance."
        elif count_unsuccessful == 6:
            return "You had 6 unsuccessful goblet squats. Focus on maintaining a full range of motion and avoid rushing through the reps. Full motion ensures complete muscle activation."
        elif count_unsuccessful == 7:
            return "You had 7 unsuccessful goblet squats. Keep your heels on the ground and drive through them as you stand. Good posture is essential for effective workouts."
        elif count_unsuccessful == 8:
            return "You had 8 unsuccessful goblet squats. Retract your shoulder blades and keep your chest up to maintain proper alignment. Proper alignment helps prevent injury."
        elif count_unsuccessful == 9:
            return "You had 9 unsuccessful goblet squats. Concentrate on engaging your core and glutes with each rep. Focusing on these muscles helps improve stability and performance."
        elif count_unsuccessful == 10:
            return "You had 10 unsuccessful goblet squats. Review your technique to improve your form and prevent future unsuccessful attempts. Consistent practice leads to better results."
        else:
            return "It seems you had more than 10 unsuccessful goblet squats. Take a step back and reassess your form and technique. Consider reducing the weight to focus on proper form."

    def gen_feedback_unsuccessful(self, unsuccessful1, unsuccessful2):
        if unsuccessful1 == 0 and unsuccessful2 == 0:
            return "Great job! You haven't had any unsuccessful goblet squats. Keep up the excellent work by maintaining proper form and focus."
        elif unsuccessful1 == 1 and unsuccessful2 == 1:
            return "You had 1 unsuccessful goblet squat. Ensure that you are keeping your chest up and your back straight. Focus on your form and control."
        elif unsuccessful1 == 2 and unsuccessful2 == 2:
            return "You had 2 unsuccessful goblet squats. Remember to keep your knees tracking over your toes and avoid letting them collapse inward. Engage your core throughout the movement."
        elif unsuccessful1 == 3 and unsuccessful2 == 3:
            return "You had 3 unsuccessful goblet squats. Work on controlling the movement both on the way down and up. Make sure to squat to a depth where your thighs are parallel to the ground."
        elif unsuccessful1 == 4 and unsuccessful2 == 4:
            return "You had 4 unsuccessful goblet squats. Ensure you are maintaining a firm grip on the weight and keeping it close to your chest. Keep your heels on the ground and drive through them as you stand."
        elif unsuccessful1 == 5 and unsuccessful2 == 5:
            return "You had 5 unsuccessful goblet squats. Remember to breathe correctly – inhale as you squat down and exhale as you stand up. Proper breathing helps maintain stability and control."
        else:
            return "It seems you had more than 5 unsuccessful goblet squats. Consider reducing the weight to focus on perfecting your form. Pay attention to each rep, keeping your back straight and your movements controlled."


    def play_sound(self, sound_file):
        pygame.mixer.init()
        try:
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"An error occurred while trying to play the sound: {e}")

    def tts_sound(self, text_file):
        engine = pyttsx3.init()
        rate = engine.getProperty('rate') # getting details of current speaking rate
        engine.setProperty('rate', 150) # setting up new voice rate
        volume = engine.getProperty('volume') #getting to know current volume level (min=0 and max=1)
        engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1

        voices = engine.getProperty('voices')  #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
        try:
            engine.say(text_file)
            engine.runAndWait()
            if engine._inLoop:
                engine.endLoop()
        except Exception as e:
            print(f"An error occurred while trying to play the sound: {e}")



