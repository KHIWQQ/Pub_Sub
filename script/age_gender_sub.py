#!/usr/bin/env python3
import rospy
import subprocess
from my_package.msg import age_gender

def callback(data):
    rospy.loginfo(f"I found {data.age} year-old {data.gender}")
    subprocess.call(["espeak", f"I found {data.age} year-old {data.gender}"])

def age_gender_sub():
    rospy.init_node('age_gender_sub', anonymous=False)
    rospy.Subscriber("/ppl_classification", age_gender, callback)
    rospy.spin()

if __name__== '__main__':
    age_gender_sub()