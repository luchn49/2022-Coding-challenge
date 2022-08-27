import json
import os

import config


class Model():
    def __init__(self):

        self.Officers = {}
        self.Incidents = {}
        self.OfficersIncidents = {}
        self._init_data("officers")
        self._init_data("incidents")
        self._init_data("officers_incidents")

    def _init_data(self, table):
        if table == "officers":
            if not self.Officers:
                with open(os.path.join(config.DATABASE, "Officers.json")) as file:
                    self.Officers = json.load(file)
        elif table == "incidents":
            if not self.Incidents:
                with open(os.path.join(config.DATABASE, "Incidents.json")) as file:
                    self.Incidents = json.load(file)
        elif table == "officers_incidents":
            if not self.OfficersIncidents:
                with open(os.path.join(config.DATABASE, "OfficersIncidents.json")) as file:
                    self.OfficersIncidents = json.load(file)
        else:
            raise Exception("Not found table")

    def get_data(self, table):
        if table == "officers":
            return self.Officers
        elif table == "incidents":
            return self.Incidents
        elif table == "officers_incidents":
            return self.OfficersIncidents
        else:
            raise Exception("Not found table")

    def search(self, table, obj_id):
        if table == "officers":
            return self.Officers.get(obj_id)
        elif table == "incidents":
            return self.Incidents.get(obj_id)
        elif table == "officers_incidents":
            return self.OfficersIncidents.get(obj_id)
        else:
            raise Exception("Not found table")

    def update_table(self, table, obj_id, value):
        if table == "officers":
            if obj_id in self.Officers:
                self.Officers[obj_id] = value
        elif table == "incidents":
            if obj_id in self.Incidents:
                self.Incidents[obj_id] = value
        elif table == "officers_incidents":
            if obj_id in self.OfficersIncidents:
                self.OfficersIncidents[obj_id] = value
        else:
            raise Exception("Not found table")

    def save(self, table):
        if table == "officers":
            with open("Officers.json", "w") as file:
                json.dump(self.Officers, file)
        elif table == "incidents":
            with open("incidents.json", "w") as file:
                json.dump(self.Incidents, file)
        elif table == "officers_incidents":
            with open("Officersincidents.json", "w") as file:
                json.dump(self.OfficersIncidents, file)
        else:
            raise Exception("Not found table")




