# Pull base image.
FROM mysql:5.7

# Code below is to install github opensource project mysql2redis 👉 https://github.com/dawnbreaks/mysql2redis
# install dependences
RUN apt-get  update
RUN apt-get  install -y  git gcc cmake \
    && apt-get install -y  libjemalloc1 libjemalloc-dev \
    && apt install -y libexpat1-dev  libmysqlclient-dev libaprutil1-dev libapr1-dev \
    && ln -s /usr/include/apr-1.0 /usr/include/apr-1

RUN apt update \
    && apt install -y libmariadbclient-dev libmariadbclient-dev-compat

RUN cd ~ \
    && git clone --depth=1 http://github.com/redis/hiredis  \
    && cd hiredis \
    && make \
    && make install 

# if you are modifying this file and want to use mysql below version 5.7.8, you should uncomment this section to get lib_mysqludf_json.so and uncomment line 106 to install json udf at startup
#RUN cd ~ \
#    && git clone --depth=1 https://github.com/mysqludf/lib_mysqludf_json.git \
#    && cd lib_mysqludf_json \
#    && gcc $(mysql_config --cflags) -shared -fPIC -o lib_mysqludf_json.so lib_mysqludf_json.c \
#    && cp lib_mysqludf_json.so /usr/lib/mysql/plugin

RUN cd ~ \
    && git clone --depth=1 https://github.com/dawnbreaks/mysql2redis.git \
    && cd mysql2redis \
    && make \
    && cp lib_mysqludf_redis_v2.so /usr/lib/mysql/plugin/

# create udf at startup
RUN cd ~/mysql2redis/test \
    # && mv install_json_udf.sql /docker-entrypoint-initdb.d \  # if you are modifying this file and want to use mysql below version 5.7.8, you should uncomment this line to install json udf at startup
    && mv install_redis_udf.sql /docker-entrypoint-initdb.d

# clean
RUN cd ~ \
    && rm -rf * \
    && apt-get  remove -y git wget gcc \
    && apt-get autoremove -y && apt-get autoclean -y \
    && apt-get clean && rm -rf /var/lib/apt/lists/*