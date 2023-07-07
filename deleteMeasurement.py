from ripe.atlas.cousteau import AtlasStopRequest



ATLAS_API_KEY = "0712dd3e-dcf7-4d88-8da2-bb4848765bdb"
def deleteMeasurement(msmid):
    atlas_request = AtlasStopRequest(msm_id=msmid, key=ATLAS_API_KEY)

    (is_success, response) = atlas_request.create()
    print(is_success, response)


#deleteMeasurement(53144724)
#deleteMeasurement(53119940)
#deleteMeasurement(53119941)