FROM python:2.7-slim

WORKDIR /app
ADD honeyd.conf
ADD honeypots/Honeyd/ /app

RUN apt-get update
RUN git libevent-dev libdumbnet-dev libpcap-dev libpcre3-dev libedit-dev bison flex libtool automake zlib1g-dev make
RUN mv configure.in configure.ac
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install

EXPOSE 1234

CMD ["honeyd", "-d", "-f", "honeyd.conf"]