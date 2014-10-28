import re
import json

{
"Cylindrical_Equal_Area":"+proj=cea +lon_0=%.16g +lat_ts=%.16g +x_0=%.16g +y_0=%.16g ",
"Bonne":"+proj=bonne +lon_0=%.16g +lat_1=%.16g +x_0=%.16g +y_0=%.16g ",
"Cassini_Soldner": "+proj=cass +lat_0=%.16g +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"New_Zealand_Map_Grid": "+proj=nzmg +lat_0=%.16g +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"Transverse_Mercator":"+proj=etmerc +lat_0=%.16g +lon_0=%.16g +k=%.16g +x_0=%.16g +y_0=%.16g ",
#"+proj=utm +zone=%d "
#"+proj=utm +zone=%d +south ",
#"+proj=tmerc +lat_0=%.16g +lon_0=%.16g +k=%.16g +x_0=%.16g +y_0=%.16g "
"Transverse_Mercator_South_Orientated": "+proj=tmerc +lat_0=%.16g +lon_0=%.16g +k=%.16g +x_0=%.16g +y_0=%.16g +axis=wsu ",
"Mercator_1SP":"+proj=merc +lon_0=%.16g +k=%.16g +x_0=%.16g +y_0=%.16g ",
#"+proj=merc +lon_0=%.16g +lat_ts=%.16g +x_0=%.16g +y_0=%.16g ",
"Mercator_2SP":"+proj=merc +lon_0=%.16g +lat_ts=%.16g +x_0=%.16g +y_0=%.16g ",
#SRS_PT_MERCATOR_AUXILARY_SPHERE: "+proj=merc +a=%.16g +b=%.16g +lat_ts=%.16g +lon_0=%.16g +x_0=%.16g +y_0=%.16g +k=%.16g +units=m +nadgrids=@null +wktext  +no_defs",
"Oblique_Stereographic":"+proj=sterea +lat_0=%.16g +lon_0=%.16g +k=%.16g +x_0=%.16g +y_0=%.16g ",
"Stereographic":"+proj=stere +lat_0=%.16g +lon_0=%.16g +k=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=stere +lat_0=90 +lat_ts=%.16g +lon_0=%.16g +k=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=stere +lat_0=-90 +lat_ts=%.16g +lon_0=%.16g +k=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=eqc +lat_ts=%.16g +lat_0=%.16g +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=gstmerc +lat_0=%.16g +lon_0=%.16g +k_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=gnom +lat_0=%.16g +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=ortho +lat_0=%.16g +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=laea +lat_0=%.16g +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=aeqd +lat_0=%.16g +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=eqdc +lat_0=%.16g +lon_0=%.16g +lat_1=%.16g +lat_2=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=mill +lat_0=%.16g +lon_0=%.16g +x_0=%.16g +y_0=%.16g +R_A ",
"+proj=moll +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=eck1 +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=eck2 +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=eck3 +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=eck4 +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=eck5 +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=eck6 +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=poly +lat_0=%.16g +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=aea +lat_1=%.16g +lat_2=%.16g +lat_0=%.16g +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=robin +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=vandg +lon_0=%.16g +x_0=%.16g +y_0=%.16g +R_A ",
"+proj=sinu +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=gall +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=goode +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=igh "
"+proj=geos +lon_0=%.16g +h=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=lcc +lat_1=%.16g +lat_2=%.16g +lat_0=%.16g +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=lcc +lat_1=%.16g +lat_0=%.16g +lon_0=%.16g +k_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=somerc +lat_0=%.16g +lon_0=%.16g +k_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=omerc +lat_0=%.16g +lonc=%.16g +alpha=%.16g +k=%.16g +x_0=%.16g +y_0=%.16g +no_uoff ",
"+proj=somerc +lat_0=%.16g +lon_0=%.16g +k_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=omerc +lat_0=%.16g +lonc=%.16g +alpha=%.16g +k=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=tpeqd +lat_1=%.16g +lon_1=%.16g +lat_2=%.16g +lon_2=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=iwm_p +lat_1=%.16g +lat_2=%.16g +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=wag1 +x_0=%.16g +y_0=%.16g ",
"+proj=wag2 +x_0=%.16g +y_0=%.16g ",
"+proj=wag3 +lat_ts=%.16g +x_0=%.16g +y_0=%.16g ",
"+proj=wag4 +x_0=%.16g +y_0=%.16g ",
"+proj=wag5 +x_0=%.16g +y_0=%.16g ",
"+proj=wag6 +x_0=%.16g +y_0=%.16g ",
"+proj=wag7 +x_0=%.16g +y_0=%.16g ",
"+proj=somerc +lat_0=%.16g +lon_0=%.16g +x_0=%.16g +y_0=%.16g ",
"""

def testWKT(code):
    sumCode = 0
    codeWords = ['GEOGCS','GEOCCS','PROJCS','LOCAL_CS']
    for w in codeWords:
        sumCode += 1 + code.find(w)
    return sumCode

def extend(source):
    destination = {}
    if not source:
        return destination
    for prop in source:
        value = source[prop]
        if value:
            destination[prop] = value
    return destination
        

def mapit(obj, key, v):
    new_v = []
    for aa in v:
        o = {}
        sExpr(aa, o)
        new_v.append(o)

    rst = {}
    for b in new_v:
        rst = extend(rst, b)
        
    obj[key] = rst
    return obj

def sExpr(v, obj):
    if not isinstance(v, list):
        obj[v] = True
        return obj
    else:
        key = v[0]
        v = v[1:]
        if key == 'PARAMETER':
            key = v[0]
            v = v[1:]
        if len(v) == 1:
            if isinstance(v[0], list):
                obj[key] = {}
                sExpr(v[0], obj[key])
            else:
                obj[key] = v[0]
        elif not len(v):
            obj[key] = True
        elif key == 'TOWGS84':
            obj[key] = v
        else:
            obj[key] = {}
            if ['UNIT', 'PRIMEM', 'VERT_DATUM'].count(key) > 0:
                obj[key] = {
                    'name': v[0].lower(),
                    'convert': v[1]
                }
                if len(v) == 3:
                    obj[key]["auth"] = v[2]
            elif key == 'SPHEROID':
                obj[key] = {
                    'name': v[0], 'a':v[1], 'rf':v[2]
                }
                if len(v) == 4:
                    obj[key]['auth'] = v[3]
            elif ['GEOGCS', 'GEOCCS', 'DATUM', 'VERT_CS', 'COMPD_CS', 'LOCAL_CS', 'FITTED_CS', 'LOCAL_DATUM'].count(key) > 0:
                v[0] = ['name', v[0]]
                obj = mapit(obj, key, v)
            else:
                allItemList = True 
                for item in v:
                    if not isinstance(item, list):
                        allItemList = False
                        break
                if allItemList:
                    obj = mapit(obj, key, v)
                else:
                    obj = sExpr(v, obj[key])
        return obj

def rename(obj, params):
    outName = params[0]
    inName = params[1]
    if (outName not in obj) and (inName in obj):
        obj[outName] = obj[inName]
        if len(params) == 3:
            obj[outName] = params[2](obj, obj[outName])
    return obj
            
def d2r(_wkt, _input):
    D2R = 0.01745329251994329577
    return float(_input) * D2R 
    
def cleanWKT(wkt):
    if wkt["type"] == 'GEOGCS':
        wkt["projName"] = 'longlat'
    elif wkt["type"] == 'LOCAL_CS':
        wkt["projName"] = 'identity'
        wkt["local"] = True
    else:
        if isinstance(wkt['PROJECTION'], dict):
            wkt["projName"] = wkt["PROJECTION"].keys()[0]
        else:
            wkt['projName'] = wkt['PROJECTION'];

    if wkt['UNIT']:
        wkt['units'] = wkt['UNIT']['name'].lower()
        if wkt['units'] == 'metre':
            wkt['units'] = 'meter'
        if wkt['UNIT']['convert']:
            wkt['to_meter'] = float(wkt['UNIT']['convert'])

    if wkt['GEOGCS']:
        if wkt['GEOGCS']['DATUM']:
            wkt['datumCode'] = wkt['GEOGCS']['DATUM']['name'].lower()
        else:
            wkt['datumCode'] = wkt['GEOGCS']['name'].lower()

        if wkt['datumCode'][:2] == 'd_':
            wkt['datumCode'] = wkt['datumCode'][2:]

        if wkt['datumCode'] == 'new_zealand_geodetic_datum_1949' or wkt['datumCode'] == 'new_zealand_1949':
            wkt['datumCode'] = 'nzgd49'

        if wkt['datumCode'] == "wgs_1984":
            if wkt['PROJECTION'] == 'Mercator_Auxiliary_Sphere':
                wkt['sphere'] = True
            wkt['datumCode'] = 'wgs84';

        if wkt['datumCode'][-6:] == '_ferro':
            wkt['datumCode'] = wkt['datumCode'][:-6]

        if wkt['datumCode'][-8:] == '_jakarta':
            wkt['datumCode'] = wkt['datumCode'][:-8]

        if wkt['datumCode'].find('belge') > -1:
            wkt['datumCode'] = "rnb72"

        if wkt['GEOGCS']['DATUM'] and wkt['GEOGCS']['DATUM']['SPHEROID']:
            wkt["ellps"] = wkt['GEOGCS']['DATUM']['SPHEROID']['name'].replace('_19', '')
            wkt["ellps"] = re.sub(r'[Cc]larke\_18', 'clrk', wkt["ellps"])
            if wkt["ellps"].lower()[:13] == "international":
                wkt["ellps"] = 'intl'

            wkt["a"] = wkt['GEOGCS']['DATUM']['SPHEROID']['a']
            wkt["rf"] = float(wkt['GEOGCS']['DATUM']['SPHEROID']['rf'])

        if wkt['datumCode'].find('osgb_1936')> -1:
            wkt['datumCode'] = "osgb36"

    if "b" in wkt and (not wkt["b"].isdigit()): # not number
        wkt["b"] = wkt["a"]

    def toMeter(_wkt, _input):
        ratio = 1 
        if 'to_meter' in _wkt:
            ratio = _wkt["to_meter"]
        return float(_input) * ratio

    def renamer(_wkt, a):
        return rename(_wkt, a)

    _list = [
        ['standard_parallel_1', 'Standard_Parallel_1'],
        ['standard_parallel_2', 'Standard_Parallel_2'],
        ['false_easting', 'False_Easting'],
        ['false_northing', 'False_Northing'],
        ['central_meridian', 'Central_Meridian'],
        ['latitude_of_origin', 'Latitude_Of_Origin'],
        ['scale_factor', 'Scale_Factor'],
        ['k0', 'scale_factor'],
        ['latitude_of_center', 'Latitude_of_center'],
        ['lat0', 'latitude_of_center', d2r],
        ['longitude_of_center', 'Longitude_Of_Center'],
        ['longc', 'longitude_of_center', d2r],
        ['x0', 'false_easting', toMeter],
        ['y0', 'false_northing', toMeter],
        ['long0', 'central_meridian', d2r],
        ['lat0', 'latitude_of_origin', d2r],
        ['lat0', 'standard_parallel_1', d2r],
        ['lat1', 'standard_parallel_1', d2r],
        ['lat2', 'standard_parallel_2', d2r],
        ['alpha', 'azimuth', d2r],
        ['srsCode', 'name']
    ]
    for i,item in enumerate(_list):
        wkt = renamer(wkt, item)

    if "long0" not in wkt and "longc" in wkt and \
        (wkt['PROJECTION'] == 'Albers_Conic_Equal_Area' or wkt['PROJECTION'] == "Lambert_Azimuthal_Equal_Area"):
        wkt["long0"] = wkt["longc"]
        
    return wkt
 
def wkt(code):
    wkt = "," + code
    wkt = re.sub(r'\s*\,\s*([A-Z_0-9]+?)(\[)', r',["\1",', wkt)[1:]
    wkt = re.sub(r'\s*\,\s*([A-Z_0-9]+?)\]', r',"\1"]', wkt)
    lisp = json.loads(wkt)
    _type = lisp[0]
    _name = lisp[1]
    lisp = lisp[2:]
    lisp = ['output', ['type', _type], ['name', _name]] + lisp
   
    obj = {}
    obj = sExpr(lisp, obj)
    obj = cleanWKT(obj["output"])
    return extend(obj)
 
def parse(code):
    if testWKT(code):
        wkt(code)


def Export2Proj4(wkt):
    if 'type' in wkt:
        if wkt['type'] == "GEOGCS":
            "+proj=longlat "
        elif wkt['type'] == "GEOCCS":
            "+proj=geocent "
        elif wkt['
        

firstProjection = 'PROJCS["NAD83 / Massachusetts Mainland",GEOGCS["NAD83",DATUM["North_American_Datum_1983",SPHEROID["GRS 1980",6378137,298.257222101,AUTHORITY["EPSG","7019"]],AUTHORITY["EPSG","6269"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.01745329251994328,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4269"]],UNIT["metre",1,AUTHORITY["EPSG","9001"]],PROJECTION["Lambert_Conformal_Conic_2SP"],PARAMETER["standard_parallel_1",42.68333333333333],PARAMETER["standard_parallel_2",41.71666666666667],PARAMETER["latitude_of_origin",41],PARAMETER["central_meridian",-71.5],PARAMETER["false_easting",200000],PARAMETER["false_northing",750000],AUTHORITY["EPSG","26986"],AXIS["X",EAST],AXIS["Y",NORTH]]'


parse(firstProjection)