FROM ruby
MAINTAINER "Jeremy Redd <jredd42@gmail.com>"

#RUN apt-get -y update && apt-get -y install libicu-dev
RUN gem install omniauth-github
RUN git clone https://github.com/jradd/omnigollum.git /opt/omnigollum

WORKDIR /opt/omnigollum
RUN gem build omnigollum.gemspec
RUN gem install omnigollum*.gem

ADD config.rb /config.rb

WORKDIR /wiki
RUN git init

EXPOSE 8212
CMD gollum /wiki  --port 8212 --config /config.rb
