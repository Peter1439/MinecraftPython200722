# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:25:33 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random,time
pos = mc.player.getTilePos()

while True :
    x = pos.x+random.uniform(-20,20)
    y = pos.y
    z = pos.z+random.uniform(-20,20)
    
    mc.spawnEntity(x,y,z,63)
    time.sleep(0.2)