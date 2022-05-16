# Sarsa-Algorithm

## Q-Learning
Q-learning is an off policy reinforcement learning algorithm that seeks to find the best action to take given the current state. It’s considered off-policy because the q-learning function learns from actions that are outside the current policy, like taking random actions, and therefore a policy isn’t needed. More specifically, q-learning seeks to learn a policy that maximizes the total reward.

<img src="https://github.com/BhanuPrakashPebbeti/Balancing-Pendulum-with-Q-Learning/blob/main/assets/Q-learning.jfif" width="400" height="150">

## Important Terms in Q-Learning
- States: The State, S, represents the current position of an agent in an environment. 
- Action: The Action, A, is the step taken by the agent when it is in a particular state.
- Rewards: For every action, the agent will get a positive or negative reward.
- Episodes: When an agent ends up in a terminating state and can’t take a new action.
- Q-Values: Used to determine how good an Action, A, taken at a particular state, S, is. Q (A, S)

## Bellman Equation
The Bellman Equation is used to determine the value of a particular state and deduce how good it is to be in/take that state. This equation is used to update the Q-Table. The optimal state will give us the highest optimal value. 

<img src="https://github.com/BhanuPrakashPebbeti/Balancing-Pendulum-with-Q-Learning/blob/main/assets/bellman-equation.jfif" width="600" height="200">

## Q-Learning Pseudo code

<img src="https://github.com/BhanuPrakashPebbeti/Balancing-Pendulum-with-Q-Learning/blob/main/assets/Q-Learning%20Psuedo%20code.png" width="600" height="300">

## Reward Stats while Training Q-Learning

<img src="https://github.com/BhanuPrakashPebbeti/Balancing-Pendulum-with-Q-Learning/blob/main/Q-Learning/Statistics.png" width="400" height="400">

## Problem with Q-Learning
  The important part of the Q-Learning is maxQ(S', a') is at the same time the biggest problem of Q-Learning. In fact, this is the reason why this algorithm performs poorly in some stochastic environments. Because of max operator Q-Learning can overestimate Q-Values for certain actions.
  
## Solution - Double Q-Learning
  The proposed solution is to maintain two Q-value functions QA and QB, each one gets update from the other for the next state.
The update consists of finding the action a' that maximises QA in the next state (Q(s’, a') = Max Q(s’, a)), then use a' to get the value of QB(s’, a') in order to update QA(s, a).
  
## Double Q-Learning Pseudo code

<img src="https://github.com/BhanuPrakashPebbeti/Balancing-Pendulum-with-Q-Learning/blob/main/assets/Double%20Q-Learning%20Psuedo%20code.png" width="600" height="300">

## Reward Stats while Training Double Q-Learning

<img src="https://github.com/BhanuPrakashPebbeti/Balancing-Pendulum-with-Q-Learning/blob/main/Double-Q-Learning/Statistics.png" width="400" height="400">

## Pendulum Balancing 
![Pendulum_gif](https://github.com/BhanuPrakashPebbeti/Balancing-Pendulum-with-Q-Learning/blob/main/assets/Pendulum-Q.gif)

