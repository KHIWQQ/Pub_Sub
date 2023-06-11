import rospy
from my_package.msg import age_gender

def age_gender_pub(age, gender):
    pub =rospy.Publisher('/ppl_classification', age_gender,queue_size=10)
    rospy.init_node('age_gender_pub', anonymous=False)
    msg = age_gender()
    msg.age = age
    msg.gender = gender
    pub.publish(msg)

if __name__=='__main__':
    try:
        age = int(input("Age: "))
        gender = input("Gender: ")
        age_gender_pub(age, gender)
    except rospy.ROSInterruptException:
        pass



