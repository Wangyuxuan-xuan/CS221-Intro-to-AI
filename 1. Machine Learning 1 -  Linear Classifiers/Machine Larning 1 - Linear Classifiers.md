# Machine Larning 1 - Linear Classifiers

![Alt text](Linear%20Classifier.png)

Sign means you gotta commit, which side are you on?

Visual intuition:
![Alt text](Screenshot%202024-03-06%20110928.png)
![Alt text](Screenshot%202024-03-06%20111112.png)

![Alt text](Screenshot%202024-03-06%20111504.png)



Decision boundary
# Loss Minimization


The leaner take some data and retruns a predictor

From what we wanna compute to how we wanna compute

### Loss Function
Loss(x,y,w)
![](2024-03-06-13-25-58.png)


Score and Margin 
![](2024-03-06-13-31-21.png)
When margin is less than 0, it means the prediction is confidently wrong
(The score and actual Y has different signs)

![](2024-03-06-13-35-20.png)
The Loss function means: did u make mistake or not
[f(w) = y] : this returns 0 or 1 depends on the statement is true or false
![](2024-03-06-13-37-09.png)


## Linear Regression
### Residual
Try to catch how much did I wrong
![](2024-03-06-13-40-19.png)
Redidual is the distance between the true value y and the predicted value y

### Squared Loss
![](2024-03-06-13-41-49.png)
Squared Residual

![](2024-03-06-13-44-14.png)

Which one to choose?
The squared loss is kinda like "mean", where its value may got affected by outliers extremely

For standerded deviation, you can think that as medium, which less affected by outliers

## Minimize Loss => Train Loss
![](2024-03-06-13-55-03.png)

The sum of all loss averanged by the number of training data

This is a function of w(weight) because we wanna find a weight vector that best fit for all the data(points)

# Stochastic gradient descent

## Optimization Algorithm
Terrin map(等高线)

### Gredinent
Where the value is increase the most

![](2024-03-13-11-07-08.png)
![](2024-03-13-11-09-17.png)

The gradient decent is great, but for morden examples with millions of examples, this can be really slow
![](2024-03-13-11-23-18.png)
It's slow because We have go through all the points for each iterations

The idea for `Stochastic gradient descent` is that, maybe we don't have to do it

![](2024-03-13-11-27-19.png)

This grediant is from all the examples from all points in your trainning set.

![](2024-03-13-11-26-50.png)

It is a sum of different things pointing to different directions, which all averange out to this direction.

So maybe we can not agarange all of them, maybe just a couple of them, or even just pick one of them

The key idea is **It not about quality, it's about quantity**


## Step size
Choose wisely, either too big or too small won't be good

## Gradient descent for zero-one classification 
It won't work because the gradient is 0 lol

We can try to make it non-0 though
![](2024-03-13-13-32-45.png)

![](2024-03-13-13-36-59.png)

![](2024-03-13-13-36-34.png)

## Summary
![](2024-03-13-13-39-13.png)

- To train, you have to access how well you are doing: 
    - You can use margin or residual for classification or Regression respectively
- You can define loss functions
- Optimizing with SGD(which turns out to be a lot faster than GD)

```python
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


```