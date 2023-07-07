import json
class IOwrapper():
    def __init__(self, filename):
        self.filename = filename
        self.nodes = []
        self.output = []

    def addNode(self, newnode):
        self.nodes.append(newnode)

    def printAllNodes(self):
        for node in self.nodes:
            node.print()

    def storeSeries(self, listmsms, src, dst):
        prot = ['dnsV4', 'icmpV4', 'tracerouteV4', 'httpV4', 'ntpV4', 'SslcertV4',
                'dnsV6', 'icmpV6', 'tracerouteV6', 'httpV6', 'ntpV6', 'SslcertV6']
        ind = 0
        print(src.name, dst.name)
        for msm in listmsms:
            self.output.append({"srcId":src.id, "srcName": src.name, "dstId":dst.id, "dstName":dst.name, "type": prot[ind], "msmid": msm})
            ind = ind + 1

    def storeResultsJsonFile(self, filename):
        print("store results to file", filename)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.output, f, ensure_ascii=False, indent=4)

class Node:
  def __init__(self, name, fqdn,id, ipv4, ipv6):
    self.name = name
    self.fqdn = fqdn
    self.id = id
    self.ipv4 = ipv4
    self.ipv6 = ipv6

  def print(self):
    print("Node: ", self.name, self.fqdn, self.id, self.ipv4, self.ipv6)

#p1 = Node("John", 36, "195.58.160.2",None)