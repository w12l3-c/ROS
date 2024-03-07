# RaspberryPi read from topic and output from GPIO
import GPIO
import rospy
from std_msgs.msg import String, Float32

POWER = 18
GND = 23
POLARITY = 24

def callback(data):
    rospy.loginfo(f"{rospy.get_caller_id}: Recieved: {data.data}")
    if data.data == "forward":
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
    elif data.data == "backward":
        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
    elif data.data == "stop":
        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)


if __name__ == "__main__":
    rospy.init_node('reciever')
    rospy.loginfo("Reciever node started")
    rospy.Subscriber("linear_act", String, callback)

    rospy.spin()

