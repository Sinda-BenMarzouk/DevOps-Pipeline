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
    ![test](https://user-images.githubusercontent.com/60546216/172487113-b28cc890-a4c3-4b21-a43c-203db598e4c7.png)
    
    * Build : Build the Docker Image and push it to Dockerhub.
    ![build](https://user-images.githubusercontent.com/60546216/172487221-5e5788f6-ff24-4538-a931-d8b11544f28d.png)
 
    
    * Deploy : It is an EC2 deployment job through ssh.
    ![deploy](https://user-images.githubusercontent.com/60546216/172487369-44511307-0f73-48df-8581-8d519bb95ac8.png)

    
