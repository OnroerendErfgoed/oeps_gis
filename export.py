#!/usr/bin/python
# -*- coding: utf-8 -*-

from oeps import Exporter
from config import layer_conf, get_output_filename

exporter = Exporter(get_output_filename())
for layername, layer in layer_conf.register.items():
    exporter.append_xml(layer)

exporter.export()
