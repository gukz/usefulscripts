#!/bin/bash
PYTHON3=/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu
test -d $PYTHON3 || exit
sudo apt install python3-dev
sudo apt install make
sudo apt install libncurses5-dev
sudo make distclean 
sudo ./configure --with-features=huge \
    --enable-multibyte \
    --enable-python3interp \
    --with-python3-config-dir=$PYTHON3 \
    --enable-gui=gtk2 \
    --enable-largefile \
    --disable-netbeans \
    --enable-fail-if-missing \
    --enable-cscope \
    --prefix=/usr/local/
sudo make VIMRUNTIMEDIR=/usr/share/vim/vim80
sudo make install
