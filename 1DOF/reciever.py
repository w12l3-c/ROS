# RaspberryPi read from topic and output from GPIO
import gpio as GPIO
# import RPi.GPIO as GPIO # Only can be used on RaspberryPi
import rospy
from std_msgs.msg import String, Float32

POWER = 18
GND = 23
POLARITY = 24

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(POWER, GPIO.OUT)
# GPIO.setup(GND, GPIO.OUT)
# GPIO.setup(POLARITY, GPIO.OUT)

def callback(data):
    rospy.loginfo(f"Recieved: {data.data}")
    if data.data == "forward":
        # GPIO.output(18, GPIO.HIGH)
        # GPIO.output(23, GPIO.LOW)
        print("Actuator going forward")
    elif data.data == "backward":
        # GPIO.output(18, GPIO.LOW)
        # GPIO.output(23, GPIO.HIGH)
        print("Actuator going backward")
    elif data.data == "stop":
        # GPIO.output(18, GPIO.LOW)
        # GPIO.output(23, GPIO.LOW)
        print("Actuator stops")


if __name__ == "__main__":
    rospy.init_node('reciever')
    rospy.loginfo("Reciever node started")
    rospy.Subscriber("linear_act", String, callback)

    rospy.spin()

