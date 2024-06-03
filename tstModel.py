from model.model import Model

myModel =  Model()
myModel.buildGraph(60*60*1000)
print(myModel.getGraphDetails())