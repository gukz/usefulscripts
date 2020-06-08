#!/bin/bash
# sudo make distclean 
sudo ./configure --with-features=huge \
    --enable-multibyte \
    --enable-python3interp=yes \
    --enable-gui=gtk2 \
    --enable-cscope \
    --prefix=/usr/local/
sudo make VIMRUNTIMEDIR=/usr/share/vim/vim82
sudo make install
