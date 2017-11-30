# The story:

Bad news... Canvas is going down :(

Last Friday's afternoon Jerzy came to us and said:

Instracture Inc. has gone bankrupt. They're shutting down Canvas LMS next Saturday. You've got to do something!

Our reaction was simple:

Let's create our own Learning Management System. We'll call it Codecool Management System (CcMS).


# User stories

User stories are very similar to use cases. However they are more precise and defined in form of text. They are like instructions for testing the system. We'll use them during project evaluation.

###### US_J_01

As Jurek,
I want to sign in as a manager,
So that I have access to administrative features.

###### US_J_02

As Jurek,
I want to add a mentor,
So that a new mentor can access the system.

###### US_J_03

As Jurek,
I want to remove a mentor,
So that a mentor cannot access the system anymore.

###### US_J_04

As Jurek,
I want to edit mentor's data,
So that mentor's data is up to date.

###### US_J_05

As Jurek,
I want to see a list of mentors,
So that I know who's working for me.

###### US_J_06

As Jurek,
I want to see a list of students,
So that I know how my students perform.

###### US_KM_01

As Kati or Miriam,
I want to sign in as a regular employee,
So that I can see only features that are relevant to me.

###### US_KM_02

As Kati or Miriam,
I want to see a list of students,
So that I know who's studying and how to contact with them.

###### US_M_01

As a mentor,
I want to sign in as a mentor,
So that I manage my class.

###### US_M_02

As a mentor,
I want to see a list of students,
So that I know how they perform.

###### US_M_03

As a mentor,
I want to add an assignment,
So that it is available to students for submission.

###### US_M_04

As a mentor,
I want to grade an assignment submitted by students,
So that I can track student's performance.

###### US_M_05

As a mentor,
I want to check attendance of students,
So that I can track student's engagement.

###### US_M_06

As a mentor,
I want to add a student to a class,
So that a new student can access the system.

###### US_M_07

As a mentor,
I want to remove a student from class,
So that a student cannot access the system anymore.

###### US_M_08

As a mentor,
I want to edit student's data,
So that I student's data is up to date.

 

###### US_S_01

As a student,
I want to sign in as a Student,
So that I can access features relevant to me.

###### US_S_02

As a student,
I want to submit an assignment,
So that mentor can grade it.

###### US_S_03

As a student,
I want to view my grades,
So that I can see how I perform.

Sample usage

Jerry's usage:

'$python main.py
Please provide a username:
Jerzy
Please provide a password:
*****
Welcome Jerzy!
What would you like to do:
   (1) List mentors
   (2) List students
   (3) Add mentor
   (4) Remove mentor
   (5) Edit mentor
   (0) Exit CcMS
Option: 1' 
~~~
/-------------------------\
| Id  |   Name  | Surname |
|-----+---------+---------|
| 1   | Mateusz | Ostafil |
\-------------------------/
~~~
# Student's usage:

'$python main.py'
~~~
Please provide a username:
Student
Please provide a password:
*****
Welcome Student!
What would you like to do:
    (1) View my grades
    (2) Submit assignment
    (0) Exit CcMS
~~~
# Other requirements

All data should be saved to .csv so that they are available after application restart
Application has to be an OOP application
 

# The design

Now comes the design phase. In this phase we define what classes we'll implement in the system. Think for a while and discuss with your team how would you model it. Then draw an UML use case and class diagram.

