Title: SMTP
Date: 2017-04-26 09:56:04
Tags: EMAIL, SMTP



# Email

python邮件服务器MTA：smtp协议

python客户端MUA：本地协议pop3, 远程协议imap

***

# sendmail

开源的smtp服务器．

安装sendmail:

    $ sudo apt-get install sendmail
    $ sudo apt-get install sendmail-cf

配置：

    $ sudo vim /etc/hosts
      127.0.0.1 localhost.localdomain    localhost    hostname

    $ sudo vim /etc/mail/sendmail.mc
      modify 127.0.0.1 to 0.0.0.0, 才能发送给其它机器，否则只能发给本机．
      DAEMON_OPTIONS('..., Port=smtp, Addr=127.0.0.1')dnl
    # mv sendmail.cf sendmail.cf.old
    # m4 sendmail.mc > sendmail.cf

测试：

    $ echo "test mail" | /usr/sbin/sendmail -s "subject" yourmail@domain.com

***

# Python的email标准库

服务端：

1. smtplib

客户端：

1. smtpd
2. poplib
3. imaplib

