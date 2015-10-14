#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import tkMessageBox

from oeps import Exporter
from config import layer_conf, get_output_filename
         
class OepsGisGui:
    '''GUI screen'''

    def __init__(self, master, layer_conf):
        
        self.layer_conf = layer_conf
        self.layernames = [key for key in layer_conf.register]
        
        #setup Frame
        frame = Frame(master)
        frame.pack()

        #setup layers frame
        frame_layers = Frame(frame)
        frame_layers.pack(side=TOP)

        #add label to layers frame
        self.label = Label(frame_layers, 
                           text='Selecteer lagen:', 
                           width=16)
        self.label.pack(side=TOP, padx=0, pady=5, anchor=W)

        #add select widget to layers frame
        self.layers_selectbox = Listbox(
                                 frame_layers,
                                 selectmode=MULTIPLE,
                                 width=20,
                                 height=len(self.layernames),
                                 bg='#fcfcfc',
                                 fg='#010101',
                                 bd=1)
        self.layers_selectbox.pack(padx=15, pady=0)
        
        # add options to select widget
        for layername in self.layernames:
            self.layers_selectbox.insert(END, layername)

        #add button frame
        frame_buttons = Frame(frame)
        frame_buttons.pack()

        #add export button
        self.export_button = Button(frame_buttons,
                                          text='Exporteer selectie')
        self.export_button.pack(side=TOP, padx=10, pady=10)
        self.export_button.config(command = self.export_layers)
           
    def export_layers(self):
        items = self.layers_selectbox.curselection()
        items = [self.layernames[item] for item in items]
        exporter = Exporter(get_output_filename())
        try:
            for item in items:
                exporter.append_xml(self.layer_conf.register[item])
            exporter.export()
            SuccesView()
        except:
            ErrorView(sys.exc_info()[0])
        

class SuccesView:

      def __init__(self):
         self.message = 'De lagen werden succesvol geëxporteerd.'
         tkMessageBox.showinfo('Lagen geëxporteerd', self.message) 

class ErrorView:

    def __init__(self, e):
        self.error = e
        tkMessageBox.showerror('Fout bij het exporteren', e)

if __name__ == '__main__':
    root = Tk()
    root.title('OEPS export')
    app = OepsGisGui(root, layer_conf)
    root.mainloop()
