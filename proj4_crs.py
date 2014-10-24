import re
import json

def testWKT(code):
    sumCode = 0
    codeWords = ['GEOGCS','GEOCCS','PROJCS','LOCAL_CS']
    for w in codeWords:
        sumCode += 1 + code.find(w)
    return sumCode

def extend(destination, source):
    if not destination:
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
    

def sExpr(v, obj):
    if not isinstance(v, List):
        obj[v] = True
        return
    else:
        key = v[0]
        v = v[1:]
        if key == 'PARAMETER':
            key = v[0]
            v = v[1:]
        if len(v) == 1:
            if isinstance(v[0], List):
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
                    'name': v[0].lower()
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
                mapit(obj, key, v)
            else:
                allItemList = True 
                for item in v:
                    if not isinstance(item, List):
                        allItemList = False
                        break
                if allItemList:
                    mapit(obj, key, v)
                else:
                    sExpr(v, obj[key])

def rename(obj, params):
  outName = params[0]
  inName = params[1]
  if !(outName in obj) && (inName in obj):
    obj[outName] = obj[inName]
    if params.length === 3:
      obj[outName] = params[2](obj[outName])

def cleanWKT(wkt):
    if wkt["type"] == 'GEOGCS':
        wkt["projName"] = 'longlat'
    elif wkt["type"] == 'LOCAL_CS':
        wkt["projName"] = 'identity'
        wkt["local"] = True
    else:
        if isinstance(wkt['PROJECTION'] == dict):
            wkt["projName"] = wkt["PROJECTION"].keys()[0]
        else:
            wkt['projName'] = wkt['PROJECTION'];

    if wkt['UNIT']:
        wkt['units'] = wkt['UNIT']['name'].lower()
        if wkt['units'] == 'metre':
            wkt['units'] = 'meter'
        if wkt['UNIT']['convert']:
            wkt['to_meter'] = parseFloat(wkt['UNIT']['convert'], 10)

    if wkt['GEOGCS']:
        if wkt['GEOGCS']['DATUM']:
            wkt['datumCode'] = wkt['GEOGCS']['DATUM']['name'].lower()
        else:
            wkt['datumCode'] = wkt['GEOGCS']['name'].lower()

        if wkt['datumCode'].slice(0, 2) == 'd_':
            wkt['datumCode'] = wkt['datumCode'].slice(2)

        if wkt['datumCode'] == 'new_zealand_geodetic_datum_1949' or wkt['datumCode'] == 'new_zealand_1949':
            wkt['datumCode'] = 'nzgd49'

        if wkt['datumCode'] == "wgs_1984":
            if wkt['PROJECTION'] == 'Mercator_Auxiliary_Sphere':
                wkt['sphere'] = True
            wkt['datumCode'] = 'wgs84';

        if wkt['datumCode'].slice(-6) == '_ferro':
            wkt['datumCode'] = wkt['datumCode'].slice(0, - 6)

        if wkt['datumCode'].slice(-8) == '_jakarta':
            wkt['datumCode'] = wkt['datumCode'].slice(0, - 8)

        if ~wkt['datumCode'].indexOf('belge'):
            wkt['datumCode'] = "rnb72"

        if wkt['GEOGCS']['DATUM'] and wkt['GEOGCS']['DATUM']['SPHEROID']:
            wkt["ellps"] = wkt['GEOGCS']['DATUM']['SPHEROID']['name'].replace('_19', '').replace(/[Cc]larke\_18/, 'clrk')
            if wkt["ellps"].toLowerCase().slice(0, 13) === "international":
                wkt["ellps"] = 'intl'

            wkt["a"] = wkt['GEOGCS']['DATUM']['SPHEROID']['a']
            wkt["rf"] = parseFloat(wkt['GEOGCS']['DATUM']['SPHEROID']['rf'], 10)

        if wkt['datumCode'].indexOf('osgb_1936'):
            wkt['datumCode'] = "osgb36"

    if wkt["b"] and !isFinite(wkt["b"]): # not number
        wkt["b"] = wkt["a"]

    def toMeter(input):
        ratio = wkt['to_meter'] || 1
        return parseFloat(input, 10) * ratio

    def renamer(a):
        return rename(wkt, a)

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
        _list[i] = renamer[item]

    if not wkt.long0 and wkt.longc and \
        (wkt['PROJECTION'] == 'Albers_Conic_Equal_Area' or wkt['PROJECTION'] == "Lambert_Azimuthal_Equal_Area"):
        wkt.long0 = wkt.longc
 
def wkt(code):
    wkt = "," + code
    wkt = re.sub(r'\s*\,\s*([A-Z_0-9]+?)(\[)', r',["\1",', wkt)[1:]
    wkt = re.sub(r'\s*\,\s*([A-Z_0-9]+?)\]', r',"\1"]', wkt)
    lisp = json.loads(wkt)
    _type = lisp[0]
    _name = lisp[1]
    lisp = lisp[2:]
    lisp = ['output', 'type', _type, 'name', _name] + lisp
   
    obj = {}
    sExpr(lisp, obj)
    cleanWKT(obj["output"])
    return extend(self, obj["output"])
 
def parse(code):
    if testWKT(code):
        wkt(code)
