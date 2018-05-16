Title: Apache
Date: 2016-09-27 03:25:26
Tags: Apache, httpd



# Apache

<https://github.com/apache/httpd>

<http://httpd.apache.org/>

ubuntu/debian：

    sudo aptitude install apache2

redhat/centos/fedora:

    $ sudo yum install httpd2

启动服务器：

    service apache2 start

启动浏览器查看：

    http://localhost:80

***

# apache命令

a2ensite

    $ sudo a2ensite <site>

a2dissite

    $ sudo a2dissite <site>

a2enmod

    $ sudo a2enmod <mod>

a2dismod

    $ sudo a2dismod <mod>

