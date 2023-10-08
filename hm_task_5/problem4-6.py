import pandas as pd
import matplotlib.pyplot as plt

df_emojis = pd.read_csv('emojis.csv')

#print(df_emojis)

print(df_emojis.groupby('Subcategory')['Rank'].sum().idxmin())

plt.plot(df_emojis.groupby('Year')['Year'].count())
plt.savefig('emojis.png')
#plt.show()


def find_cat(str_cat: str):
    res = df_emojis[df_emojis.Category.str.contains(str_cat)]
    if not res.empty:
        per_emoj = res.shape[0]/df_emojis.shape[0]*100
        return f'Процент эмоджи категории \'{str_cat}\' - {"{:.2f}".format(per_emoj)} %'
    else:
        return 'Такой категории нет'


print(find_cat('People & Body'))
