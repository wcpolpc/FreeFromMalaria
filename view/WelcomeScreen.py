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


from gettext import gettext as _
class GameWelcomeScreen():
    '''
    classdocs
    '''
    def __init__(self,controll):
        '''
        Constructor
        '''
        
        
      
              
        self.xml=gtk.Builder();        
                
        ##init the background image buffer
    
        
        # Load Glade XML
        self.xml.add_from_file("glade/welcomeScreen.ui")
        
        # Get Window
        self.w = self.xml.get_object('window1')
        #self.w.connect("delete_event", gtk.main_quit)
        
        # Get Windows child
        self.w_child = self.w.get_child()
        
        self.w_child;
        # self.widget will be attached to the Activity
        # This can be any GTK widget except a window
        self.widget = self.w_child
        
        ##get the contoller  
        self.controller=controll
        
        #Sound toggle button
        
        self.play_button=self.xml.get_object('versionlabel')
        self.play_button.set_label('v 4.2a')


        
        self.play_button=self.xml.get_object('play')
        self.playlabela=_('Play the Game')
        self.play_button.set_label(self.playlabela)
        self.play_button.connect("button_press_event", self.comic_press_event)
        
#        self.map_button=self.xml.get_object('maps')
#        self.map_button.connect("button_press_event", self.map_press_event)

       
        self.options=self.xml.get_object('optionslabel')
        options=(_('Options'));
        self.options.set_text(options);
            

        self.play_label=self.xml.get_object('playlabel')
        playlabel=_('Play the Game')
        self.play_label.set_text(playlabel)
        

        
        self.lang_label=self.xml.get_object('languagelabel')
        lang_label=_('Current language:')
        self.lang_label.set_text(lang_label+self.controller.get_current_user_selection())
        
        
        self.prepare_language_drop()
        
    def prepare_language_drop(self):
        self.combo=self.xml.get_object('languagecombo')
       
        #load the approved list of languages

        store=gtk.ListStore(str)
       
        self.populate_approved_languages(store);
       
        self.combo.set_model(store)
        cell = gtk.CellRendererText()
        self.combo.pack_start(cell, True)
        self.combo.add_attribute(cell, 'text',0)
        self.combo.connect('changed', self.changed_cb)    
    def populate_approved_languages(self, combo):
         
         langs=self.controller.get_approved_langages();
         for i in langs:
           
            combo.append([i])
    
   
    def changed_cb(self,widget):
        try:
           
            model = widget.get_model()
            index = widget.get_active()
           
            if(self.controller.load_language_by_user_selection(model[index][0])):
                 dialog = gtk.MessageDialog(parent=None,
                                       buttons=gtk.BUTTONS_OK,
                                       flags=gtk.DIALOG_DESTROY_WITH_PARENT,
                                       type=gtk.MESSAGE_QUESTION,
                                       message_format="Language Loaded Successfully!");
                 dialog.set_title("Language Loaded!");
                 result = dialog.run()
                 dialog.destroy()
                 
                 
                 lang_label=_('Change the current language from '+ self.controller.get_current_user_selection())
                 self.lang_label.set_text(lang_label)
                
            
        except IOError :# as err:
            dialog = gtk.MessageDialog(parent=None,
                                       buttons=gtk.BUTTONS_OK,
                                       flags=gtk.DIALOG_DESTROY_WITH_PARENT,
                                       type=gtk.MESSAGE_QUESTION,
                                       message_format='ERROR: Failed to load language: '+model[index][0]);
            dialog.set_title("Language Error");
            result = dialog.run()
            dialog.destroy()

          
    def get_window(self):
        return self.w
    
    def sound_toggle_event(self,widget,source):
        
        print widget.get_active();
        if widget.get_active():
            self.controller.set_sound(True);
        else:
          # If control reaches here, the toggle button is up
          self.controller.set_sound(False);
          
    def comic_press_event(self,widget,event):
        if(self.controller!=None):
            self.controller.play_game("Comic",None)
    def map_press_event(self,widget,event):
        self.controller.play_game("Maps",None)
   
        
    def send_terminate(self):
        return True;

        
        
        