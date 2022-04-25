![Demo](demo.gif)
[Project Demo](http://mariownyou.pythonanywhere.com)

# Тестовое задание в devman
1. Соеденить существующий frontend с django проектом
2. Исопльзовать данные из бд на вместо заглушек
3. Сделать админку максимально удобной для заполнения

### Проблемы
Очень интересное тестовое задание но есть проблемы с формулировками некоторых задач.  
Например:

> 6 шаг -- Картинки можно упорядочить - выбрать которая из них первая и где второая  

Не совсем понятно что требуется сделать (отсортировать или задать порядок относительно модели Place)


### Переменные окружения и запуск локально
Создайте `.env` в корне проекта и задайте следющие переменные:

```bash
SECRET_KEY='some secure key'
ALLOWED_HOSTS='*'
DEBUG=true

# вы также можете указать и другие необходимые переменные
SESSION_COOKIE_SECURE=false
CSRF_COOKIE_SECURE=false
SECURE_SSL_REDIRECT=false
SECURE_HSTS_INCLUDE_SUBDOMAINS=false
```



Создайте виртуально окружение и установите зависимости

``` bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```



### load_place и пример json файла
Приложение поддерживает импортирование мест из стороннего json файла. 
Достаточно указать ссылку на файл и запусть manage команду.  `./manage.py load_place https://some-site/file.json`
json файл должен соответствовать следующему формату: 

``` json
{
    "title": "Антикафе Bizone",
    "imgs": [   "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
    ],
    "description_short": "Краткое описание",
    "description_long": "Длинное описание, поддерживате html разметку",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```


