# [Проект 1. Анализ вакансий из HeadHunter](https://github.com/MorozovOV/My-Projects/blob/master/Проект%20по%20SQL/Анализ%20вакансий%20из%20HeadHunter.ipynb)

## Оглавление  
[1. Описание проекта](.README.md#Описание-проекта)  
[2. Какой кейс решаем?](.README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](.README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)  
[5. Результат](.README.md#Результат)    
[6. Выводы](.README.md#Выводы) 

### Описание проекта    
Кадровое агенство, подбирающее вакансии для IT-специалистов, хочет создать модель машинного обучения, которая будет рекомендовать вакансии клиентам агентства, претендующим на позицию Data Scientist.

:arrow_up:[к оглавлению](README.md#Оглавление)


### Какой кейс решаем?    
Нужно исследовать данные с целью того, чтобы понять, что они из себя представляют и насколько соответствуют целям проекта.

**Метрика качества**     
Результат оценивается по глубине анализа данных, логичности построения запросов и полноте выводов.

**Что практикуем**     
Учимся делать SQL-запросы к базе данных, анализировать данные (Data Understanding), делать выводы по проведённым исследованиям.


### Краткая информация о данных
В качестве исходных данных мы использовали схему public базы данных project_sql, которая состоит из пяти таблиц:
1. VACANCIES хранит в себе данные по вакансиям,
2. AREAS. Таблица-справочник, которая хранит код города и его название,
3. EMPLOYERS. Таблица-справочник со списком работодателей,
4. INDUSTRIES. Таблица-справочник вариантов сфер деятельности работодателей,
5. EMPLOYERS_INDUSTRIES. Дополнительная таблица, которая существует для организации связи между работодателями и сферами их деятельности.
  
:arrow_up:[к оглавлению](README.md#Оглавление)


### Этапы работы над проектом  
Работа над проектом проходила в пять этапов.

На первом этапе происходил предварительный анализ данных. Цель данного этапа - знакомство с данными в таблицах, получение основной статистической информации по таблицам.

На втором этапе проводился детальный анализ вакансий. Цель данного этапа - установление взаимосвязей и закономерностей в данных из различных таблиц. Так, были выявлены регионы-лидеры по количеству вакансий; вакансии, в которых не указана зарплатная "вилка"; оценена средняя минимальная и средняя максимальная заработная плата; установлено количество вакансий для каждого сочетания типа рабочего графика и типа трудоустройства; определён наиболее востребованный опыт работы.

На третьем этапе был произведён анализ работодателей. Цель этапа - определение наиболее активных работодателей на рынке труда, а также условий, которые они предлагают соискателям. В частности, были выявлены лидеры по выставленным вакансиям среди работодателей; определена локация данных работодателей, а тажке сфера деятельности, в которую они нанимают соискателей; установлено, какое количество вакансий размещает лидер отечественной IT-индустрии - компания "Яндекс" - в городах-миллионниках.

На четвёртом этапе происходил предметный анализ данных. Цель данного этапа - исследование требований работодателей к дата-сайентистам. В результате было установлено, сколько вакансий имеет то или иное отношение к работе с данными, а также по ключевому сочетанию символов выявлено, какое количество вакансий подходит для начинающих дата-сайентистов. Кроме того, определено количесвто вакансий для дата-сайентистов, в которых требуется знание SQL (или PostgreSQL) и Python, владение сколькими навыками в среднем ожидают работодатели от дата-сайентистов, а также, на какую зарплату могут претендовать соискатели данной специальности.

На пятом финальном этапе были проведены дополнительные исследования. Цель данного этапа - сделать выводы на основе данных и провести дополнительные исследования в случае необходимости. На данном этапе было проанализировано, какие вакансии и какие навыки наиболее востребованы на рынке труда, а также проанализирован рынок труда в городах Саратове и Энгельсе, которые являются для меня родными и мне, как жителю города Энгельса, важно знать перспективы дальнейшего трудоустройства в регионе моего проживания.

:arrow_up:[к оглавлению](README.md#Оглавление)


### Результаты:  
В результате проделанной работы были выявлены закономерности и взаимосвязи в данных, необходимые для построения модели машинного обучения.

:arrow_up:[к оглавлению](README.md#Оглавление)


### Выводы:  
Проведённое исследование способствовало построению модели машинного обучения по поиску вакансий на HeadHunter для дата-сайентистов. Цель проекта достигнута.

:arrow_up:[к оглавлению](.README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами
