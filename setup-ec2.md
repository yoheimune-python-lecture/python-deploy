# EC2セットアップ手順

## EC2サーバーへssh接続
```shell
# デスクトップで作業する場合の例
cd Desktop

# (Macのみ）鍵ファイルの権限を変更.
chmod 400 gs-python-exp-1.pem

# サーバーへSSH接続
ssh -i gs-python-exp-1.pem ec2-user@3.112.196.57  # 注意：IPアドレスは変わる場合があります.
```

## 自分のPythonアプリを、EC2サーバーへインストール.
ここではディレクトリ（00）とします。適宜読み替えてご利用ください。  
また、Githubリポジトリは課題演習用のものを利用しています。
```shell

# 自身に割り当てられたディレクトリに移動.
# 00 -> /var/www/html/00
# 01 -> /var/www/html/01
# ...
# 99 -> /var/www/html/99
cd /var/www/html/00

# Githubにアップした自身のリポジトリからダウンロード.
git clone https://github.com/yoheimune-python-lecture/hand-written-digit-recognition.git

# 上記でダウンロードしたフォルダに移動.
cd hand-written-digit-recognition

# さらに、flaskアプリケーションのあるフォルダに移動.
cd practice

# 起動できるかを試してみる（起動できたら 「ctrl + z」で終了）.
python3 app.py
```

gunicornを起動します。起動する際のポート番号を「00」などの番号に応じて変更してください。
```shell
# 00の場合、8000
# 01の場合、8001
# ...
# 99の場合、8099
/usr/local/bin/gunicorn -w 1 -b 0.0.0.0:8000 --reload app:app
```
上記で起動できると、アクセスからアクセスできます.
```text
# 00の場合、8000
# 01の場合、8001
# ...
# 99の場合、8099

# gunicornに直接アクセス.
http://3.112.196.57:8000/

# apache -> gunicorn とアクセス.
http://3.112.196.57/00/
```

## FYI
以下参考までに。  
今回利用しているEC2のセットアップ内容や、gunicornの永続化を記載しています.

### 初期セットアップ
```shell

sudo su -

# Misc dependencies.
yum -y update && yum clean all
yum -y install bzip2-devel libffi-devel wget which yum git vim
yum -y groupinstall "Development Tools"

# OpenSSL 1.1
amazon-linux-extras install -y epel
yum -y install openssl11 openssl11-devel

# Python
cd /root
wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz
tar -xzf Python-3.11.1.tgz
cd Python-3.11.1 && ./configure && make && make altinstall
ln -s /usr/local/bin/python3.11 /usr/local/bin/python3
ln -s /usr/local/bin/pip3.11 /usr/local/bin/pip3
pip3 install flask numpy matplotlib scipy scikit-learn gunicorn

# Apache設定（ベーシック）
yum -y install httpd
sed -ri 's/#ServerName www.example.com:80/ServerName localhost:80/g;' /etc/httpd/conf/httpd.conf
sed -ri 's/AllowOverride None/AllowOverride All/g;' /etc/httpd/conf/httpd.conf
sed -ri 's/Options Indexes FollowSymLinks/Options Indexes FollowSymLinks ExecCGI/g;' /etc/httpd/conf/httpd.conf
sed -ri 's/#AddHandler cgi-script .cgi/AddHandler cgi-script .py .cgi/g;' /etc/httpd/conf/httpd.conf

# Apache設定（100人分の転送処理）
for i in `seq -w 0 99`
do
    tmp="ProxyPass /${i} http://localhost:80${i}/"
    echo $(eval echo ${tmp}) >> /etc/httpd/conf/httpd.conf
done
systemctl enable httpd
systemctl start httpd

# タイムゾーン
timedatectl set-timezone Asia/Tokyo

# 100人分のディレクトリ作成.
for i in `seq -w 0 99`
do
    tmp="/var/www/html/${i}"
    mkdir $(eval echo ${tmp})
done
chown -R ec2-user:ec2-user /var/www/html
```


### gunicornの永続化（systemdの利用）
systemd などを用いて、gunicornの起動を永続化することができます.
```shell
# vim gunicorn-00.service
[Unit]
Description=gunicorni-00 daemon
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=/var/www/html/00/hand-written-digit-recognition/practice
ExecStart=/usr/local/bin/gunicorn -w 1 -b 0.0.0.0:8000 --reload app:app
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```
上記の設定を追加後、sysetmdでの起動や自動起動設定を行うことができます.
```shell
systemctl start gunicorn-00
systemctl enable gunicorn-00
```

