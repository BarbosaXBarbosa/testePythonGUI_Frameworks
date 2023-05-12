# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:27:21 2023

@author: João Victor Barbosa
"""

from kivy.app import App
from kivy.uix.button import Button

class ExemploApp(App):
    def build(self):
        return Button(text='Olá, Mundo!')