# 运维速查手册

## redis 连接数过多
``` sh
docker exec -it $(docker ps | grep redis | awk '{print $1}') redis-cli -a {pwd}
127.0.0.1:6379> info # info命令能查看关于 Redis 服务器的各种信息和统计数值.
...
# Clients
connected_clients:391
...

```

> 找出有问题的client
> client list: 列出全部客户端信息.
```sh 
127.0.0.1:6379> client list
id=7863 addr=172.18.0.104:56836 fd=6150 name= age=72 idle=72 flags=N db=0 sub=0 psub=0 multi=-1 qbuf=0 qbuf-free=0 obl=0 oll=0 omem=0 events=r cmd=ping
id=7864 addr=172.18.0.50:56262 fd=6151 name= age=72 idle=72 flags=N db=9 sub=0 psub=0 multi=-1 qbuf=0 qbuf-free=0 obl=0 oll=0 omem=0 events=r cmd=ping
id=7865 addr=172.18.0.104:56840 fd=6152 name= age=72 idle=72 flags=N db=0 sub=0 psub=0 multi=-1 qbuf=0 qbuf-free=0 obl=0 oll=0 omem=0 events=r cmd=ping
...
```

> 分析所有客户端连接信息
> tips:
> awk '{print $2}: 输出第二列, 即IP. addr=172.18.0.104:56836.
> awk -F "[=:]" '{print $2}': 通过等号和冒号拆分addr=172.18.0.104:56836, 并输出中间的IP.
> sort: 排序.
> uniq -c: 统计数量并在每列旁边显示该行重复出现的次数.
> 
```sh
cat client-list | awk '{print $2}' | awk -F "[=:]" '{print $2}' | sort | uniq -c | sort -k1,1nr | head -5
5432 172.18.0.50
4244 172.18.0.104
  43 172.18.0.59
  40 172.18.0.54
  32 172.18.0.55

```

> 定位到ip后
> docker inspect: 获取容器/镜像的元数据. --format: 用模板格式化输出.
```sh 
$ docker inspect --format='{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq) | grep 172.18.0.50
/docker_xxxxx-service - 172.18.0.50
$ docker inspect --format='{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq) | grep 172.18.0.104
/docker_yyyyy-service - 172.18.0.104
```
