from api.models import Model

model = Model()

def algorithms(event):
    if event["type"] == "IncidentOccurred":
        if event["incident_id"] in model.Incidents:
            model.Incidents[event["incident_id"]] = {
                "codeName": event["codeName"],
                "loc": {
                    "x": event["loc"]["x"],
                    "y": event["loc"]["y"]
                },
                "is_resolved": False
            }
    elif event["type"] == "IncidentResolved":
        if event["incident_id"] in model.Incidents:
            model.Incidents[event["incident_id"]]["is_resolved"] = True
    elif event["type"] == "OfficerGoesOnline":
        if event["officer_id"] in model.Officers:
            model.Officers[event["officerId"]]["is_online"] = True
            model.Officers[event["officerId"]]["badgeName"] = True
    elif event["type"] == "OfficerLocationUpdated":
        if event["officer_id"] in model.Officers:
            model.Officers[event["officerId"]]["loc"] = event["loc"]
    elif event["type"] == "OfficerGoesOffline":
        if event["officer_id"] in model.Officers:
            model.Officers[event["officerId"]]["is_online"] = False
    else:
        raise Exception("Can not recognize event")
    #TODO
    pass


def mapping_event(ch, method, properties, event):
    return algorithms(event)