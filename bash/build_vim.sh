./configure --enable-multibyte \
            --enable-pythoninterp \
            --enable-luainterp \
            --enable-gui=gtk2 --enable-cscope --prefix=/usr
make VIMRUNTIMEDIR=/usr/share/vim/vim82/
sudo make install
