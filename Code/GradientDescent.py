points = [(2,4), (4,2)]

#Let's say just the linear function passes the origin
def F(w):
    # sumError = 0
    # for x,y in points:
    #     residual = w*x - y
    #     squareError = residual**2
    #     sum += squareError
    #     # We wanna minimize this error
    # return sumError
    return sum((w*x - y)**2 for x, y in points)

def dF(w):
    #外层求导 后内层求导
    return sum(2*(w*x - y)*x for x, y in points)

# Gradient Descent
w = 0

stepSize = 0.01
for t in range(100):
    errorSum = F(w)
    gradient = dF(w)
    #Gradient tells me where the function is increasing so we move to the oppisite direction
    w = w - gradient * stepSize
    print("iteration {}: w = {}, ErrorSum F(w) = {}, gradient = {}".format(t, w, errorSum, gradient))