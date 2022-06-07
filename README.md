# Application for Software Testing & DevOps Pipeline
A CRUD python application used to demonstrate the examples of the 4 types of software testing and implemented through the CI/CD pipeline.

## Application Description

- The user can create, read, update or delete a note from the todo list.
- We used sqlite3 for the database, initialised in database.py which contains the tables we specified (in our case, only Note)
- We used Flask for the web development.

Here's a video demonstrating the possible functionalities of our application :

https://user-images.githubusercontent.com/60546216/172417281-4435aae7-8923-40c2-93aa-5dcdffc52e5f.mp4


## Software Testing 
- Each one of these test levels is located in a seperate folder with its Readme file:
    * UnitTest
    * IntegrationTest
    * e2e Test
    * UAT

## Devops Pipeline
- We integrated a CI/CD pipeline on Push using GitHub Actions, Docker and Amazon EC2.

The workflow consists of 3 jobs :


    * Test: Run Unit Tests and Integration Tests.
 ![test](https://user-images.githubusercontent.com/60546216/172487904-eb5aa3b8-916b-4d1c-a917-af626cd632c8.png)

    
    * Build : Build the Docker Image and push it to Dockerhub.
  ![build](https://user-images.githubusercontent.com/60546216/172487509-825afb87-0b70-4960-a164-cb529d77c9bf.png)


    
    * Deploy : It is an EC2 deployment job through ssh.
![deploy](https://user-images.githubusercontent.com/60546216/172487527-ec8f56ed-513a-437e-aae7-1436d2334b32.png)

    
