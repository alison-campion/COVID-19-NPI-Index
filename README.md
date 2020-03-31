# COVID-19-NPI-Index
Tracking non-pharmaceutical interventions made in the effort to slow the spread of covid-19

## Description
Please comment on the "COVID-19 NPI Index" project. Our goal is to create a data-driven “index” to 1) quantify the strength of the Non-Pharmaceutical Interventions (NPIs) put in place in a jurisdiction and later 2) develop a measure of enforcement of NPIs. The NPIs are a sum of NPI actions, each with a relative numerical weight. As society creates more NPIs, the highest values (full NPI action) will grow larger. We expect to update the COVID-19 NPI Index every 2 - 4 weeks during the early days of pandemic and less frequently as we reach equilibrium. Our initial graphical display shows a map of the USA with the COVID-19 NPI Index calculated for each state. Select a state and see the detail of each state with the timeline associated with each NPI. We'd like to partner with other clinicians, researchers and public health experts to refine the index. Please join in!


## Methodology
### Data Acquisition
Thus far, we have been manually tracking state-level executive orders issued by the governors of all 50 states, Puerto Rico, and Washington, D.C.. Our principal source of information is the [National Governors’ Association website ](https://www.nga.org/coronavirus/). See the table below for the types of NPIs and executive order variables included. For each variable, we recorded the date of announcement or date of planned implementation if noted. We also included the date of order expiration if provided. The dates of order expiration are updated if the order durations lengthen.

### NPI Index Development
To create the NPI Index, each NPI was assigned a numerical value to represent its “strictness,” based on our knowledge of epidemiology and human behavior. See the table below for the values assigned to each NPI.

| NPI Type        | Executive Order    | Sources        | Index Value |
|:--------------- |:------------------ |:--------------|:------------:|
| Social distancing | Mass gathering restrictions (1000 people) |  NGA | 5 |
| | Mass gathering restrictions (250 people) | NGA | 6 |
| | Mass gathering restrictions (100 people) | NGA | 7 | 
| | Mass gathering restrictions (50 people) | NGA | 8 | 
| | Mass gathering restrictions (25 people) | NGA | 9 | 
| | Mass gathering restrictions (10 people) | NGA | 10 |
| | *Telework recommendation* | *in progress* |  |
| | Restaurant and bar closure (take-out and delivery only) | NGA | 15 | 
| | Non-essential business closure | 15 | NGA | 
| School closure | K-12 school closure | 15 | NGA | 
| | Daycare/preschool closure | *in progress* | 11 | 
| | College/university closure |  *in progress* | 12 |
| Population restrictions | Stay at home/indoors ("shelter in place"), **recommended** for certain populations (e.g. age 65+) | NGA | 18 | 
| | Stay at home/indoors ("shelter in place"), **required** for all people (except essential workers) | NGA | 20 | 
| | Curfew | NGA | 16 | 
| | *Travel restrictions, **recommended*** | *in progress* | 12 | 
| | *Travel restrictions, **required*** | *in progress* | 18 | 
| Resource activation | State of Emergency declared | NGA | 10 | 
| | National Guard activation | NGA | 10 | 
| | Major Disaster declaration | NGA | 10 | 

Additional interventions include those that strengthen the capacity of the healthcare system. These interventions are likely to have an effect on reducing the number of deaths due to COVID-19 but less likely to directly affect transmission and number of cases in the population. These variables--along with others--could be assembled into a separate Index focused on the healthcare system.

|     |     |
|:--------------- |:------------------ |
| Healthcare system capacity strengthening | Medical licensure relaxation |
| | Elective surgeries postponed |
| | 1135 CMS waiver approved |

## Example Output
Here is our NPI Index calculated for March 30, 2020 for each state in the U.S.


## Next Steps
There are a few directions we’d like to head next-- we would like to collaborate with others to make these happen:
1) Statistically test our index against case and death rates in each state and make adjustments to the weighting as necessary.
2) Develop a method to measure implementation/enforcement of the NPIs and add this parameter to the index.
3) Determine the best way to incorporate data about healthcare system capacity strengthening-- should these interventions be built into their own index? Or should these interventions be added to the current NPI Index?


## Participants

Nicole Campion Dialo, fifth-year student at the University of Maryland School of Medicine, anticipating graduation with MD and MPH in spring 2020.

Tim Olivier MD, 2020 graduate of the University of Massachusetts Medical School

Alison Campion, Research Associate at [Development Data Lab](http://www.devdatalab.org/).


## Resources and References
* Prem, K et al. The effect of control strategies to reduce social mixing on outcomes of the COVID-19 epidemic in Wuhan, China: a modelling study. The Lancet Public Health. 2020 March 25. [Available here.](https://www.thelancet.com/journals/lanpub/article/PIIS2468-2667(20)30073-6/fulltext).
* MITRE COVID-19 Healthcare Coalition. Assessing change in COVID-19 case and death rates across different countries. 2020 March 25. [Available here.](https://c19hcc.org/resource/country-comparison#case_and_death_counts_over_time)
* New Zealand COVID-19 Alert Levels. [Available here.](https://covid19.govt.nz/assets/COVID_Alert-levels_v2.pdf)
* National Governors Association. What Steps Have States Taken To Address Coronavirus? COVID-19 Updates. [Available here.](https://www.nga.org/coronavirus/)
