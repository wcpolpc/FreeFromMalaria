#This file is part of FreeFromMalaria.
#
#FreeFromMalaria is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#FreeFromMalaria is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with FreeFromMalaria.  If not, see <http://www.gnu.org/licenses/>. 
#
# Original author: World Class Project www.worldclassproject.org.uk

import gtk
#import gtk.glade
import gtk.gdk 
import time;
import gobject;
import cairo;
import pygame;

from view import ViewScreen
from gettext import gettext as _

class MyComicScreen():
	
	'''
	classdocs
	'''


	def __init__(self,controller):
		'''
		Constructor
		
		
		'''
		#hook up to the controller
		self.controller=controller;
		
				   
		self.xml=gtk.Builder();		
				
		##init the background image buffer
	
		
		# Load Glade XML
		self.xml.add_from_file("glade/comicScreen.ui")
		
		# Get Window
		self.w = self.xml.get_object('window1')
	   
		#self.w.connect("delete_event", gtk.main_quit)
		
		# Get Windows child
		self.w_child = self.w.get_child()
		# self.widget will be attached to the Activity
		# This can be any GTK widget except a window
		self.widget = self.w_child
		
		#print "COMIC SCREEN"
	   # print self.widget;
		
		self.bgpixbuf = gtk.gdk.pixbuf_new_from_file("images/1.jpg")
		
		##set up the drawing area
		self.draw = self.xml.get_object('draw');
		self.draw.connect("expose-event", self.expose)
		self.vbox= self.xml.get_object('vbox1');
		white = gtk.gdk.color_parse("white")

	   

		
		self.scene_index= 0;
		
		self.label = self.xml.get_object('label')
	   # self.label.set_markup("<span size='10000'>"+self.text[self.scene_index]+"</span>");
		
		self.vbox.remove(self.label)
		eb = gtk.EventBox()
		eb.add(self.label)
		eb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("white"))
		self.vbox.add(eb)

	  
		
		
		

	
	   
		
		
	   
 
		
	   # self.reset_timer();

	   
		
		self.draw.set_events(gtk.gdk.EXPOSURE_MASK
							| gtk.gdk.LEAVE_NOTIFY_MASK
							| gtk.gdk.BUTTON_PRESS_MASK
							| gtk.gdk.POINTER_MOTION_MASK
							| gtk.gdk.POINTER_MOTION_HINT_MASK)
  
	
	def send_terminate(self):
		return True;
	def update_scene(self,index_array):
		
		self.text=index_array[0];
		image=index_array[1];
		self.sound=index_array[2];
		self.bgpixbuf = gtk.gdk.pixbuf_new_from_file(image)
		self.change_event();
		return True  
	def prev_press_event(self, widget, event):
		self.controller.previous_scene();
		self.change_event();
		return True  
	
  
	def change_event(self):
		
	   
		self.draw.queue_draw();
		self.label.set_markup("<span size='10000' background='white'>"+self.text+"</span>");
		#print "SOUND IS",self.controller.get_sound();
		
		if(self.controller.get_sound()==True):
				#if already playing stop the previous sound and restart
			if(pygame.mixer.get_busy()==True):
					pygame.mixer.stop();
					pygame.mixer.init(22050, -32, 2, 4096)
			
			s=pygame.mixer.Sound(self.sound)
			s.set_volume(0.2)
			channel = s.play()
		 #self.reset_timer();
		
	def expose(self, widget, event):
	   
	   #self.ctx = self.draw.window.cairo_create()
		cr = self.draw.window.cairo_create()
		cr.set_source_rgb(255, 255, 255)
		cr.paint()
		comic_position=int( (self.draw.window.get_size()[0])/2.0)-int(self.bgpixbuf.get_width()/2.0);
		text_position_y=int( self.bgpixbuf.get_height()+10);
		text_position_x=int((self.draw.window.get_size()[0])/2.0)-int(200/2.0)
		cr.set_source_pixbuf(self.bgpixbuf, comic_position, 0)
		cr.paint()
		
	   
		#DRAW FONT HERE
 
	def get_window(self):
		return self.w  
		
		# Signals used to handle backing pixmap
		
