При выполнении задания я исходил из логики, что фильтр по объявлениям уже применён, об этом свидетельствует то, что на основном скриншоте мы    видим множество карточек товара с Samsung, а иначе в поисковой выдаче было бы множество телефонов других производителей.


# Высокий приоритет багов

### Баг 1
Логотип Avito  написан с ошибкой

![b1p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p1.png)

### Баг 2
В результатах поиска появляется вариант с исключенным параметром памяти **«256 ГБ»**

![b2p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p2.png)

![b2p2](https://github.com/k4dms/avitoqa/blob/main/first/screens/p3.png)

  

### Баг 3
В результатах поиска появляется телефон несоответствующего производителя

![b3p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p4.png)

![b3p2](https://github.com/k4dms/avitoqa/blob/main/first/screens/p5.png)

### Баг 4
Результаты поиска содержат неподходящие варианты по параметру цена 

> Пользователем выбрана цена **<= 50000**

![b4p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p6.png)

![b4p2](https://github.com/k4dms/avitoqa/blob/main/first/screens/p7.png)

### Баг 5

Телефоны на картинках в данных товарах не соответствуют заявленным характеристикам

> Приоритет бага зависит от происхождения: если проблема в базе данных
> картинок -  **High**, если это проблема модерации –  **Low**.

![b5p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p8.png)

![b5p2](https://github.com/k4dms/avitoqa/blob/main/first/screens/p9.png)

  

# Средний приоритет багов

### Баг 6
Отсутствует визуальное обозначение о том, какой вариант представления карточек на странице выбран пользователем

![b6p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p10.png)

### Баг 7
В данных карточках отсутствует город
  
![b7p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p11.png)

![b7p2](https://github.com/k4dms/avitoqa/blob/main/first/screens/p12.png)

### Баг 8
Нижняя навигационная панель смещена вверх, исходя из границ предоставленного скриншота

![b8p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p13.png)

### Баг 9
Отсутствует тумблер для выбора **«Сначала из Москвы»**

![b9p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p14.png)


### Баг 10
В правом поле в параметрах цены **отсутствует обозначение «до» и валюта**

![b10p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p15.png)

# Низкий приоритет багов

### Баг 11
Отступы в карточках разные для разных карточек

![b11p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p16.png)

### Баг 12
Различие размеров текста в заголовке

![b12p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p17.png)

### Баг 13
Цвет текста **«Искать только в названиях»** отличается от дефолтного

![b13p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p18.png)

![b13p2](https://github.com/k4dms/avitoqa/blob/main/first/screens/p19.png)

### Баг 14
Большой отступ между заголовками и ценой

![b14p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p20.png)

### Баг 15
Элемент строки поиска вылезает за границы соседних элементов

![b15p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p21.png)

![b15p2](https://github.com/k4dms/avitoqa/blob/main/first/screens/p22.png)

### Баг 16
Наименования разделов начинаются с маленькой буквы

![b16p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p23.png)

### Баг 17
Галочка в чек-боксе выбора памяти выделяется из общей дизайн системы

![b17p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p24.png)

![b17p2](https://github.com/k4dms/avitoqa/blob/main/first/screens/p25.png)

### Баг 18
Значение поля **«Производитель»** задизейблено

![b18p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p26.png)

### Баг  19
Нижний отступ слишком большой

![b19p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p27.png)

### Баг 20
Уточнить у дизайнера о толщине стрелок

В данных элементах

![b20p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p28.png)

![b20p2](https://github.com/k4dms/avitoqa/blob/main/first/screens/p29.png)

Также у дизайнера толщину этих элементов

![b20p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p30.png)

### Баг 21
Элемент с указанием **«рыночная цена»** и **«цена ниже рыночной»** находятся на разной высоте относительно нижней границе картинки:

![b21p1](https://github.com/k4dms/avitoqa/blob/main/first/screens/p31.png)
