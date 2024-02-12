import numpy as np
import math

class RotationalJoint():
    def __init__(self, axis, angle):
        self.axis = axis
        self.angle = angle

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


class PrismaticJoint():
    def __init__(self, axis, distance):
        self.axis = axis
        self.distance = distance

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


def calculate_dh_matrix(joints, movement):
    transformation_matrices = []
    accumulated_matrix = np.dot(movement.get_matrix(), np.eye(4)) # Movement Matrix

    for joint in joints:
        joint_matrix = joint.get_matrix()
        accumulated_matrix = np.dot(joint_matrix, accumulated_matrix)
        transformation_matrices.append(accumulated_matrix)

    return transformation_matrices



