#!/usr/bin/env python3
import rospy
from my_package.srv import EspeakExercise, EspeakExerciseResponse
import subprocess

def handle_speak_request(req):
    rospy.loginfo("Recived request to speak: " + req.message)
    subprocess.call(["espeak", req.message])
    rospy.loginfo("Finish speak")
    return EspeakExerciseResponse("Finish speak")

def speak_server():
    rospy.init_node('speak_service_server')
    rospy.Service('speak', EspeakExercise, handle_speak_request)
    rospy.loginfo("Ready to speak")
    rospy.spin()

if __name__=="__main__":
    speak_server()

