# ETL - Using Covid-19 Data
* Group Members: Charles Hedeen, Autum Perconti, Brock Vriesman, and Audric Perger.


# Objective:
* Our objective is to perform the ETL (Extract, Transform, and Load) operation on reliable Covid-19 data. The data sources will be cleaned and combine into one dataset. The combined dataset will then be uploaded to MongoDB.  
* We sourced COVID-19 data from multiple websites. We found data on : test results (positive and negative), deaths, hospital beds (available, occupied, etc.). The database will be broken down to be sorted and merged by state.
* Additionally, we will create a Python Web Scraper App to automate the <i>extract</i> process.

# *E* - Extract data 
### <u>Data</u>:
 * We sourced datasets with data on: **test results** (positive and negative, deaths) and **hospital beds** (available, occupied, etc.).
 * **State abbreviations** data will be used to combine datasets. 
* Sources:
  * https://covidtracking.com/data - daily testing data by state
  * https://healthdata.gov/dataset/covid-19-estimated-patient-impact-and-hospital-capacity-state/resource/1051acef-72b2-4fbc#{} - estimated number of beds data
  * https://worldpopulationreview.com/states/state-abbreviations - states names and abbreviations
    * (all sourced as CSV files)


# *T* - Transform data

### <u>Tools used in the transform stage</u>: 
* CSV files and source data from the internet 
* Python Jupyter Notebook - Successfully developed a Python app to automate the transform process by: pulling in CSV files, cleaning each and combining datasets into one DataFrame to be exported. 
* Python's PyMongo Module - 
* MongoDB's Compass - verify data uploaded 

### <u>Transform Process</u>:
* Read each dataset into Python, identify format and structural differences between the datasets.
* The two datasets were joined on state abbreviations. Below are descriptions of each dataset:
  * <u>Test results dataset</u> original CSV file contained a variety of statistics regarding test results. The focus was on: date, state, negative, negative increase, positive, positive increase, death, death probable, pending, and total test results.
    * see Dataset_cleaning&merging.ipynb for cleaning of data
  * <u>Estimated number of beds available and occupied by Covid patients dataset</u>. This CSV file provided data on: inpatient beds occupied estimate, percent estimate and total number/percentage of beds available.
    * see estimatedBeds.ipynb file for code
  * <u>State abbreviations dataset</u>. Used to join datasets.
* Datasets merged into one DataFrame. The final DataFrame will be exported as a CSV file and uploaded to our non-relational Database, MongoDB.

# *L* - Load to NoSQL database
### <u>Using MongoDB</u>:
Code in the 'CSV_to_MongoDB', if run from beginning to end, will create a Mongo database on your local machine which will allow you to analyze the data independently. Assuming you have MongoDB running in the background on your machine. [Click Here](https://docs.mongodb.com/manual/mongo/#start-the-mongo-shell-and-connect-to-mongodb) to learn how to run MongoDB on your local machine.

Steps to take to create database on local machine:
* Be sure to have MongoDB installed on your machine
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

# Web scraper and Flask app:

The final part of our project was to approach the question from a different angle to accomplish something similar but noticeably different. Instead of pulling in large amounts of data from CSV files to create a large database of COVID-19 testing data across states, what about trying to scrape just a few selective fields of data off the website that provides the same data? In this case, from the URL https://covidtracking.com/data (the same source as the CSV files from above) using the beautifulsoup and splinter modules, we successfilly scraped only the state name, total cases, and new cases (as updated daily). This data was stored as a list of dictionaries that was then converted into a Mongo database and used for a flask app to display the scraped data in a bootstrap HTML table on a localhost server.

This process mirrors the same basic ETL steps taken using CSVs using pandas, just in a noticeably different way. The extraction part is obviously the most different. Instead of selecting CSVs containing lots of fields that need to be merged into a pandas DataFrame and cleaned of unwanted data, scraping the website into a beautifulsoup object provides all the information on the webpage in a format that's virtually impossible to read and needs to be traversed with splinter to pull out the wanted information.

Once this data has been scraped into a beautifulsoup object, the transformation step simply involves traversal to desired data and reformatted as a list of dictionaries. In the initial build of the scraper, I was able to use 'class' to pull the data, but after running it later on I discovered that the class names had been changed, which may be an anti-scraping tactic used by the website. I had to rewrite it to use 'browser.find_by_xpath' which now works just as well as the original build. 

After the extraction (scraping) and transformation (spliter tranversal and saving as a list of dictionaries), the final step of loading this into a Mongo database happens automatically within the flask app after the scrape has been initiated with the browser redirecting back to the homepage where the scraped data is displayed as a bootstrap table. 

This Extraction, Transformation, and Loading process looks very different from the CSVs-to-pandas-dataframe method, and it has it's own benefits, downsides, and challenges. One benefit is that once the app and scraper have been created, it can be used to retrieve all the fields of data specified as it has been updated on the site just by running the scraper again. This makes it very convenient if being used regularly to retrieve the most up-to-date information from the same web source. The biggest downside to this method as opposed to using pandas is that you need to know ahead of time what information you want to get, or else be forced to set up a splinter traversal to every single field of data that you might possibly want. This can get cumbersome and requires spending a lot of time using the inspector function in your web browser to fully understand how to get the data you want. 

This data scraped is only one half of what would be needed to fulfill the requirements and, given enough time, the first part of the process would be replicated with another set of relevant data scraped from elsewhere and combined together to be a full ETL, but it serves as a working skeleton for what is possible using web scrapping and the presentation using flask.
