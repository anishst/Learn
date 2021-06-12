FROM alpine
# install java
RUN  apk add openjdk8
# set java to path variable
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/bin
# set working directory 
WORKDIR /usr/share/app
# add code to work directory
ADD Test.java Test.java
# compile and run program; $NAME will have the value user types in when running the program
ENTRYPOINT javac Test.java && java Test $NAME