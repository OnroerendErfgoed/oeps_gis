 #!/usr/bin/python                                                               
 # -*- coding: utf-8 -*-                                                         
                                                                                 
import os
import ogr
import glob
import time
import argparse
from oeps import Exporter                                                       
from config import get_output_filename    
from conf.conf import Layer

parser = argparse.ArgumentParser(description='Batch convert shapefiles of the \
                                                              same dibe type.')
parser.add_argument(
                    '-d',
                    metavar='DATAFOLDER',
                    type=str, 
                    help='Path to datafolder', 
                    dest='datafolder',
                    required=True
                   )
parser.add_argument(
                    '-t',
                    metavar='TYPE',
                    help='Type of dibe object', 
                    dest='dibe_type',
                    required=True
                   )
parser.add_argument(
                     '-i',
                     metavar='ID_FIELD',
                     help='Fieldname of the field containing the identifiers \
                                                         of the dibe-objects',
                     dest='dibe_id_fieldname',
                     required=True
                    )  
args = parser.parse_args()

for shapefile in glob.glob(os.path.join(args.datafolder,"*.shp")):
    layer = Layer(
                  args.dibe_type , 
                  os.path.basename(shapefile),
                  args.dibe_id_fieldname,
                  shapefile
                 )
    exporter = Exporter(get_output_filename())                                            
    exporter.append_xml(layer)                                                  
    exporter.export()  

