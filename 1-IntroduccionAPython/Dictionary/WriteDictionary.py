import pickle

d={'url':'https://www.google.com/', 'txt':'Buscar', 'img':'Search'}

with open('dictionary.bin','wb') as fh:
        pickle.dump(d,fh)

print('done...')