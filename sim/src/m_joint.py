import rospy
from pynput import keyboard
from std_msgs.msg import Float64, String
from gazebo_msgs.msg import LinkState, LinkStates
from sensor_msgs.msg import JointState  
from control_msgs.msg import JointControllerState

def callback(data):
    rospy.loginfo("=====================================")
    rospy.loginfo("Recieved: ")
    rospy.loginfo(data)

    rospy.loginfo("=====================================")



def robot_controller():
    rospy.init_node('m_joint')
      
    pub = rospy.Publisher('/arm/b_joint_position_controller/command', Float64, queue_size=10)
    sub = rospy.Subscriber('/arm/b_joint_position_controller/state', JointControllerState, callback)
    
    rospy.loginfo("m_joint node started") 

    rate = rospy.Rate(5000) # 10hz    
    while not rospy.is_shutdown():
        value = input("Enter value(in radians): ")

        if -3.14 <= float(value) <= 3.14:
            rospy.loginfo(f"Publishing to m_joint: {value}")
            pub.publish(float(value))

        rate.sleep()

    
    rospy.spin()


if __name__ == '__main__':
    try:
        robot_controller()
    except Exception as e:
        pass



"""
gazebo_msgs/LinkStates:
string[] name
geometry_msgs/Pose[] pose
  geometry_msgs/Point position
    float64 x
    float64 y
    float64 z
  geometry_msgs/Quaternion orientation
    float64 x
    float64 y
    float64 z
    float64 w
geometry_msgs/Twist[] twist
  geometry_msgs/Vector3 linear
    float64 x
    float64 y
    float64 z
  geometry_msgs/Vector3 angular
    float64 x
    float64 y
    float64 z

    
gazebo_msgs/LinkState:
string link_name
geometry_msgs/Pose pose
  geometry_msgs/Point position
    float64 x
    float64 y
    float64 z
  geometry_msgs/Quaternion orientation
    float64 x
    float64 y
    float64 z
    float64 w
geometry_msgs/Twist twist
  geometry_msgs/Vector3 linear
    float64 x
    float64 y
    float64 z
  geometry_msgs/Vector3 angular
    float64 x
    float64 y
    float64 z
string reference_frame

"""