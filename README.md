# IPC using Docker Containers
This is a simple IPC prototype which is designed to demonstrate one to one producer-consumer communication using docker containers.

This project is mainly concerned about following three phases:

1. Producer:
    Producer program(Producer.py) genrates 10 random numbers between 1 to 24 (We can change this as per need) and send it to the host called "ipc_server_dns_name" and port 5000. 

2. Consumer:
   Consumer checks for the data on ipc_server_dns_name:5000, picks up the data and print on the terminal. (hostname and port number should be consistent with producer program)
   
3. Containerizing:
   To package producer and consumer as separate containers.



 Note:
  We cannot use 127.0.0.1 as a hostname to communicate with other container as both are running as different containers. If we use localhost, then consumer will listen to its own ip address and producer writes the data on its own ipaddress:port.



Steps to run the container:

1. Base functional requirement should be docker daemon host running on the machine.
2. Pull the producer container from yashashree2001 docker hub repository. (docker pull yashashree2001/producer)
3. Pull the consumer container from yashashree2001 docker hub repository. (docker pull yashashree2001/consumer)
4. Create a docker network to make communication between both the containers (docker network create <network_name> )  
      (e.g. docker network create prod_cons) 
5. First run the producer container (docker run --rm --network=<network name from step 4> --name ipc_server_dns_name yashashree2001/producer)
6. Run the consumer container (docker run --rm --network=<network name from step 4> yashashree2001/consumer)
7. Press Ctrl+C to close the connection
  (if you are getting permission denied for above docker commands, try to use sudo as a prefix for each command :))
  
    
    
    if you are making containers from scratch from above code: 
    
    Replace 2 and 3 steps with below:   
    
    2. Route to producer folder from terminal and create an image using command : docker build -t yashashree2001/producer .
    3. Route to consumer folder from termianl and create an image using command : docker build -t yashashree2001/consumer .
