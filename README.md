oeps_gis
========

Exporteren van gislocaties van shapefile naar oeps XML formaat

Builden voor Windows
--------------------

*Opmerking: uitleen-laptop 2153598 is klaar reeds klaar om te builden. Builds 
zijn beschikbaar op: V:\1_3_Ondersteuning\4_IT_Tools-progs\oeps_gis*

* Installeer dependencies (ogr, shapely). Dit is het eenvoudigst door de 
osgeo4w-installer te gebruiken. registreer daarna de osgeo4w python in de
registry. Zie hiervoor: http://trac.osgeo.org/osgeo4w/ticket/114

* installeer py2exe met de installer

* maak een setup.py voor py2exe (zal later toegevoegd worden)

* Installeer VSexpress 2010

* run python setup.py py2exe

Installeren bij gebruiker
-------------------------

* kopieer de gebuilde applicatie naar de v-schijf
* kopier de vioe_edit folder met de shapefiles naar de map gebruikersgegevens/gebruiker
* maak eventueel een snelkoppeling naar dist/export.exe

