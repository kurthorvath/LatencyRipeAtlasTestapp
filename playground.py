from createMeasurement import *
from deleteMeasurement import *
from Node import *
all = []
all.append(Node("Universität Klagenfurt","",
                6827, "143.205.170.32","143.205.170.32")),
all.append(Node("Anexia","at-klu-as42473.anchors.atlas.ripe.net",
                6120, "178.255.156.202","2a00:11c0::1:0:0:3e"))
all.append(Node("cuas","si-lju-as2107.anchors.atlas.ripe.net",
                7046, "194.182.186.87","2a04:c45:e00:64c2:4b9:78ff:fe00:982"))
all.append(Node("Arnes","si-lju-as2107.anchors.atlas.ripe.net",
                6861, "193.2.63.12","2001:1470:8000:603::12"))
all.append(Node("BIX","hu-bud-as12303.anchors.atlas.ripe.net",
                6039, "5.28.0.17","2a00:e6a0:3:1011"))

#S = Node("Arnes","si-lju-as2107.anchors.atlas.ripe.net", 6861, "193.2.63.12","2001:1470:8000:603::12")
#D = Node("Kurt","-", 1, "10.44.113.15","2001:4bb8:182:72a9:4569:ae9e:7528:d028")

#(is_success, response) = createICMPv6TOip(S, D)
#print(is_success, response)