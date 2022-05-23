from random import choice

def brujula():
    return choice(['N','NxE','NNE','NExN','NE','NExE','ENE','ExN','E','ExS','ESE','SExE','SE','SExS','SSE','SxE','S','SxO','SSO','SOxS','SO','SOxO','OSO','OxS','O','OxN','ONO','NOxO','NO','NOxN','NNO','NxO'])

for i in range(15):
    print(brujula()) 
