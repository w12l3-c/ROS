import numpy as np
import math
from math import cos, sin, tan, sqrt
from numpy.linalg import inv, multi_dot

class RotationalJoint():
    def __init__(self, axis, angle):
        self.axis = axis
        self.angle = angle
        self.matrix = self.get_matrix()

    def get_matrix(self):
        axis = self.axis
        angle = self.angle
        c = math.cos(angle)
        s = math.sin(angle)
        t = 1 - c
        x, y, z = axis

        return np.array([
            [t*x*x + c, t*x*y - s*z, t*x*z + s*y, 0],
            [t*x*y + s*z, t*y*y + c, t*y*z - s*x, 0],
            [t*x*z - s*y, t*y*z + s*x, t*z*z + c, 0],
            [0, 0, 0, 1]
        ])
    
    def update_angle(self, angle):
        self.angle = angle
        self.matrix = self.get_matrix()


class PrismaticJoint():
    def __init__(self, axis, distance):
        self.axis = axis
        self.distance = distance
        self.matrix = self.get_matrix()

    def get_matrix(self):
        axis = self.axis
        distance = self.distance
        x, y, z = axis

        return np.array([
            [1, 0, 0, x*distance],
            [0, 1, 0, y*distance],
            [0, 0, 1, z*distance],
            [0, 0, 0, 1]
        ])
    
    def update_distance(self, distance):
        self.distance = distance
        self.matrix = self.get_matrix()
    
class Links():
    def __init__(self, length, alpha, a, d):
        self.length = length
        self.alpha = alpha
        self.a = a
        self.d = d
        self.matrix = self.get_matrix()

    # DH Matrix
    def get_matrix(self):
        length = self.length
        alpha = self.alpha
        a = self.a
        d = self.d

        c_alpha = math.cos(alpha)
        s_alpha = math.sin(alpha)

        return np.array([
            [c_alpha, -s_alpha, 0, a],
            [s_alpha*c_alpha, c_alpha*c_alpha, -s_alpha, -s_alpha*d],
            [s_alpha*s_alpha, c_alpha*s_alpha, c_alpha, c_alpha*d],
            [0, 0, 0, 1]
        ])
    
class LinearLinks():
    def __init__(self, length, x, y, z):
        # Origin of the Link relative to base
        self.x = x
        self.y = y
        self.z = z

        # Length of the Link
        self.length = length

        self.matrix = self.get_matrix()

    # DH Matrix
    def get_matrix(self):
        return np.array([
            [1, 0, 0, self.x],
            [0, 1, 0, self.y],
            [0, 0, 1, self.z],
            [0, 0, 0, 1]
        ])


def calculate_dh_matrix(links, joints, movement, mvmt_joint):
    transformation_matrices = []
    accumulated_matrix = np.eye(4)

    for i, joint in enumerate(joints):
        joint_matrix = joint.matrix
        link_matrix = links[i].matrix

        # mvmt * A1 * A2 * A3 * ... * An
        if i == mvmt_joint:
            if isinstance(joint, RotationalJoint):
                joint.update_angle(movement)
                joint_matrix = joint.matrix
            elif isinstance(joint, PrismaticJoint):
                joint.update_distance(movement)
                joint_matrix = joint.matrix
        
        accumulated_matrix = multi_dot([accumulated_matrix, link_matrix, joint_matrix]) # Order matters
        transformation_matrices.append(accumulated_matrix)

    return transformation_matrices


if __name__ == '__main__':
    links = [
        LinearLinks(1, 0, 0, 0),
        LinearLinks(1, 0, 0, 1),
        LinearLinks(1, 0, 1, 1),
        LinearLinks(1, 0, 2, 1)
    ]

    joints = [
        RotationalJoint([0, 0, 1], 0),
        RotationalJoint([0, 1, 0], 0),
        RotationalJoint([0, 1, 0], 0),
        RotationalJoint([0, 1, 0], 0)
    ]

    movement = 60
    mvmt_joint = 1

    transformation_matrices = calculate_dh_matrix(links, joints, movement, mvmt_joint)


    for i in transformation_matrices:
        print(i)
    print(transformation_matrices[-1])  # End effector's pose






