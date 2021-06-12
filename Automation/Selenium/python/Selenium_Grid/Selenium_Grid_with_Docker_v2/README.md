#  Steps to get docker selenium grid running

1. create yaml file: docker-compose.yml
2. navigate to yaml file 
3. run this command: ```docker-compose up```; use this if you don't want to see console messages: ```docker-compose up -d``` 
4. test grid is running by going to: https://localhost:4444/grid/console
5. to stop ```docker-compose down```
6. use this command to see run status: ```docker-compose ps```


## Scale up chrome

1. ```docker-compose up -d --scale chrome=4```

## Scale up chrome and firefox
docker-compose up -d --scale chrome=3 --scale firefox=3
