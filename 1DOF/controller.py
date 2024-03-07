import rospy
# import keyboard
import datetime
from pynput import keyboard
from std_msgs.msg import Float32, String
import os

current_key = None

def on_press(key):
    global current_key
    try:
        if key.char == 'w':
            current_key = 'w'
        elif key.char == 's':
            current_key = 's'
        elif key.char == 'q':
            current_key = 'q'
    except AttributeError:
        pass  

def on_release(key):
    global current_key
    current_key = 'q'


if __name__ == "__main__":
    rospy.init_node('controller')
    rospy.loginfo("Controller node started")

    pub = rospy.Publisher('linear_act', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    )
    listener.start()

    while not rospy.is_shutdown():
        if current_key == ('w'):
            pub.publish("forward")
        elif current_key == ('s'):
            pub.publish("backward")
        elif current_key == ('q'):
            pub.publish("stop")
        rate.sleep()