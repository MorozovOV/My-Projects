# [Проект 5. Предсказание продолжительности поездки в такси. Задача регрессии.](https://github.com/MorozovOV/My-Projects/blob/master/Проект%20по%20линейной%20регрессии/Проект%20по%20линейной%20регрессии.ipynb)

## Оглавление  
[1. Описание проекта](README.md#Описание-проекта)  
[2. Какой кейс решаем?](README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](README.md#Этапы-работы-над-проектом)  
[5. Результат](README.md#Результат)    
[6. Выводы](README.md#Выводы) 

### Описание проекта    
Известно, что стоимость такси в США рассчитывается на основе фиксированной ставки и тарифной стоимости, величина которой зависит от времени и расстояния. Тарифы варьируются в зависимости от города. В свою очередь, время поездки зависит от множества факторов, таких как направление поездки, время суток, погодные условия и так далее. Таким образом, если мы разработаем алгоритм, способный определять длительность поездки, мы сможем прогнозировать её стоимость самым тривиальным образом, например, просто умножая стоимость на заданный тариф.
Задача, которую мы будем решать, была представлена в качестве [Data Science-соревнования](https://www.kaggle.com/competitions/nyc-taxi-trip-duration/overview) с призовым фондом в 30 000 $ на платформе Kaggle в 2017 году.

:arrow_up:[к оглавлению](README.md#Оглавление)

### Какой кейс решаем?    
**Бизнес-задача**: определить характеристики и с их помощью спрогнозировать длительность поездки на такси..

**Техническая задача для специалиста в Data Science**: построить модель машинного обучения, которая на основе предложенных характеристик клиента будет предсказывать числовой признак — время поездки такси, то есть решить задачу регрессии.

**Метрика качества**     
Метрикой качества решения поставленной задачи будет среднеквадратичная логарифмическая ошибка, RMSLE (Root Mean Squared Log Error).

**Использованные библиотеки Python**
* pandas
* numpy
* matplotlib
* seaborn
* plotly.express
* sklearn
* scipy
* xgboost

### Краткая информация о данных
В использованном нами [набре данных](https://drive.google.com/file/d/1X_EJEfERiXki0SKtbnCL9JDv49Go14lF/view) содержится следующая информация:
* id — уникальный идентификатор поездки;;
* vendor_id — уникальный идентификатор поставщика услуг (таксопарка), связанного с записью поездки;
* pickup_datetime — дата и время, когда был включён счётчик поездки;
* dropoff_datetime — дата и время, когда счётчик был отключён;
* pickup_longitude — долгота, на которой был включён счётчик;
* pickup_latitude — широта, на которой был включён счётчик;
* dropoff_longitude — долгота, на которой счётчик был отключён;
* dropoff_latitude — широта, на которой счётчик был отключён;
* passenger_count — количество пассажиров в транспортном средстве (введённое водителем значение);
* store_and_fwd_flag — флаг, который указывает, сохранилась ли запись о поездке в памяти транспортного средства перед отправкой поставщику (Y — хранить и пересылать, N — не хранить и не пересылать поездку);
* trip_duration — продолжительность поездки в секундах (целевой признак).

:arrow_up:[к оглавлению](README.md#Оглавление)

### Этапы работы над проектом  
Работа над проектом проходила в пять этапов.

**1. Первичная обработка данных**. В рамках этой части мы сформировали набор данных на основе предложенных нам источников информации, а также обработали пропуски и выбросы в данных.

**2. Разведывательный анализ данных (EDA)**. Исследовали данные, нащупали первые закономерности и выдвинули гипотезы.

**3. Отбор и преобразование признаков**. На этом этапе мы перекодировали и преобразовали данные таким образом, чтобы их можно было использовать при решении задачи регрессии — для построения модели.

**4. Решение задачи регрессии: линейная регрессия и деревья решений**. На данном этапе мы построили свои первые прогностические модели и оценили их качество. Тем самым мы создали baseline, который помог нам ответить на вопрос: «Решаема ли вообще представленная задача?»

**5. Решение задачи регрессии: ансамбли моделей и построение прогноза**. На заключительном этапе мы доработали наше предсказание с использованием более сложных алгоритмов и оценили, с помощью какой модели возможно сделать более качественные прогнозы.

:arrow_up:[к оглавлению](README.md#Оглавление)

### Результаты:  
В результате проделанной работы датасет был обработан и проанализирован. Для улучшения качества модели в набор данных были добавлены новые признаки, в том числе и при помощи кластеризации на основе алгоритма k-means. Данные были логарифмирваны, закодированы и нормализованы. При помощи алгоритма SelectKBest были отобраны признаки, наиболее скоррелированные с целевой переменной. Для построения финальной модели были опробованы алгоритмы линейной регрессии, решающих деревьев, полиноминальной регрессии 2 степени, а также ансамблевые методы: случайный лес, градиентный бустинг, экстремальный градиентный бустинг.

:arrow_up:[к оглавлению](README.md#Оглавление)

### Выводы:  
Лучший результат показала модель, предсказывающая продолжительность поездки на основе экстремального градиентного бустинга (XGBoost). Метрика RMSLE на финальной модели составила 0.39412. Цель проекта достигнута.

:arrow_up:[к оглавлению](README.md#Оглавление)

Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами
