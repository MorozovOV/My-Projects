import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import sys 

# Определяем путь к загружаемому файлу:
path = input('Введите расположение файла и нажмите "Enter": ')
name = input('Введите название файла и нажмите "Enter": ')
# Загружаем файл по указанному пути:
df = pd.read_excel(path + '\\' + name)

# Запрашиваем максимальный балл:
max_score = int(input('Введите максимально возможное количество баллов и нажмите "Enter": '))

# Удаляем мусорные столбцы при их наличии:
cols_to_delete = ['№', 'Код ППЭ', 'Аудитория', 'Код МСУ', 'Документ', 'Код ОО']
for col in cols_to_delete:
    if col in df.columns:
        df = df.drop(col, axis = 1)
        
# Сцепляем фамилию, имя и отчество:
df['Ученик'] = df['Фамилия'] + ' ' + df['Имя'] + ' ' + df['Отчество']
df = df.drop(['Фамилия', 'Имя', 'Отчество'], axis = 1)

# Функция для настройки подписи долей круговой диаграммы:
def func(pct, allvalues):
    absolute = round(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} чел.)".format(pct, absolute)

if 'Годовая оценка' in df.columns:
    # Функция для определения соответствия оценки за ВПР триместровой оценке:
    def get_compliance(row):
        if row['Оценка'] > row['Годовая оценка']:
            result = 'повышение'
        elif row['Оценка'] < row['Годовая оценка']:
            result = 'понижение'
        else :
            result = 'соответствие'
        return result

    # Используя функцию, добавляем столбец "Соответствие":
    df['Соответствие'] = df.apply(get_compliance, axis=1)
    
    # Считаем процент соответсвия по школе:
    compliance = df.groupby('Соответствие')['Класс'].count()
    
    # Круговая диаграмма соответствия:
    fig1 = plt.pie(
        compliance, 
        labels = pd.DataFrame(compliance).index, 
        autopct=lambda pct: func(pct, pd.DataFrame(df['Оценка'].value_counts())['count'])
    )
    plt.title('Соответствие по школе')
    plt.savefig('Соответствие по школе.png')
    
# Добавляем столбцы с заданиями первой части:
for i in np.arange(1, len(df['Задания с кратким ответом'][0]) + 1):
    df[f'Задание {i}'] = df['Задания с кратким ответом'].apply(lambda x: 1 if x[i - 1] == '+' 
                                                               else 0 if x[i - 1] == '-'
                                                               else x)
  
# Запоминаем количество заданий в первой части:
part_1_tasks_number = i

# Добавляем столбцы с заданиями второй части:
for n in np.arange(0, len(df['Задания с развёрнутым ответом'][0])/4):
    i += 1
    k = int(n * 4)
    df[f'Задание {int(i)}'] = df['Задания с развёрнутым ответом'].apply(lambda x: int(x[k]))
    
# Функция для рсчёта успеваемости:
def get_achivement(data):
    '''
    Расчёт успеваемости
    data -> DataFrame
    На выходе - успеваемость в процентах
    '''
    achievement = round((data[data['Оценка'] == 5].shape[0] + data[data['Оценка'] == 4].shape[0] + data[data['Оценка'] == 3].shape[0]) / data.shape[0] * 100, 1)
    return achievement

# Функция для рсчёта успеваемости:
def get_quality(data):
    '''
    Расчёт качества
    data -> DataFrame
    На выходе - качество в процентах
    '''
    quality = round((data[data['Оценка'] == 5].shape[0] + data[data['Оценка'] == 4].shape[0]) / data.shape[0] * 100, 1)
    return quality

# Функция для рсчёта среднего балла:
def get_mean_score(data):
    '''
    Расчёт среднего балла
    data -> DataFrame
    На выходе - средний балл
    '''
    mean_score = round(data['Первичный балл'].mean(), 2)
    return mean_score

# Функция для рсчёта средней оценки:
def get_mean_mark(data):
    '''
    Расчёт средней оценки
    data -> DataFrame
    На выходе - средняя оценка
    '''
    mean_mark = round(data['Оценка'].mean(), 2)
    return mean_mark

# Создаём список классов:
classes_list = sorted(list(set(df['Класс'].tolist())))

# Рассчитываем основные статистические показатели по классам:
# Для каждого показателя формируем свой список:
k = 0

# Пустые списки, в которые будем заносить основные метрики по классам:
achievements = []
qualities = []
mean_scores = []
mean_marks = []
max_scores = []

while k < len(classes_list):
    # Перебираем классы из списка classes_list и обрезаем датасет по данному классу:
    results_class = df[df['Класс'] == classes_list[k]]
    
    # Считаем метрики по каждому классу и сохраняем их в списки:
    
    # Успеваемость:
    grade_class = get_achivement(results_class)
    achievements.append(grade_class)
    
    # Качество:
    quality_class = get_quality(results_class)
    qualities.append(quality_class)
    
    # Средний балл:
    mean_score_class = get_mean_score(results_class)
    mean_scores.append(mean_score_class)
    
    # Средняя оценка:
    mean_mark_class = get_mean_mark(results_class)
    mean_marks.append(mean_mark_class)
    
    # Макс. балл:
    max_score_class = results_class['Первичный балл'].max()
    max_scores.append(max_score_class)
    
    k += 1
    
# Преобразуем полученные списки в дата-фреймы для удобства последующей визуализации:
results_df = pd.DataFrame({'Классы': classes_list,
                            'Успеваемость': achievements})
qualities_df = pd.DataFrame({'Классы': classes_list,
                            'Качество': qualities})
mean_scores_df = pd.DataFrame({'Классы': classes_list,
                                'Средний балл': mean_scores})
mean_marks_df = pd.DataFrame({'Классы': classes_list,
                            'Средняя оценка': mean_marks})
max_scores_df = pd.DataFrame({'Классы': classes_list,
                            'Макс. балл': max_scores})
mean_percents_df = mean_scores_df.copy()
mean_percents_df['Средний процент выполнения'] = round(mean_percents_df['Средний балл'] / max_score * 100, 1)
mean_percents_df = mean_percents_df.drop('Средний балл', axis = 1)

#Создаём файл "Отчёт", в который будем записывать отчётную информацию.
stdoutOrigin=sys.stdout 
sys.stdout = open("Отчёт.txt", "w")
    
# Выводим основные статистические показатели по школе:
print('СТАТИСТИКА ПО ШКОЛЕ:')
print(f'Успеваемость - {get_achivement(df)}%')
print(f'Качество - {get_quality(df)}%')
print(f'Средний итоговый балл - {get_mean_score(df)}')
print(f'Средняя оценка - {get_mean_mark(df)}')
print(f'Средний процент выполнения - {round(get_mean_score(df) / max_score * 100, 1)}')
print(f"Максимальный первичный балл - {df['Первичный балл'].max()}")
print(f'''Оценку "2" получили: {df[df['Оценка'] == 2]['Ученик'].tolist()}''')

# Закрываем файл "Отчёт"
sys.stdout.close()
sys.stdout=stdoutOrigin

# Создаём временную таблицу только с заданиями:
temp = df[df.columns[-i:]]

# Рассчитываем процент выполнения каждого задания    
n = 0
percent_list = [] # Пустой список со значениями процентов выполнения заданий
while n < part_1_tasks_number:
    # Рассчёт процентов выполнения заданий первой части и заполнение списка:
    percent_list.append(round(temp[temp.columns[n]].sum() / (temp[temp.columns[n]].count()) * 100, 2))
    n += 1
    
while n < i:
    # Рассчёт процентов выполнения заданий второй части и заполнение списка:
    percent_list.append(round(temp[temp.columns[n]].sum() / ((temp[temp.columns[n]].count()) * int(df['Задания с развёрнутым ответом'][0][2+4*(n - part_1_tasks_number)])) * 100, 2))
    n += 1
    
# Словарь с номерами заданий и рассчитанными процентами их выполнения:
tasks_dict = {'Задания': list(np.arange(1, (i + 1))),
            'Процент выполнения': percent_list}
# Преобразуем в дата-фрем для удобства визуализации:
tasks_dict_df = pd.DataFrame(tasks_dict)
    
# Визуализируем процент выполнения заданий:
fig, axes = plt.subplots(figsize = (20, 7))
ax = sns.barplot(tasks_dict_df, x = 'Задания', y = 'Процент выполнения', ax = axes)
ax.set_title('Процент выполнения заданий по школе')
ax.bar_label(ax.containers[0], fontsize=10)
plt.savefig('Процент выполнения заданий по школе.png')

# Визуализируем основные статистические показатели по классам:
fig, axes = plt.subplots(figsize = (20, 7))
ax = sns.barplot(results_df, x = 'Классы', y = 'Успеваемость', ax = axes)
ax.set_title('Успеваемость по классам')
ax.bar_label(ax.containers[0], fontsize=10)
plt.savefig('Успеваемость по классам.png')

fig, axes = plt.subplots(figsize = (20, 7))
ax = sns.barplot(qualities_df, x = 'Классы', y = 'Качество', ax = axes)
ax.set_title('Качество по классам')
ax.bar_label(ax.containers[0], fontsize=10)
plt.savefig('Качество по классам.png')

fig, axes = plt.subplots(figsize = (20, 7))
ax = sns.barplot(mean_scores_df, x = 'Классы', y = 'Средний балл', ax = axes)
ax.set_title('Средний балл по классам')
ax.bar_label(ax.containers[0], fontsize=10)
plt.savefig('Средний балл по классам.png')

fig, axes = plt.subplots(figsize = (20, 7))
ax = sns.barplot(mean_marks_df, x = 'Классы', y = 'Средняя оценка', ax = axes)
ax.set_title('Средняя оценка по классам')
ax.bar_label(ax.containers[0], fontsize=10)
plt.savefig('Средняя оценка по классам.png')

fig, axes = plt.subplots(figsize = (20, 7))
ax = sns.barplot(max_scores_df, x = 'Классы', y = 'Макс. балл', ax = axes)
ax.set_title('Максимальный первичный балл по классам')
ax.bar_label(ax.containers[0], fontsize=10)
plt.savefig('Максимальный первичный балл по классам.png')

fig, axes = plt.subplots(figsize = (20, 7))
ax = sns.barplot(mean_percents_df, x = 'Классы', y = 'Средний процент выполнения', ax = axes)
ax.set_title('Средний процент выполнения по классам')
ax.bar_label(ax.containers[0], fontsize=10)
plt.savefig('Средний процент выполнения по классам.png')

k = 0

while k < len(classes_list):
    # Перебираем классы из списка classes_list и обрезаем датасет по данному классу:
    results_class = df[df['Класс'] == classes_list[k]]
    
    # Строим круговую диаграмму распределения оценок:
    fig, axes = plt.subplots(figsize = (20, 7))
    ax = plt.pie(
        results_class['Оценка'].value_counts(), 
        labels = pd.DataFrame(results_class['Оценка'].value_counts()).index, 
        autopct=lambda pct: func(pct, pd.DataFrame(results_class['Оценка'].value_counts())['count'])
    )
    plt.title(f'Распределение оценок в {classes_list[k]} классе')
    plt.savefig(f'Распределение оценок в {classes_list[k]} классе.png')
        
    # Обрезаем таблицу до заданий:
    temp = results_class[results_class.columns[-i:]]    
    # Рассчитываем процент выполнения каждого задания    
    n = 0
    percent_list = [] # Пустой список со значениями процентов выполнения заданий
    while n < part_1_tasks_number:
        # Рассчёт процентов выполнения заданий первой части и заполнение списка:
        percent_list.append(round(temp[temp.columns[n]].sum() / (temp[temp.columns[n]].count()) * 100, 2))
        n += 1    
    while n < i:
        # Рассчёт процентов выполнения заданий второй части и заполнение списка:
        percent_list.append(round(temp[temp.columns[n]].sum() / ((temp[temp.columns[n]].count()) * int(df['Задания с развёрнутым ответом'][0][2+4*(n - part_1_tasks_number)])) * 100, 2))
        n += 1    
    # Словарь с номерами заданий и рассчитанными процентами их выполнения:
    tasks_dict = {'Задания': list(np.arange(1, (i + 1))),
                'Процент выполнения': percent_list}
    # Преобразуем в дата-фрем для удобства визуализации:
    tasks_dict_df = pd.DataFrame(tasks_dict)    
    # Визуализируем процент выполнения заданий:
    fig, axes = plt.subplots(figsize = (20, 7))
    ax = sns.barplot(tasks_dict_df, x = 'Задания', y = 'Процент выполнения', ax = axes)
    ax.set_title(f'Процент выполнения заданий в {classes_list[k]} классе')
    ax.bar_label(ax.containers[0], fontsize=10)
    plt.savefig(f'Процент выполнения заданий в {classes_list[k]} классе.png')
        
    # Круговая диаграмма соответствия, если добавлен столбец с годовыми оценками:
    if 'Годовая оценка' in df.columns:
        fig, axes = plt.subplots(figsize = (20, 7))
        ax = plt.pie(
            results_class['Соответствие'].value_counts(), 
            labels = pd.DataFrame(results_class['Соответствие'].value_counts()).index, 
            autopct=lambda pct: func(pct, pd.DataFrame(results_class['Соответствие'].value_counts())['count'])
        )
        plt.title(f'Соответствие годовой оценке в {classes_list[k]} классе')
        plt.savefig(f'Соответствие годовой оценке в {classes_list[k]} классе.png')

    k += 1
    
# Считаем всю статистику по учителям, если добавлен такой столбец:
if 'Учитель' in df.columns:
    # Создаём список учителей:
    teachers_list = sorted(list(set(df['Учитель'].tolist())))
    
    # Пустые списки, в которые будем заносить основные метрики по классам:
    achievements = []
    qualities = []
    mean_scores = []
    mean_marks = []
    max_scores = []
    
    k = 0
    
    while k < len(teachers_list):
        # Перебираем учителей из списка teachers_list и обрезаем датасет по данному учителю:
        results_teacher = df[df['Учитель'] == teachers_list[k]]
        
        # Считаем метрики по каждому классу и сохраняем их в списки:
    
        # Успеваемость:
        grade_class = get_achivement(results_teacher)
        achievements.append(grade_class)
    
        # Качество:
        quality_class = get_quality(results_teacher)
        qualities.append(quality_class)
    
        # Средний балл:
        mean_score_class = get_mean_score(results_teacher)
        mean_scores.append(mean_score_class)
    
        # Средняя оценка:
        mean_mark_class = get_mean_mark(results_teacher)
        mean_marks.append(mean_mark_class)
    
        # Макс. балл:
        max_score_class = results_teacher['Первичный балл'].max()
        max_scores.append(max_score_class)
        
        # Строим круговую диаграмму распределения оценок:
        fig, axes = plt.subplots(figsize = (20, 7))
        ax = plt.pie(
            results_teacher['Оценка'].value_counts(), 
            labels = pd.DataFrame(results_teacher['Оценка'].value_counts()).index, 
            autopct=lambda pct: func(pct, pd.DataFrame(results_teacher['Оценка'].value_counts())['count'])
        )
        plt.title(f'Распределение оценок у учителя {teachers_list[k]}')
        plt.savefig(f'Распределение оценок у учителя {teachers_list[k]}.png')
        
        # Обрезаем таблицу до заданий:
        temp = results_teacher[results_teacher.columns[-i:]]    
        # Рассчитываем процент выполнения каждого задания    
        n = 0
        percent_list = [] # Пустой список со значениями процентов выполнения заданий
        while n < part_1_tasks_number:
            # Рассчёт процентов выполнения заданий первой части и заполнение списка:
            percent_list.append(round(temp[temp.columns[n]].sum() / (temp[temp.columns[n]].count()) * 100, 2))
            n += 1    
        while n < i:
            # Рассчёт процентов выполнения заданий второй части и заполнение списка:
            percent_list.append(round(temp[temp.columns[n]].sum() / ((temp[temp.columns[n]].count()) * int(df['Задания с развёрнутым ответом'][0][2+4*(n - part_1_tasks_number)])) * 100, 2))
            n += 1    
        # Словарь с номерами заданий и рассчитанными процентами их выполнения:
        tasks_dict = {'Задания': list(np.arange(1, (i + 1))),
                    'Процент выполнения': percent_list}
        # Преобразуем в дата-фрем для удобства визуализации:
        tasks_dict_df = pd.DataFrame(tasks_dict)    
        # Визуализируем процент выполнения заданий:
        fig, axes = plt.subplots(figsize = (20, 7))
        ax = sns.barplot(tasks_dict_df, x = 'Задания', y = 'Процент выполнения', ax = axes)
        ax.set_title(f'Процент выполнения заданий у учителя {teachers_list[k]}')
        ax.bar_label(ax.containers[0], fontsize=10)
        plt.savefig(f'Процент выполнения заданий у учителя {teachers_list[k]}.png')
        
        # Круговая диаграмма соответствия, если добавлен столбец с годовыми оценками:
        if 'Годовая оценка' in df.columns:
            fig, axes = plt.subplots(figsize = (20, 7))
            ax = plt.pie(
                results_teacher['Соответствие'].value_counts(), 
                labels = pd.DataFrame(results_teacher['Соответствие'].value_counts()).index, 
                autopct=lambda pct: func(pct, pd.DataFrame(results_teacher['Соответствие'].value_counts())['count'])
            )
            plt.title(f'Соответствие годовой оценке у учителя {teachers_list[k]}')
            plt.savefig(f'Соответствие годовой оценке у учителя {teachers_list[k]}.png')
            
        k += 1    
    
    # Преобразуем полученные списки в дата-фреймы для удобства последующей визуализации:
    results_df = pd.DataFrame({'Учитель': teachers_list,
                                'Успеваемость': achievements})
    qualities_df = pd.DataFrame({'Учитель': teachers_list,
                                'Качество': qualities})
    mean_scores_df = pd.DataFrame({'Учитель': teachers_list,
                                    'Средний балл': mean_scores})
    mean_marks_df = pd.DataFrame({'Учитель': teachers_list,
                                'Средняя оценка': mean_marks})
    max_scores_df = pd.DataFrame({'Учитель': teachers_list,
                                'Макс. балл': max_scores})
    mean_percents_df = mean_scores_df.copy()
    mean_percents_df['Средний процент выполнения'] = round(mean_percents_df['Средний балл'] / max_score * 100, 1)
    mean_percents_df = mean_percents_df.drop('Средний балл', axis = 1)    
    
    # Визуализируем основные статистические показатели по учителям:
    fig, axes = plt.subplots(figsize = (20, 7))
    ax = sns.barplot(results_df, x = 'Учитель', y = 'Успеваемость', ax = axes)
    ax.set_title('Успеваемость по учителям')
    ax.bar_label(ax.containers[0], fontsize=10)
    plt.savefig('Успеваемость по учителям.png')

    fig, axes = plt.subplots(figsize = (20, 7))
    ax = sns.barplot(qualities_df, x = 'Учитель', y = 'Качество', ax = axes)
    ax.set_title('Качество по учителям')
    ax.bar_label(ax.containers[0], fontsize=10)
    plt.savefig('Качество по учителям.png')

    fig, axes = plt.subplots(figsize = (20, 7))
    ax = sns.barplot(mean_scores_df, x = 'Учитель', y = 'Средний балл', ax = axes)
    ax.set_title('Средний балл по учителям')
    ax.bar_label(ax.containers[0], fontsize=10)
    plt.savefig('Средний балл по учителям.png')

    fig, axes = plt.subplots(figsize = (20, 7))
    ax = sns.barplot(mean_marks_df, x = 'Учитель', y = 'Средняя оценка', ax = axes)
    ax.set_title('Средняя оценка по учителям')
    ax.bar_label(ax.containers[0], fontsize=10)
    plt.savefig('Средняя оценка по учителям.png')

    fig, axes = plt.subplots(figsize = (20, 7))
    ax = sns.barplot(max_scores_df, x = 'Учитель', y = 'Макс. балл', ax = axes)
    ax.set_title('Максимальный первичный балл по учителям')
    ax.bar_label(ax.containers[0], fontsize=10)
    plt.savefig('Максимальный первичный балл по учителям.png')

    fig, axes = plt.subplots(figsize = (20, 7))
    ax = sns.barplot(mean_percents_df, x = 'Учитель', y = 'Средний процент выполнения', ax = axes)
    ax.set_title('Средний процент выполнения по учителям')
    ax.bar_label(ax.containers[0], fontsize=10)
    plt.savefig('Средний процент выполнения по учителям.png')
    
df.to_excel('Возвращённый протокол.xlsx', index=False)