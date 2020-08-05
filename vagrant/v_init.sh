#!/bin/sh

set -e

# Ubuntu mirror

cp /etc/apt/sources.list /etc/apt/sources.list.bak
cat << EOF | tee /etc/apt/sources.list
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
EOF

# Docker
apt-get update
apt-get -y install apt-transport-https ca-certificates curl software-properties-common
# step 2: 安装GPG证书
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | apt-key add -
# Step 3: 写入软件源信息
add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
# Step 4: 更新并安装Docker-CE
apt-get -y update
apt-get -y install docker-ce
sudo groupadd docker
sudo gpasswd -a ${USER} docker

mkdir -p /etc/systemd/system/docker.service.d

cat << EOF | tee /etc/systemd/system/docker.service.d/docker.conf
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2375 --containerd=/run/containerd/containerd.sock
EOF

cat << EOF | tee /etc/docker/daemon.json
{
  "registry-mirrors": [
    "https://dockerhub.azk8s.cn",
    "https://hub-mirror.c.163.com",
    "https://registry.docker-cn.com"
  ]
}
EOF

systemctl daemon-reload
systemctl restart docker

sudo apt install -y tmux
sudo apt install -y zsh
sudo apt install -y gcc

sudo apt install -y libmysqlclient-dev
sudo apt install -y python3-dev
sudo apt install -y silversearcher-ag

sudo apt install -y python3-pip
sudo pip3 install -U python-language-server
sudo pip3 install -U flake8

sudo apt autoclean
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

