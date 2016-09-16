
import Node

myFile = open('Data\\dataSample.txt','r')

myString = myFile.readline()

myNode = Node.Node()
myNode.createFromString(myString)

print(myNode.name, '\n', myNode.vertices)
