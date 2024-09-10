import numpy as np

## Modeling y=wx
true_w = np.array([1, 2, 3, 4, 5])
points = []


dimension = len(true_w)
for i in range(1000000):
    x = np.random.randn(dimension)
    y = true_w.dot(x) + np.random.randn()
    points.append((x, y))

### gradientDecent
def F(w):
    '''
    The error function that we wanna minimize
    '''
    return sum( (w.dot(x) - y)**2 for x, y in points) / len(points)

def DF(w):
    '''
    The gradient of F(w)
    '''
    return sum( 2*(w.dot(x) - y)* x for x, y in points) / len(points)

### SGD
def SF(w, i):
    '''
    The error function that we wanna minimize
    '''
    x, y = points[i]
    return (w.dot(x) - y)**2

def SDF(w, i):
    '''
    The gradient of F(w)
    '''
    x, y = points[i]
    return 2*(w.dot(x) - y)* x

## Algorithm

def gradientDecent(F, DF):

    w = np.array([0, 0, 0, 0, 0])
    stepSize = 0.01
    for i in range(100):
        errorSum = F(w)
        gradient = DF(w)
        w = w - gradient*stepSize
        print("iteration {} error sum {} weight {}".format(i, errorSum, w))

def StochasticGradientDecent(SF, SDF, dimension, stopThreshold):
    w = np.array([0, 0, 0, 0, 0])
    stepSize = 0.01
    for i in range(10000):
        index = np.random.randint(len(points))
        errorSum = SF(w, index)
        gradient = SDF(w, index)
        w = w - gradient*stepSize
            
        print("iteration {} error sum {} weight {}".format(i, errorSum, w))

        if(errorSum < stopThreshold):
            break

# gradientDecent(F, DF)
StochasticGradientDecent(SF, SDF, dimension, 0.0001)