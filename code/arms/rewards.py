import random
def reward_vectors( horizon, num_sims):
    n_arms = 2
    a = [0,1]
    b = [1,0]
    c = [0,0]
    d = [1,1]
    fi = []
    se = []
    for i in range(horizon/2):
        f = random.randint(0,3)
        s = random.randint(0,3)
        #print f, s
        if f == 0:
            fi.extend(a)
        elif f == 1:
            fi.extend(b)
        elif f == 2:
            fi.extend(c)
        elif f == 3:
            fi.extend(d)
        if s == 0:
            se.extend(a)
        elif s == 1:
            se.extend(b)
        elif s == 2:
            se.extend(c)
        elif s == 3:
            se.extend(d)
    fi = fi*num_sims
    se = se*num_sims
    return [fi,se]
#print reward_vectors(300,5000)[1][:300]
