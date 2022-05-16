# Sarsa-Algorithm

## SARSA
SARSA algorithm is a slight variation of the popular Q-Learning algorithm. For a learning agent in any Reinforcement Learning algorithm it’s policy can be of two types:- 

- On Policy: In this, the learning agent learns the value function according to the current action derived from the policy currently being used.
- Off Policy: In this, the learning agent learns the value function according to the action derived from another policy.

The difference between these two algorithms is that SARSA chooses an action following the same current policy and updates its Q-values whereas Q-learning chooses the greedy action, that is, the action that gives the maximum Q-value for the state, that is, it follows an optimal policy.

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

## Reward Stats while Training Double Q-Learning

<img src="https://github.com/BhanuPrakashPebbeti/Sarsa-Algorithm/blob/main/Statistics.png" width="400" height="400">

## CartPole 
![CartPole_gif](https://github.com/BhanuPrakashPebbeti/Sarsa-Algorithm/blob/main/CartPole.gif)

