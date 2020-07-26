#!/bin/sh
config_vim() {
    test -d ~/.oh-my-zsh || git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
    test -d ~/.oh-my-zsh/plugins/zsh-autosuggestions || git clone git://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/plugins/zsh-autosuggestions
    test -d ~/.oh-my-zsh/plugins/zsh-syntax-highlighting || git clone git@github.com:zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/plugins/zsh-syntax-highlighting
    ln -s /g/vim_config ~/.vim
    ln -s /g/vim_config/vimrc ~/.vimrc
    ln -s /g/vim_config/zshrc ~/.zshrc
    ln -s /g/vim_config/tmux.conf ~/.tmux.conf
    chsh -s /bin/zsh
}
config_vim

config_git() {
    git config --global user.email "gukz@qq.com"
    git config --global user.name "gukz"
    git config --global alias.st "status -sb"
    git config --global alias.pm "push origin master"
    git config --global alias.br "branch"
    git config --global alias.ck "checkout"
    git config --global alias.cma "commit --amend"
    git config --global alias.cm "commit -m"
    git config --global alias.rb "rebase"
    git config --global core.editor "vim"
}

config_git
