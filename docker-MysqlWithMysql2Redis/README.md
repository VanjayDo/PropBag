# MysqlWithMysql2Redis

### 说明
MysqlWithMysql2Redis是一个基于[官方的mysql5.7 dockerfile](https://github.com/docker-library/mysql/tree/master/5.7)定制的mysql镜像, 其中集成了github开源项目[mysql2redis](https://github.com/dawnbreaks/mysql2redis), 是一个利用udf解决了mysql数据跟redis数据同步的问题.

### DockerImage
我已由该Dockerfile构建了镜像并上传到Docker Hub, 详情请见 👉 [vanjaydo/mysql2redis](https://hub.docker.com/r/vanjaydo/mysql2redis/)

### DockerImage使用教程
使用`docker run -d --name mysql2redis --env MYSQL_ROOT_PASSWORD=123456 vanjaydo/mysql2redis --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci`命令即可快速启动

详情请见 👉 [使用Mysql2Redis自动更新数据到Redis](https://blog.safeandsound.cn/post/PushData2RedisWithMysql2Redis.html)


git clone --depth=1 https://github.com/mysqludf/lib_mysqludf_json.git

gcc $(/usr/bin/mysql_config_editor --cflags) -shared -fPIC -o lib_mysqludf_json.so lib_mysqludf_json.c 