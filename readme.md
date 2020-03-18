# Usage
まずsettings-sample.pyを元にsettings.pyを作成する  
変更する項目はデータベース設定関連

次にmysqlとdjangoのコンテナをビルドする  
$ docker-compose build

コンテナを立てる  
$docker-compose up

mysqlに対してテーブルを作成するコマンドを打つ  
$ docker-compose exec web bash python3 manage.py migrate  

あとは  
localhost:8000/webapp
や
localhost:8000/admin  
などとurlを打ち込んでページを閲覧できる

# Setup
```
$ docker-compose build  
$ docker-compose up -d  
$ docker-compose exec web bash python3 manage.py migrate
```
