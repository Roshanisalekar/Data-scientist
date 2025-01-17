                 set method 


(1) add()	: 	Adds an element to the set.

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

(2) clear()  : The clear() method removes all elements in a set.

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

(3) copy() : The copy() method copies the set.

fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)

(4) difference()	-  :	Returns a set containing the difference between two or more sets

x = {"apple", "banana", "cherry"}

y = {"google", "microsoft", "apple"}

z = x.difference(y) 

print(z)

(5) difference_update()	-=  : 	Removes the items in this set that are also included in another, specified set

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y) 

print(x)

(6) intersection()	&	: Returns a set, that is the intersection of two other sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) 

print(z)

(7) intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)

(8) pop () : 

The pop() method removes a random item from the set.

This method returns the removed item.

fruits = {"apple", "banana", "cherry"}

fruits.pop() 

print(fruits)

(9) remove () : The remove() method removes the specified element from the set.

fruits = {"apple", "banana", "cherry"}

fruits.remove("banana") 

print(fruits)

(10)  union()	| : Return a set containing the union of sets

x = {"apple", "banana", "cherry"}

y = {"google", "microsoft", "apple"}

z = x.union(y) 

print(z)

(11) update()	|=  : 	Update the set with the union of this set and others

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y) 

print(x)




