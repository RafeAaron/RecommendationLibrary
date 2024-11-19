#Users Class
from record import History
import json

class User:

    def __init__(self, id:str, history:History = None):
        self.id = name

        if history == None:
            self.history:History = []
        else:
            self.history:History = history.getHistory()

    def addToHistory(self, data:list):
        self.history.addToHistory(data)

    def deleteFromHistory(self, id:str, category:str=None):
        self.history.deleteRecordHistory(id, category)

    def searchInHistory(self, id:str, category:str):
        self.history.searchForRecordInHistory(id, category)

    def objectToDict(self):
        return {"user": {"id": self.id, "history": self.history.objectToDict()}}
    
    def toJSON(self):
        return json.dumps(self.objectToDict())
