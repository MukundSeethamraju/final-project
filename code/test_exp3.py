execfile("core.py")
#execfile("rewards.py")
import random

random.seed(1)
def arms():
    while True:
        amount = input("Enter the number of arms:   ")
        try:
            val = int(amount)
            if val >= 0:
                break
            else:
                print("number of arms can't be negative, try again")
        except ValueError:
            print("number of arms must be a number, try again")
    return val


def arms1(n_arms):
    while True:
        amount = input("Enter the number of adversarial arms:   ")
        try:
            val = int(amount)
            if val >= 0 and val <= n_arms:
                break
            else:
                print("number of adversarial arms can't be negative or greater than number of arms possible, try again")
        except ValueError:
            print("number of arms must be a number, try again")
    return val


def arms2(n_arms, n_adversarial):
    while True:
        amount = input("Enter the number of bernoulli arms:   ")
        try:
            val = int(amount)
            if val >= 0 and val <= (n_arms - n_adversarial):
                break
            else:
                print("number of bernoulli arms can't be negative or greater than number of arms possible, try again")
        except ValueError:
            print("number of arms must be a number, try again")
    return val


def arms3(n_arms, n_adversarial, n_bernoulli):
    while True:
        amount = input("Enter the number of normal arms:   ")
        try:
            val = int(amount)
            if val >= 0 and val == (n_arms - n_adversarial - n_bernoulli):
                break
            else:
                print("number of bernoulli arms can't be negative or greater than number of arms possible, try again")
        except ValueError:
            print("number of arms must be a number, try again")
    return val

def mean(numbers):
    return float(sum(numbers))/len(numbers)

def variance(numbers):
    a = float(sum(numbers))/len(numbers)
    v = sum((a - value)**2 for value in numbers) / len(numbers)
    return v

def add(a,b):
    c = []
    for i in range(len(a)): 
        c.append(float(a[i] + b[i])/2)
    return c

def subtract(a,b):
    c = []
    for i in range(len(a)):
        c.append(float(a[i] - b[i]))
    return c

#n_arms = arms()
n_arms = 2
'''
n_adversarial = arms1(n_arms)
n_bernoulli = arms2(n_arms, n_adversarial)
n_normal = arms3(n_arms, n_adversarial, n_bernoulli)
'''

'''
num_sims = int(raw_input('Enter the number of simulations:  '))
horizon = int(raw_input("Enter the time horizon:  "))
'''
all_arms = [0,1]

num_sims = 5000
horizon = 300

#earlier arms
'''
if n_adversarial > 0:
  t = 0
  adversarial_arms = []
  for i in range(n_adversarial):
    active_start = int(raw_input("enter the start time for 1:  "))
    active_end = int(raw_input("enter the end time for 1:  "))
    adversarial_arms.append(AdversarialArm(t,active_start,active_end))
  all_arms.extend(adversarial_arms)

if n_bernoulli > 0:
  means2 = []
  for i in range(n_bernoulli):
    means2.append(float(raw_input("Enter the mean for Bernoulli arm: \t")))
  bernoulli_arms = map(lambda (mu): BernoulliArm(mu), means2)
  all_arms.extend(bernoulli_arms)

if n_normal > 0:
  means3 = []
  sigma3 = []  normal_arms = []
  for i in range(n_normal):
    means3.append(float(raw_input("Enter the mean for normal arm:  ")))
    sigma3.append(float(raw_input("Enter the sigma for corresponding normal arm:  ")))
    normal_arms.append(NormalArm(means3[i], sigma3[i]))
  all_arms.extend(normal_arms)
'''



#random.shuffle(all_arms)

gamma = 0.4
#gamma = float(raw_input("Enter gamma value for Exp3:  "))
import time
start_time = time.time()

algo = Exp3(gamma, [])
algo.initialize(n_arms)

#re_matrix  = reward_vectors(horizon, num_sims)
#print 1, reward_vectors(horizon, num_sims)[1][:300]


r = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1]]     


results = test_algorithm(algo, all_arms, num_sims, horizon, r[0]*num_sims, r[1]*num_sims)


print("--- %s seconds ---" % (time.time() - start_time))

#calculating variation
mean_of_vectors = add(results[0],results[1])
x = np.array(subtract(mean_of_vectors,results[0]))
y = np.array(subtract(mean_of_vectors,results[1]))
variation = float(np.linalg.norm(x)**2) +  float(np.linalg.norm(y)**2)

f = open('results.txt', 'a')
f.write('%f,%f,%f,%f\n'%(variation/5000, variance(results[0]), variance(results[1]), mean(results[6])))  # python will convert \n to os.linesep
f.close()

                               


