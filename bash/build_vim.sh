#!/bin/bash
PYTHON3=/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu
VIMRUNTIME=/usr/share/vim/vim80
VIMDIR=/usr/
test -d $PYTHON3 || (echo "python dir not found" && exit)
test -d $VIMRUNTIME || (echo "vim runtime not found" && exit)
sudo apt install make
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
    --prefix=$VIMDIR
sudo make VIMRUNTIMEDIR=$VIMRUNTIME
sudo make install
