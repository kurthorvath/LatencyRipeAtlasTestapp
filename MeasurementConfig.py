class MeasurementConfig:
  def __init__(self, filename):
    self.filename = filename


  def print(self):
    print("Node: ", self.name, self.fqdn, self.id, self.ipv4, self.ipv6)