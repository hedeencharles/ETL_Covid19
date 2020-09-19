# Small_Group_Project
### Group Members: Charles Hedeen, Autum, Brock Vriesman, Audric Perger

<<<<<<< HEAD
fake edit
=======
## Project Idea: 
-Use COVID-19 data from multiple websites. We found data on : test results (postitive and negative), deaths, hospital beds (available, occupied, etc.).
-We plan to break the database down to be sorted and merged by state.


## Type of Data:
 -We found two CSV files containing data on : test results (postitive and negative), deaths, hospital beds (available, occupied, etc.).
 -We will merge these two files on states to have data by each state available.

    Websites:
    https://covidtracking.com/data - daily testing data by state
    https://worldpopulationreview.com/states/state-abbreviations - states names and abbreviations


## Type of Database:
-We will use the Mongo database to publish our findings.
>>>>>>> 76f991f9c4326384241b48df961f48176c6f8818

### Using MongoDB:
Code in the 'CSV_to_MongoDB', if run from beginning to end, will create a Mongo database on your local machine which will allow you to analyize the data independently.

Steps to take to create database on local machine:
    - Be sure you have MongoDB installed on your machine
    - Open the 'MongoDB Compass Community App' and click the 'Connect' button
        [MongoDB Compass Community App Home Page](/Resources/Images/MongoDB_Home_Screen.png)
    - In the repository folder you have cloned to your machine, open Jupyter Notebook by typing 'jupyter notebook' into the command line
    - In Jupyter Notebook, navigate to the 'CSV_to_MongoDB' notebook
    - Inside 'CSV_to_MongoDB', run the Kernel (If you want to run cell by cell, click into the top cell and click SHIFT + ENTER down the entire list of cells)
    - Navigate back to the 'MongoDB Compass Community App' and click the refresh button in the top left corner
        [Refresh DB List](/Resources/Images/Refresh_DB_List.png)
        You should now see a database titled '  final_testing_beds_db' and within that database, a collection titled 'testing_beds'

Querying the database:
    - Basic querying code is available in the 'CSV_to_MongoDB' notebook. Code that gives you all of the contents in the database as well as starter code for querying based on field values.
    