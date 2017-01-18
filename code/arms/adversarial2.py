class AdversarialArm2():
  def __init__(self, t, active_start, active_end):
    self.t = t
    self.active_start = active_start
    self.active_end = active_end
  
  def draw(self):
    self.t = self.t + 1
    if self.active_start <= self.t <= self.active_end:
      return 1.0
    else:
      return 0.0

a = [0,1]
b = [1,0]
c = [0,0]
d = [1,1]
def arms_vectors(a,b,c,d,n):

    random_vector = [0 for i in range(n)]
    
    
