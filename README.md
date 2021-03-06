## Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

### Что это ?
Учебный проeкт. По легенде необходимо доработать винный сайт-магазин. По _ТЗ_ нужно генерировать ассортимент сайта из высланного заказчиком _xlsx-файла_.

__Пример высылаемого _xlsx-файла_:__

| Категория | Название | Сорт | Цена | Картинка | Акция |
|---|---|---|---|---|-----------------|
| Белые вина|Белая леди|Дамский пальчик|399|belaya_ledi.png|Выгодное предложение|
| Напитки|Коньяк классический||350|konyak_klassicheskyi.png|
| Белые вина|Ркацители|Ркацители|499|rkaciteli.png|
| Красные вина|Черный лекарь|Качич|399|chernyi_lekar.png|
| Красные вина|Хванчкара|Александраули|550|hvanchkara.png|
| Белые вина|Кокур|Кокур|450|kokur.png|
| Красные вина|Киндзмараули|Саперави|550|kindzmarauli.png|
| Напитки|Чача||299|chacha.png|Выгодное предложение |
| Напитки|Коньяк кизиловый||350|konyak_kizilovyi.png|

__Примечания__    
Скрипт принимает на вход _xlsx-файл_ и с помощью шаблонизатора формирует страницу. Разбивает по категориям и добавляет стикер к продукции со скидкой. Названиe колонок(список) и их переименованиe(словарь) вынесены в глобальные переменные. Это позволит быстро адаптировать скрипт при изменении формата высылаемого файла.    


### Зачем ?
Код написан в учебных целях — это урок в курсе по _Python_ и веб-разработке на сайте [Devman](https://dvmn.org).

Исходный код находится [_здесь_](https://github.com/devmanorg/wine).


### Как запустить ?

 1. Склонировать проeкт
```
you@name: git clone https://github.com/StiffRedson/wine.git
```

 2. Установить окружение
 ```
 you@name: python3 -m venv venv
 you@name: source venv/bin/activate
 you@name: pip install -r requirements.txt
```

3. Запуск

 Скрипт запускается привычным образом с аргументом (название высланного заказчиком _exel-файла_)

```
 you@name: python3 main.py file_name
 ```

Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Контакты
---
| Contacts | Ivan Fedorov          |
|----------|-----------------------|
| Email    | StiffRedson@gmail.com |
| Telegram | @StivaRedson          |
