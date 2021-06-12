https://hub.docker.com/_/python

docker run -it --rm --name simple_python_script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python hello_world.py

