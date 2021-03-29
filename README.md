# yamdb
![workflow](https://github.com/SafonovRoman/yamdb_final/actions/workflows/yamdb.yaml/badge.svg)

## Описание проекта:

Данный проект являетсягрупповым в курсе Яндекс.Практикум для python разработчиков. Ключевая задача проекта - собрать все полученные ранее знания по проектированию api и научиться готовить проекты к деплою.

## Автор
### Сафонов Роман - [github](https://github.com/SafonovRoman/)

Репозиторий с [проектом](https://github.com/SafonovRoman/infra_sp2).
Развернуто [тут](http://130.193.41.133/)
[Документация](http://130.193.41.133/redoc/)

### Технологии

При разработке проекта были использованы следующие технологии:

* Python
* Django
* DRF
* Gunicorn
* Docker
* Nginx
* PostgreSQL

### Инструкция по сборке:
1. Установить Docker
2. Запустить команду "docker-compose up" из папки с проектом
3. Подключиться к контейнеру "web" (например "docker exec -it infra_sp2_web_1 bash") и выполнить "python manage.py migrate"
4. Собрать статику командой "python manage.py collectstatic"
5. Там же создать суперпользователя ("python manage.py createsuperuser")


