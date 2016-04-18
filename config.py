# -*- coding: utf-8 -*-

import os
from datetime import datetime
from conf.conf import Layer, LayerConfig

layer_conf = LayerConfig()

layer_conf.add_layer(Layer('dibe_relict', 'edit_dibe_relict.shp', 'relict_id', 'BSK'))
layer_conf.add_layer(Layer('dibe_geheel', 'edit_dibe_geheel.shp', 'Id','BSK'))
layer_conf.add_layer(Layer('dibe_orgel', 'edit_dibe_orgel.shp', 'ID', 'BSK'))
layer_conf.add_layer(Layer('cai_relict', 'edit_cai_relict.shp', 'Id', 'BSK'))
layer_conf.add_layer(Layer('cai_zone', 'edit_cai_zone.shp', 'Id', 'BSK'))
layer_conf.add_layer(Layer('ile_boom', 'edit_ile_boom.shp', 'Id', 'BSK'))
layer_conf.add_layer(Layer('ile_park', 'edit_ile_park.shp', 'Id', 'BSK'))
layer_conf.add_layer(Layer('ile_relict', 'edit_ile_relict.shp', 'Id', 'BSK'))
layer_conf.add_layer(Layer('ivm_varend', 'edit_ivm_varend.shp', 'Id', 'BSK'))
layer_conf.add_layer(Layer('woi_relict', 'edit_woi_relict.shp', 'ID', 'BSK'))
layer_conf.add_layer(Layer('deo_gebeurtenis', 'edit_deo_gebeurtenis.shp', 'Id', 'BSK'))
layer_conf.add_layer(Layer('bes_bescherming', 'edit_bes_bescherming.shp', 'Id', 'BSK'))

def get_output_filename():

    if os.name != 'nt':
        output_filename = os.path.join(os.path.expanduser('~'), 
                               'oeps_export',
                               'oeps_export_' 
                               + (datetime.now().isoformat()).replace(':', '-') 
                               +'.xml'
                               )
    else:
        output_filename = os.path.join('d:\\', 
                                       'gebruikersgegevens',
                                        os.path.split(os.path.expanduser('~'))[1],
                                        'oeps_export',
                                        'oeps_export_'
                                        + (datetime.now().isoformat()).replace(':', '-') 
                                        +'.xml'                                          
                                       )
    return output_filename
