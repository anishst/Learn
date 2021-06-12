# Appium

Appium is an open source automation tool for running scripts and testing native applications, mobile-web applications and hybrid applications on Android or iOS using a webdriver.

http://appium.io/

## Appium Features
- appium concepts: http://appium.io/docs/en/about-appium/intro/?lang=en#appium-concepts
- architecture
    - appium client code > uses JSON to talk to appium server
    - appium server
    - devices/virtual mobile device
- can write test cases in different languages
    - Java, Python, ...
- Supported Platforms
    - iOS
    - Android
    - Firefox OS

## Appium Setup

1. Download Java SDK: https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
   - Set JAVA_HOME path and add sdk bin path to Path variable
2. Setup Android Studio: 
    - Download https://developer.android.com/studio
    - install app
    - find install path: ```C:\Users\<user>\AppData\Local\Android\Sdk```
    - set new system var: ```ANDROID_HOME``` and point to android/sdk foler
    - add ```sdk/tools``` folder to path variable
    - add ```sdk/tools/bin``` folder to path variable
3. Create Virtual Device
    - Open Android Studio
    - Create basic project: File > New Project> Basic Activity
    - wait for build process to complete
    - You should now see Tools > AVD Manager and SDK Manager 
        - AVD = android virtual device
    - click on AVD Manager
    - click on 'Create Virtual Device'
    - select a device (ex. Pixel 2) click Next
    - select an android system image and click on Download link
        - Component Installer window appears and downloads image
    - click Next when download is completed
    - Give 'AVD Name' ; ex. PixelEmulator
        - leave defaults under Advanced Settings
        - NOTE: This part didn't work well in Virtual machine
    - ways to open emulator
        - open android studio > tools > AVD Manager > Your Virtual devices and use Play under Actions column
        - or use command line w/o opening android studio: ```emulator -avd <nameofimage>```
 3. Install NPM
    - need to check ; looks like new 
 3. Install Appium
    - ```npm install -g appium ```     
    - run by running 'appium
    '
## Docker Appium

https://github.com/appium/appium-docker-android

Start appium-docker-android

docker run --privileged -d -p 4273:4723 -v -/.android:/root.android -v /dev/bus/usb:/dev/bus/usb --name appium-container appium/appium

## Troubleshooting

Failed to install Intel HAXM. For details, please check the installation log: "C:\Users\<username>>\AppData\Local\Temp\3\haxm_log.txt"
HAXM installation failed. To install HAXM follow the instructions found at: https://software.intel.com/android/articles/installation-instructions-for-intel-hardware-accelerated-execution-manager-windows
Installer log is located at C:\Users\<username>>\AppData\Local\Temp\3\haxm_log.txt
Installer log contents:
=== Logging started: 5/27/2020  15:44:46 ===
This computer does not support Intel Virtualization Technology (VT-x) or it is being exclusively used by Hyper-V. HAXM cannot be installed. 
Please ensure Hyper-V is disabled in Windows Features, or refer to the Intel HAXM documentation for more information.

https://github.com/intel/haxm

if ADB.EXE outdate error: 
1. tried didn't work: https://developer.android.com/studio/releases/platform-tools.html
2. trying now: https://stackoverflow.com/questions/39036796/unable-to-locate-adb-using-android-studio

 Missing emulator engine program for 'x86' CPU.:
https://www.stkent.com/2017/08/10/update-your-path-for-the-new-android-emulator-location.html


windows 10 hyper v support: 

- https://www.youtube.com/watch?v=M7XoHaG2h0U&t=387s
- https://android-developers.googleblog.com/2018/07/android-emulator-amd-processor-hyper-v.html