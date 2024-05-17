# for open-cv mediapipe pose estimation
import cv2
import mediapipe as mp
import time
import math

# for gemini api
import os
import google.generativeai as genai
from dotenv import load_dotenv

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
            
    def feedback_bicep(self, value):
    # Check if the condition for feedback is met
        if value >= 100:
            return "Well done!"
        elif 90 >= value >= 1:
            return f"Keep pushing! you are at {int(value)}%"
        elif value == 0:
            return "Start any moment now!"
        return None  # No feedback if condition is not met

    def update_next_per_left(self, next_per_left):
        self.next_per_left = next_per_left

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
            return "You've reached 5 bicep curls with your left arm. Despite some unsuccessful attempts, you're halfway there! Stay positive, stay motivated, and keep pushing forward."
        elif count == 4:
            return "You've attempted 4 bicep curls with your left arm. Remember, every attempt, successful or not, is progress. Stay resilient, stay disciplined, and keep moving forward."
        elif count == 3:
            return "You've attempted 3 bicep curls with your left arm. Unsuccessful attempts are opportunities for growth. Use them as learning experiences to refine your technique."
        elif count == 2:
            return "You've attempted 2 bicep curls with your left arm. Don't be discouraged by unsuccessful attempts. Stay focused, stay determined, and keep pushing towards your goal."
        elif count == 1:
            return "You've attempted 1 bicep curl with your left arm, but faced some unsuccessful tries. Stay committed to improvement. Focus on proper form and give it your best effort."
        elif count == 0:
            return "You have not completed a single successful repetition with your left arm. Don't be discouraged! Take it as a learning opportunity, reset, and approach it with renewed determination."

    def right_arm_unsuccessful_feedback(self, count):
        if count == 5:
            return "You've reached 5 bicep curls with your right arm. Despite some unsuccessful attempts, you're halfway there! Stay positive, stay motivated, and keep pushing forward."
        elif count == 4:
            return "You've attempted 4 bicep curls with your right arm. Remember, every attempt, successful or not, is progress. Stay resilient, stay disciplined, and keep moving forward."
        elif count == 3:
            return "You've attempted 3 bicep curls with your right arm. Unsuccessful attempts are opportunities for growth. Use them as learning experiences to refine your technique."
        elif count == 2:
            return "You've attempted 2 bicep curls with your right arm. Don't be discouraged by unsuccessful attempts. Stay focused, stay determined, and keep pushing towards your goal."
        elif count == 1:
            return "You've attempted 1 bicep curl with your right arm, but faced some unsuccessful tries. Stay committed to improvement. Focus on proper form and give it your best effort."
        elif count == 0:
            return "You have not completed a single successful repetition with your left arm. Don't be discouraged! Take it as a learning opportunity, reset, and approach it with renewed determination."



