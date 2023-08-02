## avl_task
Repo for technical task


## Contains
* Jenkins_config
* service1
* service2
* create-namespace.yaml
* deploy.sh
* docker-compose.yaml
* README.md
* service1-deployment.yaml
* service2-deployment.yaml

## About

* Service1 and service2 dirs contain python scripts, Dockerfiles and requirements.txt for both services.
* Service1 is a web service that uses flask and returns hash value of given string.
* Service2 downloads content of a given webpage and sends it to service1 to calculate hash number.

* Images for both services can be built with "docker-compose build".
* Containers for both services can be ran with "docker-compose up".
* Services can be tested with Curl while containers are runnig. e.g: "curl -X POST -H "Content-Type: application/json" -d '{"url":"https://www.index.hr/"}' http://localhost:8001/hash_webpage"

* deploy.sh is a bash script that takes versions for service1 and service2 and uses docker-compose to deploy them. After they are running, they are tested with curl.

* service1-deployment.yaml is file for applyng kubernetes deployment for service1
* service2-deployment.yaml is file for applyng kubernetes deployment for service2