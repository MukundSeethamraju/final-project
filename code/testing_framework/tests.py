def test_algorithm(algo, arms, num_sims, horizon):
  chosen_arms = [0.0 for i in range(num_sims * horizon)]
  rewards = [0.0 for i in range(num_sims * horizon)]
  cumulative_rewards = [0.0 for i in range(num_sims * horizon)]
  #sim_nums = [0.0 for i in range(num_sims * horizon)]
  #times = [0.0 for i in range(num_sims * horizon)]
  cumulative_all_rewards = {a : [0 for i in range(num_sims*horizon)] for a in range(len(arms))}
  all_rewards = {a : [] for a in range(len(arms))}
  best_arm = [0 for i in range(num_sims * horizon)]
  cumulative_regret = [0 for i in range(num_sims * horizon)]
  for sim in range(num_sims):
    sim = sim + 1
    algo.initialize(len(arms))
    
    for t in range(horizon):
      t = t + 1
      index = (sim - 1) * horizon + t - 1
      #sim_nums[index] = sim
      #times[index] = t

     
      for i in range(len(arms)):
        all_rewards[i].append(arms[i].draw())
        if t == 1:
          cumulative_all_rewards[i][index] = all_rewards[i][index]
        else:
          cumulative_all_rewards[i][index] = cumulative_all_rewards[i][index - 1] + all_rewards[i][index]

            
      chosen_arm = algo.select_arm()
      chosen_arms[index] = chosen_arm
      
      reward = all_rewards[chosen_arms[index]][index]
      #reward = arms[chosen_arms[index]].draw()
      rewards[index] = reward
      
      if t == 1:
        cumulative_rewards[index] = reward
      else:
        cumulative_rewards[index] = cumulative_rewards[index - 1] + reward
      
      algo.update(chosen_arm, reward)
  for i in range(num_sims * horizon):
    a = cumulative_all_rewards[0][i] 
    for j in range(len(arms)):
      if a < cumulative_all_rewards[j][i]:
        best_arm[i] = j
  for i in range(num_sims*horizon):
    cumulative_regret[i] = cumulative_all_rewards[best_arm[i]][i] - cumulative_rewards[i]
  return [chosen_arms, rewards, cumulative_rewards, cumulative_regret]

