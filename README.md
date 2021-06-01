# greehill-restful-app
## Description
A simple containerized API implemented in Python, with K8S manifests, and Helm chart to deploy the app to Kubernetes. The project contains the following:
* API implemented in Python and Flask.
* Dockerfile for containerization
* Python packages to install listed in `requirements.txt`
* Helm chart to deploy the application
* K8S manifests used during development 
## Prerequisites
* A running Minikube cluster with enabled NGINX Ingress controller
* Helm
## Setup
`helm install <release-name> ./MyChart`

Then use

`kubectl get ingress --watch`

and wait for the Ingress to be deployed. Once its IP address is ready you can update your /etc/host file or DNS to redirect your chosen host name to that IP address.

After that the API will be available under your given hostname.

## Usage

The API has three endpoints which can be invoked the following way (using the default hostname described in `values.yaml`)

Returns the current time in UTC:

`curl restapi.example.com/api/v1/time`

Returns CPU utilization of the instance running the API:

`curl restapi.example.com/api/v1/status`

Returns a json serialized `HWSerial` object with a given string parameter:

`curl restapi.example.com/api/v1/serializer/<string-parameter>`
