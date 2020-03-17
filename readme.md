# Usage
まずmysqlとdjangoのコンテナを立てる
$ docker-compose build

webのコンテナに入る
$ docker-compose exec web bash

mysqlに対してテーブルを作成するコマンドを打つ
$ python manage.py migrate

あとは
localhost:8000/webapp
や
localhost:8000/admin
などとurlを打ち込んでページを閲覧できる
