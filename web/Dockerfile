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

# Apache インストール
RUN yum -y install httpd
RUN sed -ri 's/#ServerName www.example.com:80/ServerName localhost:80/g;' /etc/httpd/conf/httpd.conf
RUN sed -ri 's/AllowOverride None/AllowOverride All/g;' /etc/httpd/conf/httpd.conf
RUN sed -ri 's/Options Indexes FollowSymLinks/Options Indexes FollowSymLinks ExecCGI/g;' /etc/httpd/conf/httpd.conf
RUN sed -ri 's/#AddHandler cgi-script .cgi/AddHandler cgi-script .py .cgi/g;' /etc/httpd/conf/httpd.conf
RUN echo "ProxyPass /gunicorn http://gunicorn:8000/" >> /etc/httpd/conf/httpd.conf

# タイムゾーンなど設定
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
ENV LANG="ja_JP UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8" \
    TZ="Asia/Tokyo"
