#!/usr/bin/python

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

from oeps import Exporter
from config import layer_conf, get_output_filename
         
class OepsGisGui:
    '''GUI screen'''

    def __init__(self, master, layer_conf):
        
        self.layer_conf = layer_conf
        frame = Frame(master)
        frame.pack()

        frame_layers = Frame(frame)
        frame_layers.pack()

        frame_buttons = Frame(frame)
        frame_buttons.pack()

        self.layers_selectbox = Listbox(
                                 frame_layers,
                                 selectmode=MULTIPLE,
                                 width=60,
                                 bg='#fcfcfc',
                                 fg='#010101',
                                 bd=1)
        self.layers_selectbox.pack(side=LEFT, padx=10, pady=10)

        self.layernames = [key for key in layer_conf.register]
        for layername in self.layernames:
            self.layers_selectbox.insert(END, layername)

        self.export_button = Button(frame_buttons,
                                          text='Exporteer lagen',
                                          )
        self.export_button.pack(side=LEFT, padx=10, pady=15)
        self.export_button.config(command = self.export_layers)
           
    def export_layers(self):
        items = self.layers_selectbox.curselection()
        items = [self.layernames[item] for item in items]
        exporter = Exporter(get_output_filename())
        for item in items:
            exporter.append_xml(self.layer_conf.register[item])
        exporter.export()
        
        
if __name__ == '__main__':
    root = Tk()
    root.title('test')
    app = OepsGisGui(root, layer_conf)
    root.mainloop()
