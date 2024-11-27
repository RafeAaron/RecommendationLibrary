import sys

sys.path.append("/home/rafeaaron/Desktop/RecommendationLibrary/src")
print(sys.path)

from recommendationengine import recommendationengine
from recommendationengine import storageengine
from recommendationengine import filteringengine

def main():
    storage = storageengine.StorageEngine("./test/Data/data.json")
    filter = filteringengine.FilteringEngine()

    mydata = storage.returnDataInCategory("movies") + storage.returnDataInCategory("songs") + storage.returnDataInCategory("notifications")

    for value in mydata:
        print(value)



if __name__ == '__main__':
    main()
