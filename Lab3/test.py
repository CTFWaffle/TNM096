import copy
import random
class clause(set):
  def __init__(self,p,n):
    self.p = set(p)
    self.n = set(n)
  
  def __hash__(self):
    return hash((frozenset(self.p), frozenset(self.n)))

  def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.p == other.p and self.n == other.n
  
  def __deepcopy__(self, memo):
        # Create a blank object without calling __init__
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))
        return result

  def __repr__(self):
    return f"{' '.join(self.p)} {' '.join(['¬' + x for x in self.n])}"
  
  def Remove_duplicates(self):
    C = self.p.intersection(self.n)
    if C:
      self.p -= C
      self.n -= C


def Resolution (A, B):
  A_ = copy.deepcopy(A)
  B_ = copy.deepcopy(B)
  if not (A_.p.intersection(B_.n)) and not(A_.n.intersection(B_.p)):
    return False

  if A_.p.intersection(B_.n):
    a = A_.p.intersection(B_.n).pop() # "The pop() method removes a random item from the set."
    #a=set(a)
    A_.p.remove(a)
    B_.n.remove(a)
  else:
    a = A_.n.intersection(B_.p).pop()
    A_.n.remove(a)
    B_.p.remove(a)

  C = clause(A_.p.union(B_.p),A_.n.union(B_.n))
  
  if C.p.intersection(C.n):
    return False
  return C

def Incorporate_clause(A,KB):
  #Check if similar
  for B in copy.deepcopy(KB):
    if B == A:
      return KB
  #Check to remove
  for B in copy.deepcopy(KB):
    if B.p.issubset(A.p) and B.n.issubset(A.n):
      return KB
    if A.p.issubset(B.p) and A.n.issubset(B.n):
      KB.remove(B)
  
  KB = KB.union(set({A}))
  return KB

def Incorporate(S,KB):
  for A in copy.deepcopy(S):
    #print('KB before: ',KB)
    KB = Incorporate_clause(A,KB)
    #print('KB after: ',KB)
  return KB


def Solver(KB):
  #KB = Incorporate(KB,set())
  while(True):
    S = set({})
    KB_ = copy.deepcopy(KB)
    for A in KB:
      for B in KB:
        if A == B:
          continue
        C = Resolution(A,B)
        if C is not False:
          S = S.union(set({C}))
            

    if not S:
      return KB

    #Print info
    print("S: ")
    for A in S:
      print(A)
    print("\n")
    KB = Incorporate(S,KB)
    
    print("KB: ")
    for A in KB:
      print(A)
    print("\n")

    if KB_ == KB:
      return KB

def Bob():
    KB = set()
    # Formalae:
    # sun ∧ money ⇒ ice
    # money ∧ ¬ice ⇔ movie
    # ¬sun ∧ ¬money ⇒ cry

    # Clauses:
    # C1 = ¬sun ∨ ¬money ∨ ice
    # C2 = ¬money ∨ ice ∨ movie
    # C3 = ¬movie ∨ money
    # C4 = ¬movie ∨ ¬ice
    # C5 = sun ∨ money ∨ cry

    C1 = clause({'ice'},{'money','sun'})
    C2 = clause({'ice','movie'},{'money'})
    C3 = clause({'money'},{'movie'})
    C4 = clause({},{'movie','ice'})
    C5 = clause({'sun','money','cry'},{})
    C6 = clause({'movie'},{}) 

    
    KB = set({C1,C2,C3,C4,C5,C6})
    print("Original KB: ")
    for A in KB:
      print(A)
    print("\n")
    KB = Solver(KB)
    
    return KB

b=Bob()
#b.remove(clause({'ice','movie'},{'money'}))
for c in b:
  print('Clause: ',c)