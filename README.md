# **Yoga Moves And Their Sequences**

## **Contents**

* [Intro](#Introduction)
    * [Objective](#Objective)
    * [Proposal](#Proposal)
* [Architecture](#Architecture)
    * [Trello Board](#Trello-Board)
    * [Risk Assessment](#Risk-Assessment)
    * [Entity Relationship Diagram](entity-relationship-diagram)
    * [Continuous Integration](#continous-integration)
* [Development](#Development)
    * [Unit Testing](#Unit-Testing)
* [Footer](#Footer)


## **Introduction**

### **Objective**

For this project our main goal was:
> To create a CRUD application that utilised the supporting tools, methodologies and technologies covered so far during our training.

Specifically we were required to:  

* Create a Trello board or equivelant detailing our user stories, use cases and tasks needed in order to complete the project.
* Create a relational database with at least two tables in it modeling a relationship between said tables. A one to many relationship was the basic requirement needed.
* Put forward clear documentation from a design phase highlighting the architecture used as well as a detailed risk assessment.
* Build a functional CRUD application created with Python, following the best practices and design principles relating to the requirements set on our Trello board. 
* Design fully automated tests for validation of the application.
* Build a fully functioning front-end website using Flask.
* Fully integrate our code into a version contol system using a feature-branch model which will then be built through a CI server and deployed to a cloud based virtual machine.

### **Proposal**

For my project my aim was to create a website focusing on yoga sequences and the moves that make up said sequences. Users could create as many yoga moves as they desired and then add their moves to a sequence allowing them to build thier own workout. 

The best way I can show you what my aim was is by detailing the CRUD functionality below:

**Create:**

* Yoga Move:
    * Name
    * Instructions
    * Difficulty

* Yoga Sequence:
    * Name
    * Difficulty
    * Time (To complete in minutes)
    * Moves (referenced from Yoga Moves database)

**Read:**

* The yoga moves along with their instructions and difficulty level
* The yoga sequences along with their overall difficulty, time to complete and the moves within the sequence.

**Update:**

* Contents of Yoga Move.
* Contents of Yoga Sequence.

**Delete:**
* Yoga Moves
* Yoga Sequence

## **Architecture**

### **Trello Board**

[Link to my trello](https://trello.com/b/uiTDLXOj/yoga-database)

I decided to use Trello because it is simple in it's design, free to use and is a good visual aid to manage your progress. I implemented MOSCOW prioritisation using a color scheme. I then came up with users stories to outline what was essential for the project and what could be added later on given time. 

![Image of trello board](https://i.imgur.com/uGmkthF.png)

### **Risk Assessment**

[Link to my risk assessment](https://drive.google.com/file/d/1sVfHTS3elFST2yJLKFw23mm5o9dXxSsp/view?fbclid=IwAR2iUwtC9rpF7Q6T-WdpysZn49X9h6FEpmyEuyMg-PZLmy_1wVFVJn74WLs)

For my initial risk assessment I focused more on the physical risks associated with attempting to do yoga. This initial analysis along with the user stories put forward, helped me clarify what types of information to host on my site aswell as within my database. For instance, a risk that came up was the possibilty of injury for the user. This lead me to display warnings on my site and showed me it would be important to have a difficulty section within the database, stemming from beginner to intermediate to advanced. The rows highlighted in grey came after I learned more about the risks associated with databases from the course.

![Image of risk assessment](https://i.imgur.com/pzFothU.png)


### **Entity Relationship Diagram**

The first version of my ERD was as follows:

![One to many ERD](https://i.imgur.com/vMe0edK.png)

As you can see, my initial idea was to have a one to many database relationship between yoga_moves and yoga_sequences. This would have worked if each sequence had its own set of moves. However, due to the fact that I wanted the user to be able to reference the same moves in multiple sequences it then became clear that a many to many relationship was needed. I created a third table to reference both of the primary keys from the other two tables as you can see below:

![Many to many ERD](https://i.imgur.com/b4gayXX.png)


### **Continous Integration**

Through learning about continous integration and having now experienced it in practice within my own project, I see how it would fit in well with any business. It allows for a streamlined development process that leads to deploying a product that has a strong foundation. I use Git as my version control system to push my code to andd then used Jenkins to fetch and build the repositiory. Finally I used Pytest in combination with Jenkins to display the coverage reports.

![Image of CI Pipeline](https://i.imgur.com/ebrOYh5.png)


## **Development**

### **Unit Testing**

As mentioned unit testing was used to ensure that the functionality of different parts of my database all ran correctly. I attempted to be as in depth as possible with my testing. I wanted to ensure that all elements of the database were covered. I ran pytest in the terminal of my app and ended up with 100% coverage as seen below.

![Image of terminal tests](https://i.imgur.com/5Swfy00.png)

I then created two .sh files, one for running the program and one for running the test through Jenkins. As you can see the result returned was the same.

![Image of tests run through jenkins](https://i.imgur.com/3bcAn7p.png)

## **Footer**

### **Future Improvements**:

There are a number of improvements I would like to make given the time in the future.

* I would implement selenium testing within my tests so that I could ensure that the site was tested in the most thorough way possible.
* I would look at creating a comment section and rating system for the yoga poses and sequences created, ,so that users could share knowledge with each other. This would also requre a social media style username and password functionality.
* FInally I would incorporate images and videos in to my html code so any user could visually see how to do a specific pose, rather than just reading about how to.

### **Author**

Joshua Browne