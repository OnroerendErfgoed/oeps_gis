import os
from lxml import etree
from oeps import Exporter
from config import layer_conf, output_filename

exporter = Exporter(output_filename)
for layername, layer in layer_conf.register.iteritems():
    exporter.append_xml(layer)

exporter.export(pretty=True)
