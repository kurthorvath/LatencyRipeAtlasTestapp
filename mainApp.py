from createMeasurement import *
from deleteMeasurement import *
from Node import *

from datetime import datetime
from ripe.atlas.cousteau import (
  Ping,
  Traceroute,
  AtlasSource,
  AtlasCreateRequest
)


def procTask(src, dst):
    #return createFullMeasure(src, dst)
    return createICMPv4TOip(src, dst)

storage = IOwrapper("inp.xlsx")
storage.addNode(Node("Arnes","si-lju-as2107.anchors.atlas.ripe.net", 6861, "193.2.63.12","2001:1470:8000:603::12"))
storage.addNode(Node("Anexia","at-klu-as42473.anchors.atlas.ripe.net", 6120, "178.255.156.202","2a00:11c0::1:0:0:3e"))
#storage.addNode(Node("BIX","hu-bud-as12303.anchors.atlas.ripe.net", 6039, "5.28.0.17","2a00:e6a0:3:1011"))

storage.addNode(Node("Feldkirchen-oja","", 52690, "77.220.115.19",""))
#storage.addNode(Node("Villach-net4you","", 15439, "5.28.0.17","194.177.153.171")) #AS6798
#storage.addNode(Node("Hermagor-NETcompany ","", 50074, "185.56.124.18","")) #AS50226


for src in storage.nodes:
    for dst in storage.nodes:
        if src.name is not dst.name:
            print('map: ', src.name, dst.name)
            stat, resp = procTask(src, dst)
            print("Result: ", stat, "Resp:", resp)
            storage.storeSeries(resp['measurements'], storage.nodes[0], storage.nodes[1])
            storage.storeResultsJsonFile('test.json')

#stat, resp = procTask(storage.nodes[0], storage.nodes[1])
#stat = True
#resp = [1,2,3,4,5,6]
#print("Result: ", stat, "Resp:", resp)
#storage.storeSeries(resp['measurements'],storage.nodes[0], storage.nodes[1])
#storage.storeResultsJsonFile('test.json')

exit()


