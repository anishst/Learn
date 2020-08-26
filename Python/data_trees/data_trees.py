# https://medium.com/swlh/making-data-trees-in-python-3a3ceb050cfd

Families = {'Peter':'Paul', 'Jim':'Tommy', 'Carlos':'Diego'}
for Parent, Son in Families.items():
  print(f"{Parent} is {Son}'s Dad")

print("\n","*"*100 )
Families = {'Peter':['Paul','Patty'], 'Jim':['Tommy','Timmy','Tammy'], 'Carlos':['Diego']}
for Parent, Children in Families.items():
        print(f"{Parent} has {len(Children)} kid(s):" )
        print(f"{', and '.join([str(Child) for Child in [*Children]])}")

# Reduced/Alternative way of saying the same without thing formatting:
for Parent, Children in Families.items():
        print(str(Parent) + ' has ' + str(len(Children)) + ' kid(s):')
        print(*Children)

# Dictionary (once more this is a forest of 3 trees:)
Families = {
            'Peter':
                   {'Paul':{'Dog','Toucan'} ,
                    'Patty': {'Turtle'}},
            'Jim':
                   {'Tommy':{'Hamster'},
                    'Timmy':{'Hamster'},
                    'Tammy':{'Hamster'}},
            'Carlos':
                   {'Diego':{'Cat','Ferret','Fox'}}
            }
for Parent, Children in Families.items():
        print(f"{Parent} has {len(Children)} kid(s):" )
        print(f" {', and '.join([str(Child) for Child in [*Children]])}")
        for Child, pets in Children.items():
            print(f"  {Child} has {len(pets)} pet(s):")
            print(f"    {', and '.join([str(pet) for pet in [*pets]])}")

# using classes

"""Barebones minimal general Tree & Node, using lists, but can also use dictionaries if you need key value pairs"""
class Tree():
    def __init__(self,root):
        self.root = root
        self.children = []
    def addNode(self,obj):
        self.children.append(obj)
class Node():
    def __init__(self, data):
        self.data = data
        self.children = []
    def addNode(self,obj):
        self.children.append(obj)
# USAGE:
FunCorp =  Tree('Head Honcho') # Create a tree and add root data.
print(FunCorp.root) # ask the Tree for it's root.
# Add children to root:
FunCorp.addNode(Node('VP of Stuff'))
FunCorp.addNode(Node('VP of Shenanigans'))
FunCorp.addNode(Node('VP of Hootenanny'))
# Get children of root:
print(f'C suite: {", ".join(str(child.data) for child in FunCorp.children)}')
# Add Node to the first child of the Tree:
FunCorp.children[0].addNode(Node('General manager of Fun'))
# Get the first child of the first child of the Tree:
print(f'The position under {FunCorp.children[0].data} is: {FunCorp.children[0].children[0].data}')


# ===
"""Barebones general Tree & Node"""
class Tree():
    def __init__(self,root):
        self.root = root
        self.children = []
        self.Nodes = []
    def addNode(self,obj):
        self.children.append(obj)
    def getAllNodes(self):
        self.Nodes.append(self.root)
        for child in self.children:
            self.Nodes.append(child.data)
        for child in self.children:
            if child.getChildNodes(self.Nodes) != None:
                child.getChildNodes(self.Nodes)
        print(*self.Nodes, sep = "\n")
        print('Tree Size:' + str(len(self.Nodes)))
class Node():
    def __init__(self, data):
        self.data = data
        self.children = []
    def addNode(self,obj):
        self.children.append(obj)
    def getChildNodes(self,Tree):
        for child in self.children:
            if child.children:
                child.getChildNodes(Tree)
                Tree.append(child.data)
            else:
                Tree.append(child.data)
# Add a bunch of nodes
FunCorp =  Tree('Head Honcho')
FunCorp.addNode(Node('VP of Stuff'))
FunCorp.addNode(Node('VP of Shenanigans'))
FunCorp.addNode(Node('VP of Hootenanny'))
FunCorp.children[0].addNode(Node('General manager of Fun'))
FunCorp.children[1].addNode(Node('General manager Shindings'))
FunCorp.children[0].children[0].addNode(Node('Sub manager of Fun'))
FunCorp.children[0].children[0].children[0].addNode(Node('Employee of the month'))
# Get all nodes (unordered):
FunCorp.getAllNodes()