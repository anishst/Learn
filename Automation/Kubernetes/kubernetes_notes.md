# Kubernetes

- open-source system for automating deployment, scaling and management of containerized applcation
- founded by Google
- system for running many different types of containers over multiple different machines
- use when you need to run many different containers with different images
- Docker container orchestrator. This means we can automatically balance workloads, keeping deployments highly available, responsive, and efficient.
- [Overview](https://kubernetes.io/docs/home/)

![Architecture](https://d33wubrfki0l68.cloudfront.net/2475489eaf20163ec0f54ddc1d92aa8d4c87c96b/e7c81/images/docs/components-of-kubernetes.svg)


## Master
- controls all the nodes
- where we interact with kubernetes with Kube-API server via $kubectl
- etcd - key/value storage, persistent storage
    - by https://coreos.com/
- controllers
    - node 
    - replication
    - endpoint
    - service/account & token
- scheduler

## Nodes
- workers; does the real job using manifest file (JSON or YAML)
- components
    - kubelet
        - agent that runs on each node in cluster
    - kube-proxy
        - network manager
    - container runtime
        - software responsible for running containers
            - ex. Docker, rkt, runc etc.
## Pods
- simplest unit
- encapsulates an app container
- pod yaml example; src: https://medium.com/better-programming/getting-started-with-kubernetes-for-python-254d4c1d2041
    ```yaml

    apiVersion: v1
    kind: Pod
    metadata:
      name: api-pod
      labels:
        run: connectApi
    spec:
      containers:
        - name: client
          image: jamescalam/hello-api
          ports:
            - containerPort: 3000
    ```
  
## Pre-reqs
 
- Windows: docker for Windows with Hyper-V enabled
- Mac: docker for Mac
- kubectl command line utility to interact with Kubernetes clusters
- Windows Install: https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-windows


## Overall Setup
- For dev envs use minikube
    - minikube
        - for managing the VM ( LOCAL Only) 
    - kubectl 
        - for managing containers in node (this is used in dev and production)
- For prod
    - Managed solutions
        - amazon elastic container service for Kubernetes (EKS)
        - setup on AWS: https://github.com/yankils/Simple-DevOps-Project/blob/master/Kubernetes/Kubernetes-setup.MD
        - google cloud Kubernetes engine (GKE)
    - DIY setup
- Setup Videos: https://bah.udemy.com/course/valaxy-devops/learn/lecture/15899610?start=225#overview


## Install order
1. install kubectl
2. Install a VM driver virtualbox
3. install minikube  - https://kubernetes.io/docs/tasks/tools/install-minikube/

## Minikube Setup on Windows Pro

These instructions are for setting up and installing Minikube and its dependencies for use on Windows Pro with Docker Desktop and HyperV

### Install Kubectl
1. Create a new directory that you will move your kubectl binaries into. A good place would be C:\bin

2. Download the latest kubectl executable from the link on the Kubernetes doc page:
   https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-windows

3. Move this downloaded .exe file into the bin directory you created.

4. Use Windows search to type “env” then select “Edit the system environment variables”

5. In the System Properties dialog box, click “Environment Variables”.

6. In System Variables click on the “Path” Variable and then click “Edit”

7. Click “New” and then type C:\bin

8. Drag the newly created path so that it is higher in order than Docker's binaries. This is very important and will ensure that you will not have an out of date kubectl client.

9. Click "OK"

10. Restart your terminal and test by typing kubectl into it. You should get the basic commands and help menu printed back to your screen. If this doesn't work try restarting your machine.

11. Run kubectl version --client to verify that you are using the newest version and not the out of date v1.10 version

### Install Minikube
1. Download the Windows installer here:

https://storage.googleapis.com/minikube/releases/latest/minikube-installer.exe

2. Double click the .exe file that was downloaded and run the installer. All default selections are appropriate.

3. Open up your terminal and test the installation by typing minikube. You should get the basic commands and help menu printed back to your screen. If this doesn't work try restarting your machine.

Starting Up Minikube
Since by default Minikube expects VirtualBox to be used, we need to tell it to use the hyperv driver instead, as well as the Virtual Switch we created earlier.

Start up a terminal as an Administrator. Then, in your terminal run:

minikube start --vm-driver hyperv

Important note, all minikube commands must be run in the context of an elevated Administrator.

## Install on Mac and Linux

https://kubernetes.io/docs/tasks/tools/install-minikube/


## The Process
- We create our Docker image.
- Upload the image to Docker Hub.
- Configure our pod, which houses the container
- Configure our cluster network using a service.
- Deploy our pod and service to the cluster.
- Deploy a python api - https://medium.com/better-programming/getting-started-with-kubernetes-for-python-254d4c1d2041 

## Cluster Setup Steps

1. make sure you can access minikube:
    - minikube version
    - if needed add local bin to path var: ```export PATH=$PATH:/usr/local/bin```
2. start cluster: ```minikube start```
    - will take few mins
    - check status: ```minikube status```
3. verify kubectl: ```kubectl version```
4. get cluster info: ```kubectl cluster-info```
5. get cluster ip addr: ```minikube ip```
6. view k8 dashboard: ```minikube dashboard```
7. if dashboard doesn't launch automatically, get url from command. example: ```http://127.0.0.1:45205/api/v1/namespaces/kube-system/services/http:kubernetes-dashboard:/proxy/```
8. view nodes from command prompt: ```kubectl get nodes```
9. create a container: ```kubectl run my-web-server --image=nginx --port=80```
10. view pod list: ```kubectl get pods```
11. get pod details: ```kubectl describe pod <podname>```
12. get node details: ```kubectl describe node minikube```
13. expose a service: ```kubectl expose deployment my-web-server --type=NodePort```
    - you can view the service in the Dashboard under services section; private ip
14. view exposed services: ```kubectl describe service my-web-server```
    - ```Name:                     my-web-server
        Namespace:                default
        Labels:                   run=my-web-server
        Annotations:              <none>
        Selector:                 run=my-web-server
        Type:                     NodePort
        IP:                       10.108.68.151
        Port:                     <unset>  80/TCP
        TargetPort:               80/TCP
        NodePort:                 <unset>  30045/TCP
        Endpoints:                172.17.0.5:80
        Session Affinity:         None
        External Traffic Policy:  Cluster
        Events:                   <none>
        ```
15. access the service public ip address:
    - ```minikube service my-web-server --url=true```
        - it will give you the public ip; example: ```http://192.168.99.100:30045```
        - click to access. you should see the nginx default page
16. accesss logs using cmd: ```kubectl logs <service name>```; example: ```kubectl logs my-web-server-59c4495c76-m6vp4```
17. scaling the app
    - get current services running: ```kubectl get deployment```  
        ```
        NAME            READY     UP-TO-DATE   AVAILABLE   AGE
        my-web-server   1/1       1            1           36m```    
    - scale the service:  ```kubectl scale --replicas=3 deployment/my-web-server```
        - output: ```deployment.extensions/my-web-server scaled```
    - get service instance count: ```kubectl get deployment```
        ```
        NAME            READY     UP-TO-DATE   AVAILABLE   AGE
        my-web-server   3/3       3            3           40m
        ``` 
18. stop/delete the cluster: 
    - stop ```minikube stop```
    - delete ```minikube delete```
    
    
## Videos
- Kubernetes for Tester series: https://www.youtube.com/playlist?list=PL6tu16kXT9PpKXQADb8AyJ1zHyp7xDHHo

## Resources

- [Play with K8 - A simple, interactive and fun playground to learn Kubernetes](https://labs.play-with-k8s.com/)
    - [Workshop](https://training.play-with-kubernetes.com/kubernetes-workshop/)