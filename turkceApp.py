# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:17:34 2018

@author: dcmunden
"""

import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, FallOutTransition
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.widget import Widget

import sqlite3 as sq

import random

Config.set('graphics','width','324')
Config.set('graphics','height','576')



class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen,self).__init__(**kwargs) 
    
        Clock.schedule_once(self.menuScreen2, 5)
        
    def menuScreen2(self,dt):
        sm.transition = FallOutTransition()
        sm.current = 'menu'



class MenuScreen(Screen):
    
    learn_bg_r = NumericProperty(0.3)
    learn_bg_b = NumericProperty(0.3)
    learn_bg_g = NumericProperty(0.3)
    
    practice_bg_r = NumericProperty(0.3)
    practice_bg_b = NumericProperty(0.3)
    practice_bg_g = NumericProperty(0.3)

    takeTest_bg_r = NumericProperty(0.3)
    takeTest_bg_b = NumericProperty(0.3)
    takeTest_bg_g = NumericProperty(0.3)

    extras_bg_r = NumericProperty(0.3)
    extras_bg_b = NumericProperty(0.3)
    extras_bg_g = NumericProperty(0.3)
        
    def learn_button_press(self):
        self.ids['learn_button'].background_color = 0.9294117,0.105882,0.14117647,1
        self.learn_bg_r = 0.9294117
        self.learn_bg_b = 0.105882
        self.learn_bg_g = 0.14117647
        
    def learn_button_release(self):
        self.ids['learn_button'].background_color = 0.3,0.3,0.3,1
        self.learn_bg_r = 0.3
        self.learn_bg_b = 0.3
        self.learn_bg_g = 0.3   

    def practice_button_press(self):
        self.ids['practice_button'].background_color = 0.9294117,0.105882,0.14117647,1
        self.practice_bg_r = 0.9294117
        self.practice_bg_b = 0.105882
        self.practice_bg_g = 0.14117647
    
    def practice_button_release(self):
        self.ids['practice_button'].background_color = 0.3,0.3,0.3,1
        self.practice_bg_r = 0.3
        self.practice_bg_b = 0.3
        self.practice_bg_g = 0.3
        
    def takeTest_button_press(self):
        self.ids['takeTest_button'].background_color = 0.9294117,0.105882,0.14117647,1
        self.takeTest_bg_r = 0.9294117
        self.takeTest_bg_b = 0.105882
        self.takeTest_bg_g = 0.14117647
        
    def takeTest_button_release(self):
        self.ids['takeTest_button'].background_color = 0.3,0.3,0.3,1
        self.takeTest_bg_r = 0.3
        self.takeTest_bg_b = 0.3
        self.takeTest_bg_g = 0.3
        
    def extras_button_press(self):
        self.ids['extras_button'].background_color = 0.9294117,0.105882,0.14117647,1
        self.extras_bg_r = 0.9294117
        self.extras_bg_b = 0.105882
        self.extras_bg_g = 0.14117647
        
    def extras_button_release(self):
        self.ids['extras_button'].background_color = 0.3,0.3,0.3,1
        self.extras_bg_r = 0.3
        self.extras_bg_b = 0.3
        self.extras_bg_g = 0.3
    


       
        
        



class MyScreenManager(ScreenManager):
    pass



class TurkceApp(App):   
    def build(self):
        global sm
        sm = MyScreenManager()
        return sm
    
    
    
class TempScreen(Screen):
    pass
    

class PracticeScreen(Screen):

    question = StringProperty()
    answer_r = StringProperty()
    answer_w1 = StringProperty()
    answer_w2 = StringProperty()
    answer_w3 = StringProperty()


    def __init__(self, **kwargs):
        super(Screen,self).__init__(**kwargs) 
    
        self.conn = sq.connect(r'C:\Users\CrunchyTiger\Desktop\kivy\Türkçe_Tavşanı\turkceApp\database\turk_eng_db.sqlite')

        self.cursor = self.conn.cursor()

        self.cursor.execute("SELECT max(ID) from TURK_ENG")

        self.ID_full_range = list(range(1,self.cursor.fetchone()[0]+1))

        self.get_question_answers()


    def get_question_answers(self):

        # select an ID for a question
        question_ID = random.choice(self.ID_full_range)
        # remove that ID from future selection
        self.ID_full_range.remove(question_ID)
        # temporary removal for this question
        adjusted_range = self.ID_full_range
        # set one of the answers to the correct ID
        answer_right_ID = question_ID
        # select more random IDs for the wrong answers
        wrong_answers_IDs = []
        for IDs in range(3):
            cur_wrong_ID = random.choice(adjusted_range)
            wrong_answers_IDs.append(cur_wrong_ID)
            adjusted_range.remove(cur_wrong_ID)
        
        # get and set question text
        self.cursor.execute("SELECT TURKISH FROM TURK_ENG WHERE ID = ?",(question_ID,))
        for row in self.cursor:
            self.question = row[0]

        # get and set right answer text
        self.cursor.execute("SELECT ENGLISH FROM TURK_ENG WHERE ID = ?",(answer_right_ID,))
        for row in self.cursor:
            self.answer_r = row[0]

        # get and set right answer text
        self.cursor.execute("SELECT ENGLISH FROM TURK_ENG WHERE ID = ?",(wrong_answers_IDs[0],))
        for row in self.cursor:
            self.answer_w1 = row[0]

        # get and set right answer text
        self.cursor.execute("SELECT ENGLISH FROM TURK_ENG WHERE ID = ?",(wrong_answers_IDs[1],))
        for row in self.cursor:
            self.answer_w2 = row[0]

        # get and set right answer text
        self.cursor.execute("SELECT ENGLISH FROM TURK_ENG WHERE ID = ?",(wrong_answers_IDs[2],))
        for row in self.cursor:
            self.answer_w3 = row[0]



    
    
if __name__ == '__main__':
    TurkceApp().run()