FROM ubuntu:16.04

ENV XMRSTAK_CMAKE_FLAGS -DXMR-STAK_COMPILE=generic -DCUDA_ENABLE=OFF -DOpenCL_ENABLE=OFF

RUN apt-get update \
    && set -x \
    && apt-get install -qq --no-install-recommends -y build-essential ca-certificates cmake git libhwloc-dev libmicrohttpd-dev libssl-dev

RUN git clone https://github.com/fireice-uk/xmr-stak.git \
    && cd /xmr-stak \
    && bash -c 'echo -e "#pragma once \nconstexpr double fDevDonationLevel = 0.0 / 100.0;" > ./xmrstak/donate-level.hpp' \
    && cmake ${XMRSTAK_CMAKE_FLAGS} . \
    && make \
    && cd - \
    && mv /xmr-stak/bin/* /usr/local/bin/ \
    && rm -rf /xmr-stak \
    && apt-get purge -y -qq build-essential cmake git libhwloc-dev libmicrohttpd-dev libssl-dev \
    && apt-get clean -qq

VOLUME /mnt

WORKDIR /mnt

ENTRYPOINT ["/usr/local/bin/xmr-stak"]