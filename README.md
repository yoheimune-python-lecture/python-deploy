# python-deploy

## 注意
本サンプルは、製作時から時間経過することで古くなっていたり、個々人のローカル環境によって、エラーが発生する可能性があります。  
エラーとなった場合には、エラーメッセージなど確認しつつ、対処してみてください。

## 準備
以下のコマンドでDockerコンテナのビルドと起動を行います.
```shell
docker compose build
docker compose up
```

## CGIのサンプル.
上記でコンテナを起動後、下記でアクセスできます。
```text
http://localhost:8889/cgi-sample.py
```

## Gunicornのサンプル.
上記でコンテナを起動後、下記でアクセスできます。
```text
http://localhost:8000/
```

## Apache -> Gunicornのサンプル.
上記でコンテナを起動後、下記でアクセスできます。
```text
http://localhost:8889/gunicorn
```

## WSGIのサンプル（@ローカル環境）
下記より起動できます.  
Pythonは3系であることを想定します.
```shell
cd web
python wsgi-sample.py
```
以下よりアクセスできます。
```text
http://0.0.0.0:8880
```

## FYI
* OS : CentOS7.8
* Python version : 3.11.1
* Pythonパス : /usr/local/bin/python3
* Apache : 2.4

## References
* [WSGIとは - Wikipedia](https://ja.wikipedia.org/wiki/Web_Server_Gateway_Interface)
* [Gunicorn公式サイト](https://gunicorn.org/)