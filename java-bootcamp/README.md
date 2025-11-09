# Java basics

> this is recap for me

- java is a strongly and  statically typed language, which means type checking is done during compile type as opposed to RUN TIME like python. 
- java is a typical OO language
- supports concurrency (multithreading)
- java is platform-independent, source code is compliled into bytecode, which the JVM interprets 
- objects and instance variables are allocated into heap memory
- local primitive variables and references are stored on the stack during method execution (hence the stack overflow errors)
- the JVM automatically handles object lifecycle, allocating memory when objects are created and reclaiming memory when objects are no longer reachable



# SPRING!: 
- spring is a comprehensive and modular framework for java that facilitates dependency injection, data access, transaction management, etc. 
- Springboot is built on top of the spring framework, and it streamlines the creation of standalone applications with embedded servers, auto config and prod ready features
- Spring MVC



# Tamr specifics: 
- they use GCP, they are cloud native
- BigQuery and bigtable: central storage of golden records. BigTable is a key/value noSQL store, used for high throughput storage
- docker and kubernetes: know about containers, orchestration, and the microservice architecture
- gRPC, protobufs: 
	- protobufs: protocol buffers, a system developed by google for efficiently serializing structured data. 
	- serialization means: taking data (like objects, structs, etc) and turining it into a compact binary format, so you can send it over the network or save it to a disk. 
	- gRPC (google's RPC framework) REQUIRES protobufs, which is why it is relevant to tamr's tech stack

	- What are RPC frameworks and what is gRPC? 
	- RPC stands for remote procedure call, core idea is call a function that lives on another machine as if it were local
	- instead of sending it over the network via HTTP RESTful request, you just call a function, and the framework handles all the network calls and communications underneath. 
	- RPC frameworks generally handle serialization, transport (sending data over the network like HTTP/1.1 TCP) and code generation, giving us a client and server stubs so that both sides can talk in the same language automatically
	- yo this is sick
	- gRPC generally performs better than REST. should use this for the next project i do


- BigQuery, Snowflake:
	- bigquery is a serverless, managed data warehouse that runs on GCP
 - so i think it is just like a sql store but for really big data? interesting
 - Snowflake is a cloud native data warehouse that runs on AWS, Azure or GCP.
 - you manage warehouses (essentially compute clusters) that you can scale up or down as needed (highly scalabile like microservices)


-**Kubernetes, Helm, Istio, Docker**: 
- docker is for containerization (put your app in a box), runs everywhere tge same way I have written Dockerfiles before
```
example:
FROM python:3.10
COPY ./app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```
`docker build -r myapp . `
`docker run -p 5000:5000 myapp`

- K8s: Run thousands of boxes at scale
- kubernetes is a container orchestration system, it manager how and where docker containers run of a cluster of machines. it decides whatruns where, when to scale up or down, load balancing, etc.
- kubernetes helps with microservice architecture, scaling, and orchestration of containers, works in tandem with docker

- Helm is an app store and a config manager for kubernetes. it is like npm or pip for kubernetes apps
- Istio is traffic control and a security layer for microservices

```
Developer builds app
   ↓
Docker → packages it into a container
   ↓
Kubernetes → runs and manages containers in production
   ↓
Helm → simplifies deploying/managing Kubernetes configs
   ↓
Istio → manages how containers talk to each other (network, security, telemetry)

```
- jenkins: helps automate building code, running tests, packaging, and deploying to servers or cloud infrastructures.
- 


