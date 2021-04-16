#This file builds and image and runs it
#!/usr/bin/env bash

ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
echo ${ROOT_DIR}
echo "**********************Building an IMAGE*******************"
docker build -t centosjemeter .

echo "**********************Running a CONTAINER*****************"
docker run --rm -v "${ROOT_DIR}:/opt/apache-jmeter-5.2.1/code" centosjemeter ${@}

echo "CONTAINER RAN SUCCESSFULLY"