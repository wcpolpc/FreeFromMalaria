#! /usr/bin/env python
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

import view.ComicScreen

import gtk
import controller.GameController
#import view.
class devtest2:
    def __init__(self, runaslib=True,):
        file_path="/home/dev/Desktop/olpc";
        to_journal = file(    file_path, "w")
        try:
            to_journal.write("EE")
        finally:
            to_journal.close()
        
        #self.gameModel=model.GameState.MyGameState(None,1)
        self.controller=controller.GameController.GlobalGameController(None)
        #self.view=view.TeacherScreen.GameTeacherScreen(controller)
       # self.view=view.WelcomeScreen.GameWelcomeScreen(self.controller)
        #self.view=view.MapScreen.MyMapScreen(controller)
        #self.view=view.MIScreen.GameMIScreen(self.controller)
        #self.view=view.DoctorScreen.GameDoctorScreen(controller)
        #self.view=view.SwatScreen.GameSwatScreen(controller)
        #self.view=view.MapScreen.MyMapScreen(controller)
        #self.view=view.ComicScreen.MyComicScreen(self.controller)
        self.view=view.QuizScreen.GameQuizScreen(["quiz","what is the answer?","*answer@correct","answer2@wrong2","answer3@wrong3","answer4@answer4"],self.controller)
        #self.view=self.controller.get_current_view();
        self.window=self.view.get_window()
        self.w_child=self.window.get_child()
        self.widget = self.w_child
        if not runaslib:
            self.window.show_all()
            gtk.main()
            
    def next_scene(self,scene_num):
        if scene_num==2:
            #print "ee"
            self.view=view.MIScreen.GameMIScreen(self)
            self.window=self.view.get_window()
            self.w_child=self.window.get_child()
            self.widget = self.w_child
            self._main_view = gtk.VBox()
            
        
            
       
                
if __name__ == '__main__':
            devtest2(False)

