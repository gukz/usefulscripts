#!/bin/bash

check_non_empty() {
  # $1 is the content of the variable in quotes e.g. "$FROM_EMAIL"
  # $2 is the error message
  if [[ "$1" == "" ]]; then
    echo "ERROR: specify $2"
    exit -1
  fi
}

check_exec_success() {
  # $1 is the content of the variable in quotes e.g. "$FROM_EMAIL"
  # $2 is the error message
  if [[ "$1" != "0" ]]; then
    echo "ERROR: $2 failed"
    echo "$3"
    exit -1
  fi
}

CurDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# get host ip
HostIP="$(ip route get 1 | awk '{print $NF;exit}')"

# set data dir
MyData=/data/mysql/data
MyLog=/data/mysql/logs

MyData2=/data/mysql_new/data
MyLog2=/data/mysql_new/logs

start() {

  img_name="mysql"

  docker kill $img_name 2>/dev/null
  docker rm -v $img_name 2>/dev/null

  docker run -d --name $img_name \
    -v ${CurDir}/conf:/etc/mysql/conf.d \
    -v ${MyData}:/var/lib/mysql \
    -v ${MyLog}:/var/log/mysql \
    -e MYSQL_ROOT_PASSWORD=p123456 \
    -p 3306:3306 \
    --log-opt max-size=10m \
    --log-opt max-file=9 \
    mysql:5.7 \
    --character-set-server=utf8mb4 \
    --collation-server=utf8mb4_unicode_ci

    # --net=host \
  check_exec_success "$?" "start mysql container"
}

start_new() {

  img_name="mysql_new"

  docker kill $img_name 2>/dev/null
  docker rm -v $img_name 2>/dev/null

    # --net=host \
    # -v ${MyData}:/var/lib/mysql \
    # -v ${MyLog}:/var/log/mysql \

  docker run -d --name $img_name \
    -v ${CurDir}/conf:/etc/mysql/conf.d \
    -v ${MyData2}:/var/lib/mysql \
    -v ${MyLog2}:/var/log/mysql \
    -e MYSQL_ROOT_PASSWORD=p123456 \
    -p 3307:3306 \
    --log-opt max-size=10m \
    --log-opt max-file=9 \
    mysql:5.7 \
    --character-set-server=utf8mb4 \
    --collation-server=utf8mb4_unicode_ci

  check_exec_success "$?" "start ${img_name} container"
}


stop() {
  docker stop mysql 2>/dev/null
  docker rm -v mysql 2>/dev/null
}

destroy() {
  stop
  rm -rf ${MyData}
  rm -rf ${MyLog}
}

createdb() {
  docker exec mysql mysql -u root -pp123456 -e "create database $1 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
}

##################
# Start of script
##################

case "$1" in
  start) start ;;
  start_new) start_new ;;
  stop) stop ;;
  restart)
    stop
    start
    ;;
  destroy) destroy ;;
  createdb) createdb $2;;
  *)
    echo "Usage:"
    echo "./mysql.sh start|stop|restart"
    echo "./mysql.sh destroy"
    echo "./mysql.sh createdb [db_name]"
    exit 1
    ;;
esac

exit 0
