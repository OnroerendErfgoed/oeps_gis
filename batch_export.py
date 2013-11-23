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
                    nargs=1,
                    help='Path to datafolder', 
                    dest='datafolder'
                   )
parser.add_argument(
                    '-t',
                    metavar='TYPE',
                    nargs=1,
                    help='Type of dibe object', 
                    dest='dibe_type'
                   )
parser.add_argument(
                     '-i',
                     metavar='ID_FIELD',
                     nargs=1,
                     help='Fieldname of the field containing the identifiers \
                                                         of the dibe-objects',
                     dest='dibe_id_fieldname'
                    )  
args = parser.parse_args()

for shapefile in glob.glob(os.path.join(args.datafolder[0],"*.shp")):
    layer = Layer(
                  args.dibe_type[0] , 
                  os.path.basename(shapefile),
                  args.dibe_id_fieldname[0],
                  shapefile
                 )
    exporter = Exporter(get_output_filename())                                            
    exporter.append_xml(layer)                                                  
    exporter.export()  

