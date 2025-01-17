                          list method

(1) append ()  : The append() method appends an element to the end of the list.

example :

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)

(2) clear () : The clear() method removes all the elements from a list.

example :

fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)

(3) copy () : The copy() method returns a copy of the specified list.

exaple :

fruits = ["apple", "banana", "cherry"]

x = fruits.copy()

print(x)


(4) count () : Returns the number of elements with the specified value.

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)

print(x)

(5) extend()  : The extend() method adds the specified list elements (or any iterable) to the end of the current list.

example : 

fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)

print(fruits)

(6) index() : The index() method returns the position at the first occurrence of the specified value.

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)


(7) insert () : The insert() method inserts the specified value at the specified position.


Parameter	Description
position  :	Required. A number specifying in which position to insert the value
element   :	Required. An element of any type (string, number, object etc.)The pop() method removes the element at the specified position.

fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)

(8)  pop ()  : The pop() method removes the element at the specified position.

Parameter	Description
pos	Optional : A number specifying the position of the element you want to remove, default value is -1, which returns the last item

fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)

print(x)

print(fruits)


(9) remove () : The remove() method removes the first occurrence of the element with the specified value.

fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)


(10) reverse ()  : The reverse() method reverses the sorting order of the elements.

fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)

(11) sort () : The sort() method sorts the list ascending by default.

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)

                
