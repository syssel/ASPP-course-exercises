# Exercises for Day 3
Numpy and inheritance

## 1. Numpy exercises

#### a. Create a null vector of size 10 but the fifth value which is 1
```python
x = np.zeros(10)
x[4] = 1
```

#### b. Create a vector with values ranging from 10 to 49
```python
x = np.arange(10, 50) 
```

#### c. Reverse a vector (first element becomes last) 
```python
x = x[::-1]
```

#### d. Create a 3x3 matrix with values ranging from 0 to 8
```python
x = np.arange(0,9).reshape((3,3))
```

#### e. Find indices of non-zero elements from [1,2,0,0,4,0]
```python
x = np.array([1,2,0,0,4,0])
non_zero = x>0
```

#### f. Create a random vector of size 30 and find the mean value
```python
m = np.mean(np.random.random(30))
```

#### g. Create a 2d array with 1 on the border and 0 inside
```python
x = np.zeros((5,5))
x[(0, -1),:] = 1
x[:, (0, -1)] = 1
```

#### h. Create a 8x8 matrix and fill it with a checkerboard pattern
```python
n=8
board = np.zeros((n,n))
for start in range(0,2):
    for i in range(start, n, 2): 
        board[start::2,i] = 1

```

#### i. Create a checkerboard 8x8 matrix using the tile function
```python
n=8
board = np.tile([1,0], int(n*n/2)).reshape((n,n))
board[np.arange(1,n,2),:] = np.flip(board[np.arange(1,n,2),:], axis=1)
```

#### j. Given a 1D array, negate all elements which are between 3 and 8, in place
```python
Z = np.arange(11)
Z[np.logical_and(Z>3, Z<8)]*=-1
print(Z)
```

#### k. Create a random vector of size 10 and sort it
```python
Z = np.random.random(10)
Z.sort()
print(Z)
```

#### l. Consider two random array A anb B, check if they are equal
```python
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.all(A==B)
print(equal)
```

#### m. How to convert an integer (32 bits) array into a float (32 bits) in place?
```python
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = Z.view("float32")
print(Z.dtype)
```

#### n. How to get the diagonal of a dot product?
```
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diagonal(C)
print(D)
```

## 2. Speed optimization using Numpy
Revisit the ```matmult.py``` example from yesterday and improve its performance using Numpy.

## 3. Examples on classes and inheritance in Python

#### a. Create a "Person" class which takes firstname and lastname as arguments to the constructor (```___init___```) and define a method that returns the full name of the person as a combined string.
```python
class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def name(self):
        return ", ".join([self.firstname.capitalize(), self.lastname.capitalize()])
```

#### b. Create a "Student" class which inherits from the "Person" class, takes the subject area as an additional argument to the constructor and define a method that prints the full name and the subject area of the student.
```python
class Student(Person):
    def __init__(self, firstname, lastname, subject):
        super(Student, self).__init__(firstname, lastname)
        self.subject = subject
    def info(self):
        return self.name()+" studies "+self.subject
```

#### c. You should be able now to use your "Student" class like this:
```
In [1]: from classroom import Student
In [2]: me = Student('Benedikt', 'Daurer', 'physics') 
In [3]: me.info() 
Benedikt Daurer studies physics
```

#### d. Create a "Teacher" class which also inherits from "Person", takes the name of the course (e.g. Python programming) as an argument and define a method that prints the full name of the teacher and the course he teaches. 
```python
class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        super(Teacher, self).__init__(firstname, lastname)
        self.course = course  
    def info(self):
        return self.name()+" teaches "+self.course
```