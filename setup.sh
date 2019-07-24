sudo apt-get update
sudo apt-get install -y build-essential unzip zip python-pip nginx
curl -s "https://get.sdkman.io" | bash
source "/home/charsyam/.sdkman/bin/sdkman-init.sh"
sdk install java 8.0.212-amzn
pip install kafka-python

wget https://artifacts.elastic.co/downloads/logstash/logstash-7.2.0.tar.gz
tar zxvf logstash-7.2.0.tar.gz

wget http://mirror.navercorp.com/apache/kafka/2.2.0/kafka_2.12-2.2.0.tgz
tar zxvf kafka_2.12-2.2.0.tgz
