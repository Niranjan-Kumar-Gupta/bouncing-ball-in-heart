from visual import*
from visual.graph import*
import numpy as np
scene.background = color.white
r = 2
dtheta = np.pi/50
t = 0
heart_list = []
while(t <= 2*pi):
    heart_list.append(vector(-16*sin(t)**3,13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t),0))
    t += dtheta
    
heart= curve(pos=heart_list,color = color.red)

sphere2 = sphere(pos = vector(2,0,0),radius=0.4,color = color.blue,make_trail=True,retain=0)

sphere3 = sphere(pos = vector(0,0,0),radius=0.4,color = color.red)
hit_direction = vector(1,2,0)

dt = 0.09

while(True):
    rate(500)
    magnitude = mag(sphere2.pos)
    for i in range(0,len(heart_list)):
        
        x = mag(heart_list[i])
        
       
        
        if magnitude + sphere2.radius >= x:
            hit_direction -= 2*sphere2.pos*dot(sphere2.pos,hit_direction)/magnitude**2
            
    sphere2.pos += hit_direction*dt

