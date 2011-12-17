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

from gettext import gettext as _
import gtk


import controller.GameController
import os
import time
import sys
from view import WelcomeScreen

try:
	import json
	json.dumps
except (ImportError, AttributeError):
	import simplejson as json
	


# Load our own source code from gtktest.py
# There you can find the main class gtktest()


# Load sugar libraries
from sugar.activity import activity  
from sugar.graphics.toolbutton import ToolButton


class FreeFromMalariaActivity(activity.Activity):
	def __init__(self, handle):
		activity.Activity.__init__(self, handle)
		self.activity_state = {}
		self._name = handle
		self.set_title(_("Free From Malaria"))
		
		restartTitle = _("End User Licence");
		restartText = _("The materials in this game are in no way intended to replace or supersede professional medical care, advice, diagnosis or treatment of a doctor. The game only provides general advice on Malaria. This advice may not apply to everyone in every locality. If you notice medical symptoms or feel ill, you should consult your doctor. Please seek further advice from your local health authority for further information about Malaria.All information provided in this activity has been produced using peer reviewed scientific and health documentation. By clicking OK you agree that this game should be used for general educational and information purposes only and is not intended to replace medical advice or act as a diagnosis tool. For more details please visit http://worldclassproject.org.uk/.");
		dialog = self.create_dialog_ok(restartTitle, restartText)
		result = dialog.run()
		dialog.destroy()

		
		   
		
		#init the controller
		#game controller
	  
	   
		


		if handle.object_id == None:
			print "Launched from home."
		else:
			print "Journal resume."

		# Set title for our Activity
		self.set_title('Free From Malaria')

		# Attach sugar toolbox (Share, ...)
		 # Use old <= 0.84 toolbar design
		toolbox = activity.ActivityToolbox(self)
		view_tool_bar = toolbox.get_activity_toolbar();#gtk.Toolbar()

		#for debug only
#		self.previous_chapter = ToolButton('gtk-media-forward-rtl')
#		self.previous_chapter.set_tooltip("Previous Chapter")
#		self.previous_chapter_id = self.previous_chapter.connect('clicked', self.previous_chapter_clicked)
#		view_tool_bar.insert(self.previous_chapter, 0)
#		self.previous_chapter.show()
		########################################
		self.previous_scene_button = ToolButton('previous')
		self.previous_scene_button.set_tooltip("Previous Scene")
		self.previous_scene_id = self.previous_scene_button.connect('clicked', self.previous_scene_clicked)
		view_tool_bar.insert(self.previous_scene_button, 1)
		self.previous_scene_button.show()
		###########print "CHANGING"
		self.next_scene = ToolButton('next')
		self.next_scene.set_tooltip("Next Scene")
		self.next_scene_id = self.next_scene.connect('clicked', self.next_scene_clicked)
		view_tool_bar.insert(self.next_scene, 2)
		self.next_scene.show()
		###########
		#disable comic buttons in the main menu
		self.set_navigation(False)
	   ######################
		self.sound = ToolButton('audio-volume-high')
		homeString = _("Enable/Disable Sound");
		self.sound.set_tooltip(homeString)
		self.sound_id = self.sound.connect('clicked', self.sound_clicked)
		view_tool_bar.insert(self.sound, 3)
		self.sound.show()
		#############################
		###########
		self.reload = ToolButton('reload')
		restart = _("Restart");
		self.reload.set_tooltip(restart)
		self.reload_id = self.reload.connect('clicked', self.reload_clicked)
		view_tool_bar.insert(self.reload, 4)
		self.reload.show()
		######################
		
		
		
		######################
		self.home = ToolButton('go-home')
		homeString = _("Go to main menu");
		self.home.set_tooltip(homeString)
		self.home_id = self.home.connect('clicked', self.home_clicked)
		view_tool_bar.insert(self.home, 5)
		self.home.show()
		#############################
		
	
	  
		
		
		
		view_tool_bar.show()
	   # toolbox.add_toolbar('Game Control', view_tool_bar)
		self.set_toolbox(toolbox)
		toolbox.show()
		activity_toolbar = toolbox.get_activity_toolbar()
		activity_toolbar.share.props.visible = False
		
		#global game state
	   
		##restore previous session
		self.controller = controller.GameController.GlobalGameController(self) 
		
		self.read_and_parse_prefs(os.environ['SUGAR_ACTIVITY_ROOT'] + '/data/defaults')
		
		
		#welcomeview = WelcomeScreen.GameWelcomeScreen(self.controller);
		
	   
	   
		#self.create_new_window(welcomeview)
#		self.mywindow = welcomeview.get_window()
#		self.w_child = self.mywindow.get_child()
#		self.widget = self.w_child
#		self.pack_and_show()
		
	   
	
		
	
	def next_scene_clicked(self, event):
	 
	   self.controller.next_scene();
	def previous_scene_clicked(self, event):
	   self.controller.previous_scene();
	def reload_clicked(self, event):
		restartTitle = _("Restart The Story?");
		restartText = _("Are you sure you want to restart the story?");
		dialog = self.create_dialog(restartTitle, restartText)
		result = dialog.run()
		dialog.destroy()

		if result == gtk.RESPONSE_YES:
		   self.controller.reload();
	def home_clicked(self, event):
	  restartTitle = _("Restart The Main Menu?");
	  restartText = _("Are you sure you want to return to the main menu?");
	  dialog = self.create_dialog(restartTitle, restartText)
	  
	  result = dialog.run()
	  dialog.destroy()

	  if result == gtk.RESPONSE_YES:
		self.controller.play_game("Welcome", None);
	def sound_clicked(self, event):
	  if(self.controller.get_sound() == True):
	  	self.sound.set_icon("audio-volume-muted")
		self.controller.set_sound(False);
	  else:
		self.controller.set_sound(True);
		self.sound.set_icon("audio-volume-high")  

	
	  
	def create_dialog(self, title, message):
		dialog = gtk.MessageDialog(parent=None,

		buttons=gtk.BUTTONS_YES_NO,

		flags=gtk.DIALOG_DESTROY_WITH_PARENT,

		type=gtk.MESSAGE_QUESTION,
	  
		message_format=message);
		dialog.set_title(title)
		return dialog;
	
	def create_dialog_ok(self, title, message):
		dialog = gtk.MessageDialog(parent=None,

		buttons=gtk.BUTTONS_OK,

		flags=gtk.DIALOG_DESTROY_WITH_PARENT,

		type=gtk.MESSAGE_QUESTION,
	  
		message_format=message);
		dialog.set_title(title)
		return dialog;
	##disables the nav buttons when comic is not being shown
	def set_navigation(self, switch):
		
	   
		 self.previous_scene_button.set_sensitive(switch);
		 self.next_scene.set_sensitive(switch);
		
		   
	def create_new_window(self, view):
		
		
		 
		#self.view = view;	 
		self.mywindow = view.get_window()
		 
	   
		
		self.w_child = self.mywindow.get_child()
		 
		self.widget = self.w_child
		 
		
#		if(self.widget==None or self.w_child==None):
#			raise RuntimeError("No widget available")
		self.pack_and_show()
		
	def pack_and_show(self):
		# Create the main container
		self._main_view = gtk.VBox()

		# Import our class gtktest():

		# Step 1: Load class, which creates gtktest.widget
		#self.gtktest = devtest2(self)

		# Step 2: Remove the widget's parent
		if self.widget.parent:
			self.widget.parent.remove(self.widget)
 
		# Step 3: We attach that widget to our window
		self._main_view.pack_start(self.widget)

		# Display everything
		self.widget.show()
		self._main_view.show()
		self.set_canvas(self._main_view)
		self.show_all()
	def read_and_parse_prefs(self, file_path):
		#Parse and set preference data from a given file.
		#file_path=os.environ['SUGAR_ACTIVITY_ROOT'] + '/data/defaults'
		#file_path=os.environ['SUGAR_ACTIVITY_ROOT'] + '/data/defaults';
		print "Restoring ", file_path
		try:
			read_file = open(file_path, 'r')
			self.activity_state = json.loads(read_file.read())
			
			if self.activity_state.has_key('comic_index'):
			
					comic_index = self.activity_state['comic_index']
#					print "Restoring with index ",comic_index
					self.controller.set_comic_index(comic_index)
					print "Restored COMIC SCENE from ", file_path
				   
			if self.activity_state.has_key('current_language_code'):
					current_language = self.activity_state['current_language_code']
					self.controller.load_language_by_code(current_language)
					print "Restored LANGUAGE from ", file_path
			self.controller.update_scene();
			read_file.close();
		  
		   
		except IOError:# as (errno, strerror):
			print "Error: Preferences error"
		except AttributeError:# as (errno):
			print "Warning: controller not initialised and prefs called. {0}"
		except:
			raise; 
		
	def read_file(self, file_path):
		#Read state from datastore.
		
		self.read_and_parse_prefs(file_path)


	def write_file(self, file_path):
#		#"""Write state to journal datastore and to persistent file system.
#		#"""
		#file_path=os.environ['SUGAR_ACTIVITY_ROOT'] + '/data/defaults';
#		print "WRITING FILE TO JOURNAL : "+os.environ['SUGAR_ACTIVITY_ROOT'] + '/data/defaults'
		# BUG [ID: 3334629]
		try:
			print "WRITING FILE TO JOURNAL : " + file_path
			self.activity_state['comic_index'] = self.controller.get_comic_index();
			self.activity_state['current_language_code'] = self.controller.get_current_language_code();
	  
			serialised_data = json.dumps(self.activity_state)
		
   
			to_journal = file(file_path, 'w')
			try:
	   	
				to_journal.write(serialised_data)
			except:
				raise
			finally:
				to_journal.close()
		
				to_persistent_fs = file(os.environ['SUGAR_ACTIVITY_ROOT'] + '/data/defaults', 'w')
		
			try:
				to_persistent_fs.write(serialised_data)
			except:
				raise;
			finally:
				to_persistent_fs.close()
		except AttributeError:# BUG [ID: 3334629]
			print "Warning: controller not initialised and trying to write. {0}"
		  

