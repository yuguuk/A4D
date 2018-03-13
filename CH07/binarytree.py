from bintrees import BinaryTree

data = {3:'White', 2:'Red', 1:'Green', 5:'Orange', 4:'Yellow', 7:'Purple', 0:'Magenta'}

tree = BinaryTree(data)
tree.update({6: 'Teal'})

def displayKeyValue(key, value):
    print('Key: ', key, ' Value: ', value)

tree.foreach(displayKeyValue)
print('Item 3 contains: ', tree.get(3))
print('The maximum item is: ', tree.max_item())
