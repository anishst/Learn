REM docker-compose -f docker-compose.yaml up --scale chrome=4 >>output.txt
docker-compose -f docker-compose.yaml up --scale chrome=3 --scale firefox=3 >>output.txt