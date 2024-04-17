#!/usr/bin/env python
# coding: utf-8

# # Комментарий ревьюера
# <div class="alert alert-block alert-info">
# Привет, Михаил! Меня зовут Анвар Ганиев, и я буду проверять твой проект. Предлагаю общаться на «ты» :) Но если это не удобно - дай знать, и мы перейдем на "вы". Моя основная цель — не указать на совершенные тобою ошибки, а поделиться своим опытом и помочь тебе стать data scientist'ом.
# 
# Видно, что ты старался, делая проект. Все ключевые этапы в работе выполнены, так что в целом справиться с задачей тебе удалось. Есть ещё несколько аспектов, которые требуют твоего внимания. Комментарии по ним помечены <span style='color:Red'> красным цветом ❌ </span>. Комментарии я буду оставлять под ячейками, к которым они относятся. А еще писать в заголовке v{номер версии}, чтобы знать, при какой проверке, я их оставлял. После их доработки проект будет принят. Осталось совсем немного, буду ждать твою работу на повторное ревью 🙂
# 
# <span style='color:Green'> Зелёным цветом ✅  </span> отмечены удачные и элегантные решения, на которые можно опираться в будущих проектах. <span style='color:Gold'> Жёлтым цветом ⚠️</span>выделено то, что в следующий раз можно сделать по-другому. Ты можешь учесть эти комментарии при выполнении будущих заданий или доработать проект сейчас (однако это не обязательно).
# 
# Давай работать над проектом в диалоге: если ты что-то меняешь в проекте по моим рекомендациям — пиши об этом. Выбери для своих комментариев какой-то заметный цвет, так мне будет легче отследить изменения. Пожалуйста, не перемещай, не изменяй и не удаляй мои комментарии. Всё это поможет выполнить повторную проверку твоего проекта оперативнее
# </div>
# 

# <h1>Содержание<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Подготовка-данных" data-toc-modified-id="Подготовка-данных-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Подготовка данных</a></span><ul class="toc-item"><li><span><a href="#-Комментарий-ревьюера-v1" data-toc-modified-id="-Комментарий-ревьюера-v1-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span> Комментарий ревьюера v1</a></span></li><li><span><a href="#-Комментарий-ревьюера-v1" data-toc-modified-id="-Комментарий-ревьюера-v1-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span> Комментарий ревьюера v1</a></span></li><li><span><a href="#-Комментарий-ревьюера-v1" data-toc-modified-id="-Комментарий-ревьюера-v1-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span> Комментарий ревьюера v1</a></span></li><li><span><a href="#Вывод-по-блоку:" data-toc-modified-id="Вывод-по-блоку:-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Вывод по блоку:</a></span></li><li><span><a href="#-Комментарий-ревьюера-v1" data-toc-modified-id="-Комментарий-ревьюера-v1-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span> Комментарий ревьюера v1</a></span></li></ul></li><li><span><a href="#Анализ-данных" data-toc-modified-id="Анализ-данных-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Анализ данных</a></span><ul class="toc-item"><li><span><a href="#Концентрация-металлов-(Au,-Ag,-Pb)-на-различных-этапах-очистки" data-toc-modified-id="Концентрация-металлов-(Au,-Ag,-Pb)-на-различных-этапах-очистки-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Концентрация металлов (Au, Ag, Pb) на различных этапах очистки</a></span></li><li><span><a href="#-Комментарий-ревьюера-v1" data-toc-modified-id="-Комментарий-ревьюера-v1-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span> Комментарий ревьюера v1</a></span><ul class="toc-item"><li><span><a href="#Вывод-по-этапам-очистки" data-toc-modified-id="Вывод-по-этапам-очистки-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Вывод по этапам очистки</a></span></li></ul></li><li><span><a href="#Распределения-размеров-гранул-сырья-на-обучающей-и-тестовой-выборках" data-toc-modified-id="Распределения-размеров-гранул-сырья-на-обучающей-и-тестовой-выборках-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Распределения размеров гранул сырья на обучающей и тестовой выборках</a></span><ul class="toc-item"><li><span><a href="#Вывод-поразмерам-гранул" data-toc-modified-id="Вывод-поразмерам-гранул-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>Вывод поразмерам гранул</a></span></li></ul></li><li><span><a href="#-Комментарий-ревьюера-v1" data-toc-modified-id="-Комментарий-ревьюера-v1-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span> Комментарий ревьюера v1</a></span></li><li><span><a href="#-Комментарий-ревьюера-v2" data-toc-modified-id="-Комментарий-ревьюера-v2-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span> Комментарий ревьюера v2</a></span></li><li><span><a href="#Cуммарная-концентрация-всех-веществ-на-разных-стадиях:-в-сырье,-в-черновом-и-финальном-концентратах." data-toc-modified-id="Cуммарная-концентрация-всех-веществ-на-разных-стадиях:-в-сырье,-в-черновом-и-финальном-концентратах.-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Cуммарная концентрация всех веществ на разных стадиях: в сырье, в черновом и финальном концентратах.</a></span></li><li><span><a href="#-Комментарий-ревьюера-v1" data-toc-modified-id="-Комментарий-ревьюера-v1-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span> Комментарий ревьюера v1</a></span></li><li><span><a href="#-Комментарий-ревьюера-v1" data-toc-modified-id="-Комментарий-ревьюера-v1-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span> Комментарий ревьюера v1</a></span><ul class="toc-item"><li><span><a href="#Вывод-по-концентрации" data-toc-modified-id="Вывод-по-концентрации-2.8.1"><span class="toc-item-num">2.8.1&nbsp;&nbsp;</span>Вывод по концентрации</a></span></li></ul></li><li><span><a href="#Вывод-по-разделу" data-toc-modified-id="Вывод-по-разделу-2.9"><span class="toc-item-num">2.9&nbsp;&nbsp;</span>Вывод по разделу</a></span></li></ul></li><li><span><a href="#Модель" data-toc-modified-id="Модель-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Модель</a></span><ul class="toc-item"><li><span><a href="#-Комментарий-ревьюера-v1" data-toc-modified-id="-Комментарий-ревьюера-v1-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span> Комментарий ревьюера v1</a></span></li><li><span><a href="#-Комментарий-ревьюера-v1" data-toc-modified-id="-Комментарий-ревьюера-v1-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span> Комментарий ревьюера v1</a></span></li><li><span><a href="#-Комментарий-ревьюера-v1" data-toc-modified-id="-Комментарий-ревьюера-v1-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span> Комментарий ревьюера v1</a></span></li><li><span><a href="#Вывод-по-разделу" data-toc-modified-id="Вывод-по-разделу-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Вывод по разделу</a></span></li></ul></li><li><span><a href="#Общий-вывод" data-toc-modified-id="Общий-вывод-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Общий вывод</a></span></li><li><span><a href="#Чек-лист-готовности-проекта" data-toc-modified-id="Чек-лист-готовности-проекта-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Чек-лист готовности проекта</a></span><ul class="toc-item"><li><span><a href="#-Итоговый-комментарий" data-toc-modified-id="-Итоговый-комментарий-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span> Итоговый комментарий</a></span></li><li><span><a href="#-Комментарий-ревьюера-v2" data-toc-modified-id="-Комментарий-ревьюера-v2-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span> Комментарий ревьюера v2</a></span></li></ul></li></ul></div>

# # Восстановление золота из руды

# Подготовьте прототип модели машинного обучения для «Цифры». Компания разрабатывает решения для эффективной работы промышленных предприятий.
# 
# Модель должна предсказать коэффициент восстановления золота из золотосодержащей руды. Используйте данные с параметрами добычи и очистки. 
# 
# Модель поможет оптимизировать производство, чтобы не запускать предприятие с убыточными характеристиками.
# 
# Вам нужно:
# 
# 1. Подготовить данные;
# 2. Провести исследовательский анализ данных;
# 3. Построить и обучить модель.
# 
# Чтобы выполнить проект, обращайтесь к библиотекам *pandas*, *matplotlib* и *sklearn.* Вам поможет их документация.

# ## Подготовка данных

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import mean_absolute_error, make_scorer, mean_squared_error
from sklearn.dummy import DummyRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV, cross_validate, KFold
import warnings
warnings.filterwarnings("ignore")


# In[2]:


train = pd.read_csv('/datasets/gold_recovery_train_new.csv')
test = pd.read_csv('/datasets/gold_recovery_test_new.csv')
full = pd.read_csv('/datasets/gold_recovery_full_new.csv')


# In[3]:


full.info()


# In[4]:


test.info()


# In[5]:


train.info()


# In[6]:


train.duplicated().sum()


# In[7]:


test.duplicated().sum()


# In[8]:


full.duplicated().sum()


# In[9]:


train.isna().sum().sum()


# In[10]:


test.isna().sum().sum()


# In[11]:


full.isna().sum().sum()


# In[12]:


train['rougher.output.recovery']


# Вывод:  
# В датасете full 19439 строк и 87 столбцов, нет явных дубликатов и 4481 пропуск  
# В датасете train 14149 строк и 87 столбцов, нет явных дубликатов и 4100 пропусков  
# В датасете test 5290 строк и 53 столбца, нет явных дубликатов и 90 пропусков

# <div class="alert alert-success"> ✅ 
# <h3> Комментарий ревьюера v1</h3>
# 
# Данные загружены, первичный осмотр и выводы корректные
# 

# Создаем функцию, которая будет проверять эффективность обогащения

# In[13]:


def efficiency_check(C, F, T):
    numerator = (C*(F-T))
    denominator =(F*(C-T))
    total = numerator / denominator * 100
    return total


# In[14]:


recovery=train.dropna().reset_index()
rougher_output_recovery=recovery['rougher.output.recovery'] # база
rougher_output_tail_au=recovery['rougher.output.tail_au'] # доля золота в отвальных хвостах после флотации/очистки
rougher_input_feed_au=recovery['rougher.input.feed_au'] # доля золота в сырье/концентрате до флотации/очистки
rougher_output_concentrate_au=recovery['rougher.output.concentrate_au'] # доля золота в концентрате после флотации/очистки


# In[15]:


total = efficiency_check(rougher_output_concentrate_au,rougher_input_feed_au,rougher_output_tail_au)
total


# In[16]:


total.min()


# In[17]:


total.max()


# Как мы видим значения лежат между 0 и 100, что соотвествует логике и накладывать ограничения смысла нет

# In[18]:


mean_absolute_error(total,rougher_output_recovery)


# Можно сказать, что значения посчитаны в целом верно

# 
# <div class="alert alert-success"> ✅ 
# <h3> Комментарий ревьюера v1</h3>
# 
# Верно, полученное значение оказалось в достаточной степени маленьким, чтобы можно было утверждать о правильности рассчёта.
# 
# 

# In[19]:


test_col = test.columns
full_col = full.columns


# In[20]:


main_list = set(full_col)-set(test_col)


# In[21]:


main_list = list(main_list)


# In[22]:


main_list=pd.Series(main_list)
main_list.sort_values()


# **Предобработка**

# In[23]:


full['date']


#  Вообще данные индексируются датой и временем получения информаци по признаку date. Не вижу особого смысла распространеться на этот признак. Так как пропусков не так много чтобы это было проблемой, соседние показатели часто похожи поэтому можно заменить пропуски на значения впереди благодаря методу `ffill`

# In[24]:


full=full.fillna(method='ffill')
train=train.fillna(method='ffill') 
test=test.fillna(method='ffill')


# <div class="alert alert-success"> ✅ 
# <h3> Комментарий ревьюера v1</h3>
# 
# Хорошо, что внимательно читаешь задание =) Тут было бы неправильно заполнять медианой или средним, так как значения фичей сильно зависят от этапа обработки
# 
# PS заполнить пропуски также можно было методами pandas: bfill/ interpolate , это вполне уместно. Хочу посоветовать тебе статью, которая рассматривает разные способы обработки пропусков, выделяет их плюсы и минусы, думаю, тебе может быть интересно: https://loginom.ru/blog/missing
# 
# 

# In[25]:


display(full.isna().sum().sum())
display(train.isna().sum().sum())
display(test.isna().sum().sum())


# ### Вывод по блоку:  
# Средняя абсолютная ошибка равна 9.82970122149377e-15, можно сказать, что значения посчитаны в целом верно.  
# Также в датасетах былии обнаружены пропуски  
# В test пропущены фичи после каждой фазы производства. Кроме того есть наш целевой признак final.output.

# <div class="alert alert-warning"> ⚠️
# <h3> Комментарий ревьюера v1</h3>
# 
# Точнее в тестах отсутствуют выходные (output) и расчетные (calculation) характеристики. Значит, их нельзя использовать при обучении, так как они еще не будут доступны к моменту начала процесса

# ## Анализ данных

# ###  Концентрация металлов (Au, Ag, Pb) на различных этапах очистки

# Создаем датафрейм содержащий все требуемые концентрации и исследуем их на графиках. Повторим для первичной, вторичной и финальной обработки

# In[26]:


rougher_input_feed_ = []
rougher_input_feed_ = pd.DataFrame(rougher_input_feed_)
rougher_input_feed_['rougher.input.feed_ag'] = full['rougher.input.feed_ag']
rougher_input_feed_['rougher.input.feed_pb'] = full['rougher.input.feed_pb']
rougher_input_feed_['rougher.input.feed_au'] = full['rougher.input.feed_au']


# In[27]:


plt.figure(figsize=(20,10))
a = sns.set(style="darkgrid")
a = sns.boxplot(data=rougher_input_feed_)
plt.title('Входная концентрация металлов', fontsize=22)
plt.show()


# In[28]:


primary_concetrates = []
primary_concetrates = pd.DataFrame(primary_concetrates)
primary_concetrates['primary_cleaner.output.concentrate_ag']=full['primary_cleaner.output.concentrate_ag']
primary_concetrates['primary_cleaner.output.concentrate_pb']=full['primary_cleaner.output.concentrate_pb']
primary_concetrates['primary_cleaner.output.concentrate_au']=full['primary_cleaner.output.concentrate_au']


# In[29]:


plt.figure(figsize=(20,10))
a = sns.set(style="darkgrid")
a = sns.boxplot(data=primary_concetrates)
plt.title('Концентрация металлов первичная очистка', fontsize=22)
plt.show()


# In[30]:


final_output_concentrate = []
final_output_concentrate = pd.DataFrame(final_output_concentrate)
final_output_concentrate['final.output.concentrate_ag']=full['final.output.concentrate_ag']
final_output_concentrate['final.output.concentrate_pb']=full['final.output.concentrate_pb']
final_output_concentrate['final.output.concentrate_au']=full['final.output.concentrate_au']


# In[31]:


plt.figure(figsize=(20,10))
a = sns.set(style="darkgrid")
a = sns.boxplot(data = final_output_concentrate)
plt.title('Концентрация металлов финальная очистка', fontsize=22)
plt.show()


# **Вывод по диаграмме размаха**
# По "ящикам с усами" видно, что для всех металлов существуют выбросы. Для всех металлов с ходом очистки увеличивается количество выбросов

# <div class="alert alert-danger"> ❌
# <h3> Комментарий ревьюера v1</h3>
# 
# Разве? Кажется, ты не те этапы используешь.
#     
# 
# Нужны этапы: 
#     
#     rougher.input.feed_
#     rougher.output.concentrate_
#     final.output.concentrate_
#     

# <div class="alert alert-block alert-info"><b>Комментарий студента</b>
#     
# <b>Изменения:</b> Согласен, со вторичной я напутал. Зачем я хвосты (tail) исследовал...Но все равно, мне кажется, задание требует посмотреть `концентрацию` именно в процессе очистки, а то есть:  
#     флотация - `rougher.output.concentrate_`  
#     первичная - `primary_cleaner.output.concentrate_`   
#     финальная - `final.output.concentrate_`  
# Но я добалю `rougher.input.feed_` -входной<br></div> 

# Вероятно большенство нулей на графиках являеются нечем иным как выбросами, если их не учесть можно попасть в неприятную ситуацию

# In[32]:


full = full[full['primary_cleaner.output.concentrate_ag'] > 0]
full = full[full['primary_cleaner.output.concentrate_pb'] > 0]
full = full[full['primary_cleaner.output.concentrate_au'] > 0]

full = full[full['rougher.input.feed_ag'] > 0]
full = full[full['rougher.input.feed_pb'] > 0]
full = full[full['rougher.input.feed_au'] > 0]

full = full[full['final.output.concentrate_ag'] > 0]
full = full[full['final.output.concentrate_pb'] > 0]
full = full[full['final.output.concentrate_au'] > 0]


# In[33]:


primary_concetrates = []
primary_concetrates = pd.DataFrame(primary_concetrates)
primary_concetrates['primary_cleaner.output.concentrate_ag']=full['primary_cleaner.output.concentrate_ag']
primary_concetrates['primary_cleaner.output.concentrate_pb']=full['primary_cleaner.output.concentrate_pb']
primary_concetrates['primary_cleaner.output.concentrate_au']=full['primary_cleaner.output.concentrate_au']

rougher_input_feed_ = []
rougher_input_feed_ = pd.DataFrame(rougher_input_feed_)
rougher_input_feed_['rougher.input.feed_ag'] = full['rougher.input.feed_ag']
rougher_input_feed_['rougher.input.feed_pb'] = full['rougher.input.feed_pb']
rougher_input_feed_['rougher.input.feed_au'] = full['rougher.input.feed_au']

final_output_concentrate = []
final_output_concentrate = pd.DataFrame(final_output_concentrate)
final_output_concentrate['final.output.concentrate_ag']=full['final.output.concentrate_ag']
final_output_concentrate['final.output.concentrate_pb']=full['final.output.concentrate_pb']
final_output_concentrate['final.output.concentrate_au']=full['final.output.concentrate_au']


# In[34]:


plt.figure(figsize=(20,10), dpi= 80)
sns.kdeplot(rougher_input_feed_['rougher.input.feed_ag'], shade=True, color="g", label="AG", alpha=.7)
sns.kdeplot(rougher_input_feed_['rougher.input.feed_pb'], shade=True, color="k", label="PB", alpha=.7)
sns.kdeplot(rougher_input_feed_['rougher.input.feed_au'], shade=True, color="gold", label="AU", alpha=.7)

plt.title('Входная концентрация металлов', fontsize=22)
plt.xlabel("% Metal concentrate")
plt.ylabel("Friqency")
plt.legend()
plt.show()
print("Среднее для AG:",rougher_input_feed_['rougher.input.feed_ag'].mean())
print("Среднее для PB:",rougher_input_feed_['rougher.input.feed_pb'].mean())
print("Среднее для AU:",rougher_input_feed_['rougher.input.feed_au'].mean())


# In[35]:


plt.figure(figsize=(20,10), dpi= 80)
sns.kdeplot(primary_concetrates['primary_cleaner.output.concentrate_ag'], shade=True, color="g", label="AG", alpha=.7)
sns.kdeplot(primary_concetrates['primary_cleaner.output.concentrate_pb'], shade=True, color="k", label="PB", alpha=.7)
sns.kdeplot(primary_concetrates['primary_cleaner.output.concentrate_au'], shade=True, color="gold", label="AU", alpha=.7)

plt.title('Концентрация металлов первичная очистка', fontsize=22)
plt.xlabel("% Metal concentrate")
plt.ylabel("Friqency")
plt.legend()
plt.show()
print("Среднее для AG:", primary_concetrates['primary_cleaner.output.concentrate_ag'].mean())
print("Среднее для PB:",primary_concetrates['primary_cleaner.output.concentrate_pb'].mean())
print("Среднее для AU:",primary_concetrates['primary_cleaner.output.concentrate_au'].mean())


# In[36]:


plt.figure(figsize=(20,10), dpi= 80)
sns.kdeplot(final_output_concentrate['final.output.concentrate_ag'], shade=True, color="g", label="AG", alpha=.7)
sns.kdeplot(final_output_concentrate['final.output.concentrate_pb'], shade=True, color="k", label="PB", alpha=.7)
sns.kdeplot(final_output_concentrate['final.output.concentrate_au'], shade=True, color="gold", label="AU", alpha=.7)

plt.title('Концентрация металлов финальная очистка', fontsize=22)
plt.xlabel("% Metal concentrate")
plt.ylabel("Friqency")
plt.legend()
plt.show()
print("Среднее для AG:", final_output_concentrate['final.output.concentrate_ag'].mean())
print("Среднее для PB:",final_output_concentrate['final.output.concentrate_pb'].mean())
print("Среднее для AU:",final_output_concentrate['final.output.concentrate_au'].mean())


# **Вывод по концентрации**  
# Можно заметить, что каждая процедура очистки влияет на содержание металлов в веществе. Содержание Золота - как наш главный показатель, по итогу возрасло с 32 до 44, значение Серебра упало с 8 до 5, а вот значения для свинца даже немного возрасли после всей очистки с 9,8 до 10

# Посмотрим что происходит с содержанием металлов на этапе флотации

# In[37]:


plt.figure(figsize=(20,10), dpi= 80)
sns.kdeplot(full['rougher.output.concentrate_ag'], shade=True, color="g", label="AG", alpha=.7)
sns.kdeplot(full['rougher.output.concentrate_pb'], shade=True, color="k", label="PB", alpha=.7)
sns.kdeplot(full['rougher.output.concentrate_au'], shade=True, color="gold", label="AU", alpha=.7)

plt.title('Концентрация металлов флотация', fontsize=22)
plt.xlabel("% Metal concentrate")
plt.ylabel("Friqency")
plt.legend()
plt.show()
print("Среднее для AG:", full['rougher.output.concentrate_ag'].mean())
print("Среднее для PB:",full['rougher.output.concentrate_pb'].mean())
print("Среднее для AU:",full['rougher.output.concentrate_au'].mean())


# #### Вывод по этапам очистки
# По сравнению с входным концентратом произошли слудующие изменения  
# Концентрация:  
# Золота увеличилась в 9,8 раз  
# Серебра уменьшилась в 3 раза  
# Свинца увеличилась в 1,6 раз

# ### Распределения размеров гранул сырья на обучающей и тестовой выборках

# In[38]:


feed_size = []
feed_size = pd.DataFrame(feed_size)
feed_size['primary_cleaner.input.feed_size']=train['primary_cleaner.input.feed_size']
feed_size['rougher.input.feed_size']=train['rougher.input.feed_size']
feed_size['primary_cleaner.input.feed_size']=test['primary_cleaner.input.feed_size']
feed_size['rougher.input.feed_size']=test['rougher.input.feed_size']


# In[39]:


feed_size.describe()


# In[40]:


#for k in ['rougher', 'primary_cleaner']:
     #plt.hist(train[f'{k}.input.feed_size'], color ='b', label='Обучающая выборка', bins=50, alpha=0.5, density=True)
     #plt.hist(test[f'{k}.input.feed_size'], color ='r',label='Тестовая выборка', bins=50, alpha=0.5, density=True)

    #plt.xlabel('Размер гранул сырья')
    #plt.ylabel('Частота')
    #plt.title('Распределениие размеров гранул сырья')
    #plt.grid(alpha=0.1)
    #plt.rcParams['figure.figsize']=[10,20]
    #plt.legend()
    #plt.show|
    
    #display(f'Характеристикаи распределения размеров гранул сырья на обучающей выборке:', train[f'{k}.input.feed_size'].agg(['mean','std']))
    #display(f'Характеристикаи распределения размеров гранул сырья на тестовой выборке:', test[f'{k}.input.feed_size'].agg(['mean','std']))


# In[41]:


train['rougher.input.feed_size'].hist(color ='b', label='Обучающая выборка',figsize=(9,6), bins=50, alpha=0.5, density=True)
test['rougher.input.feed_size'].hist(color ='r',label='Тестовая выборка', figsize=(9,6), bins=50, alpha=0.5, density=True)
plt.xlabel('Размер гранул сырья')
plt.ylabel('Частота')
plt.title('Распределениие размеров гранул сырья')
plt.xlim(0, 150)
display(f'Характеристикаи распределения размеров гранул сырья на обучающей выборке:', train[f'rougher.input.feed_size'].agg(['mean','std']))
display(f'Характеристикаи распределения размеров гранул сырья на тестовой выборке:', test[f'rougher.input.feed_size'].agg(['mean','std']))


# In[42]:


train['primary_cleaner.input.feed_size'].hist(color ='b', label='Обучающая выборка',figsize=(9,6), bins=50, alpha=0.5, density=True)
test['primary_cleaner.input.feed_size'].hist(color ='r',label='Тестовая выборка', figsize=(9,6),bins=50, alpha=0.5, density=True)
plt.xlabel('Размер гранул сырья')
plt.ylabel('Частота')
plt.title('Распределениие размеров гранул сырья')
plt.xlim(0, 30)
display(f'Характеристикаи распределения размеров гранул сырья на обучающей выборке:', train[f'primary_cleaner.input.feed_size'].agg(['mean','std']))
display(f'Характеристикаи распределения размеров гранул сырья на тестовой выборке:', test[f'primary_cleaner.input.feed_size'].agg(['mean','std']))


# In[43]:


# ЯЧЕЙКА РЕВЬЮЕРА

train['rougher.input.feed_size'].hist(bins=50, figsize=(9,6), density=True)
test['rougher.input.feed_size'].hist(bins=50, figsize=(9,6), density=True)
plt.xlim(0, 150)


# In[44]:


# ЯЧЕЙКА РЕВЬЮЕРА

train['primary_cleaner.input.feed_size'].hist(bins=100, figsize=(9,6), density=True)
test['primary_cleaner.input.feed_size'].hist(bins=100, figsize=(9,6), density=True)
plt.xlim(0, 30)


# #### Вывод поразмерам гранул  
# Как видно из таблицы данные по первичной обработке для тестовой и обучающей выборке почтии не отличаются, совсем немного отличается среднее (на 0,055971) и минимальные и максимальные значения.    
# Для флотации разниц чуть больше в среднем - 4,288759 и в std на 3,923552  
# В принципе разницы буквально нет и такая разница в концентрации  данных модели не помешает

# <div class="alert alert-danger"> ❌
# <h3> Комментарий ревьюера v1</h3>
# 
# Сложно говорить о распределениях, не видя их графически. Тут корректнее строить графики плотности, так как количество данных в train/test датасетах отличается. Например, с помощью `sns.distplot()` или же просто добавить `density=True` в параметры `plt.hist()`.
# 

# <div class="alert alert-block alert-info"><b>Комментарий студента</b>
#     
# <b>Изменения:</b> На самом деле видел как делать график на семинаре, но я ума не приложу почему он у меня не получается и что за выбросы у нуля...<br></div> 

# <div class="alert alert-danger"> ❌
# 
# <h3> Комментарий ревьюера v2</h3>
# 
# Что-то с масштабом не так еще =) Я выше построил графики выбрав другие значения параметров, все ок выглядит теперь

# <div class="alert alert-block alert-info"><b>Комментарий студента</b>
#     
# <b>Изменения:</b> Исправил под свой лад, так и не понял как работал код у чела тут - 33 минута:  
#     https://disk.yandex.ru/d/UFhYWRKg6y-UYg/video1871620095.mp4   
#     Но для меня конечно главное - это просто сдать ))  
#     а то времени нет<br></div> 

# ###  Cуммарная концентрация всех веществ на разных стадиях: в сырье, в черновом и финальном концентратах. 

# In[45]:


# Сумма концентраций метраллов входного сырья
full['sum_concentrate_rougher_input'] = full['rougher.input.feed_ag']+full['rougher.input.feed_pb']+full['rougher.input.feed_sol']+full['rougher.input.feed_au']


# In[46]:


# Сумма концентраций металлов после первичной очистки
full['sum_rougher.output.concentrate']=full['rougher.output.concentrate_ag']+full['rougher.output.concentrate_pb']+full['rougher.output.concentrate_sol']+full['rougher.output.concentrate_au']


# In[47]:


# Сумма концентраций металлов после финальной очистки
full['sum_final_output_concentrate']=full['final.output.concentrate_ag']+full['final.output.concentrate_pb']+full['final.output.concentrate_sol']+full['final.output.concentrate_au']


# <div class="alert alert-danger"> ❌
# <h3> Комментарий ревьюера v1</h3>
# 
# В задании требуется следующее: Исследуйте суммарную концентрацию всех веществ на разных стадиях: в сырье, в черновом и финальном концентратах.
#     
# 
# в сырье — это столбец rougher.input.feed_
# 
# в черновом концентрате - это столбец rougher.output.concentrate_
# 
# в финальном концентрате - это столбец final.output.concentrate_ 
# 

# In[48]:


# Итог
sum_concentrate=['sum_concentrate_rougher_input','sum_rougher.output.concentrate','sum_final_output_concentrate']


# In[49]:


plt.figure(figsize=(20,10), dpi= 80)
sns.kdeplot(full['sum_concentrate_rougher_input'], shade=True, color="g", label="Флотация", alpha=.7)
sns.kdeplot(full['sum_rougher.output.concentrate'], shade=True, color="c", label="Первичная обработка", alpha=.7)
sns.kdeplot(full['sum_final_output_concentrate'], shade=True, color="gold", label="Финальная обработка", alpha=.7)

plt.title('Общая концентрация металлов', fontsize=22)
plt.xlabel("% Metal concentrate")
plt.ylabel("Friqency")
plt.legend()
plt.show()
print("Среднее для входного материала:", full['sum_concentrate_rougher_input'].mean())
print("Среднее для пеервичной обработки:",full['sum_rougher.output.concentrate'].mean())
print("Среднее для финальной обработки:",full['sum_final_output_concentrate'].mean())


# На самом деле заметно, что значения до 40 особого смысла для графика не несут и поэтому их нужно удалить

# <div class="alert alert-success"> ✅ 
# <h3> Комментарий ревьюера v1</h3>
# 
# Все верно, такие выбросы маловероятны, лучше их убрать.
# 
# 

# In[50]:


full = full[full['sum_final_output_concentrate'] > 40]
full = full[full['sum_rougher.output.concentrate'] > 40]
full = full[full['sum_concentrate_rougher_input'] > 40]


# In[51]:


plt.figure(figsize=(20,10), dpi= 80)
sns.kdeplot(full['sum_concentrate_rougher_input'], shade=True, color="g", label="Флотация", alpha=.7)
sns.kdeplot(full['sum_rougher.output.concentrate'], shade=True, color="c", label="Первичная обработка", alpha=.7)
sns.kdeplot(full['sum_final_output_concentrate'], shade=True, color="gold", label="Финальная обработка", alpha=.7)

plt.title('Общая концентрация металлов', fontsize=22)
plt.xlabel("% Metal concentrate")
plt.ylabel("Friqency")
plt.legend()
plt.show()
print("Среднее для входного материала:", full['sum_concentrate_rougher_input'].mean())
print("Среднее для первичной обработки:",full['sum_rougher.output.concentrate'].mean())
print("Среднее для финальной обработки:",full['sum_final_output_concentrate'].mean())


# Так как мы убрали эти 40% из full выборки нужно убрать их и из train, чтобы не путать модель

# In[52]:


train['sum_concentrate_rougher_input'] = train['rougher.input.feed_ag']+train['rougher.input.feed_pb']+train['rougher.input.feed_sol']+train['rougher.input.feed_au']


# In[53]:


train['sum_rougher.output.concentrate']=train['rougher.output.concentrate_ag']+train['rougher.output.concentrate_pb']+train['rougher.output.concentrate_sol']+train['rougher.output.concentrate_au']


# In[54]:


train['sum_final_output_concentrate']=train['final.output.concentrate_ag']+train['final.output.concentrate_pb']+train['final.output.concentrate_sol']+train['final.output.concentrate_au']


# In[55]:


train=train[train['sum_final_output_concentrate']>40]
train=train[train['sum_rougher.output.concentrate']>40]
train=train[train['sum_concentrate_rougher_input']>40]
train=train.reset_index()


# In[56]:


plt.figure(figsize=(20,10), dpi= 80)
sns.kdeplot(train['sum_concentrate_rougher_input'], shade=True, color="g", label="Входной", alpha=.7)
sns.kdeplot(train['sum_rougher.output.concentrate'], shade=True, color="c", label="Первичная обработка", alpha=.7)
sns.kdeplot(train['sum_final_output_concentrate'], shade=True, color="gold", label="Финальная обработка", alpha=.7)

plt.title('Общая концентрация металлов', fontsize=22)
plt.xlabel("% Metal concentrate")
plt.ylabel("Friqency")
plt.legend()
plt.show()
print("Среднее для входного материала:", train['sum_concentrate_rougher_input'].mean())
print("Среднее для первичной обработки:",train['sum_rougher.output.concentrate'].mean())
print("Среднее для финальной обработки:",train['sum_final_output_concentrate'].mean())


# In[57]:


plt.figure(figsize=(7,7))
b = sns.set(style="darkgrid")
b = sns.boxplot(data=train['sum_concentrate_rougher_input'])


# #### Вывод по концентрации  
# Заметно, что во время флотации данные находятся на нормальном распределении с четковыраженным максимум и постепенно убывающими краями. Первичная обработка уменьшает концентрацию металлов в веществе почти на 5-10%. Финальная же обработка выдает на выход ярко выраженное вещество с концентрацией вокруг 69% и дает более частое распределениие данных вокруг 69%

# ### Вывод по разделу
# 1. Было обнаружено, что концентрация металлов растет на этапе первичной очистки, а потом убывает на вторичной, однако, по итогу на выходе получается вещество, которое более насыщенно золотом, чем на входе. Однако, важное заамечание, что концентрация свинца почти не выводится из смеси сппустя все этапы обработки.  
# 2. Распеределение размера гранул на тренироовочной и теестовой выборке было исследовано и сильной разницы в концентрации обнаружено не было
# 3. Суммарная концентрация металлов незначительно увеличивается на первичной обработке. На финальной стадии обработки видно качественное увелечение смеси до 70%

# ## Модель

# - Пишем функцию sMAPE по образцу
# - Подготавливаем данные к последующему построению моделей

# ![Image%20%283%29.png](attachment:Image%20%283%29.png)

# In[58]:


def smape(target, pred):
    smape = abs(target - pred) / ((abs(target) + abs(pred))/2) * 100
    smape = smape.fillna(value=0)
    smape = sum(smape)/len(smape)
    return smape


# In[59]:


train = train[test.columns]


# In[60]:


needed_target = full.loc[:,['date','rougher.output.recovery','final.output.recovery']]


# In[61]:


train = train.merge(needed_target, on='date')
test = test.merge(needed_target, on='date')


# In[62]:


test.columns


# In[63]:


x_train_r = train.drop(['rougher.output.recovery', 'final.output.recovery', 'date'], axis=1)
x_test_r = test.drop(['rougher.output.recovery', 'final.output.recovery', 'date'], axis=1)

y_train_r = train['rougher.output.recovery']
y_test_r = test['rougher.output.recovery']

x_train_f = train.drop(['rougher.output.recovery', 'final.output.recovery', 'date'], axis=1)
x_test_f = test.drop(['rougher.output.recovery', 'final.output.recovery', 'date'], axis=1)

y_train_f = train['final.output.recovery']
y_test_f = test['final.output.recovery']


# - Подгатавливаем целевой признак и остальные признаки 
# - Удаляем лишний столбец, который лишь будет мешать обучению моделей
# - Прописываем random_state

# In[64]:


rs=12345


# In[65]:


pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestRegressor(n_estimators=120, random_state=rs))
])

params = [
    {
        'model': [RandomForestRegressor(n_estimators=15, random_state=rs)],
        'model__max_features': np.linspace(0.1, 1, 10)
    }, {
        'model': [LinearRegression()]
    }
]


# - Для обучения и анализа будем использовать 2 модели: `Random Forest Regressor, Linear Regression`
# - С помощью `GridSearchCV` подберем наиболее "удачные" параметры
# - Преобразуем исследуемую метрику в объект оценки (score) для последующей работы над кросс валидацией. Используем метод make_scorer из библиотеки sklearn. Чем меньше smape тем лучше качество модели, поэтому для нас минимум smape - лучший результат для этого напишем параметр greater_is_better=False

# - Подготовим значения SMAPE для подбора `GridSearchCV`, с помощью функции `make_scorer`

# In[66]:


smape_score = make_scorer(smape, greater_is_better=False)


# <div class="alert alert-success"> ✅ 
# <h3> Комментарий ревьюера v1</h3>
# 
# `greater_is_better=False` - отлично! Обычно забывают, что нам нужно минимизировать функцию, а дефолтно она максимизируется=)
# 
# Немного про кастомный скоринг и параметр `greater_is_better=False` в `make_scorer` : вот очень хорошая статья - https://kiwidamien.github.io/custom-loss-vs-custom-scoring.html
#     
# Если кратко, то твой результат при использовании cross_val_score со своей метрикой и флагом `greater_is_better=False` остается таким же, только с отрицательным значением (знак минус - особенность библиотечной реализации скорера, можно брать значения по модулю), так как есть метрика (по которой мы выбираем модель) и есть лосс (по которой обучается модель). Так вот make_scorer создает метрику из лосса, по которой ты выбираешь лучшую модель, но сама модель будет обучаться по встроенной функции потерь (скорее всего MSE), так что это нужно только для выбора модели. Просто принято ставить флаг greater_is_better=False для метрик, которые являются лоссами (не все метрики лоссы, например, recall, precision и тп).
#     
# НО если ты используешься гридсерч, то `greater_is_better=False` нужно указывать обязательно, так как best_estimator_ выбирает лучшую модель по метрике уже самостоятельно =)
# 
# 
# 

#  Проводим кросс-валидацию (с помощью `KFold`) и делим данные на 5 частей

# In[67]:


cv = KFold(n_splits=5, shuffle=False)
grid_r = GridSearchCV(pipe, param_grid=params, cv=cv, n_jobs=-1, scoring=smape_score)


# <div class="alert alert-warning"> ⚠️
# <h3> Комментарий ревьюера v1</h3>
# 
# Обычный GridSearchCV довольно долго делает расчеты, так как проверяет все комбинации. На практике обычно какие-то параметры сильно важнее других, поэтому по ним нет особого смысла итерироваться, поэтому рекомендую использовать RandomizedSearchCV. Скорее всего ты немного просядешь по метрикам, зато сильно выиграешь в скорости обучения. А еще очень советую изучить, как работать с либой optuna для подбора параметров
# 
# 

# <div class="alert alert-block alert-info"><b>Комментарий студента</b>
#     
# <b>Изменения:</b> Да, окей спасибо! Для учебный проектов RandomizedSearchCV конечно лучше подойдет. Учту в следующий проектах<br></div> 

# In[68]:


get_ipython().run_cell_magic('time', '', 'grid_r.fit(x_train_r, y_train_r)')


# In[69]:


print('Лучшие параметры:', grid_r.best_params_)
print('Лучшее sMAPE значение:', -grid_r.best_score_)


# In[70]:


grid_f = GridSearchCV(pipe, param_grid=params, cv=cv, n_jobs=-1, scoring=smape_score)


# In[71]:


get_ipython().run_cell_magic('time', '', 'grid_f.fit(x_train_f, y_train_f)')


# - Подбираем параметры

# In[72]:


print('Лучшие параметры:', grid_f.best_params_)
print('Лучшее sMAPE значение:', -grid_f.best_score_)


# - Подставляем лучшие параметры в модель и высчитываем sMAPE(rougher)

# In[73]:


pipe_r = grid_r.best_estimator_

pipe_r.fit(x_train_r, y_train_r)
y_pred = pipe_r.predict(x_test_r)

smape_r = smape(full['rougher.output.recovery'].iloc[x_test_r.index], y_pred)
print('Значение sMAPE(rougher):', smape_r)


# In[74]:


pipe_f = grid_f.best_estimator_
    
pipe_f.fit(x_train_f, y_train_f)
y_pred_f = pipe_f.predict(x_test_f)

smape_f = smape(full['final.output.recovery'].iloc[x_test_f.index],y_pred_f)
print('Значение sMAPE(final):', smape_f)


# - Подставляем лучшие параметры в модель и высчитываем sMAPE(final)

# In[75]:


final_smape = 0.25 * smape_r + 0.75 * smape_f
print('Итоговое значение sMAPE:', final_smape)


# - Высчитываем итоговое значение sMAPE

# In[76]:


median_r = pd.Series(y_train_r.median(), index=y_test_r.index)
median_f = pd.Series(y_train_f.median(), index=y_test_f.index)

median_smape_r = smape(y_test_r, median_r)
median_smape_f = smape(y_test_f, median_f)

res = (median_smape_r*0.25) + (median_smape_f* 0.75)
print('median_smape_r:', median_smape_r)
print('median_smape_f:', median_smape_f)
print('Значение sMAPE для медианной модели:', res)


# In[77]:


first_model = pipe_r.score(x_test_r, y_test_r)
secound_model = pipe_f.score(x_test_f,y_test_f)

dummy_model_1 = DummyRegressor(strategy='mean', constant=None, quantile=None)
dummy_model_1.fit(x_train_r, y_train_r)
dummy_model_1.predict(y_test_r)
score_dummy_1 = dummy_model_1.score(x_test_r,y_test_r)

dummy_model_2 = DummyRegressor(strategy='mean', constant=None, quantile=None)
dummy_model_2.fit(x_train_f, y_train_f)
dummy_model_2.predict(y_test_f)
score_dummy_2 = dummy_model_2.score(x_test_f,y_test_f)

print('Первая модель:', first_model)
print('Вторая модель:', secound_model)
print('DummyRegressor_1:', score_dummy_1)
print('DummyRegressor_2:', score_dummy_2)


# Как мы видим наши результаты(R2) получились лучше константной модели

# <div class="alert alert-danger"> ❌
# <h3> Комментарий ревьюера v1</h3>
# 
# Желательно сравнить с константной моделью, например с DummyRegressor. Из одного значения метрики не ясно, насколько адекватны предсказания моделей
# 
# 

# ### Вывод по разделу
# Были построены модели и улучшены благодаря GridSearchCV  
# Лучше себя показала модель RandomForestRegressor с медианным показателем smape = 4.69

# ## Общий вывод
# 
# 1) Данные были исследованы и обработаны  
# 2) Проведен исследовательский анализ данных  
# 3) Построены модели и была выбрана наилучшая    
# 4) Была написана функция для вычисления sMAPE. С помощью кросс-валидации и `GridSearchCV` были подобраны лучшие параметры для  моделей

# ## Чек-лист готовности проекта

# - [x]  Jupyter Notebook открыт
# - [ ]  Весь код выполняется без ошибок
# - [ ]  Ячейки с кодом расположены в порядке выполнения
# - [ ]  Выполнен шаг 1: данные подготовлены
#     - [ ]  Проверена формула вычисления эффективности обогащения
#     - [ ]  Проанализированы признаки, недоступные в тестовой выборке
#     - [ ]  Проведена предобработка данных
# - [ ]  Выполнен шаг 2: данные проанализированы
#     - [ ]  Исследовано изменение концентрации элементов на каждом этапе
#     - [ ]  Проанализированы распределения размеров гранул на обучающей и тестовой выборках
#     - [ ]  Исследованы суммарные концентрации
# - [ ]  Выполнен шаг 3: построена модель прогнозирования
#     - [ ]  Написана функция для вычисления итогового *sMAPE*
#     - [ ]  Обучено и проверено несколько моделей
#     - [ ]  Выбрана лучшая модель, её качество проверено на тестовой выборке

# <div class="alert alert-block alert-info">
# <h3> Итоговый комментарий</h3>
# 
# Большое спасибо за проделанную работу. Видно, что приложено много усилий. Работа в целом и каждый шаг в отдельности сделаны хорошо. Я оставил несколько советов, надеюсь они будут учтены в этом или будущих проектах. Осталось совсем чуть-чуть, чтобы я принял твой проект:
# 
# 
# 1) Переделать графики в анализе данных
#     
# 2) Добавить сравнение с константной моделью
# 
# 
# Жду исправлений =)
# 
# 

# <div class="alert alert-success"> ✅ 
# <h3> Комментарий ревьюера v2</h3>
# 
# Осталось подправить момент с графиками =)

# In[ ]:




