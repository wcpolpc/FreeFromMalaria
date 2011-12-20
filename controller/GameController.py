##This file is part of FreeFromMalaria.
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

import gtk;
from view import ComicScreen;
from view import WelcomeScreen
from view import QuizScreen;
import pygame;
import os.path
import sys
class GlobalGameController:
	'''
	classdocs
	'''
  
   

	def __init__(self, activity):
		'''
		Constructor
		'''
		self.activity = activity;
				
		#initialise the sound system first
		self.sound = True;
		self.sound_error = False;
		try:
			pygame.mixer.init(22050, -32, 2, 4096)
			print "SOUND INITIALIZED"
			
		except:
			print "Unexpected error:", sys.exc_info()[0]
			print "Error:ERROR in SOUND"
			self.sound = False;
			
		self.comic_index = 0;
		self.current_game = "Welcome"
		##enable the UI buttons only if the comic is active
		self.activity.set_navigation(self.current_game == "Comic" or self.current_game=="Prevent");
		
		##load all registered languages		
		self.read_approved_langages();
		#default load english
		#self.user_selection = "English (en)";
		self.load_language_by_code("en")
		
		#initialise the views
		welcome = WelcomeScreen.GameWelcomeScreen(self);
		#self.comic = ComicScreen.MyComicScreen(self);
		#self.quiz=QuizScreen.GameQuizScreen(self);
		self.view = welcome;
		if(self.activity != None):
		   self.activity.create_new_window(self.view)
		
	def read_file(self, file_path):
	 try:
		self.index_array = []
		inp = open (file_path, "r")
		#the number of lines in the file is the number of scenes.
		self.max_scenes = 0;
		#read line into array 
		for line in inp.readlines():
		   self.max_scenes = self.max_scenes + 1;
			# add a new sublist
		   self.index_array.append([])
		  
			# loop over the elemets, split by whitespace
		   for i in line.split(';'):
			   
				# convert to integer and append to the last
				# element of the list
				self.index_array[-1].append(i.rstrip('\n'))
				
		
		return
	 except:
		raise;
	def read_approved_langages(self):
		
		inp = open ("files/languages.txt", "r")
		#read line into array 
		
		self.language_map = {};
		self.languages = [];
		for line in inp.readlines():
			splits = line.split(";")
			formatted = '(%(a)s) (%(b)s)' % {'a':splits[0], 'b': splits[1].rstrip('\n')};
			#formatted = "{",splits[0],"}"," ({",splits[1].rstrip('\n'),"})";
			##add to the map for subsequent reverse lookup i.e. how to look up the landuage based on the user input in the combo
			self.language_map.setdefault(formatted , []).append(splits[1].rstrip('\n'))
			
			##add results to return list
			self.languages.append(formatted);
		   
		
		return; 
	
	def get_approved_langages(self):	
		return self.languages;
	def set_sound(self, isOn):
		self.sound = isOn
		
	def get_sound(self):
		#if there is a sound error return false?
		return self.sound;
	def get_sound_error(self):
		#if there is a sound error return false?
		return self.sound_error;
	def next_scene(self):
		#print "UPDATE next"
		#print self.comic_index;
		#print self.max_scenes;
		if(self.comic_index + 1 < self.max_scenes):
			self.comic_index = self.comic_index + 1;
			self.update_scene();
	def previous_scene(self):
		#print "UPDATE prev"
		#print self.comic_index;
		#print self.max_scenes;
		if(self.comic_index - 1 >= 0):
			self.comic_index = self.comic_index - 1;
			self.update_scene();
	def reload(self):
		self.comic_index = 0;
		
		
		self.update_scene();
		
	def update_scene(self):
		
#		print "Max scenes", self.max_scenes;
#		print "current comic", self.comic_index;
#		print "Current Game", self.current_game;

		if(self.comic_index < self.max_scenes and self.comic_index >= 0):
			file_line = self.index_array[self.comic_index];
			#bring up the quiz if thats what the file says
			if(file_line[0] == "quiz"):
				self.play_game("Quiz", file_line)
				self.view.initialize(file_line)
			#if we are still on the comic then draw the next scene
			else:
				#return to the comic first
				if(self.current_game != "Comic"):
				
				   self.play_game("Comic", None)
				 
				
				self.view.update_scene(file_line);
			
   
				
	
			
	def get_comic_index(self):
		return self.comic_index;
	
	def play_game(self, game_name, args):
		self.current_game = game_name
		if (self.current_game == "Comic"):
			self.view = ComicScreen.MyComicScreen(self);#self.comic;
			if(args == "Continue"):
					self.next_scene()
			elif(args == "Return"):
					self.previous_scene()
			elif(args == "Start"):
					self.comic_index=0;
			self.update_scene();
			
		
		elif (self.current_game == "Welcome"):
			self.view = WelcomeScreen.GameWelcomeScreen(self);
		elif(self.current_game == "Quiz"):
			self.view = QuizScreen.GameQuizScreen(self);
		else:
			raise NameError("Failed to start game"); 
		
		##disable the nav buttons if we are not in a comic
		self.activity.set_navigation(self.current_game == "Comic" or self.current_game=="Prevent");
		self.activity.create_new_window(self.view);
	def set_comic_index(self, index):
		
		self.comic_index = index;
		
	def load_language_by_code(self, lang):
		self.load_language(lang);
		
	def get_language_code_by_user_selection(self, user_selection):
		if(user_selection in self.language_map):
			return self.language_map[user_selection][0]	
		else:
			raise Exception("Language "+user_selection+" not registered");
	def get_current_language_code(self):
		return self.current_language_code
	def load_language_by_user_selection(self, user_selection):	
		#self.user_selection=user_selection;##redundant update fix later
		return self.load_language(self.get_language_code_by_user_selection(user_selection));
	#def get_current_user_selection(self):
		#return self.user_selection;
	def get_current_user_selection(self):
		
		for key,value  in self.language_map.items():
			
			if(value[0]==self.current_language_code):
				return key
		return None; 
		
	def get_current_game(self):
		return self.current_game;	
	def load_language(self, lang_code):
		print "CONTROLLER "
		print self.language_map;
		
		
		path="";
		try:	
			path = "files/";
			
			path += lang_code;
			 
			self.read_file(path)
			##only update the current language once the file has been loaded
			self.current_language_code = lang_code;
			return True;
		except:
			message = "ERROR: Unable to load language: "
			message += path;
			message += " : Language file not installed,"; 
			raise IOError(message, "");
			
		##todo what to do on button press
		
		
		
		#self.bgpixbuf = gtk.gdk.pixbuf_new_from_file(indexString) 
		
		
if __name__ == '__main__':
			GlobalGameController(False)  
			  
	
		
	
		
	
		
