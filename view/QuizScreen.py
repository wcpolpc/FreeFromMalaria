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
import random;

from gettext import gettext as _
class GameQuizScreen():
    '''
    classdocs
    '''
    def __init__(self,cont):
        '''
        Constructor
        '''
       
        ##get the contoller  
        self.controller=cont
              
        self.xml=gtk.Builder();        
                
        ##init the background image buffer
    
        
        # Load Glade XML
        self.xml.add_from_file("glade/quizScreen.glade")
        
        # Get Window
        self.w = self.xml.get_object('window1')
        #self.w.connect("delete_event", gtk.main_quit)
        
        # Get Windows child
        self.w_child = self.w.get_child()
        # self.widget will be attached to the Activity
        # This can be any GTK widget except a window
        self.widget = self.w_child
      
       
        self.continue_button= self.xml.get_object('continue');
        self.continue_button.set_sensitive(False);
        self.continue_button.connect("button_press_event", self.continue_game)
        
        self.previous_button= self.xml.get_object('previous');
        self.previous_button.connect("button_press_event", self.return_game)
      
        
        

    def initialize(self,question_array):
         self.qanda = question_array;
         self.prepare_questions();
    def return_game(self,widget,event):
        self.controller.play_game("Comic","Return");
        
    def get_window(self):
        return self.w
    def prepare_questions(self):
        question = self.xml.get_object('question')
        question.set_text(self.qanda[1])
        self.sublist = self.qanda[2:6]
        
        ##randomise the questions
        random.shuffle( self.sublist)
        
        ##assign the correct answer
        string=self.sublist[0]
        a1 = self.xml.get_object('a1')
        a1.set_text( string.split('@')[0] );
        button1= self.xml.get_object('button1')
        if(string[0]=="*"):
            button1.connect("button_press_event", self.right0)
        else:
            button1.connect("button_press_event", self.wrong0)
            
        
         ##assign the wrong answers
        string=self.sublist[1]
        a2 = self.xml.get_object('a2')
        a2.set_text( string.split('@')[0] );
        button2= self.xml.get_object('button2')
        #button2.connect("button_press_event", self.a2)
        if(string[0]=="*"):
            button2.connect("button_press_event", self.right1)
        else:
            button2.connect("button_press_event", self.wrong1)
        
        string=self.sublist[2]
        a3 = self.xml.get_object('a3')
        a3.set_text( string.split('@')[0] );
        button3= self.xml.get_object('button3')
        #button3.connect("button_press_event", self.a3)
        if(string[0]=="*"):
            button3.connect("button_press_event", self.right2)
        else:
            button3.connect("button_press_event", self.wrong2)
        
        string=self.sublist[3]
        a4 = self.xml.get_object('a4')
        a4.set_text( string.split('@')[0] );
        button4= self.xml.get_object('button4')
        #button4.connect("button_press_event", self.a4)
        
        if(string[0]=="*"):
            button4.connect("button_press_event", self.right3)
        else:
            button4.connect("button_press_event", self.wrong3)
        
        
        
        self.reset_icon(-1);
       
    ###########
    # Button callbacks
    ############
    
    def continue_game(self,widget,event):
        self.controller.play_game("Comic","Continue");
        
     
    def right0(self,widget,event):
        answer_label=self.xml.get_object('answer')
        string=self.sublist[0]
        answer_label.set_text(string.split('@')[1])
        image=self.xml.get_object('tick0')
        image.set_from_file("images/right.png");
        self.reset_icon(0);
        self.continue_button.set_sensitive(True);
    def right1(self,widget,event):
        answer_label=self.xml.get_object('answer')
        string=self.sublist[1]
        answer_label.set_text(string.split('@')[1])
        image=self.xml.get_object('tick1')
        image.set_from_file("images/right.png");
        self.reset_icon(1);
        self.continue_button.set_sensitive(True);
    def right2(self,widget,event):
        answer_label=self.xml.get_object('answer')
        string=self.sublist[2]
        answer_label.set_text(string.split('@')[1])
        image=self.xml.get_object('tick2')
        image.set_from_file("images/right.png");
        self.reset_icon(2);
        self.continue_button.set_sensitive(True);
    def right3(self,widget,event):
        answer_label=self.xml.get_object('answer')
        string=self.sublist[3]
        answer_label.set_text(string.split('@')[1])
        image=self.xml.get_object('tick3')
        image.set_from_file("images/right.png");
        self.reset_icon(3);
        self.continue_button.set_sensitive(True);
    def wrong0(self,widget,event):
        answer_label=self.xml.get_object('answer')
        string=self.sublist[0]
        answer_label.set_text(string.split('@')[1])
        image=self.xml.get_object('tick0')
        image.set_from_file("images/wrong.png");
        self.reset_icon(0);
        self.continue_button.set_sensitive(False);
    
    def wrong1(self,widget,event):
        answer_label=self.xml.get_object('answer')
        string=self.sublist[1]
        answer_label.set_text(string.split('@')[1])
        image=self.xml.get_object('tick1')
        image.set_from_file("images/wrong.png");
        self.reset_icon(1);
        self.continue_button.set_sensitive(False);
        
    def wrong2(self,widget,event):
        answer_label=self.xml.get_object('answer')
        string=self.sublist[2]
        answer_label.set_text(string.split('@')[1])
        image=self.xml.get_object('tick2')
        image.set_from_file("images/wrong.png");
        self.reset_icon(2);
        self.continue_button.set_sensitive(False);
        
    def wrong3(self,widget,event):
        answer_label=self.xml.get_object('answer')
        string=self.sublist[3]
        answer_label.set_text(string.split('@')[1])
        image=self.xml.get_object('tick3')
        image.set_from_file("images/wrong.png");
        self.reset_icon(3);
        self.continue_button.set_sensitive(False);
    
    def reset_icon(self, index):
        
        if(index!=0):
            image=self.xml.get_object('tick0')
            image.set_from_file("images/question.png");
        if(index!=1):
            image=self.xml.get_object('tick1')
            image.set_from_file("images/question.png"); 
        if(index!=2):
            image=self.xml.get_object('tick2')
            image.set_from_file("images/question.png"); 
        if(index!=3):
            image=self.xml.get_object('tick3')
            image.set_from_file("images/question.png");  
  
        
         
         
         
        
    
   

        
        
        
