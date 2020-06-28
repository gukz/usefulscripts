#!/bin/sh
code() {
    # sudo passwd root
    export LC_ALL=en_US.UTF-8
    sudo cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
    sudo apt-get install ntpdate
    sudo ntpdate -u ntp.api.bz
    sudo apt update
    sudo apt install -y translate-shell
    sudo apt install -y python3-pip
    sudo apt install -y zsh
    sudo apt install -y vim
    sudo apt install -y tmux
    sudo apt install -y silversearcher-ag
    sudo pip3 install flake8
    sudo pip3 install python-language-server
    sudo apt remove --purge tracker   # 删除缓存
    # TODO go 环境 安装
    # sudo apt autoclean # 清理旧版本的软件缓存
    # sudo apt clean     # 清理所有软件缓存
    # sudo apt autoremove # 删除系统不再使用的孤立软件
    # dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P # 清除残余的配置文件

    # sudo apt-get remove --purge 软件名   # 删除软件
    # 删除多余内核
    # uname -a  # 查看当前ubuntu系统的内核
    # dpkg --get-selections|grep linux # 查看安装的所有内核
    # sudo apt-get remove linux-image-xxxxxxxxx-generic  # 把xxxx替换成相应的内核版本
    # sudo apt-get remove linux-headers-xxxxxx
    # sudo apt-get remove linux-headers-xxxxxx-generic
    # sudo /usr/sbin/update-grub  # 清理内核后，重新生成grub文件
}

code()
