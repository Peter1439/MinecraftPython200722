# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:32:14 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
for i in range(20):
    mc.setBlock(x+i,y-1,z+i,57)