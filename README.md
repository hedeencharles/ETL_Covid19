# ETL Small Group Project
### Group Members: Charles Hedeen, Autum Perconti, Brock Vriesman, Audric Perger


# E- Extract
### Project Idea: 
* Use COVID-19 data from multiple websites. We found data on : test results (postitive and negative), deaths, hospital beds (available, occupied, etc.).
-We plan to break the database down to be sorted and merged by state.

### Type of Data:
 * We found two CSV files containing data on : test results (postitive and negative, deaths), and hospitalbeds (available, occupied, etc.).
 * We will merge these two files on states to have data by each state available.

* Websites:
    * https://covidtracking.com/data - daily testing data by state
    * https://worldpopulationreview.com/states/state-abbreviations - states names and abbreviations
    * https://healthdata.gov/dataset/covid-19-estimated-patient-impact-and-hospital-capacity-state/resource/1051acef-72b2-4fbc#{} - estimated beds data

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

Web scraper and Flask app:

The final part of our project was to approach the question from a different angle to accomplish something similar but noticably different. Instead of pulling in large amounts of data from CSV files to create a large database of COVID-19 testing data across states, what about trying to scrape just a few selective fields of data off the website that provides the same data? In this case, from the URL https://covidtracking.com/data (the same source as the CSV files from above) using the beautifulsoup and splinter modules, and pulled out just the state name, total cases, and new cases (as updated daily). This data was stored as a list of dictionaries that was then converted into a Mongo database and used for a flask app to display the scraped data in a bootstrap HTML table on a localhost server.

This process mirrors the same basic ETL steps taken using CSVs using pandas, just in a noticably different way. The extraction part is obviously the most differnt. Instead of selecting CSVs containing lots of fields that need to be merged into a pandas dataframe and cleaned of unwanted data, scraping the website into a beautifulsoup object provides all the information on the webpage in a format that's virtually impossible to read and needs to be traversed with splinter to pull out the wanted information.

Once this data has been scraped into a beautifulsoup object, the transformation step simply involves traversal to desired data and reformated as a list of dictionaries. In the initial build of the scraper, I was able to use 'class' to pull the data, but after running it later on I discovered that the class names had been changed, which may be an anti-scraping tactic used by the website. I had to rewrite it to use 'browser.find_by_xpath' which now works just as well as the original build. 

After the extraction (scraping) and transformation (spliter tranversal and saving as a list of dictionaries), the final step of loading this into a Mongo database happens automatically within the flask app after the scrape has been initiated with the browser redirecting back to the homepage where the scraped data is displayed as a bootstrap table. 

This Extraction, Transformation, and Loading process looks very different from the CSVs-to-pandas-dataframe method, and it has it's own benefits, downsides, and challenges. One benefit is that once the app and scraper have been created, it can be used to retrieve all the fields of data specified as it has been updated on the site just by running the scraper again. This makes it very convinient if being used regularly to retrieve the most up-to-date information from the same web source. The biggest downside to this method as opposed to using pandas is that you need to know ahead of time what information you want to get, or else be forced to set up a splinter traversal to every single field of data that you might possibly want. This can get cumbersome and requires spending a lot of time using the inspector function in your webbrowser to fully understand how to get the data you want. 

ideally, the Mongo DB would be dropped every time the scrape was run to ensure the data displayed was actually up to date and not leftover from a previous scrape. However, this was not able to be accomplished in time for submission of this porject, and instead the page now displays the date and time of the most recent scrape. 

This data scraped is only one half of what would be needed to fullfil the requirements and, given enough time, the first part of the process would be replicated with another set of relevant data scraped from elsewhere and combined together to be a full ETL, but it serves as a working skeleton for what is possible using web scrapping and the presentation using flask.
