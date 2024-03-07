import rospy
import keyboard
from std_msgs.msg import Float32, String


if __name__ == "__main__":
    rospy.init_node('controller')
    rospy.loginfo("Controller node started")

    pub = rospy.Publisher('linear_act', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        if keyboard.is_pressed('w'):
            pub.publish("forward")
        elif keyboard.is_pressed('s'):
            pub.publish("backward")
        elif keyboard.is_pressed('q'):
            pub.publish("stop")
        rate.sleep()