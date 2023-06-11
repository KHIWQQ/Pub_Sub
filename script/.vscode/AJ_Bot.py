#!/usr/bin/env python3
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtleBot:
    def __init__(self):
        rospy.init_node("turtlesim_controller",anonymous= False)
        self.pose_sub = rospy.Subscriber("/turtle1/pose", Pose, self.update_pose)
        self.vel_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
        self.current = Pose()
        self.start_pose = Pose()
        self.rate = rospy.Rate(10)
        self.tol = 0.05

    def update_pose(self, data):
        self.current.x = data.x
        self.current.y = data.y
        self.current.theta = data.theta
    
    def send_vel(self, x_vel, theta_vel):
        cmd_vel =Twist()
        cmd_vel.linear.x = x_vel
        cmd_vel.angular.z = theta_vel
        self.vel_pub.publish(cmd_vel)

    def set_start(self):
        self.rate.sleep()
        self.start_pose.x = self.current.x
        self.start_pose.y = self.current.y
        self.start_pose.theta = self.current.theta
        rospy.loginfo(f"Set start point at x = {self.start_pose.x} y = {self.start_pose.y} theta = {self.start_pose.theta}")
    
    def distance_error(self, distance_goal):
        self.rate.sleep()
        distance = math.sqrt(math.pow(self.current.x - self.start_pose.x,2)+math.pow(self.current.y - self.start_pose.y,2))
        dist_error = distance_goal - distance
        rospy.loginfo(f"distance err = {dist_error}")
        return dist_error

    def move(self, distance):
        self.set_start()
        rospy.loginfo(f"Start moving {distance} unit")
        while abs(self.distance_error(distance)) > self.tol:
            self.send_vel(0.5, 0)  
        rospy.loginfo("Arrived")
        self.send_vel(0, 0)

    def angular_error(self, angle_goal):
        self.rate.sleep()
        angle_goal = (angle_goal*math.pi)/180
        turn_angle = self.current.theta - self.start_pose.theta
        if turn_angle > math.pi:
            turn_angle -= math.pi*2
        elif turn_angle < -math.pi:
            turn_angle += math.pi*2

        angle_error = abs(angle_goal - turn_angle)
        rospy.loginfo(f"distance err = {angle_error}")
        return angle_error
    
    def turn(self, deg):
        self.set_start()
        if deg < 0:
            theta_vel = -0.5
        else:
            theta_vel = 0.5
        rospy.loginfo(f"Start turning {deg} degree")
        while abs(self.angular_error(deg)) > self.tol:
            self.send_vel(0, theta_vel)
        rospy.loginfo("finish turning")
        self.send_vel(0, 0)

if __name__ == "__main__":
    turtle = TurtleBot()
    for i in range(4):
        turtle.turn(90)
        turtle.move(4)