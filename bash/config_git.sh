#!/bin/sh
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
