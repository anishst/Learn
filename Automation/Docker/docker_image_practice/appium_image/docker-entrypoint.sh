#!/bin/bash

# the docker-entrypoint, which we used to launch the emulator, and get everything connected with Appium

# launch the emulator
exec /opt/adk/tools/emulator -avd Android -no-audio -no-window &
# setup appium
while [ -z $udid ]; do
    udid=`adb devices | grep emulator | cut -f 1`
done
exec appium -p 4723 -bp 2251 --default-capabilities '{"udid":"'${udid}'"}' &