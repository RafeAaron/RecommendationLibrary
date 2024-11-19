import sys

sys.path.append("/Users/rafeaaron/Desktop/RecommendationLibrary/src")
print(sys.path)

from recommendationengine import recommendationengine
from recommendationengine import storageengine
from recommendationengine import filteringengine

def main():
    storage = storageengine.StorageEngine("./src/test/data.json")
    filter = filteringengine.FilteringEngine()
    recommendationSystem = recommendationengine.RecommendationEngine()

    #storage.viewCategoriesOfStoredData()
    #print(storage.returnDataInCategory("songs"))
    #print(storage.returnDataInCategory("Ziki"))
    #print(filter.doesLabelExist("Titles", storage.returnDataInCategory("movies")))
    #print(storage.saveData("savedRecords.json"))

    mydata = storage.returnDataInCategory("movies") + storage.returnDataInCategory("songs") + storage.returnDataInCategory("notifications")

    for value in filter.getRecordsWithLabels(["Title", "Message"], mydata):
        print(value)



if __name__ == '__main__':
    main()
