import random
import math

def categorical_draw(probs):
  z = random.random()
  cum_prob = 0.0
  for i in range(len(probs)):
    prob = probs[i]
    cum_prob += prob
    if cum_prob > z:
      return i

  return len(probs) - 1

class Exp3ix():
  def __init__(self, gamma, alpha, weights):
    self.gamma = gamma
    self.alpha = alpha
    self.weights = weights
    return
  
  def initialize(self, n_arms):
    self.weights = [1.0 for i in range(n_arms)]
    return
  
  def select_arm(self):
    n_arms = len(self.weights)
    total_weight = sum(self.weights)
    probs = [0.0 for i in range(n_arms)]
    for arm in range(n_arms):
      probs[arm] = (self.weights[arm] / total_weight)
      #probs[arm] = probs[arm] + (self.gamma) * (1.0 / float(n_arms))
    return categorical_draw(probs)
  
  def update(self, chosen_arm, reward):
    n_arms = len(self.weights)
    total_weight = sum(self.weights)
    probs = [0.0 for i in range(n_arms)]
    for arm in range(n_arms):
      probs[arm] = (self.weights[arm] / total_weight)
      #probs[arm] = probs[arm] + (self.gamma) * (1.0 / float(n_arms))
    
    x = reward / (probs[chosen_arm] + alpha)
    
    growth_factor = math.exp((self.gamma / n_arms) * x)
    self.weights[chosen_arm] = self.weights[chosen_arm] * growth_factor
