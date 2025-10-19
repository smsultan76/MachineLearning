import pandas
import seaborn as sns
import matplotlib.pyplot as plt

data = pandas.read_csv('shopping_behavior_updated.csv')
print(data.info())

print(data.head(10))
print(data.shape)
print(data.isnull().sum())
print(data.isnull().sum().sum())

print(data.notnull().sum().sum())

print(data.isnull().sum()/data.shape[0]*100)

sns.heatmap(data.notnull())
print(plt.show())