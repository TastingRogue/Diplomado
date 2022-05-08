Data =  (2, 1.43), (3.2, 2.79), (4, 3.56),(3.6)
SavedResult = list()

def f1(p):
  result = ((p[1][1]-p[0][1])/(p[1][0]-p[0][0]))
  return result

def f2(p, sr):
  result = ((((p[2][1]-p[1][1])/(p[2][0]-p[1][0]))-sr[0])/(p[2][0]-p[0][0]))
  return result

def y(p, sr):
  result = p[0][1]+(sr[0]*(p[3]-p[0][0]))+(sr[1]*(p[3]-p[0][0])*(p[3]-p[1][0]))
  return result

SavedResult.append(f1(Data))
SavedResult.append(f2(Data, SavedResult))

print(y(Data, SavedResult))
