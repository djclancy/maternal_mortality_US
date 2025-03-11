# US Maternal Mortality Rate

## Background 

The United States has a high maternal mortality rate compared to other peer nations[^1] but there is still large variability between the various states. The federal government collects a lot of data from the states on causes of death and makes that publically accessible with some restrictions[^2]. The Census department also collects a lot of socioeconomic data decenially and annually since 2005. We plan to analyze CDC data on the causses of death to see if we can discover trends that help shed light on this issue. 

## Data Sources

* [CDC WONDER](https://wonder.cdc.gov/deaths-by-underlying-cause.html) for general information on pregnancy-related deaths. This source data set will likely be the primary one, it is accessible through queries with an online portal and we will need to do some preprossessing to get it into workable form for subsequent data analysis. We can get county-level year-over-year information for the number of people who died due to pregnancy related issues (under some usage restrictions for privacy purposes). The information can be download as a ```.txt``` file. 
* [NCHS](https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm) for information on number of births and infant deaths.
* [Census American Community Survey](https://www.census.gov/programs-surveys/acs) for some general information on the year-to-year changes in large population centers throughout the US.

## KPIs

* Data-collection and transformation: We need to reformat some of the CDC data.
* Accurately model the population-level causes of state-by-state, region-by-region, and year-by-year disparities in maternal mortality.

## Stakeholders

* People who are pregnant, may become pregnant, or who care about others who are pregnant.
* Public health officials.


## Week 2 Tasks
* Gather and clean regional data from the CDC (by year).
* Add the data from the CDC on obesity rates, nutrition, and other healthy lifestyle datasets.
* State-by-state data for states with a lot of data.
* Search for data on access on maternal care/hospital access (possibly looking through news articles for their data).
* Try to find risk categories for the data.
* Try to incorporate race data for regional data.
* Looking at age-ranges for regional data.



[^1]: https://www.cbsnews.com/news/us-maternal-mortality-rate-higher-whats-different/
[^2]: Some of this data is restricted and so we cannot include conclusions whenever there are fewer than 10 deaths in some region over a period of time.

[^1]: https://www.kff.org/racial-equity-and-health-policy/issue-brief/racial-disparities-in-maternal-and-infant-health-current-status-and-efforts-to-address-them/


