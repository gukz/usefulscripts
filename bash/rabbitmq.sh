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

# get host ip
HostIP="$(ip route get 1 | awk '{print $NF;exit}')"
HostName="$(hostname)"

CurDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DatabaseDir=/data/rabbitmq/data

start() {
  docker kill rabbitmq 2>/dev/null
  docker rm -v rabbitmq 2>/dev/null

  docker run -d --name rabbitmq \
    -v ${DatabaseDir}:/var/lib/rabbitmq \
    -e RABBITMQ_DEFAULT_USER=devos \
    -e RABBITMQ_DEFAULT_PASS=devos \
    -e RABBITMQ_DEFAULT_VHOST=devos \
    --net=host \
    --restart=always \
    --log-opt max-size=10m \
    --log-opt max-file=9 \
    rabbitmq:3.8.2-management-alpine
}

stop() {
  docker stop rabbitmq 2>/dev/null
  docker rm -v rabbitmq 2>/dev/null
}

shell() {
  docker exec -it rabbitmq bash
}

##################
# Start of script
##################

case "$1" in
  start) start ;;
  stop) stop ;;
  restart)
    stop
    start
    ;;
  shell) shell;;
  *)
    echo "Usage:"
    echo "./rabbitmq.sh start|stop|restart"
    exit 1
    ;;
esac

exit 0
