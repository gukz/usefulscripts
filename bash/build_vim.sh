#!/bin/bash
sudo apt-get install python3-dev
sudo make distclean 
sudo ./configure --with-features=huge \
    --enable-multibyte \
    --enable-python3interp \
    --with-python3-config-dir=/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu \
    --enable-gui=gtk2 \
    --enable-largefile \
    --disable-netbeans \
    --enable-fail-if-missing \
    --enable-cscope \
    --prefix=/usr/local/
sudo make VIMRUNTIMEDIR=/usr/share/vim/vim82
sudo make install
