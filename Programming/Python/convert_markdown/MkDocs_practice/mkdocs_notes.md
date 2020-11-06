# MkDocs

https://www.mkdocs.org/#getting-started

1. mkdocs new my-project
2. cd my-project
3. start server: ```mkdocs serve```
4. go to: http://127.0.0.1:8000

## Tutorials

- https://www.sitepoint.com/building-product-documentation-mkdocs/
- https://towardsdatascience.com/creating-software-documentation-in-under-10-minutes-with-mkdocs-b11f52f0fb10
- with docker
    - create docker docker file
    ```dockerfile
        FROM python:3.8
        RUN pip3 install mkdocs
        COPY ./my-project/ /my-project/
        WORKDIR /my-project/
        EXPOSE 8080
        CMD ["mkdocs", "serve"]
     ```
    - build and run: ```docker build -t imagename . && docker run -p 8080:8080 imagename```
    - https://medium.com/@edsonalcalamx/running-nethereum-docs-with-docker-5b8a4c25d42f
    - https://github.com/elamperti/docker-mkdocs