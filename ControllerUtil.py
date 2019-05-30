#!/usr/local/bin/python
## ======================================================================
##    PYTHON MODULE : Controller Creation 
##    Written by    : Ramon Partida, 2017 
##    Version       : 1.1
##    Program       : Autodesk 2011+
## ======================================================================

#Import maya modules
import maya.cmds as cmds


#Import python modules
import os, sys

class ControllerUtil(object):
	def __init__(self):
		self.var1 = 0

	
	def makeFK(allJoints):
		lastCtrl = ""

		topGrp = cmds.group(em=True, n=allJoints[0]+"_ALL_GRP")
		cmds.delete(cmds.parentConstraint(allJoints[0], topGrp, w=1))
		cmds.makeIdentity(topGrp, apply=True)

		for jnt in allJoints:
			#Make null
			nullGrp = cmds.group(em = True, n = jnt + "_null")

			#Position null and delete constraint
			cmds.delete(cmds.parentConstraint(jnt, nullGrp, w = 1))

			#Make new curve
			ctrl = cmds.circle(ch = False, n = jnt + "Ctrl")
			cmds.delete(cmds.parentConstraint(jnt, ctrl, w = 1))

			#Parent control to null
			cmds.parent(ctrl, nullGrp)

			#Constraint to bone
			cmds.parentConstraint(ctrl, jnt, w = 1)

			if not lastCtrl:
				lastCtrl = ctrl
			else:
				cmds.parent(nullGrp, lastCtrl)
				lastCtrl = ctrl

		cmds.parent(allJoints[0]+"_null", topGrp)

	
	def setCtrlColor(allControls):
		for ctrl in allControls:

			#Enable Color Overdrive
			cmds.setAttr(ctrl + '.overrideEnabled', 1)

			#Select and Change Color
			index = 0;
			cmds.setAttr(ctrl + 'overrideColor', index)

	def mirrorControls(mainGroup):
                #Duplicate selected group
                dup = cmds.duplicate(mainGroup)
                cmds.scale(-1,1,1)