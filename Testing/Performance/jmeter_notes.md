# JMeter

Apache JMeter may be used to test performance both on static and dynamic resources, Web dynamic applications.
It can be used to simulate a heavy load on a server, group of servers, network or object to test its strength or to analyze overall performance under different load types.

https://jmeter.apache.org/index.html

## Setup

Make sure you have Java 8 + setup 

1. Download binary version: http://jmeter.apache.org/download_jmeter.cgi
2. Extract contents
3. Launch tool  by clicking on ApacheJMeter.jar file: ```apache-jmeter-5.2.1\bin\ApacheJMeter.jar```

- GUI
    - templates - use for pre-defined test scenarios

## Terms

- **listener** 
    - elements that gather info about the perf test
    - used to store and view  metrics of tests
    - Latency = time to first byte
    - type of listerns
        1. View Results in Table
        2.  View Results Tree
        3.  Aggregate Report
        4. Graph Results
        5. Summary Report
        6.  Simple Data Writer
        
- **assertions**
    - Assertions =  checks on the Request/Response
    - can be assigned at test plan/ thread group/request levels
    - types:
        -  Response Assertion
        -  Duration Assertion
        -  Size Assertion
        -  HTML Assertion
        -  XML JSON Assertion
        -  XPATH Assertion

## How to create first Jmeter Test

1. Start JMeter
2. Create a TestPlan
3. Create a Thread Group (Users)
    - ramp-up period (seconds) 
4. Add a Sampler (Http)
5. Add Listeners
6. Run the Test

## JMeter HTTP(s) Test Script Recorder
- record your test on JMeter
- add & use Test Script Recorder
- add & use Recording Controller
- use proxy on Firefox, Chrome and System
- add SSL Certificate
- do Request Filtering
- use Recording Template

## Firefox Recording

1. setup proxy settings
2. import jmeter certificate

more details: https://bah.udemy.com/course/learn-jmeter-from-scratch-performance-load-testing-tool/learn/lecture/2198292?start=375#overview

## Chrome Recording

1. BlazeMeter | The Load Testing Cloud - https://chrome.google.com/webstore/detail/blazemeter-the-load-testi/ojcpfajcibinpjdgcbeajgppepnmicnl
    - record using chrome plugin
    - save and export as .jmx file
    - import in JMeter

## Tools

- Fiddler - 
- Blazemeter Proxy Recorder: https://guide.blazemeter.com/hc/en-us/articles/360000271458-Creating-the-Proxy-Recorder-Creating-the-Proxy-Recorder

## Resources

- Youtube videos
    - [Jmeter](https://www.youtube.com/watch?v=SoW2pBak1_Q&list=PLhW3qG5bs-L86nBPwx2hXXpL6FJWyKczg)