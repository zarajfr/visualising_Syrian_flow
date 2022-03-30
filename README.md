# Visualising_Syrian_flow
This is a complementary repository to visualise the synthetic and empirical trends and maps of Syrian refugee movements.
***
## Authors

 * Zahra Jafari, <zahra.jafari.17@ucl.ac.uk>
   * UCL Jill Dando Institute of Security and Crime Science, University College London
 * Toby Davies,
   * UCL Jill Dando Institute of Security and Crime Science, University College London
 * Shane Johnson,
   * UCL Jill Dando Institute of Security and Crime Science, University College London

# Requirements

The project uses Python and the source code should run on any standard operating system (i.e. Linux/Unix, MacOS, Windows).

## Python Dependencies

 - Python3.6+
 - Other dependencies can be found in the `requirements.txt`.

 To install them run `pip3 install -r requirements.txt`.

# Content of the repository

## Scripts
  - `map_destination_flow.py`
    - A module with the core functions to visualise map of destination flow
  - `trend_destination_flow.py`
    - A module with the core functions to visualise trends of destination flow

## Directories

  - `flow_data`
    - This includes spatio-temporal output of the Syrian flow simulation. These data are visualised in many forms using the codes in the scripts directory.
### Input format

The temporal intervals are monthly. The directory includes csv files corresponding to displacement flows from or towards certain location at certain month. The temporal units are across the columns and the space is across the rows.

## Results

Simulation results are saved in html, pdf and png files.
