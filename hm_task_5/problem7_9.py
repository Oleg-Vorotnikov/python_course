import pandas as pd
import matplotlib.pyplot as plt

#problem_7

df_usd = pd.read_csv('BCT-USD.csv')

df_usd['Date'] = pd.to_datetime(df_usd['Date'])
df_usd['YearMonth'] = df_usd['Date'].dt.to_period('M')
df_usd = df_usd.set_index('Date')
df_usd = df_usd.sort_index()


# print(df_usd)
def graph_usd(date1, date2):
    plt.plot(df_usd.loc[date1:date2, 'Open'])
    plt.plot(df_usd.loc[date1:date2, 'Close'])
    #plt.show()


graph_usd('2021-10-21', '2022-10-16')

#problem_8

df_usd_min = df_usd.groupby('YearMonth')['Volume'].sum()

print(df_usd_min.idxmin())

#problem_9

df_last_day_close = df_usd.groupby('YearMonth')['Close'].last().reset_index()
df_first_day_open = df_usd.groupby('YearMonth')['Open'].first().reset_index()

df_merged = pd.merge(df_last_day_close, df_first_day_open)

filtered_df = df_merged[df_merged['Close'] > df_merged['Open']]

if filtered_df.empty:
    print("Таких месяцев нет")
else:
    print(filtered_df['YearMonth'])
