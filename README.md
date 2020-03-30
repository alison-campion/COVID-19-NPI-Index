# covid-19-npi-tracker
Tracking non-pharmaceutical interventions made in the effort to slow the spread of covid-19

## Description
Please comment on the "COVID-19 NPI Index" project. Our goal is to create a data-driven “index” to 1) quantify the strength of the Non-Pharmaceutical Interventions (NPIs) put in place in a jurisdiction and later 2) develop a measure of enforcement of NPIs. The NPIs are a sum of NPI actions, each with a relative numerical weight. As society creates more NPIs, the highest values (full NPI action) will grow larger. We expect to update the COVID-19 NPI Index every 2 - 4 weeks during the early days of pandemic and less frequently as we reach equilibrium. Our initial graphical display shows a map of the USA with the COVID-19 NPI Index calculated for each state. Select a state and see the detail of each state with the timeline associated with each NPI. We'd like to partner with other clinicians, researchers and public health experts to refine the index. Please join in!


## Methodology
### Data Acquisition
Thus far, we have been manually tracking state-level executive orders issued by the governors of all 50 states, Puerto Rico, and Washington, D.C.. Our principal source of information is the [National Governors’ Association website ](https://www.nga.org/coronavirus/). See the table below for the types of NPIs and executive order variables included. For each variable, we recorded the date of announcement or date of planned implementation if noted. We also included the date of order expiration if provided. The dates of order expiration are updated if the order durations lengthen.

### NPI Index Development
To create the NPI Index, each NPI was assigned a numerical value to represent its “strictness,” based on our knowledge of epidemiology and human behavior. See the table below for the values assigned to each NPI.

| NPI Type        | Executive Order    | Sources | Index Value  |
|:--------------- |:------------------ |:------------:|
| Social distancing | Mass gathering restrictions (1000 people) | 5 | NGA |
| | Mass gathering restrictions (250 people) | 6 | NGA |
| | Mass gathering restrictions (100 people) | 7 | NGA |
| | Mass gathering restrictions (50 people) | 8 | NGA |
| | Mass gathering restrictions (25 people) | 9 | NGA |
| | Mass gathering restrictions (10 people) | 10 | NGA |
| | *Telework recommendation* |  | *in progress* |
| | Restaurant and bar closure (take-out and delivery only) | 15 | NGA |
| | Non-essential business closure | 15 | NGA |
| School closure | K-12 school closure | 15 | NGA |
| | Daycare/preschool closure | 11 | *in progress |
| | College/university closure | 12 | *in progress* |
| Population restrictions | Stay at home/indoors ("shelter in place"), **recommended** for certain populations (e.g. age 65+) | 18 | NGA |
| | Stay at home/indoors ("shelter in place"), **required** for all people (except essential workers) | 20 | NGA |
| | Curfew | 16 | NGA |
| | *Travel restrictions, **recommended*** | 12 | *in progress* |
| | *Travel restrictions, **required*** | 18 | *in progress* |
| Resource activation | State of Emergency declared | 10 | NGA |
| | National Guard activation | 10 | NGA |
| | Major Disaster declaration | 10 | NGA |

Additional interventions include those that strengthen the capacity of the healthcare system. These interventions are likely to have an effect on reducing the number of deaths due to COVID-19 but less likely to directly affect transmission and number of cases in the population. These variables--along with others--could be assembled into a separate Index focused on the healthcare system.

|     |     |
|:--------------- |:------------------ |
| Healthcare system capacity strengthening | Medical licensure relaxation |
| | Elective surgeries postponed |
| | 1135 CMS waiver approved |


## Participants

Nicole Campion Dialo, fifth-year student at the University of Maryland School of Medicine, anticipating graduation with MD and MPH in spring 2020.

Tim Olivier MD, 2020 graduate of the University of Massachusetts Medical School

Alison Campion, Research Associate at [Development Data Lab](http://www.devdatalab.org/).


## Resources
* [MITRE](https://c19hcc.org/resource/country-comparison#case_and_death_counts_over_time) 
* [New Zealand classification system for NPI](https://covid19.govt.nz/assets/COVID_Alert-levels_v2.pdf) 
