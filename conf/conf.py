# -*- coding: utf-8 -*-
import os


class Layer(object):

    def __init__(self, name, filename, id_field, path_override=None):
        self.name = name
        self.filename = filename
        self.id_field = id_field
        self._path = None
        self._basename = None
        self.path_override = path_override

    @property
    def path(self):
        return self._path

    @path.getter
    def path(self):
        if not self.path_override: 
            shp = os.path.join(os.path.expanduser('~'), 'oeps_edit', self.filename)
            if os.path.splitdrive(shp)[0]:                                                   
                shp = os.path.join('d:\\',           
                                  'gebruikersgegevens',
                                  os.path.split(os.path.expanduser('~'))[1],
                                  'oeps_edit',
                                  os.path.split(shp)[1] 
                                  )
            return shp
        else:
            return self.path_override

    @property
    def basename(self):
        return self._basename

    @basename.getter
    def basename(self):
        return os.path.splitext(self.filename)[0]


class LayerConfig(object):

    def __init__(self):
        self.register = {}

    def add_layer(self, layer):
        if os.path.exists(layer.path):
            self.register[layer.name] = layer
        
