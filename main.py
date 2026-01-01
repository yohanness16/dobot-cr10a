import numpy as np
import time
from roboticstoolbox import DHRobot, RevoluteDH
from spatialmath import SE3

# define dh parameter 
j1a = 0
j1alpha = np.pi/2
j1d = 0.1765

j2a = 0.607
j2alpha = 0
j2d = 0

j3a = 0.568
j3alpha = 0
j3d = 0

j4a = 0
j4alpha = np.pi/2
j4d = 0.125

j5a = 0
j5alpha = -np.pi/2
j5d = 0.125

j6a = 0
j6alpha = 0
j6d = 0.1114

robot = DHRobot([
    RevoluteDH(d=j1d, a=j1a, alpha=j1alpha),
    RevoluteDH(d=j2d, a=j2a, alpha=j2alpha),
    RevoluteDH(d=j3d, a=j3a, alpha=j3alpha),
    RevoluteDH(d=j4d, a=j4a, alpha=j4alpha),
    RevoluteDH(d=j5d, a=j5a, alpha=j5alpha),
    RevoluteDH(d=j6d, a=j6a, alpha=j6alpha)
], name="Dobot CR10A")

#forward kinematics 
q = [0, np.pi/6, -np.pi/4, np.pi/3, np.pi/6, 0]
T = robot.fkine(q)
print(T)



#inverse kinematics 
T_desired = SE3(0.8, 0.0, 0.3)
ik= robot.ikine_LM(T_desired)
print(ik.q)


#ploting the robot postion for different angel 

q_test = [
    [np.pi/2, 0, 0, 0, 0, 0],      
    [-np.pi/2, 0, 0, 0, 0, 0],     
    [0, np.pi/2, 0, 0, 0, 0],      
    [0, -np.pi/2, 0, 0, 0, 0],     
    [0, 0, np.pi/2, 0, 0, 0],      
    [0, 0, -np.pi/2, 0, 0, 0],     
    [0, 0, 0, np.pi/2, 0, 0],      
    [0, 0, 0, -np.pi/2, 0, 0],     
    [0, 0, 0, 0, np.pi/2, 0],      
    [0, 0, 0, 0, -np.pi/2, 0],     
    [0, 0, 0, 0, 0, np.pi/2],      
    [0, 0, 0, 0, 0, -np.pi/2]      
]

# animation 
for q in q_test:
    robot.plot(q, block=False)
    time.sleep(1)  