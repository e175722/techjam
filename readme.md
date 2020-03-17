# Usage
まずmysqlとdjangoのコンテナをビルドする  
$ docker-compose build

コンテナを立てる  
$docker-compose up

webのコンテナに入る  
$ docker-compose exec web bash

mysqlに対してテーブルを作成するコマンドを打つ  
$ python manage.py migrate

あとは  
localhost:8000/webapp
や  
localhost:8000/admin  
などとurlを打ち込んでページを閲覧できる

# Setup
```
$ docker-compose build  
$ docker-compose up -d  
$ docker-compose exec web bash  
$ python manage.py migrate
```
