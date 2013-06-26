import os
from lxml import etree
from oeps import Exporter
from config import layer_conf

exporter = Exporter()
for layername, layer in layer_conf.register.iteritems():
    exporter.export_layer(layer)
print exporter.serialize()
