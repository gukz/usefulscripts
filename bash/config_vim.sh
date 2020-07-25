#!/bin/sh
vim() {
    test -d ~/.oh-my-zsh || git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
    test -d ~/.oh-my-zsh/plugins/zsh-autosuggestions || git clone git://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/plugins/zsh-autosuggestions
    test -d ~/.oh-my-zsh/plugins/zsh-syntax-highlighting || git clone git@github.com:zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/plugins/zsh-syntax-highlighting
    ln -s /a/vim_config ~/.vim
    ln -s /a/vim_config/vimrc ~/.vimrc
    ln -s /a/vim_config/zshrc ~/.zshrc
    ln -s /a/vim_config/tmux.conf ~/.tmux.conf
    chsh -s /bin/zsh
    # ln vim config to nvim config
    test -d ~/.config || mkdir ~/.config
    ln -s /a/vim_config ~/.config/nvim
    ln -s /a/vim_confi/vimrc ~/.config/nvim/init.vim
}
vim
