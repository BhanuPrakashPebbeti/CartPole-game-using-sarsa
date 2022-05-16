# Sarsa-Algorithm

## SARSA
SARSA algorithm is a slight variation of the popular Q-Learning algorithm. For a learning agent in any Reinforcement Learning algorithm it’s policy can be of two types:- 

- On Policy: In this, the learning agent learns the value function according to the current action derived from the policy currently being used.
- Off Policy: In this, the learning agent learns the value function according to the action derived from another policy.

The difference between these two algorithms is that SARSA chooses an action following the same current policy and updates its Q-values whereas Q-learning chooses the greedy action, that is, the action that gives the maximum Q-value for the state, that is, it follows an optimal policy.

## SARSA Pseudo code

<img src="https://github.com/BhanuPrakashPebbeti/Sarsa-Algorithm/blob/main/assets/sarsa.png" width="600" height="300">

## SARSA vs Q-Learning

<img src="https://github.com/BhanuPrakashPebbeti/Sarsa-Algorithm/blob/main/assets/sarsa%20vs%20q.jpg" width="600" height="300">

## Reward Stats while Training SARSA

<img src="https://github.com/BhanuPrakashPebbeti/Sarsa-Algorithm/blob/main/sarsa/Statistics.png" width="400" height="400">

## CartPole 
![CartPole_gif](https://github.com/BhanuPrakashPebbeti/Sarsa-Algorithm/blob/main/assets/CartPole.gif)

