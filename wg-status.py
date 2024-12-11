#!/usr/bin/env python3
import json
import urllib.request
import sys

IGNORE_REGIONS = {"APAC": True , "AMER": True }
IGNORE_STATUS = { "operational": True }

data = urllib.request.urlopen("https://status.watchguard.com/api/v2/summary.json").read()
obj = json.loads(data)

# if you would like to use the local files: 
#obj = "" # initialize variable 
#with open("exampledata/outage/summary.json") as fh: 
#    obj = json.load(fh)

#print (obj)

# only use .components property : 
list = obj["components"]

# search all components: 
names = []
for component in list:
    name = component["name"]

    # regions are appended to names - separated by ":::"
    region = name[name.rindex(":")+1:len(name)]

    # ignore Regions from IGNORE_REGIONS
    if (IGNORE_REGIONS.get(region, False)): 
        continue

    # ignore (operational) status from IGNORE_STATUS
    if (IGNORE_STATUS.get(component["status"],False)): 
        continue

    # collect component-names:
    names.append(name)
    
# no errors -- no panic ;) 
if (len(names) == 0):
    print("OK All Components operational: https://status.watchguard.com")
    sys.exit(0)

failed = " ".join(names)
print("Error", failed , " https://status.watchguard.com")
sys.exit(2) # CRITICAL