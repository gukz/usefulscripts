#!/bin/sh
docker() {
    sudo apt install apt-transport-https ca-certificates software-properties-common curl
    curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu \
    $(lsb_release -cs) stable"
    sudo apt update
    sudo apt install docker-ce
    sudo groupadd docker
    sudo gpasswd -a ${USER} docker
    sudo apt install docker.io
    sudo service docker restart
    # 修改源
    # vi /etc/default/docker
    # DOCKER_OPTS="--registry-mirror=https://docker.mirrors.ustc.edu.cn"
    # systemctl restart docker.service
}
docker()
