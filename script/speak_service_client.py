import rospy
from my_package.srv import EspeakExercise, EspeakExerciseRequest

def speak_client(msg):
    rospy.wait_for_service("speak")
    try:
        speak = rospy.ServiceProxy('speak', EspeakExercise)
        req = EspeakExerciseRequest()
        req.message = msg
        resp = speak(req)
        return resp.response
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

if __name__ == '__main__':
    rospy.init_node('speak_client')
    text = str(input("Message :"))
    print("Requesting %s", (text))
    result = speak_client(text)
    


