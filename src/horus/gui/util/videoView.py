#!/usr/bin/python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------#
#                                                                       #
# This file is part of the Horus Project                                #
#                                                                       #
# Copyright (C) 2014 Mundo Reader S.L.                                  #
#                                                                       #
# Date: June 2014                                                       #
# Author: Jesús Arroyo Torrens <jesus.arroyo@bq.com>                    #
#                                                                       #
# This program is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program. If not, see <http://www.gnu.org/licenses/>.  #
#                                                                       #
#-----------------------------------------------------------------------#

__author__ = "Jesús Arroyo Torrens <jesus.arroyo@bq.com>"
__license__ = "GNU General Public License v3 http://www.gnu.org/licenses/gpl.html"

import wx

from horus.util.resources import *

class VideoView(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		self.xOffset = 0
		self.yOffset = 0

		self.defaultImage = wx.Image(getPathForImage("bq.png"))
		self.image = self.defaultImage
		self.bitmap = wx.BitmapFromImage(self.defaultImage)

		self.Bind(wx.EVT_PAINT, self.onPaint)
		self.Bind(wx.EVT_SIZE, self.onResize)

	def onPaint(self, event):
		dc = wx.PaintDC(self)
		dc.DrawBitmap(self.bitmap, self.xOffset, self.yOffset)

	def onResize(self, size):
		self.refreshBitmap()

	def setImage(self, image):
		self.image = image
		self.refreshBitmap()

	def setDefaultImage(self):
		self.setImage(self.defaultImage)

	def setFrame(self, frame):
		height, width = frame.shape[:2]
		self.image = wx.ImageFromBuffer(width, height, frame)
		self.refreshBitmap()

	def refreshBitmap(self):
		(w, h, self.xOffset, self.yOffset) = self.getBestSize()
		self.bitmap = wx.BitmapFromImage(self.image.Scale(w, h))
		self.Refresh()

	def getBestSize(self):
		(wwidth, wheight) = self.GetSizeTuple()
		(width, height) = self.image.GetSize()

		if height > 0 and wheight > 0:
			if float(width)/height > float(wwidth)/wheight:
				nwidth  = wwidth
				nheight = float(wwidth*height)/width
				xoffset = 0
				yoffset = (wheight-nheight)/2.0
			else:
				nwidth  = float(wheight*width) /height
				nheight = wheight
				xoffset = (wwidth-nwidth)/2.0
				yoffset = 0

			return (nwidth, nheight, xoffset, yoffset)
		else:
			return (0, 0, 0, 0)

