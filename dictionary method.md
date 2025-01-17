                        dictionary method 


(1) clear() : The clear() method removes all the elements from a dictionary.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)


(2) copy() :  The copy() method returns a copy of the specified dictionary.

 car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()

print(x)

(3) fromkeys () : The fromkeys() method returns a dictionary with the specified keys and the specified value.

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)


print(thisdict)

(4) get () :  The get() method returns the value of the item with the specified key.

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

(5) items() : The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

The view object will reflect any changes done to the dictionary


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)

(6) keys() :	Returns a list containing the dictionary's keys

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)

(7) values() :	Returns a list of all the values in the dictionary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)


(8) pop() :  pop()	Removes the element with the specified key

The pop() method removes the specified item from the dictionary.

The value of the removed item is the return value of the pop() method

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)

(10)popitem() :	Removes the last inserted key-value pair

 car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)


(11) setdefualt () :

setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

The setdefault() method returns the value of the item with the specified key.

If the key does not exist, insert the key, with the specified value

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "White")

print(x)
print(car)

(12) update()	:  Updates the dictionary with the specified key-value pairs

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

