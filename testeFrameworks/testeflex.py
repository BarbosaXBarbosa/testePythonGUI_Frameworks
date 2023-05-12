# -*- coding: utf-8 -*-
"""
Created on Fri May 12 09:35:01 2023

@author: João Victor Barbosa
"""

from flexx import flx

class Exemplo(flx.Widget):
    
    def init(self):
        flx.Button(text='Olá')
        flx.Button(text='Mundo')

if __name__ == '__main__':
    a = flx.App(Exemplo, title='Flexx demonstração')
    m = a.launch()
    flx.run()