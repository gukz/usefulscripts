ent的流程是，加载用户提供的schema文件，生成中间文件放到.entc目录下。然后使用go run执行这个文件，加载spec到内存中。
完成schema到spec

entc 命令需要用户提供schema位置
ent 通过生成一个go源码文件，然后go run该文件把用户定义的schema转化成json。
