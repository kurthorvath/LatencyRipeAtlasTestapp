from datetime import datetime, timedelta
from ripe.atlas.cousteau import (
  Ping,
  Http,
  Ntp,
  Sslcert,
  Dns,
  Traceroute,
  AtlasSource,
  AtlasCreateRequest
)

ATLAS_API_KEY = "0712dd3e-dcf7-4d88-8da2-bb4848765bdb"



def createFullMeasure(src, dst):
    print("create new series...")
    AS = AtlasSource(
        type="probes",
        value=src.id,
        requested=5
    )

    pingv4 = Ping(af=4, target=dst.fqdn, description="PINGv4 "+src.name+" to "+dst.name )
    httpv4 = Http(af=4, target=dst.fqdn, description="HTTPv4 " + src.name + " to " + dst.name)
    ntpv4 = Ntp(af=4, target=dst.fqdn, description="NTPv4 " + src.name + " to " + dst.name)
    Sslcertv4 = Sslcert(af=4, target=dst.fqdn, description="SslCertv4 " + src.name + " to " + dst.name)
    dnsv4 = Dns(af=4, target=dst.fqdn, query_class='IN' ,query_type='A',query_argument="google.com",description="DNSv4 " + src.name + " to " + dst.name)
    traceroutev4 = Traceroute(af=4, target=dst.fqdn, description="TRACEv4 "+src.name+" to "+dst.name, protocol="ICMP")

    pingv6 = Ping(af=6, target=dst.fqdn, description="PINGv6 " + src.name + " to " + dst.name)
    httpv6 = Http(af=6, target=dst.fqdn, description="HTTPv6 " + src.name + " to " + dst.name)
    ntpv6 = Ntp(af=6, target=dst.fqdn, description="NTPv6 " + src.name + " to " + dst.name)
    Sslcertv6 = Sslcert(af=6, target=dst.fqdn, description="SslCertv6 " + src.name + " to " + dst.name)
    dnsv6 = Dns(af=6, target=dst.fqdn, query_class='IN', query_type='A', query_argument="google.com",
                description="DNSv6 " + src.name + " to " + dst.name)
    traceroutev6 = Traceroute(af=6, target=dst.fqdn, description="TRACEv6 " + src.name + " to " + dst.name,
                              protocol="ICMP")

    atlas_request = AtlasCreateRequest(
        start_time=datetime.utcnow(),
        stop_time=datetime.utcnow()+timedelta(days=8),
        key=ATLAS_API_KEY,
        measurements=[dnsv4, pingv4, traceroutev4, httpv4, ntpv4, Sslcertv4, dnsv6, pingv6, traceroutev6, httpv6, ntpv6, Sslcertv6],
        sources=[AS]
        #is_oneoff=True
    )

    (is_success, response) = atlas_request.create()
    return is_success, response


def createICMPv6TOip(src, dst):
    print("create new series...")
    AS = AtlasSource(
        type="probes",
        value=src.id,
        requested=5
    )

    pingv6 = Ping(af=6, target=dst.ipv6, description="PINGv6 "+src.name+" to "+dst.name )

    atlas_request = AtlasCreateRequest(
        start_time=datetime.utcnow(),
        stop_time=datetime.utcnow()+timedelta(days=8),
        key=ATLAS_API_KEY,
        measurements=[pingv6],
        sources=[AS]
        #is_oneoff=True
    )

    (is_success, response) = atlas_request.create()
    return is_success, response

def createICMPv4TOip(src, dst):
    print("create new series...:", src, dst)
    AS = AtlasSource(
        type="probes",
        value=src.id,
        requested=5
    )

    pingv4 = Ping(af=4, target=dst.ipv4, description="PINGv4 "+src.name+" to "+dst.name )

    atlas_request = AtlasCreateRequest(
        start_time=datetime.utcnow(),
        stop_time=datetime.utcnow()+timedelta(hours=1),
        key=ATLAS_API_KEY,
        measurements=[pingv4],
        sources=[AS]
        #is_oneoff=True
    )

    (is_success, response) = atlas_request.create()
    return is_success, response







