# LatencyRipeAtlasTestapp
Application to import Testruns from Ripe Atlas to Postgressql DB for further analysis

Usage (no parameters requiered):

<code> python LatencyRipeAtlasTestapp.py </code>

Input must be defined in INPUT.xlsx (see sample)
Measurements can be found here (public or your own ones): https://atlas.ripe.net/measurements/

![image](https://user-images.githubusercontent.com/15867392/169769409-3b18aa40-b520-4d35-a598-aa0e6b9e899c.png)

NOTE: currently we just support PING!

if your output looks like this:

![image](https://user-images.githubusercontent.com/15867392/169769576-a515e3cf-076a-405a-833b-951f9dc88d73.png)

everyting should work properly :-)

## TODO:
- remove password from src
- add support for TRACEROUTE
- add support for TCP
