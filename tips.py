import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

st.write('# Анализ датасета чаевых (tips.csv)\n')
tips = pd.read_csv('tips.csv', index_col=0)

st.write('Датасет выглядит слеующим образом (первые 5 строк):')
st.write(tips.head())

st.write('''
Здесь **total_bill** - это общий счет (в \$), **tip** - это размер чаевых 
(также в $), **sex** - пол платившего, **smoker** - были ли в компании 
курящие или нет, **day** - день недели, **time** - время посещения 
(**lunch** - обед или **dinner** - ужин), **size** - размер компании 
''')

st.write('### Посмотрим распределение величины общего счета')
plt.style.use('seaborn')
fig, ax = plt.subplots()
sns.histplot(x='total_bill', data=tips, ax=ax);
#ax.set(xlabel='Общий счет', ylabel='Количество счетов')
st.pyplot(fig)

st.write('### Посмотрим связь между величиной счета и размером чаевых')
fig, ax = plt.subplots()
sns.regplot(x='total_bill', y='tip', data=tips)
ax.set(ylim=(0,10.5))
st.pyplot(fig)

st.write('### Теперь добавим разделение по размеру компании')
fig, ax = plt.subplots()
sns.scatterplot(x='total_bill', y='tip', hue='size', data=tips, size='size')
st.pyplot(fig)

st.write('### Оценим размер и количество чаевых на обед и ужин')
fig, ax = plt.subplots()
sns.histplot(x='tip', data=tips, hue='time')
st.pyplot(fig)


st.write('### Посмотрим величину общего счета по дням недели')
fig, ax = plt.subplots()
def day_sort(ser):
    d_order=['Thur', 'Fri', 'Sat', 'Sun']
    return ser.apply(lambda x: d_order.index(x))
     
sorted_tips = tips.sort_values(by='day', key=day_sort, ascending=True)
sns.scatterplot(x='day', y='total_bill', hue='day', data=sorted_tips)
ax.legend(loc='upper center')
st.pyplot(fig)


st.write('### Посмотрим величину счета за обед и ужин по дням недели на диаграмме размаха (ящик с усами)')
fig, ax = plt.subplots()
sns.boxplot(x='day', y='total_bill', hue='time', data=sorted_tips)
ax.legend(loc='upper center')
st.pyplot(fig)

st.write('### Давайте взглянем на величину чаевых, которые оставили мужчины и женщины')
st.write('*С разбивкой на курящих и не курящих*') 
#fig, ax = plt.subplots(2,1, figsize=(8,10) )
fig, ax = plt.subplots()
ax=sns.lmplot(x='total_bill', y='tip', data=tips.loc[tips['sex']=='Male'], hue='smoker')
ax.set(title='Male')
ax.set(ylim=(0,11))
st.pyplot(ax)

fig, ax = plt.subplots()
ax=sns.lmplot(x='total_bill', y='tip', data=tips.loc[tips['sex']=='Female'], hue='smoker')
ax.set(title='Female')
st.pyplot(ax)

st.write('### И в завершении давайте посмотрим какой процент от общего счета оставляли мужчины и женщины чаще всего (tip_percent - процент от общего счета)')
fig, ax = plt.subplots()
tips['tip_percent'] = tips['tip']/tips['total_bill'] * 100
sns.histplot(x='tip_percent', data=tips, hue='sex')
st.pyplot(fig)