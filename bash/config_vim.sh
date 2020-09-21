#!/bin/sh
SHARE_FOLDER=/g

install_docker(){
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
    
#     cat << EOF | tee /etc/systemd/system/docker.service.d/docker.conf
# [Service]
# ExecStart=
# ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2375 --containerd=/run/containerd/containerd.sock
# EOF
    
cat << EOF | tee /etc/docker/daemon.json
{
"registry-mirrors": [
    "https://hub-mirror.c.163.com",
    "https://dockerhub.azk8s.cn",
    "https://registry.docker-cn.com"
  ]
}
EOF
    
    systemctl daemon-reload
    systemctl restart docker
}

install_docker
exit;

config_source() {
    test -f /etc/apt/sources.list.bak || cp /etc/apt/sources.list /etc/apt/sources.list.bak
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
}
# sudo apt update
install_vim() {
    sudo add-apt-repository ppa:jonathonf/vim
    sudo apt update
    sudo apt install -y vim
}
install_vim

apt install -y tmux
apt install -y zsh
apt install -y gcc

sudo apt install -y libmysqlclient-dev
sudo apt install -y libncurses5-dev
sudo apt install -y silversearcher-ag
sudo apt-get install -y libglib2.0-dev
sudo apt-get install -y autotools-dev
sudo apt install -y automake

sudo apt-get install -y python3 python-dev python3-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev python-pip python3-pip

pip3 install -U python-language-server
pip3 install -U flake8

sudo apt autoclean

config_vim() {
    test -d ~/.oh-my-zsh || git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
    test -d ~/.oh-my-zsh/plugins/zsh-autosuggestions || git clone git://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/plugins/zsh-autosuggestions
    test -d ~/.oh-my-zsh/plugins/zsh-syntax-highlighting || git clone git@github.com:zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/plugins/zsh-syntax-highlighting
    rm -rf ~/.vim
    rm -rf ~/.vimrc
    rm -rf ~/.zshrc
    rm -rf ~/.tmux.conf
    ln -s $SHARE_FOLDER/vim_config ~/.vim
    ln -s $SHARE_FOLDER/vim_config/vimrc ~/.vimrc
    ln -s $SHARE_FOLDER/vim_config/zshrc ~/.zshrc
    ln -s $SHARE_FOLDER/vim_config/tmux.conf ~/.tmux.conf
    chsh -s /bin/zsh
}
config_vim

config_git() {
    git config --global user.email "wanggang@microsoft.com"
    git config --global user.name "Gang Wang"
    git config --global alias.st "status -sb"
    git config --global alias.pm "push origin master"
    git config --global alias.br "branch"
    git config --global alias.ck "checkout"
    git config --global alias.cma "commit --amend"
    git config --global alias.cm "commit -m"
    git config --global alias.rb "rebase"
    git config --global core.editor "vim --noplugin"
}

config_git

compaudit | xargs chmod g-w,o-w


install_docker
