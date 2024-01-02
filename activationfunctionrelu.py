import numpy as np

def ReLU(x):
  ReLU_x=max(0,x)
  return ReLU_x

def perceptron(x, w, b):
        """ Function implemented by a perceptron with weight vecto w and bias """
        v=np.dot(w,x)+b
        y=ReLU(v)
        return y

def NOT_percep(x):
      return perceptron(x, w=-1, b=0.5)

  # Test
print("NOT(0) = {}".format(NOT_percep(0.5)))
print("NOT(1) = {}".format(NOT_percep(10)))

def AND_percep(x):
  w = np.array([1, 1])
  b = -1.5
  return perceptron(x,w,b)

  # Test
example1 = np.array([10,1])
example2 = np.array([1,0])
example3 = np.array([0,1])
example4 = np.array([0,0])

print("AND({}, {}) = {}".format(1,1,AND_percep(example1)))
print("AND({}, {}) = {}".format(1,0,AND_percep(example2)))
print("AND({}, {}) = {}".format(0,1,AND_percep(example3)))
print("AND({}, {}) = {}".format(0,0,AND_percep(example4)))

def OR_percep(x):
    w = np.array([1,1])
    b = -0.5
    return perceptron(x, w, b)

#Test
example1 = np.array([1,1])
example2 = np.array([1,0])
example3 = np.array([0,1])
example4 = np.array([0,0])

print("OR({}, {}) = {}".format(1,1,OR_percep(example1)))
print("OR({}, {}) = {}".format(1,0,OR_percep(example2)))
print("OR({}, {}) = {}".format(0,1,OR_percep(example3)))
print("OR({}, {}) = {}".format(0,0,OR_percep(example4)))

def XOR_percep(x):
  output_AND = AND_percep(x)
  output_NOT = NOT_percep(output_AND)
  output_OR = OR_percep(x)
  x_temp = np.array([output_NOT, output_OR])
  output_AND = AND_percep(x_temp)
  return output_AND

#Test
example1 = np.array([10,1])
example2 = np.array([10,-5])
example3 = np.array([-10,-10])
example4 = np.array([1,-10])

print("XOR({}, {}) = {}".format(10,1,XOR_percep(example1)))
print("XOR({}, {}) = {}".format(10,-5,XOR_percep(example2)))
print("XOR({}, {}) = {}".format(-10,-10,XOR_percep(example3)))
print("XOR({}, {}) = {}".format(1,-10,XOR_percep(example4)))

def XNOR_percep(x):
  output_AND = AND_percep(x)
  output_NOT1 = NOT_percep(x[0])
  output_NOT2 = NOT_percep(x[1])
  output_NOT_AND = AND_percep(np.array([output_NOT1, output_NOT2]))
  x_temp = np.array([output_AND, output_NOT_AND])
  output_OR = OR_percep(x_temp)
  return output_OR


#Test
example1 = np.array([10,1])
example2 = np.array([10,-5])
example3 = np.array([-10,-10])
example4 = np.array([1,-10])

print("XNOR({}, {}) = {}".format(10,1,XNOR_percep(example1)))
print("XNOR({}, {}) = {}".format(10,-5,XNOR_percep(example2)))
print("XNOR({}, {}) = {}".format(-10,-10,XNOR_percep(example3)))
print("XNOR({}, {}) = {}".format(1,-10,XNOR_percep(example4)))
