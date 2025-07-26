import ctypes

# we will create our own dynamic array, not by using python list types but by using C array types

# 1. Creating List
class mylist:
    def __init__(self):
        self.size = 1 # the size of array
        self.n = 0 # the element inside array
        # creating a C type array with size = self.size
        self.A = self.__create_array(self.size)

#2. length property
    def __len__(self):
        return self.n

#3. append
    def append(self, item):
        print("item", item)
        if self.n == self.size:
            # resizing here
            self.__resize(self.size * 2)

        self.A[self.n] = item
        self.n = self.n + 1

    def __resize(self, new_capacity):
      temp =  self.__create_array(new_capacity)
      print("temp", temp)
      self.size = new_capacity
        # now copying the older array content into new_capacity
      for i in range(self.n):
          temp[i] = self.A[i]
          # re-assigning A
      self.A = temp
      print("self.A", self.A)

# 4. string
    def __str__(self):
        print("self.A------------", self.A)
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'


#5. Indexing
    def __getitem__(self,i):
        if 0 < i < self.n:
            return self.A[i]
        else:
            return '@Error, index out of range'

#6. pop
    def pop(self):
        if self.n == 0:
            return []
        else:
            print("@last element => ", self.A[self.n-1])
            self.n = self.n - 1
            return self

    def clear(self):
         self.n = 0
         self.size = 1


    def __create_array(self, capacity):
        return (capacity * ctypes.py_object)()

L = mylist()





print("1. printing class mylist =>", L)
print("1.2. type =>", type(L))

#2.
print("2. len =>",len(L))

#3. Append
L.append("Apple")
L.append(True)
L.append(2025)
print("3.1 append operation 1 with len =>",len(L))
L.append("Samsung")
L.append(False)
L.append(2024)
print("3.2 append operation 2 with len =>",len(L))


print("4. printing after append =>", L)


print("5.1 indexing in scope =>", L[2], " -- current length =>", len(L))
scope = 200
print(f"5.2. indexing out of scope index:{scope} =>", L[scope], " -- current length =>", len(L))


print("6. current list before pop =>", L)
L.pop()
print("6.1 pop =>", L)
L.pop()
print("6.2 pop =>", L)
L.pop()
print("6.3 pop =>", L)
L.pop()
print("6.4 pop =>", L)
L.pop()
print("6.5 pop =>", L)
L.pop()
print("6.6 pop =>", L)
L.pop()
print("6.7 pop =>", L)

L.append("Tesla")
L.append("Microsoft")
L.append(2024)

L.clear()
print("6.8=>", L)
