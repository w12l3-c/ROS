import rospy
from pynput import keyboard
from std_msgs.msg import Float64, String

def robot_controller():
    rospy.init_node('b_joint')
    pub = rospy.Publisher('b_joint_pub', Float64, queue_size=10)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        value = input("Enter value(in radians): ")

        if -3.14 <= float(value) <= 3.14:
            rospy.loginfo(f"Publishing to b_joint: {value}")
            pub.publish(float(value))

        rate.sleep()


if __name__ == '__main__':
    try:
        robot_controller()
    except Exception as e:
        pass