def test_algorithm(algo, arms, num_sims, horizon, first, second):
  chosen_arms = [0.0 for i in range(num_sims * horizon)]

  # rewards is the array containing the reward obtained in every round for the chosen arm.
  rewards = [0.0 for i in range(num_sims * horizon)]
  cumulative_rewards = [0.0 for i in range(num_sims * horizon)]

  # all_rewards is the dictionary of rewards of all arms and cumulative_all_rewards is the dictionary of cumulative rewards of all arms.
  #first = algo.reward_vectors(horizon, num_sims)[0]
  #second = algo.reward_vectors(horizon, num_sims)[1]
  '''for i in range(300):
    if (i+1)%4 == 1:
      first.append(0)
    elif (i+1)%4 == 2:
      first.append(0)
    elif (i+1)%4 == 3:
      first.append(1)
    elif (i+1)%4 == 0:
      first.append(1)
    if i < 150:
      second.append(1)
    else:
      second.append(0)
  first = first*num_sims
  second = second*num_sims'''
  
  #print first[:300]
  all_rewards = {0 : first , 1 : second}
  cumulative_all_rewards = {a : [0 for i in range(num_sims*horizon)] for a in range(len(arms))}

  # cumulative_regret is the array containing regret after every simulation.
  all_regret = []
  best_arm = []
  
  for sim in range(num_sims):
    sim = sim + 1
    algo.initialize(len(arms))
    
    for t in range(horizon):
      t = t + 1
      index = (sim - 1) * horizon + t - 1
      
     
      for i in range(len(arms)):
        #all_rewards[i].append(arms[i].draw())
        if t == 1:
          cumulative_all_rewards[i][index] = all_rewards[i][index]
        else:
          cumulative_all_rewards[i][index] = cumulative_all_rewards[i][index - 1] + all_rewards[i][index]

            
      chosen_arm = algo.select_arm()
      chosen_arms[index] = chosen_arm
      
      reward = all_rewards[chosen_arms[index]][index]
      
      rewards[index] = reward
      
      if t == 1:
        cumulative_rewards[index] = reward
      else:
        cumulative_rewards[index] = cumulative_rewards[index - 1] + reward

      algo.update(chosen_arm, reward)

  #finding the best arms
  for i in range(num_sims*horizon):
    if (i + 1)%horizon == 0:
      a = cumulative_all_rewards[0][i]
      b = 0
      for j in range(len(arms)):
        if a < cumulative_all_rewards[j][i]:
          b = j
      best_arm.append(b)

  cumulative_rewards_bestarm = []
      
  for i in range(num_sims*horizon):
    if (i + 1)%horizon == 0:
      c = 0
      cumulative_rewards_bestarm.append(cumulative_all_rewards[best_arm[c]][i])
      all_regret.append(cumulative_all_rewards[best_arm[c]][i] - cumulative_rewards[i])
      c = c+1

  cumulative_rewards1 = []
  for i in range(num_sims*horizon):
    if (i+1)%horizon == 0:
      cumulative_rewards1.append(cumulative_rewards[i])
  return [first, second, chosen_arms, rewards, all_rewards, best_arm, all_regret]

