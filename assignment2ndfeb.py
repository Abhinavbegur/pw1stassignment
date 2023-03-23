# 1) ans:immutable,ordered,indexable,iterable and yes tuple is immutable

# 2)ans : tuple methods are as follows 1.count, 2.index
#example for count
a = (1,2,2,2,2,3,3,3,444,444,5,6)
X = a.count(2)
print(X)
#example for index
b = ("a","b","c","d")
x1 =b.index("b")
print(x1)
#since tuples are imuutable and list are mutable thats why tuples have 2 built in function

# 3) ans: sets are datatypes in python which don't allow duplicates,set is unordered collection of unique element.
#example 
my_set = {1,2,2,3,4,5,8,8,9,4,9}
print(my_set)

# 4)ans :union()returns a new set without modifying the orginal set,while update() modify the orginal set by adding the elements of the specified sets
#update() methodmodifies the orginal set by adding all the unique element from another set
#example for union
set1 ={1,21,3,4}
set2 ={1,3,4,5}
set3 = set1.union(set2)
print(set3)
#example for updaste
set4 ={1,2,3,}
set5 ={2,3,4}
a1 =set4.update(set5)
print(a1)

#5)ans :dictionary is unordered collection of key & values
a2 ={"fruits": "mango" "apple" "grapes", "vegetables": "tomato" "brinjal"}
print(a2)

#6)ans: yes,we can create a nested dictionary.
a3 = {"sehb":{"colour": "red","taste":"sweet"}}
print(a3["sehb"]["taste"])

#7)ans:
dict1 = {"language":"python","course":"data sceience master"}
print(dict1.setdefault("topics",["python","machinelearning","deeplearning"]))

#8)ans:the three view objects in dictionary are:(a)keys,(b)values,(items)
dict2 = {"sports": "cricket","teams":["india","australia","england","soouthafrica","srilanka","newzeland"]}
keyveiws = dict2.keys()
print(keyveiws)
valuesview = dict2.values()
print(valuesview)
itemsview =dict2.items()
print(itemsview)
