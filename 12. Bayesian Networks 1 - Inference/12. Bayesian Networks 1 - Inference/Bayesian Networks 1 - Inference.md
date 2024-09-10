# Bayesian Networks 1 - Inference
![](2024-05-14-17-29-31.png)

Specify locally (Factors) and optimize globally (Weight)
Last time we talked about different algo for finding the maximum weight 
![](2024-05-14-17-32-03.png)

The framework is already good, with this you can come up with a lot
But what are these factors mean and how do we come up with them?
philosophically we might be quite bothered by this

So the goal of this lecture is to give more meaning to the factors, and bayesian network is the way to do that.
In a line, bayasian networks are factor graphs plus probability

Previously we already talked about a lot of modeling: search games, MDPs
And then we talked about modeling when the order of actions does not matter so much, and it is more nature to think it as variables and assignment
And now we will move on to bayasian networks where it will be a higher level of abstraction

# Basics
![](2024-05-14-17-44-06.png)
Notations;
Captital letters (S, R): random variables
samller letters (s,r): values that random variables can take
Notation P with Captital letters P(S, R): the whole probility destributions, eg P(S, R) is the destribution table
Notation P with =s, =r assignments P(S=s,, R=r): represents a signle number, which is a probility, eg: P(S=1, R=0) = 0.7

![](2024-05-14-17-51-28.png)
Marginal distribution:
eg I don't care about r, just wanna focus on s > 
Sum up probs when s = 0, s = 1 and u get the table

Conditional:
Select rows based on condition, normalize them and let them sum to 1.
normalize (a,b) means a' = a/(a+b), b' = b/(a+b)

![](2024-05-14-17-55-55.png)
Think of joint distibution as a database

**Probabilistic inference**:
You observe some evidence, that's what we know
and what we like to find out is weather it's raining

Is that reaning under condition of we know it is autumn and traffic 

Challenges:
the joint distibution table can he really huge
Cool thing about bayasian networks is that it allows us to define joint distibution using the language of factor graphs


![](2024-05-15-10-55-27.png)

![](2024-05-15-10-58-02.png)

![](2024-05-15-11-03-52.png)

A: prob if alarm going off
 
2. Define local conditional distribution

a local conditional distribution is:
P of whatever that variable is, given its parents, parents are the variable directly point into it
In this example the parents of `a` is `b` and `e`


1. define joint distribution 
   ![](2024-05-15-11-11-03.png)

The small `p` stands for local conditional distribution, it's the thing we need to define (it is the ground truth cuz we defined it)
The capital `P` stands for joint distribution 

![](2024-05-15-11-17-10.png)
Okay this is bayasian networks, and what's the connection between this and factor graphs
This looks like `weight = product of factors`
![](2024-05-15-11-22-26.png)
In this special case:
one factor per variable
has a single factor connect all parents

![](2024-05-15-11-23-42.png)
![](2024-05-15-11-28-03.png)

![](2024-05-15-11-29-26.png)
So given the alarms goes off and there's a bulargruy, decrease the prob of earthqeak

We might doubt that, `E` and `B` are independent. That's true but when we are conditioning on `A`, we already changed the independent structure of the model, which means when alarm goes off, `E` and `B` are no longer independent

## Definition
![](2024-05-15-11-36-32.png)
Xparents(i) means the value assigned to parents of i

![](2024-05-15-11-40-00.png)
if we summarize all possible values Xi can take on, it should be 1, and it is true for every settings of Xparents

![](2024-05-15-14-03-29.png)
def means by the laws of probabiliy
So by the laws of probabiliy we can take p(b)p(e) out side

We've made an algerbric operation graphcially

![](2024-05-15-14-09-36.png)
You marginalize a leaf node in Bayesian network, you can just drop it from the graph

### Consistency of local conditionals
![](2024-05-15-14-46-14.png)
They are equal

![](2024-05-15-14-47-12.png) 
Let's define it with procedure
![](2024-05-15-14-47-58.png)

![](2024-05-15-14-52-08.png)
h: coughing

![](2024-05-15-14-55-23.png)

# Probabilistic programs
![](2024-05-15-14-58-13.png)
Bernoulli: returns true with prob epsilon

define a distribution?

![](2024-05-15-15-05-13.png)
this program reduces to a particular bayesian network structure, where each Xi is only connected to Xi-1

![](2024-05-15-15-12-46.png)
For every position, generate a word given previous word

![](2024-05-15-15-15-47.png)
Convention:
If shade a variable, means u observe it
If not shade a variable, means u can't/don't observe it

![](2024-05-15-15-17-21.png)
We have two object and two independent markov chains running
At each time step, I only observe one sensor reading, and that sensor reading is gonna be some combination of the actual objects a and b

![](2024-05-15-15-29-04.png)
It's like another way around, we start with output
We first define the model

A set of variables H, which u don't observe, that generates/causes a set of variables E, which you do observe

# Inference
![](2024-05-15-15-57-56.png)
![](2024-05-15-16-11-58.png) 
1. We wanna remove as much as variables as I can
   1. Marginlize non-ancestors, meaning that anything upstream i can keep for now, anything down stream I can let go
2. Convert to a factor graph
   1. Remove the directions(cuz it's complex and easily to get confused), make things easy![](2024-05-15-16-07-47.png)
3. Condition on evidence, we are conditioning on X2, so we wrap it put and change the factors to be a partial evaluation![](2024-05-15-16-08-48.png)
4. Marginlize out the disconnected components (We care about X3 only, since they are disconnected, we can drop it since it's not related)
5. Do work, you might not just left with one node, in this step we need to solve the factor graph

![](2024-05-15-16-18-04.png)