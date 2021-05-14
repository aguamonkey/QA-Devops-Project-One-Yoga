# **Yoga Moves And Their Sequences**

## **Contents**

* [Intro](#Introduction)
    * [Objective](#Objective)
    * [Proposal](#Proposal)
* [Architecture](#Architecture)
* [Development](#Development)
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

### **Trello**

[Link to my trello](https://trello.com)

![Image of trello board]()

### **Risk Assessment**

For my initial risk assessment I focused more on the physical risks associated with attempting to do yoga. This initial analysis along with the user stories put forward, helped me clarify what types of information to host on my site aswell as within my database. For instance, a risk that came up was the possibilty of injury for the user. THis lead me to display warnings on my site and showed me it would be important to have a difficulty section to the database, stemming from beginner to intermediate to advanced. The rows highlighted in grey came after I learned more about the risks associated with databases from the course.

### **Entity Relationship Diagram**

The first version of my ERD was as follows:

![One to many ERD](https://i.imgur.com/vMe0edK.png)

As you can see, my initial idea was to have a one to many database relationship between yoga_moves and yoga_sequences. This would have worked if each sequence had its own set of moves. However, due to the fact that I wanted the user to be able to reference the same moves in multiple sequences it then became clear that a many to many relationship was needed. I created a third table to reference both of the primary keys from the other two tables as you can see below:

![Many to many ERD](https://i.imgur.com/b4gayXX.png)




### **Continous Integration**




## Development

## Footer