#!/usr/bin/env python3
import rospy
from my_package.srv import AddTwoInts,AddTwoIntsRequest

def add_two_ints_client(x, Y):
    rospy.wait_for_service("add_two_ints")
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        req = AddTwoIntsRequest()
        req.a = x
        req.b = y
        resp = add_two_ints(req)
        return resp.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

if __name__ == '__main__':
    rospy.init_node('add_two_ints_client')
    x = 10
    y = 5
    print("Requesting %s = %s"% (x, y))
    result = add_two_ints_client(x, y)
    print("%s + %s = %s" % (x, y, result ))


