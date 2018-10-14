Title: Gitlab
Date: 2016-04-15 09:41:39
Tags: DevOps, Gitlab



# Gitlab

gitlab是开源的有web界面的git服务器．

<https://about.gitlab.com/>

安装gitlab:

    sudo apt-get install -y curl openssh-server ca-certificates
    sudo apt-get install -y postfix
    curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash
    sudo EXTERNAL_URL="http://gitlab.example.com" apt-get install gitlab-ee

配置:

    /etc/gitlab/gitlab.rb

***

# CLI

备份：

    > 修改备份路径：gitlab_rails['backup_path'] = "/var/opt/gitlab/backups"
    # gitlab-rake gitlab:backup:create

重新加载配置:

    # gitlab-ctl reconfigure
