import rospy
from pynput import keyboard
import subprocess
from std_msgs.msg import Float64, String

joints = ["t_joint", "m_joint", "b_joint"]

def robot_controller():
    while True:
        joint = input("Enter which joint to move (t, m, b): ")
        joint = f"{joint.lower()}_joint"

        if joint in joints:
            subprocess.run([f"python3 ./{joint}.py"])
        else:
            print("Invalid joint")
            return

if __name__ == '__main__':
    try:
        robot_controller()
    except Exception as e:
        pass