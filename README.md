# Small_Group_Project
### Group Members: Charles Hedeen, Autum, Brock Vriesman, Audric Perger


# E- Extract
### Project Idea: 
* Use COVID-19 data from multiple websites. We found data on : test results (postitive and negative), deaths, hospital beds (available, occupied, etc.).
-We plan to break the database down to be sorted and merged by state.

### Type of Data:
 * We found two CSV files containing data on : test results (postitive and negative, deaths, hospital beds (available, occupied, etc.).
 * We will merge these two files on states to have data by each state available.

    Websites:
    https://covidtracking.com/data - daily testing data by state
    https://worldpopulationreview.com/states/state-abbreviations - states names and abbreviations

### Type of Database:
-We will use the Mongo database to publish our findings.


# T - Transform
### Use Jupyter Notebook to bring in and transform csv data
(all csv files are data by state)

The tools we used to transform our csv files we pulled from the internet was Jupyter Notebook and the Pandas module. For each of the three csv's found online, we read the csv into jupyter notebook to get an idea of the data we were working with. Once the data was in a Jupyter Notebook, we examined the columns and selected only columns relevant to our future database.

For the test results data, the original csv file provided a number of different statisitics regarding test results. We decided to focus only on: date, state, negative, negative increase, positive, positive increase, death, death probable, pending, and total test results. This was done in the COVID-19-Daily-Testing.ipynb.We will use these columns of data to merge with other csv files.
We also had to merge a csv with state abbreviations with the test results in order to merge csv with our next csv file.

The third csv file we used was data on the number of estimated beds available and occupied by Covid patients. From this csv file, we will have information on: inpatient beds occupied estimate, percent estimate and total number/percentage of beds available. This work can be found in the estimatedBeds.ipynb.

We then merged our two csv we crafted into one pandas dataframe that will include all the information from both tables. The final csv that will be deployed to our Mongo database will be broken up by state and include data from 08/12/2020 - 09/12/2020. Since we decided to merge the two csv files, we will be using a NON-RELATIONAL data base (mongodb). 


# L - Load
### Using MongoDB:
Code in the 'CSV_to_MongoDB', if run from beginning to end, will create a Mongo database on your local machine which will allow you to analyize the data independently.

Steps to take to create database on local machine:
* Be sure you have MongoDB installed on your machine
* Open the 'MongoDB Compass Community App' and click the 'Connect' button
![MongoDB Compass Community App Home Page](/Readme_files/Images/MongoDB_Home_Screen.png)
* In the repository folder you have cloned to your machine, open Jupyter Notebook by typing 'jupyter notebook' into the command line
* In Jupyter Notebook, navigate to the 'CSV_to_MongoDB' notebook
* Inside 'CSV_to_MongoDB', run the Kernel (If you want to run cell by cell, click into the top cell and click SHIFT + ENTER down the entire list of cells)
* Navigate back to the 'MongoDB Compass Community App' and click the refresh button in the top left corner
![Refresh DB List](/Readme_files/Images/Refresh_DB_List.png)
* You should now see a database titled '  final_testing_beds_db' and within that database, a collection titled 'testing_beds', and a list of documents as shown below
![Final Data Display](/Readme_files/Images/Final_Data_Display.png)

Querying the database:
* Basic querying code is available in the 'CSV_to_MongoDB' notebook. Code that gives you all of the contents in the database as well as starter code for querying based on field values.
