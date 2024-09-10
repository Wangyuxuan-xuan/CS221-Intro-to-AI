import numpy as np

###############################################################
# Modeling: what we wanna compute
# points = [(np.array([2]),4), (np.array([4]),2)]
# d = 1

# Generate artificial data
# Let's first decide what the right answer is
true_w = np.array([1, 2, 3, 4, 5])
d = len(true_w)
points = []
for i in range(10000):
    x = np.random.randn(d)
    # Add some noise lol
    y = true_w.dot(x) + np.random.randn()
    points.append((x, y))

def F(w):
    return sum((w.dot(x) - y)**2 for x, y in points) / len(points)

def dF(w):
    #外层求导 后内层求导
    return sum(2*(w.dot(x) - y)*x for x, y in points) / len(points)

def stochasticF(w, i):
    x, y = points[i]
    return (w.dot(x) - y)**2

def stochasticDF(w, i):
    x, y = points[i]
    return 2*(w.dot(x) - y)*x
###############################################################
# Algorithm: How we compute it

# the gradient descent depends on a function, the gradient, and dementionality
def gradientDescent(F, dF, dementionality):
    
    w = np.zeros(dementionality)

    stepSize = 0.01
    for t in range(100000):
        errorSum = F(w)
        gradient = dF(w)
        #Gradient tells me where the function is increasing so we move to the oppisite direction
        w = w - gradient * stepSize
        
        print("iteration {}: w = {}, ErrorSum F(w) = {}".format(t, w, errorSum))

def stochasticGradientDescent(sF, sDF, dementionality, n):
    
    w = np.zeros(dementionality)

    stepSize = 0.01
    for t in range(1000):
        for i in range(n):
            errorSum = sF(w, i)
            gradient = sDF(w, i)
            #Gradient tells me where the function is increasing so we move to the oppisite direction
            w = w - gradient * stepSize
            # Somehow this is not work lol
            # stepSize = 1.0/(t+1)
        
        print("iteration {}: w = {}, ErrorSum F(w) = {}".format(t, w, errorSum))

# gradientDescent(F, dF, d)
stochasticGradientDescent(stochasticF, stochasticDF, d, 10)
