# Zalenium

A flexible and scalable container based Selenium Grid with video recording, live preview, basic auth & dashboard.

https://opensource.zalando.com/zalenium/

## Steps to Use:
1. Pull down below docker images; big ~ 2GB
    - docker pull elgalu/selenium
    - docker pull dosel/zalenium

2. Run on Windows:
    - docker run --rm -ti --name zalenium -p 4444:4444 ^
      -v /var/run/docker.sock:/var/run/docker.sock ^
      -v /c/Users/your_user_name/temp/videos:/home/seluser/videos ^
      --privileged dosel/zalenium start   
3. access console: https://localhost:4444/grid/console

4. admin console: https://localhost:4444/grid/admin/live

5. run your tests and then you should see live preview on the console page

6. Use Interactive mode if you need to interact with the app manually

7. Dashboard: https://localhost:4444/dashboard/#
    - shows videos of all test runs; gives option to download for attaching to defect if needed
    - check selenium logs
    