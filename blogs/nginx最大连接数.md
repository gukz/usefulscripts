nginx 使用epoll，通过ulimit -n 来设定最大连接数
ulimit -n 是linux内核的参数，如果nginx是在docker里启动（docker和宿主机共享内核）
nginx启动时如果修改了nlimit -n的话，其他进程是否受影响？
需要注意什么呢

nlimit -n 配置的是nginx的worker的最大连接数，想要增大nginx的最大连接数，增加worker即可。
ulimit -n 是进程参数，与内核无关。

