# cball2.py
#   Simulation of the flight of a cannon ball (or other projectile)
#   This version uses functional (top-down) composition.

from math import pi, sin, cos

def main():
    angle, vel, h0, time = getInputs()
    xpos, ypos = 0, h0
    xvel, yvel = getXYComponents(vel, angle)
    while ypos >= 0:
        xpos, ypos, yvel = updateCannonBall(time, xpos, ypos, xvel, yvel)
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))

def getInputs():
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in meters/sec): "))
    h = eval(input("Enter the initial height (in meters): "))
    t = eval(input("Enter the time interval between position calculations: "))
    return a,v,h,t

def getXYComponents(vel, angle):
    radians = (angle * pi)/180.0
    x = vel * cos(radians)
    y = vel * sin(radians)
    return x,y

def updateCannonBall(time, xpos, ypos, xvel, yvel):
        xpos = xpos + time * xvel
        yvel1 = yvel - 9.8 * time
        ypos = ypos + time * (yvel + yvel1)/2.0
        return xpos, ypos, yvel1
     
main()


