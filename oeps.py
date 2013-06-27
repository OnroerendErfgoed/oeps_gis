#!/usr/bin/python

from lxml import etree
import ogr
from shapely.geometry import Polygon, Point, LineString
from shapely.geometry.polygon import LinearRing
from shapely.wkt import loads


class OepsPoint(Point):
 
    def xml(self):
        point_element = etree.Element(u"punt")
        x_element = etree.Element("x")
        x_element.text = unicode(self.x)
        y_element = etree.Element("y")
        y_element.text = unicode(self.y)
        point_element.append(x_element)
        point_element.append(y_element)
        return point_element


class OepsLinearRing(LinearRing):

    def __init__(self, *args, **kwargs):
        super(OepsLinearRing, self).__init__(*args)
        self.ring_type = unicode(kwargs['ring_type'])

    def xml(self):
        lr_element = etree.Element(u'ring', type=self.ring_type)
        for coord in self.coords:
            lr_element.append(OepsPoint(coord).xml())
        return lr_element


class OepsAdrespunt(object):
    
    def __init__(self, adres_id, point):
        self.adres_id = adres_id
        self.point = point

    def xml(self):
        adrespunt_element = etree.Element(u'adrespunt')
        id_element = etree.Element(u'id')
        id_element.text = unicode(self.adres_id)
        adrespunt_element.append(id_element)
        adrespunt_element.append(self.point.xml())
        return adrespunt_element


class OepsPolygoon(object):

    def __init__(self, rings):
        self.rings = rings

    def xml(self):
        polygoon_element = etree.Element(u'polygoon')
        for ring in self.rings:
            polygoon_element.append(ring.xml()) 
        return polygoon_element

           
class OepsFeature(object):

    def __init__(self, feature_id, feature_type, constituents):
        self.feature_id = feature_id
        self.feature_type = feature_type
        self.constituents = constituents

    def xml(self):
        feature_element = etree.Element(unicode(self.feature_type))
        id_element = etree.Element(u'id')
        id_element.text = unicode(self.feature_id)
        feature_element.append(id_element)
        for constituent in self.constituents:
            feature_element.append(constituent.xml())
        return feature_element


class GisLocaties(object):
    def __init__(self):
        pass

    def xml(self):
        gis_locaties_element = etree.Element(u'gis_locaties')
        return gis_locaties_element


class Exporter(object):

    def __init__(self, output_filename):
        self.root = GisLocaties().xml() 
        self.file_name = output_filename
 
    def append_xml(self, layer):
        datasource = ogr.Open(layer.path)
        if datasource is None:
            raise Exception('Failed to open %s' % (layer.path))
        lyr = datasource.GetLayerByName(layer.basename)
        lyr_defn = lyr.GetLayerDefn()
        feature_type = lyr_defn.GetGeomType()
        if feature_type == 1 and lyr_defn.GetFieldIndex('adres_id') == -1:
           self.__append_point_xml(lyr, layer) 
        if feature_type == 1 and lyr_defn.GetFieldIndex('adres_id') > -1:
           self.__append_adres_xml(lyr, layer, datasource)
        if feature_type == 3:
           self.__append_polygon_xml(lyr, layer)
            
    def __append_point_xml(self, lyr,layer):
        for i in range(lyr.GetFeatureCount()): 
            feature = lyr.GetNextFeature()
            geometry = feature.GetGeometryRef()
            identifier = feature.GetFieldAsString(layer.id_field)
            oe_point = OepsPoint(geometry.GetX(), geometry.GetY())
            oe_feature = OepsFeature(identifier, layer.name, [oe_point])
            self.root.append(oe_feature.xml())
    
    def __append_adres_xml(self, lyr, layer, ds):
        sql = 'SELECT DISTINCT %s FROM %s' % (layer.id_field, layer.basename)
        id_lyr = ds.ExecuteSQL(sql)
        for i in range(id_lyr.GetFeatureCount()):
            feature = id_lyr.GetNextFeature()
            identifier = feature.GetFieldAsString(layer.id_field)
            sql = 'SELECT * FROM %s WHERE %s = %s' % (layer.basename,
                                                      layer.id_field,
                                                      identifier)
            rs = ds.ExecuteSQL(sql)
            adrespunten = []
            for i in range(rs.GetFeatureCount()):
                feature = rs.GetNextFeature()
                geometry = feature.GetGeometryRef()
                adres = OepsAdrespunt(
                          feature.GetFieldAsString(2), 
                          OepsPoint(geometry.GetX(), geometry.GetY()))
                adrespunten.append(adres)
            oe_feature = OepsFeature(identifier, layer.name, adrespunten)
            self.root.append(oe_feature.xml())
            ds.ReleaseResultSet(rs)
        ds.ReleaseResultSet(id_lyr)

    def __append_polygon_xml(self, lyr, layer):

        def ring_export(ring, r_type):
            lin_ring = loads(ring.ExportToWkt())
            oe_ring = OepsLinearRing(lin_ring.coords, ring_type=r_type)
            return oe_ring
    
        for i in range(lyr.GetFeatureCount()):
            feature = lyr.GetNextFeature()
            geometry = feature.GetGeometryRef()
            multi_poly = ogr.ForceToMultiPolygon(geometry)
            identifier = feature.GetFieldAsString(layer.id_field)
            rings = []
            for j in range(multi_poly.GetGeometryCount()):
                poly = multi_poly.GetGeometryRef(j)
                for k in range(poly.GetGeometryCount()):
                    ring = poly.GetGeometryRef(k)
                    ring_type = 'outer' if k == 0 else 'inner'
                    rings.append(ring_export(ring, ring_type)) 
            polygoon = OepsPolygoon(rings)
            oe_feature = OepsFeature(identifier, layer.name, [polygoon]) 
            self.root.append(oe_feature.xml())

    def serialize(self, pretty=False):
        return etree.tostring(self.root, pretty_print=pretty)

    def export(self, pretty=False):
        doctree = etree.ElementTree(self.root)
        output_file = open(self.file_name, 'w')
        doctree.write(output_file, 
                      encoding="UTF-8", 
                      method="xml", 
                      pretty_print=pretty,
                      xml_declaration=True)
        output_file.close()
