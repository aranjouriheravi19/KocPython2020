<img src="img/Covid19.jpg" width=1000/>

# Covid-19 project: Investigating the effect of different factors on the COVID-19 mortality rate #

## Description
The world has been encountered with a challenging and difficult situation since COVID-19 got to a pandemic situation. Not only COVID-19 have too high rate prevalence, but also its mortality rate is high, specifically between old people. Scientists declare many factors related to the mortality rate of this disease.In this project, the effect of these factors has been investigated to specify which factors are the most effective ones.

## Table of Contents
* [Dataset](#Dataset)
* [Analysis Prodecure](#Analysis-Procedure)  
* [Results](#Results)  
* [Usage](#Usage)  
* [Conclusion](#Conclusion)  


## Dataset

The used data is available at: [owid-covid-data.csv](https://ourworldindata.org/coronavirus)

### Data Structure

* **iso_code:** The International Organization for Standardization (ISO) created and maintains the ISO
3166 standard – Codes for the representation of names of countries and their subdivisions.  

* **location:** This variable represents full name of countries.

* **date:** The dataset is organized based on date. 

* **total_cases:** It is a cumulative variable, which shows total number of infected persons in a country.                                                                          
* **new_cases:** The quantity of new confirmed infected persons during a day.

* **total_deaths :** It is a cumulative variable, which shows total number of passed away persons in a country.

* **new_deaths:** New confirmed passed away persons during a day by Covid-19.

* **total_cases_per_million:** Total number of confirmed infected people per a million population.   

* **new_cases_per_million:** Number of new confirmed infected people per a million population. 

* **total_deaths_per_million:** Total number of confirmed expired people per a million population. 

* **new_deaths_per_million:** Number of new confirmed expired people per a million population.  

* **total_tests:** It shows how many tests have been done totally in a country.  

* **new_tests:** It displays how many new tests during a day are operated in a country.  

* **total_tests_per_thousand:** Total number of tests per thounands of population  

* **new_tests_per_thousand:**   Number of new tests per thousands of population 

* **tests_units:** This variable shows with which criteria each country counts its operated tests.   

* **stringency_index:** This index indicates if there is rigid governmental rules to control the Covid-19 prevalence or not.  

* **population:** It shows the population of countries. 

* **population_density:** It shows the number of people per unit of area in each country.  

* **median_age:** It shows what the median age of a country is.  

* **aged_65_older:** The rate of people older than 65.  

* **aged_70_older:** The rate of people older than 70.  

* **gdp_per_capita:** shows a country's GDP divided by its total population.  

* **extreme_poverty:** Which portion of a society lives in the severe poverty situation. 

* **cvd_death_rate:** This index shows the prevalence of heart disease(Cardiovascular disease) in each countries.  

* **diabetes_prevalence:** This index displays the prevalence of diabetes in each countries. 

* **female_smokers:** The rate of smoking between female persons in a country. 

* **male_smokers:** The rate of smoking between male persons in a country.  

* **handwashing_facilities:** Indicates if there is handwashing facilities in a country available or not.   

* **hospital_beds_per_100k:** Specifies how many beds are available per a hundred thousands of population. 
 


## Analysis Procedure

### preprocessing
1. Rows with missing data were eliminated
2. Rows with zero total cases were dropped
3. Feature selection process:  
    * 1:
    * 2:
    * 3:
4.
5.


## Usage tips
The required packages to run the script are: matplotlib, lightgbm, pandas, sklearn, and ipywidgets  
  
  
  
**ipywidgets installation:**  
  Users can install and activate the current version of ipywidgets with pip or conda.  
  
    pip install ipywidgets
    jupyter nbextension enable --py widgetsnbextension
   


## Results

## Conclusion






Reference
-------

