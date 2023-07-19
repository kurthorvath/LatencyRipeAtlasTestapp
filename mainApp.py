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
storage.addNode(Node("University of Klagenfurt","", 6827, "143.205.170.32",""))
storage.addNode(Node("Anexia","", 6120, "178.255.156.202",""))
storage.addNode(Node("Carinthia Univ. of App. Sciences","", 7046, "194.182.186.87",""))
storage.addNode(Node("ip-it consult GmbH","", 6354, "194.93.76.42",""))
storage.addNode(Node("Netcompany","", 50074, "185.56.124.18",""))
storage.addNode(Node("OJA","", 1004905, "195.16.241.142",""))
storage.addNode(Node("net4you","", 15476, "194.177.155.138",""))
storage.addNode(Node("HTL Klagenfurt","", 50397, "193.36.189.35",""))
storage.addNode(Node("Kelag","", 6827, "217.75.176.17",""))
storage.addNode(Node("FH Kaernten","", 1853, "193.171.127.9",""))

storage.addNode(Node("Feldkirchen-oja","", 52690, "77.220.115.19",""))
storage.addNode(Node("Villach-net4you","", 15439, "5.28.0.17","194.177.153.171")) #AS6798
storage.addNode(Node("Hermagor-NETcompany","", 50074, "185.56.124.18","")) #AS50226

#storage.addNode(Node("PCH Quad9","", 0, "149.112.112.112",""))
#storage.addNode(Node("D.root OCH","", 0, "199.7.91.13","")) #AS6798
#storage.addNode(Node("J.root by verisign","", 0, "192.58.128.30","")) #AS50226

storage.addNode(Node("Arnes","", 6861, "193.2.63.12",""))
storage.addNode(Node("6connect","", 7056, "67.221.244.87",""))
storage.addNode(Node("ublox","", 6895, "185.215.195.14",""))
storage.addNode(Node("Google Frankfurt","", 6708, "34.89.240.90",""))
storage.addNode(Node("Switch Zuerich","", 6317, "130.59.80.2",""))
storage.addNode(Node("BIX","", 6039, "5.28.0.17",""))


#for src in storage.nodes:
src = Node("Hermagor-NETcompany","", 50074, "185.56.124.18","")
#src = Node("Villach-net4you","", 15439, "5.28.0.17","194.177.153.171")
for dst in storage.nodes:
        if src.name is not dst.name:
            print('map: ', src.name,' / ' ,dst.name)
            stat, resp = procTask(src, dst)
            print("Result: ", stat, "Resp:", resp)
            if stat is True:
                storage.storeSeries(resp['measurements'], src,dst)
                storage.storeResultsJsonFile('test1.json')
            else:
                print("!!!! ERROR on create new measurements", resp)

dst = Node("Hermagor-NETcompany","", 50074, "185.56.124.18","")
for src in storage.nodes:
        if src.name is not dst.name:
            print('map: ', src.name,' / ' ,dst.name)
            stat, resp = procTask(src, dst)
            print("Result: ", stat, "Resp:", resp)
            if stat is True:
                storage.storeSeries(resp['measurements'], src,dst)
                storage.storeResultsJsonFile('test1.json')
            else:
                print("!!!! ERROR on create new measurements", resp)
#stat, resp = procTask(storage.nodes[0], storage.nodes[1])
#stat = True
#resp = [1,2,3,4,5,6]
#print("Result: ", stat, "Resp:", resp)
#storage.storeSeries(resp['measurements'],storage.nodes[0], storage.nodes[1])
#storage.storeResultsJsonFile('test.json')

exit()


