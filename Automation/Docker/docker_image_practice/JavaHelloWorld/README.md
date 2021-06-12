# Java Hello world

To show how to run HelloWorld app in docker container 

1. build image with tag name of javahelloworld: ```docker build -t=javahelloworld .```
2. run image: ```docker run javahelloworld```; you will see Hello World in terminal output
    - to provide an arguments during run: ``` docker run -e NAME=ANISH javahelloworld```
3. if you want to see contents of container: ```docker run -it --entrypoint=/bin/sh javahelloworld```

