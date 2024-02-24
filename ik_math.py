import numpy as np
import math
from math import cos, sin
import fk


def find_partial(equation, variable):
    pass


# https://stackoverflow.com/questions/30791504/python-partial-derivatives-easy
def jacobian(joint_values, transformation_matrices):
    J_v = np.zeros((3, 6))
    J_w = np.zeros((3, 6))

    for i in range(joint_values.shape[1]):
        pass



def send_to_robot(joint_values):
    pass

def fk(joint_values):
    pass

def ik_iterative(desired_position, desired_orientation, current_position, current_orientation, steps, joint_values, transformation_matrices):
    desired_orientation = np.array(desired_orientation)
    desired_position = np.array(desired_position)
    current_orientation = np.array(current_orientation)
    current_position = np.array(current_position)

    goal = np.concatenate((desired_orientation, desired_position.T), axis=1)
    goal = np.concatenate((goal, np.array([[0, 0, 0, 1]])))
    
    current = np.concatenate((current_orientation, current_position.T), axis=1)
    current = np.concatenate((current, np.array([[0, 0, 0, 1]])))

    while True:
        delta = (goal - current) / steps
        delta_position = delta[:3, 3]
        delta_orientation = delta[:3, :3]

        delta_x = delta_position[0] 
        delta_y = delta_position[1] 
        delta_z = delta_position[2] 

        delta_alpha = math.acos((np.trace(delta_orientation) - 1) / 2) 
        delta_beta = math.acos((np.trace(delta_orientation) - 1) / 2) 
        delta_gamma = math.acos((np.trace(delta_orientation) - 1) / 2) 

        J = jacobian(joint_values, transformation_matrices)
        J_psuedo = np.linalg.pinv(J, rcond=1e-1)

        delta_q = np.dot(J_psuedo, delta)
        joint_values += delta_q
        send_to_robot(joint_values)

        current = fk(joint_values)

        if np.linalg.norm(delta_position) < 0.01 and np.linalg.norm(delta_orientation) < 0.01:
            break


def ik_velocity(desired_position, desired_orientation, current_position, current_orientation, speed, joint_values):
    desired_orientation = np.array(desired_orientation)
    desired_position = np.array(desired_position)
    current_orientation = np.array(current_orientation)
    current_position = np.array(current_position)

    goal = np.concatenate((desired_orientation, desired_position.T), axis=1)
    goal = np.concatenate((goal, np.array([[0, 0, 0, 1]])))
    
    current = np.concatenate((current_orientation, current_position.T), axis=1)
    current = np.concatenate((current, np.array([[0, 0, 0, 1]])))

    
    velocity = (goal - current) * speed
    velocity_trans = velocity[:3, 3]
    velocity_orientation = velocity[:3, :3]

    J = jacobian(joint_values)
    J_psuedo = np.linalg.pinv(J, rcond=1e-1)

    dot_q = np.dot(J_psuedo, velocity)
    send_to_robot(dot_q)


ik([[1, 2, 3]], [[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[0, 0, 0]], [[cos(60), -sin(60), 0], [sin(60), cos(60), 0], [0, 0, 1]])


    

