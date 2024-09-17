# Intro
![](images/2024-03-25-13-44-30.png)
Models: MDP
Inference Algorithms: be able to use model to predict and answer queries
 - Value iteration: Compute the optimal policy.
 - Policy evaluation: Estmate the value for a particular policy.
  
Learning: How you actually learn these models
 - And this lecture is going to be about learning - Reinforcement learning

## Review
![](images/2024-03-25-13-50-55.png)


Policy
A mapping from states to action
A policy tells u where to go/which action to take

When we run a policy, we get a path unti you hit the end state(In RL it's called an episode)

What happend out of the episode:
You can look at the utility: The discounted sum of rewards along the way.

![](images/2024-03-25-14-01-19.png)

In last lecture we didn't really worked with utility, because we can use iterative method to compute/approximate the expected utility(The value)

![](images/2024-03-25-14-02-53.png)
![](images/2024-03-25-14-03-48.png)
IF you say goodbye to transition and rewards, that is called reinforcement learning

For MDP: I give you everything there, and u just need to find the optimal policy
For ML: We don't know what rewards and transition(probebility) that we are gonna get

# Reinforcement Learning Intro

## MDP and RL
![](images/2024-03-25-14-11-56.png)

MDP is a offline thing
- You already have a exact model of how the "world" works
- All you need to do is just sit down and think(Compute) the best policy that collects the best rewards.
  
RL is a online thing
- We don't know how the "real world" works
- So we cannot just sit there and think(Compute) because it won't help at all
- We have to go out and perform action in the real worlds, by doing so, hopefully we'll learn something and we'll get some rewards.

## General Framework
![](images/2024-03-25-14-55-41.png)

You can treat yourself as an agent
You take action a to the environment, the environment returns you a new state s' and reward r
Two main quesions here:
- What am I gonna act(Which action should I choose)
- Upon recived reward and new state, How/what should I do to update my model of "the world".

# Monte Carlo methods

## Model-based Monte Carlo 

`Monte Carlo`: means using simples

In the beginning of RL, we have nth but data
Let's try to build MDP from that data (Estimate MDP)
![](images/2024-03-25-15-14-16.png)
In simple, we just need to figure out what the transitions and rewards are.

- Transition : Collect the data and check the ratio
- Reward: Just observe the reward that the env returns.

Q/A: *Do we always know all states and actions?*
For states we can just observe/collect as they come
For actions we have to know becasue we are an agent and we have to play the game

![](images/2024-03-25-15-23-33.png)

So it works like: You gather a bunch of data (Episodes), estimate them, build MDP, then compute

### Potential Problem
You might not explored all the states/rewards

Unless you have a policy let u goes and covers all the states
![](images/2024-03-25-15-28-53.png)

So we need to figure out how to get the data, to explore the state space, which is one of the key challenge of RL
Solution: We need a random policy

## Model-free Monte Carlo
![](images/2024-03-25-15-31-44.png)

For MDP, at the end of the day, all we need is Qopt(s,a)
Qopt(s,a) is: The maximun possible utility I could get if I'm in chance node (s,a) and I followed the optimal policy

So if we know Qopt(s,a), we would just need to follow the optimal policy and it's done, we don't need to know about the rewards/transitions.

So why don't we estimate Qopt directly, without building up the whole MDP model

![](images/2024-03-25-15-39-58.png)
SO this means, you only 
Average the utility that you get, only on a timestamp (t) that i am in a particular state s and I (keep)took action a.

![](images/2024-03-25-15-45-08.png)

We just avarage whenever we see a utility of s,a but no double counting

The small hat ^ on each notion means that: this comes form some quantity(estimate) and differentiate it from the true value

![](images/2024-03-25-15-52-22.png)
In RL we are always following some policy
On-policy: you stick to one
Off-policy: general, optimistic ???

Q/A: Is monte free always follow the same policy?
A: It is just for this particular example, it is a on policy
In other examples we can also try optimize the policy

Q/A: Which one is better, model free or model based?
Interesting question.
If u have a exact/correct model for the "world", model-based is kind of the way to go, becasue you need less data points and less computation(u already know the model!)

However in real world it is really hard to get the model 100% correct. Now with deep RL many ppl go for model free cuz u can solve diffcult problem without constructing the MDP

![](images/2024-03-25-15-58-14.png)

### Interpretations

#### Avarange
We've talked about it
#### Convex Combination
![](images/2024-03-25-16-00-42.png)
Theme variations
N : number of occurences 
It is balancing between the old utilities/values that I had and the new utility that I saw

The old is with weight `1-n`, the new one is weight `n`
`n = 1/number of occurences `

#### Stochastic Gradient Decent
![](images/2024-03-30-11-13-46.png)
u: the new data u've got
All the updates are like:
>Residual = Prediction - Target

This is implicitly doing SGD on the square loss of the Residual, so u want them to close to each other
## An Exapmle
![](images/2024-03-30-11-23-01.png)
A state (square) divided into 4 pieces, which corrsponding to 4 different actions(North south east west), and the nunber there is the Qpi value if take that action from that state
The policy is : move comletely 

# Bootstrapping
![](images/2024-03-30-12-33-25.png)
Each episode has a utility asscioated with it

The idea was to use avarange, with large amount of data to compute, u can get close to true value
But with limited data the variance is big

The key idea is 
?
## SARSA
![](images/2024-03-30-12-37-42.png)
Why called SARSA:
You are in state `s`, you took action `a`, you got a reward `r`, and you end up in state `s'` , and you took another action `a'`.

So for every quintuple that you see, you are gonna perform an update.
And this is the convex combination, where you take part of the old value and try to merge them with the new value.

The new value is: the **immidiate reward** + the discount of your estimate.

Remember what is the estimate: It is trying to be the expectation of rewards that you will get in the future.

So if Qpi estimate could be close to the true value then this will be a lot better cuz it will reduce the variance.

![](images/2024-03-30-12-48-34.png)
SO Model-free monte carlo is updating based on `u`
SARSA is updating based on `immidiate reward r` + the discount of your estimate.

![](images/2024-03-30-12-50-23.png)
SARSA is biased because it's based on its previous expirences
Monte Carlo - wait until end to update:
Cuz you need to reach the end state of your model so that u will know the utility
But for SARSA you can inmmidiately update because all u need to see is just a local windows of (s,a,r,s',a')

![](images/2024-03-30-12-57-25.png)
A. With the exact model u can compute everything
B & C. Model-free and SARSA are estimating the Qpi(the value of a policy) but not Qopt, which is a problem, because all we want is the Oopt
That's when we  need `Q-learning` which allows you to get Qopt
![](images/2024-03-30-13-00-47.png)
![](images/2024-03-30-13-01-15.png)

## Q-learning
![](images/2024-03-30-13-06-08.png)

![](images/2024-03-30-13-08-16.png)
For Q-learning it doesn't metter what action `a'` you gonna took for the next step, cuz we'll just take the one that maximizes(optimal one).

This is why SARSA is estimating the value of a policy
- Cuz what a' shows up there is a function of policy

and Q-learning is estimating the optimal policy cuz i don't care the next action, i'll just take the maximum(optimal) one

This is same ituiation of policy evaluaiton and value iteration.

> Q/A: Is q-learning on-policy or off-policy
 A: off-policy, cuz i am following whatever policy i can follow and estimate the value of the optimal policy, which is probobly not the original policy at the beginning

>While SARSA is a on-policy because i am estimating the value of Qpi

## Volcano example
Notice that the slip prob is 0 here
SARSA
![](images/2024-03-30-13-19-46.png)
The value here is Qpi, which is the value of the policy i'm following(the random policy)

Q-learning
![](images/2024-03-30-13-21-11.png)
The  value of optimal policy
Learning how to hehave optimally

# Encountering the Unknown
So we've just mentioned the algothrims.
If i hand u some data and told u there's a fixed policy, you can estimate all those values
![](images/2024-03-30-13-28-44.png)

However there's a question of exploration:
We don't even see all the states, how do u possibly act optimally
![](images/2024-03-30-13-33-35.png)
In this case, once we found a local optimium, we'll just stick to it lol

![](images/2024-03-30-13-36-46.png)
I just try differently way and learn from it, however the average utility is still bad cuz the policy was just random policy
The exploration is **not guided**
![](images/2024-03-30-13-37-09.png)
RL kind of capture the life
You are aiming for a best reward, you have to learn how the world works and improves ur policy

## Epsilon-greedy
Balancing the exploration and exploitation
This assumes that ur doing Q-learning

Epsilon is the ramdon probility u specifiy
We can do sth random once in a while
![](images/2024-03-30-14-02-43.png)

Epsilon
When u turns older, you start to explore less and exploit more lol

## Generalization
The problem is that the state space is huge and there's no way you can go down and track every possible state.
![](images/2024-03-30-14-07-22.png)

Large state space
![](images/2024-03-30-14-10-17.png)
I we follow the current way, we cannot generalize between states and actions

### Function approximation
Tell you new states that you haven't see before

  ![](images/2024-03-30-14-13-29.png)
Featrues:
eg: it's better to go to the West/East
It's better to be at the 5th row/ 6th col

So we have a smaller set of features that we can try to use it, to generalize different states you might see.

![](images/2024-03-30-14-17-02.png)
You take ur weight vector, take an update of redidual * the feature vector.
eta: like step size
![](images/2024-03-30-14-23-25.png)

# Summary
![](images/2024-03-30-14-24-39.png)

![](images/2024-03-30-14-26-05.png) 
![](images/2024-03-30-14-28-05.png)
![](images/2024-03-30-14-30-01.png)
Reinforcement learning is generally really hard, because of enumorous states and delayed feedback.
![](images/2024-03-30-14-34-05.png)
![](images/2024-03-30-14-35-06.png)
For RL we are playing against nature
Next time we'll play against an opponent who are trying to get us