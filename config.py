# -*- coding: utf-8 -*-

import os
from datetime import datetime
from conf.conf import Layer, LayerConfig

layer_conf = LayerConfig()

layer_conf.add_layer(Layer('dibe_relict', 'edit_dibe_relict.shp', 'relict_id'))
layer_conf.add_layer(Layer('dibe_geheel', 'edit_dibe_geheel.shp', 'Id'))
layer_conf.add_layer(Layer('dibe_orgel', 'edit_dibe_orgel.shp', 'ID'))
layer_conf.add_layer(Layer('cai_relict', 'edit_cai_relict.shp', 'Id'))
layer_conf.add_layer(Layer('cai_zone', 'edit_cai_zone.shp', 'Id'))
layer_conf.add_layer(Layer('ile_boom', 'edit_ile_boom.shp', 'Id'))
layer_conf.add_layer(Layer('ile_park', 'edit_ile_park.shp', 'Id'))
layer_conf.add_layer(Layer('ivm_varend', 'edit_ivm_varend.shp', 'Id'))
layer_conf.add_layer(Layer('woi_relict', 'edit_woi_relict.shp', 'ID'))
layer_conf.add_layer(Layer('deo_gebeurtenis', 'edit_deo_gebeurtenis.shp', 'Id'))
layer_conf.add_layer(Layer('bes_bescherming', 'edit_bes_bescherming.shp', 'Id'))

output_filename = os.path.join(os.path.expanduser('~'), 'oeps_export_' +
                        (datetime.now().isoformat()).replace(':', '-') + '.xml')

if os.path.splitdrive(output_filename)[0]:
    output_filename = os.path.join('d:\\', 
                                   'gebruikersgegevens',
                                   os.path.split(os.path.expanduser('~'))[1],
                                   'oeps_export',
                                   os.path.split(output_filename)[1]
                                  )
