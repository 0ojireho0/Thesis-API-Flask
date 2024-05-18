# for open-cv mediapipe pose estimation
import cv2
import mediapipe as mp
import math

import os
import pygame
import pyttsx3

# Define a class for pose detection
class poseDetector():

    def __init__(self, mode=False, upBody=False, smooth=True):

        # Initialize parameters for pose detection
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth

        # Initialize mediapipe drawing utilities and pose model
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth)

        self.previous_per_left = None
        self.next_per_left = None
        self.feedback_timer = None
        self.feedback_delay = 0.5

    # Function find pose landmarks in the image 
    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    # Function to find landmarks positions
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

    def BicepCurl(self, img, p1, p2, p3, drawpoints):
        if len(self.lmList) != 0:

            x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
            x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
            x3, y3 = self.lmList[p3][1], self.lmList[p3][2]

            measure = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
            if measure < 0:
                measure += 360
                
            if drawpoints:
                cv2.circle(img, (x1, y1), 10, (255, 0, 255), 5)
                cv2.circle(img, (x1, y1), 15, (0, 255, 0), 5)
                cv2.circle(img, (x2, y2), 10, (255, 0, 255), 5)
                cv2.circle(img, (x2, y2), 15, (0, 255, 0), 5)
                cv2.circle(img, (x3, y3), 10, (255, 0, 255), 5)
                cv2.circle(img, (x3, y3), 15, (0, 255, 0), 5)

                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 6)
                cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 6)

                cv2.putText(img, str(int(measure)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                return int(measure)

    def both_arm_feedback(self, count1, count2):
        if count1 == 10 and count2 == 10:
            return "Congratulations! You've completed all 10 bicep curls with your left arm. Celebrate your accomplishment and take pride in your hard work."
        elif count1 == 9 and count2 == 10:
            return "Only two more to go, you're at 9 bicep curls with your left arm. Concentrate on squeezing your biceps hard at the top of each repetition for maximum muscle activation."
        elif count1 == 8 and count2 == 10:
            return "You've accomplished 8 bicep curls with your left arm. Keep your upper body stable and avoid using momentum from your hips or lower back to lift the weight."
        elif count1 == 7 and count2 == 10:
            return "Great job on completing 7 bicep curls with your left arm. Maintain a steady pace and focus on maintaining tension in your biceps throughout the entire range of motion."
        elif count1 == 6 and count2 == 10: 
            return "You're now at 6 bicep curls with your left arm. Stay mindful of your shoulder alignment and avoid shrugging or tensing up your neck muscles."
        elif count1 == 5 and count2 == 10:
            return "You're halfway through with 5 bicep curls completed with your left arm. Ensure a full range of motion by fully extending your arm at the bottom of each curl and contracting your bicep at the top."
        elif count1 == 4 and count2 == 10:
            return "Congratulations on reaching 4 bicep curls with your left arm. Keep your wrist neutral and elbow tucked in close to your body to maximize muscle engagement."
        elif count1 == 3 and count2 == 10:
            return "You've now completed 3 bicep curls with your left arm. Concentrate on maintaining proper breathing patterns and engaging your core muscles for stability."
        elif count1 == 2 and count2 == 10:
            return "Well done on completing 2 bicep curls with your left arm. Focus on activating your bicep muscle fully and avoid excessive swinging or momentum."
        elif count1 == 1 and count2 == 10:
            return "You've executed 1 bicep curl with your left arm out of the planned 10. Pay attention to maintaining consistent elbow positioning and controlled movement throughout each repetition."
        elif count1 == 0 and count2 == 10:
            return "You have not completed a single repetition with your left arm. Restart the program and let's do it properly!"
        else:
            return "The count has exceeded the limit. Please reset the program."

    def left_arm_feedback(self, count):
        if count == 10:
            return "Congratulations! You've completed all 10 bicep curls with your left arm. Celebrate your accomplishment and take pride in your hard work."
        elif count == 9:
            return "Only two more to go, you're at 9 bicep curls with your left arm. Concentrate on squeezing your biceps hard at the top of each repetition for maximum muscle activation."
        elif count == 8:
            return "You've accomplished 8 bicep curls with your left arm. Keep your upper body stable and avoid using momentum from your hips or lower back to lift the weight."
        elif count == 7:
            return "Great job on completing 7 bicep curls with your left arm. Maintain a steady pace and focus on maintaining tension in your biceps throughout the entire range of motion."
        elif count == 6: 
            return "You're now at 6 bicep curls with your left arm. Stay mindful of your shoulder alignment and avoid shrugging or tensing up your neck muscles."
        elif count == 5:
            return "You're halfway through with 5 bicep curls completed with your left arm. Ensure a full range of motion by fully extending your arm at the bottom of each curl and contracting your bicep at the top."
        elif count == 4:
            return "Congratulations on reaching 4 bicep curls with your left arm. Keep your wrist neutral and elbow tucked in close to your body to maximize muscle engagement."
        elif count == 3:
            return "You've now completed 3 bicep curls with your left arm. Concentrate on maintaining proper breathing patterns and engaging your core muscles for stability."
        elif count == 2:
            return "Well done on completing 2 bicep curls with your left arm. Focus on activating your bicep muscle fully and avoid excessive swinging or momentum."
        elif count == 1:
            return "You've executed 1 bicep curl with your left arm out of the planned 10. Pay attention to maintaining consistent elbow positioning and controlled movement throughout each repetition."
        elif count == 0:
            return "You have not completed a single repetition with your left arm. Restart the program and let's do it properly!"
        else:
            return "The count has exceeded the limit. Please reset the program."

    def right_arm_feedback(self, count):
        if count == 10:
            return "Congratulations! You've completed all 10 bicep curls with your right arm. Celebrate your accomplishment and take pride in your hard work."
        elif count == 9:
            return "Only two more to go, you're at 9 bicep curls with your right arm. Concentrate on squeezing your biceps hard at the top of each repetition for maximum muscle activation."
        elif count == 8:
            return "You've accomplished 8 bicep curls with your right arm. Keep your upper body stable and avoid using momentum from your hips or lower back to lift the weight."
        elif count == 7:
            return "Great job on completing 7 bicep curls with your right arm. Maintain a steady pace and focus on maintaining tension in your biceps throughout the entire range of motion."
        elif count == 6: 
            return "You're now at 6 bicep curls with your right arm. Stay mindful of your shoulder alignment and avoid shrugging or tensing up your neck muscles."
        elif count == 5:
            return "You're halfway through with 5 bicep curls completed with your right arm. Ensure a full range of motion by fully extending your arm at the bottom of each curl and contracting your bicep at the top."
        elif count == 4:
            return "Congratulations on reaching 4 bicep curls with your right arm. Keep your wrist neutral and elbow tucked in close to your body to maximize muscle engagement."
        elif count == 3:
            return "You've now completed 3 bicep curls with your right arm. Concentrate on maintaining proper breathing patterns and engaging your core muscles for stability."
        elif count == 2:
            return "Well done on completing 2 bicep curls with your right arm. Focus on activating your bicep muscle fully and avoid excessive swinging or momentum."
        elif count == 1:
            return "You've executed 1 bicep curl with your right arm out of the planned 10. Pay attention to maintaining consistent elbow positioning and controlled movement throughout each repetition."
        elif count == 0:
            return "You have not completed a single repetition with your right arm. Restart the program and let's do it properly!"
        else:
            return "The count has exceeded the limit. Please reset the program."

    def left_arm_unsuccessful_feedback(self, count):
        if count == 5:
            return "You've reached 5 bicep curls with your left arm. Despite some unsuccessful attempts, you're halfway to your goal. Focus on maintaining a consistent tempo and engaging the correct muscle groups to improve your form and efficiency."
        elif count == 4:
            return "You've attempted 4 bicep curls with your left arm. Each attempt, successful or not, contributes to your progress. Concentrate on proper elbow positioning and full range of motion to maximize muscle activation."
        elif count == 3:
            return "You've attempted 3 bicep curls with your left arm. Use unsuccessful attempts to analyze your technique. Ensure you're not swinging your arm and that you're isolating the bicep muscle during the lift."
        elif count == 2:
            return "You've attempted 2 bicep curls with your left arm. Don't be discouraged by missed reps. Pay attention to your grip and wrist alignment to maintain stability and control throughout the movement."
        elif count == 1:
            return "You've attempted 1 bicep curl with your left arm. Commitment to improvement is key. Focus on controlled eccentric (lowering) phase and avoid using momentum to lift the weight."
        elif count == 0:
            return "You haven't completed a successful repetition with your left arm yet. Use this as an opportunity to assess and correct your technique. Start with a lighter weight if necessary, and ensure you're initiating the movement from the bicep."

    def right_arm_unsuccessful_feedback(self, count):
        if count == 5:
            return "You've reached 5 bicep curls with your right arm. Despite some unsuccessful attempts, you're halfway to your goal. Focus on maintaining a consistent tempo and engaging the correct muscle groups to improve your form and efficiency."
        elif count == 4:
            return "You've attempted 4 bicep curls with your right arm. Each attempt, successful or not, contributes to your progress. Concentrate on proper elbow positioning and full range of motion to maximize muscle activation."
        elif count == 3:
            return "You've attempted 3 bicep curls with your right arm. Use unsuccessful attempts to analyze your technique. Ensure you're not swinging your arm and that you're isolating the bicep muscle during the lift."
        elif count == 2:
            return "You've attempted 2 bicep curls with your right arm. Don't be discouraged by missed reps. Pay attention to your grip and wrist alignment to maintain stability and control throughout the movement."
        elif count == 1:
            return "You've attempted 1 bicep curl with your right arm. Commitment to improvement is key. Focus on controlled eccentric (lowering) phase and avoid using momentum to lift the weight."
        elif count == 0:
            return "You haven't completed a successful repetition with your right arm yet. Use this as an opportunity to assess and correct your technique. Start with a lighter weight if necessary, and ensure you're initiating the movement from the bicep."

    def gen_feedback_successful_count(self, count_successful):
        if count_successful == 0:
            return "Great job! You haven't had any unsuccessful bicep curls. Keep up the good work! Maintaining consistent form and focus is key to continued success "
        elif count_successful == 1:
            return "You had 1 successful bicep curl. Ensure your form is correct and avoid using momentum to lift the weight. Paying attention to each rep will help you improve "
        elif count_successful == 2:
            return "You had 2 successful bicep curls. Focus on keeping your elbows stationary and close to your torso. This helps maximize bicep engagement and effectiveness "
        elif count_successful == 3:
            return "You had 3 successful bicep curls. Concentrate on controlling the weight during both the lifting and lowering phases. Control is crucial for muscle development "
        elif count_successful == 4:
            return "You had 4 successful bicep curls. Make sure your grip is firm but not too tight, and keep your wrists straight. Proper grip helps prevent unnecessary strain "
        elif count_successful == 5:
            return "You had 5 successful bicep curls. Remember to breathe properly – exhale on the curl and inhale on the release. Proper breathing supports better performance "
        elif count_successful == 6:
            return "You had 6 successful bicep curls. Focus on maintaining a full range of motion and avoid swinging your body. Full motion ensures complete muscle activation "
        elif count_successful == 7:
            return "You had 7 successful bicep curls. Keep your back straight and ensure each rep is performed with precision. Good posture is essential for effective workouts "
        elif count_successful == 8:
            return "You had 8 successful bicep curls. Retract your shoulder blades and keep your chest up to maintain proper alignment. Proper alignment helps prevent injury "
        elif count_successful == 9:
            return "You had 9 successful bicep curls. Concentrate on the contraction of the bicep muscle with each rep. Focusing on the muscle helps improve mind-muscle connection "
        elif count_successful == 10:
            return "You had 10 successful bicep curls. Review your technique to improve your form and prevent future unsuccessful attempts. Consistent practice leads to better results "
        else:
            return "It seems you had more than 10 unsuccessful bicep curls. Take a step back and reassess your form and technique. Consider reducing the weight to focus on proper form "


    def gen_feedback_unsuccessful(self, unsuccessful1):
        if unsuccessful1 == 0:
            return "and great job! You haven't had any unsuccessful bicep curls for either arm. Keep up the excellent work by maintaining proper form and focus."
        elif unsuccessful1 == 1:
            return "and you had 1 unsuccessful bicep curl. Ensure that you are lifting with your biceps and not using momentum. Pay close attention to your form and control."
        elif unsuccessful1 == 2:
            return "and you had 2 unsuccessful bicep curls. Focus on keeping your elbows stationary and close to your torso. Engage your biceps fully and avoid swinging the weights."
        elif unsuccessful1 == 3:
            return "and you had 3 unsuccessful bicep curls. Work on controlling the weight during both the lifting and lowering phases. This will help build strength and improve your form."
        elif unsuccessful1 == 4:
            return "and you had 4 unsuccessful bicep curls. Ensure your grip is firm but relaxed, and keep your wrists straight to avoid strain. Proper grip is key to effective curls."
        elif unsuccessful1 == 5:
            return "and you had 5 unsuccessful bicep curls. Remember to breathe correctly – exhale as you curl the weight up and inhale as you lower it. Proper breathing supports better performance."
        else:
            return "and it seems you had more than 5 unsuccessful bicep curls. Consider reducing the weight to focus on perfecting your form. Pay attention to each rep, keeping your back straight and your movements controlled."

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
        engine.setProperty('rate', 250) # setting up new voice rate
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
