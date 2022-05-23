import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')

print('head',iris.head())
print('')

print('Tupla')
iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',usecols = ['sepal length'])
data = []
for i in iris.index:
    data.append(tuple(iris.values[i]))
allnodes = tuple(data)
print(allnodes)

print('Dictionary')
dictionary = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',usecols = ['sepal width']).to_dict()
print(dictionary)

print('list')
list = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',names = ['sl','sw','pl','pw','class'])
datalist = list.pl.to_list()
print(datalist)