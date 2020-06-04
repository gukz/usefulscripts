the user center provider user registry, login, user detail message storage. social account binding&unbinding.
the message center inside app, when app opened, it will update the message list, the editors publish message
from the server, million message is sended to user in seconds. we have 5 apps, each message could be set to
display on target apps, I do this by use a number to represent the target apps, each bit represent an app, so
it is easily to add more apps.
700 million data table reshard
we have sharded into 64 tables, but the data grows too fast, and now each table has over 10 million data and 
cause some slow query. I do the reshard by split all data in to several tasks, and when consumer finish a 
task, it must confirm to the producer. so the resharding process is stateless and can be restart at any time
without the risk of missing data. There has two steps, first is migrate the db data, the second is migrate the
binlog. I decouple the migrage process from project so if other project need to reshard or do similar job. Only
need tiny changes of some config. like db host and table name soon.

a project to read data from k8s informer and provider as a envoy xds server, so the envoy can do service discovery,
and reverse route for all internal service call. if a service A want to call service B, A call envoy first, then
envoy pick up a connection to service B's pod, and reverse the request.

golang building framework and develop the first project in the company, at the begining i met a lot of problems
the orm do not support insertmany on conflict, the apm report all trace to the url(we use restful api, so the path may
contains id), go swagger do 
