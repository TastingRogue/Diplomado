import pickle

t=90,3.1,False,'aCat', True

with open('tuple.bin','wb') as fh:
        pickle.dump(t,fh)

print('done...')
