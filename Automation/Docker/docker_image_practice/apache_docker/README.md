## Testing custom apache server
1.  Build image: ```docker build -t anish_apache .```
2. Test app : ```docker run -dit -p 80:80 myapacheapp ```

If you need to publish:

1. stop container
2. commit changes to new imag: ```docker commit -m "my own apache server" containerid anish_apache```
3. docker login ; enter username password
4. tag the image: ```docker tag anish_apache <dockerhubid>/tagname```
5. push to docker hub: ```docker push <dockerhubid>/tagname ```

You can test this new image by: ```docker run -p 80:80 anishst/anish_apache```