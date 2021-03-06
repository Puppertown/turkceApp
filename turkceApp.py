# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:17:34 2018

@author: dcmunden
"""

import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, FallOutTransition, SlideTransition
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.widget import Widget

from kivy.animation import Animation
from kivy.uix.label import Label

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

        self.pscreen1 = PracticeScreen(name='practice')
        sm.add_widget(self.pscreen1)

    
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
        extraBunnies = ExtrasScreen(name='extras')
        sm.add_widget(extraBunnies)
        sm.transition = SlideTransition(direction='left')
        sm.current = 'extras'
    

       
        
        



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

    question_type_label = StringProperty()

    back_button_image = StringProperty('arrow_left_green.png')

    question = StringProperty()
    answer_r = StringProperty()
    answer_w1 = StringProperty()
    answer_w2 = StringProperty()
    answer_w3 = StringProperty()

    button_location_1 = NumericProperty()
    button_location_2 = NumericProperty()
    button_location_3 = NumericProperty()
    button_location_4 = NumericProperty()

    right_bg_r = NumericProperty(0.3)
    right_bg_b = NumericProperty(0.3)
    right_bg_g = NumericProperty(0.3)

    wrong1_bg_r = NumericProperty(0.3)
    wrong1_bg_b = NumericProperty(0.3)
    wrong1_bg_g = NumericProperty(0.3)

    wrong2_bg_r = NumericProperty(0.3)
    wrong2_bg_b = NumericProperty(0.3)
    wrong2_bg_g = NumericProperty(0.3)

    wrong3_bg_r = NumericProperty(0.3)
    wrong3_bg_b = NumericProperty(0.3)
    wrong3_bg_g = NumericProperty(0.3)

    title_outerRect_width = NumericProperty(0.88)
    title_innerRect_width = NumericProperty(0.85)

    title_height = NumericProperty(0.16)
    title_position = NumericProperty(0.755)
    title_border_ratio = NumericProperty(0.91)

    answer_outerRect_width = NumericProperty(0.78)
    answer_innerRect_width = NumericProperty(0.75)
    answer_outerRect_height = NumericProperty(0.73)
    answer_innerRect_height = NumericProperty(0.58)
    answer_inner_radius = NumericProperty(15)

    def __init__(self, **kwargs):
        super(Screen,self).__init__(**kwargs) 

        # for laptop
        self.conn = sq.connect(r'turkceApp\database\turk_eng_db.sqlite')
        # for desktop
        #self.conn = sq.connect(r'database\turk_eng_db.sqlite')

        self.cursor = self.conn.cursor()

        self.cursor.execute("SELECT max(ID) from TURK_ENG")

        self.ID_full_range = list(range(1,self.cursor.fetchone()[0]+1))

        self.get_question_answers()

    def back_button_press(self):
        self.back_button_image = 'arrow_left_red.png'

    def back_button_release(self):
        sm.transition = SlideTransition(direction='right')
        sm.current = 'menu'
        if 'nextQ1' in sm.screen_names:
            previousScreen = sm.get_screen('nextQ1')
        elif 'nextQ2' in sm.screen_names:
            previousScreen = sm.get_screen('nextQ2')
        elif 'practice' in sm.screen_names:
            previousScreen = sm.get_screen('practice')
        sm.remove_widget(previousScreen)

    def answer_button_press(self,button_id):
        if 'right' in button_id:
            self.ids[button_id].background_color = 0.3,0.7,0.3,1
            self.right_bg_r = 0.3
            self.right_bg_g = 0.7
            self.right_bg_b = 0.3

            next_Q_widget = Practice_NextQWidget()
            next_Q_widget.ans_string = 'Correct!'
            next_Q_widget.widget_bg_r = 0.3
            next_Q_widget.widget_bg_g = 0.7
            next_Q_widget.widget_bg_b = 0.3
            self.add_widget(next_Q_widget)

        elif 'wrong' in button_id:
            self.ids[button_id].background_color = 0.7,0.3,0.3,1
            self.ids['answer_right'].background_color = 0.3,0.7,0.3,1
            self.right_bg_r = 0.3
            self.right_bg_g = 0.7
            self.right_bg_b = 0.3
            if '1' in button_id:
                self.wrong1_bg_r = 0.7
                self.wrong1_bg_b = 0.3
                self.wrong1_bg_g = 0.3
            elif '2' in button_id:
                self.wrong2_bg_r = 0.7
                self.wrong2_bg_b = 0.3
                self.wrong2_bg_g = 0.3  
            elif '3' in button_id:
                self.wrong3_bg_r = 0.7
                self.wrong3_bg_b = 0.3
                self.wrong3_bg_g = 0.3  

            next_Q_widget = Practice_NextQWidget()
            next_Q_widget.ans_string = 'Sorry, incorrect'
            next_Q_widget.widget_bg_r = 0.7
            next_Q_widget.widget_bg_g = 0.3
            next_Q_widget.widget_bg_b = 0.3
            self.add_widget(next_Q_widget)
        
        #animation = Animation(pos=(100, 100), t='out_bounce')
        #animation += Animation(pos=(200, 100), t='out_bounce')
        #animation &= Animation(size=(500, 500))
        #animation += Animation(size=(100, 50))

        #self.testLabel = Label(text='Hello world')
        #self.add_widget(self.testLabel)
        #animation.start(self.testLabel)

        # gittttt




    def get_question_answers(self):

        # decide if translating English-to-Turkish or Turkish-to-English
        if random.random() < .5:
            self.question_from = 'TURKISH'
            self.question_to = 'ENGLISH'
            self.question_type_label = 'Translate into English:'
        else:
            self.question_from = 'ENGLISH'
            self.question_to = 'TURKISH'
            self.question_type_label = 'Translate into Turkish:'
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

        # button y-locations
        button_locations = [0.67-i*0.115 for i in range(4)]
        
        # get and set question text
        self.cursor.execute("SELECT "+self.question_from+" FROM TURK_ENG WHERE ID = ?",(question_ID,))
        for row in self.cursor:
            self.question = row[0]

        # get and set right answer text
        self.cursor.execute("SELECT "+self.question_to+" FROM TURK_ENG WHERE ID = ?",(answer_right_ID,))
        for row in self.cursor:
            self.answer_r = row[0]
        self.button_location_1 = random.choice(button_locations)
        button_locations.remove(self.button_location_1)

        # get and set right answer text
        self.cursor.execute("SELECT "+self.question_to+" FROM TURK_ENG WHERE ID = ?",(wrong_answers_IDs[0],))
        for row in self.cursor:
            self.answer_w1 = row[0]
        self.button_location_2 = random.choice(button_locations)
        button_locations.remove(self.button_location_2)

        # get and set right answer text
        self.cursor.execute("SELECT "+self.question_to+" FROM TURK_ENG WHERE ID = ?",(wrong_answers_IDs[1],))
        for row in self.cursor:
            self.answer_w2 = row[0]
        self.button_location_3 = random.choice(button_locations)
        button_locations.remove(self.button_location_3)

        # get and set right answer text
        self.cursor.execute("SELECT "+self.question_to+" FROM TURK_ENG WHERE ID = ?",(wrong_answers_IDs[2],))
        for row in self.cursor:
            self.answer_w3 = row[0]
        self.button_location_4 = random.choice(button_locations)
        button_locations.remove(self.button_location_4)


class Practice_NextQWidget(FloatLayout):
    
    ans_string = StringProperty('')

    widget_bg_r = NumericProperty(0.3)
    widget_bg_b = NumericProperty(0.3)
    widget_bg_g = NumericProperty(0.3)

    border_width = NumericProperty(0.96)
    border_height = NumericProperty(0.90)

    def press_next(self):

        if 'nextQ1' in sm.screen_names:
            previousQ = sm.get_screen('nextQ1')
            self.newQuestion2 = PracticeScreen(name='nextQ2')
            sm.add_widget(self.newQuestion2)
            sm.current = 'nextQ2'
            sm.remove_widget(previousQ)

        elif 'nextQ2' in sm.screen_names:
            previousQ = sm.get_screen('nextQ2')
            self.newQuestion1 = PracticeScreen(name='nextQ1')
            sm.add_widget(self.newQuestion1)
            sm.current = 'nextQ1'
            sm.remove_widget(previousQ)

        else:
            previousQ = sm.get_screen('practice')
            self.newQuestion1 = PracticeScreen(name='nextQ1')
            sm.add_widget(self.newQuestion1)
            sm.current = 'nextQ1'
            sm.remove_widget(previousQ)
    

class ExtrasScreen(Screen):
    
    def pressBunnies(self):
        sm.transition = SlideTransition(direction='right')
        sm.current = 'menu'
        bunniesScreen = sm.get_screen('extras')
        sm.remove_widget(bunniesScreen)



    
if __name__ == '__main__':
    TurkceApp().run()