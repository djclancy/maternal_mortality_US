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


# What is in the repo

## Data

### Merged Data Sets

``` data/merged_data_sets``` <- Final data sets. 
Contains:
```merged_data_raw_totals.csv``` with raw totals by state.
```merged_data_scaled_totals.csv``` with features normalized by population or births.
### Data Used in Analysis

```data/acs_income_by_year``` <- American Community Survey data on state-level income distribution.

```data/behavioral_data``` <- CDC DNPAO data on nutrition, physical activity, and obesity.

```data/cdc_data``` <- CDC maternal mortality data.

```data/natality_data``` <- CDC natality data.


### Additional data for future use


```data/all_division_data``` <- American Community Survey data broken up by division instead of by state.

```data/acs_health_insurance_data``` <- health insurance information for all the states from the American Community Survey.

### Data manipulation:

In the folder ```data_manipulation``` we combine the data into the ```.csv``` files contained in ```data/merged_data_sets```.


## Analysis:

### Exploratory and Final Analysis
```final_analysis``` contains:
Exploratory analysis in ```exploratory_analysis.ipynb```.
Final comparison and analysis in ```model-training-testing.ipynb```.

### Additional analysis
We have additional exploratory analysis and model comparisons in ```additional_analysis```.


[^1]: https://www.cbsnews.com/news/us-maternal-mortality-rate-higher-whats-different/
[^2]: Some of this data is restricted and so we cannot include conclusions whenever there are fewer than 10 deaths in some region over a period of time.

[^1]: https://www.kff.org/racial-equity-and-health-policy/issue-brief/racial-disparities-in-maternal-and-infant-health-current-status-and-efforts-to-address-them/


