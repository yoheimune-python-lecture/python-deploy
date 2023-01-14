FROM centos:centos7

WORKDIR "/root"

# 事前インストール
RUN yum -y update && yum clean all
RUN yum -y install openssl-devel bzip2-devel libffi-devel wget which yum git vim
RUN yum -y groupinstall "Development Tools"

# OpenSSL 1.1
RUN yum -y install epel-release
RUN yum -y install openssl11 openssl11-devel
ENV CFLAGS="-I/usr/include/openssl11"
ENV LDFLAGS="-L/usr/lib64/openssl11 -lssl -lcrypto"

# pythonインストール
RUN wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz
RUN tar -xzf Python-3.11.1.tgz
RUN cd Python-3.11.1 && ./configure && make && make altinstall
RUN ln -s /usr/local/bin/python3.11 /usr/local/bin/python3
RUN ln -s /usr/local/bin/pip3.11 /usr/local/bin/pip3

# Pythonアプリケーションセットアップ
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

# タイムゾーンなど設定
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
ENV LANG="ja_JP UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8" \
    TZ="Asia/Tokyo"
