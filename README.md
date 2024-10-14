# Portfolio 7: MapReduce Analysis on Olympic Athletes

This repository contains the Python code and outputs for MapReduce analysis. The assignment focuses on using the MapReduce programming model to analyze Olympic athlete's data from 1980 to 2020.

## Project Overview

The objective of the assignment is to curate and analyze data from the Olympic historical dataset using the MapReduce model. The analysis spans across multiple tasks:

### Task 1: Data Curation
1. **Task 1.1 - Data Extraction:**
   - Extracted medal-winning athlete data from the Summer Olympics between 1980 and 2020.
   - Stored the extracted data in the `athletes.txt` file in the format `<athlete_id, country, year, event, medal>`.

2. **Task 1.2 - Data Organization:**
   - Implemented a MapReduce program to sort the athletes' data in ascending order based on `athlete_id`.
   - Output: `output1_2.txt`.

### Task 2: Data Analysis with MapReduce
1. **Task 2.1 - Top 3 Athletes by Medal Count:**
   - Identified the top 3 athletes with the most gold, silver, and bronze medals from 1980 to 2020.
   - Output: `output2_1.txt`.

2. **Task 2.2 - Top 3 Countries by Gold Medals:**
   - Ranked countries based on their gold medal count from 1980 to 2020.
   - Output: `output2_2.txt`.

3. **Task 2.3 - Top 3 Events by Medal Count per Decade:**
   - Analyzed the top 3 events with the highest medal counts for each decade (1980-1989, 1990-1999, etc.).
   - Output: `output2_3.txt`.

### Task 3: MapReduce Flowcharts
- Created flowcharts illustrating the process of each MapReduce program used in Task 2.

## Files Included

- **task1_1.py**: Script for extracting athlete data (Task 1.1).
- **task1_2.py**: MapReduce program for sorting athlete data (Task 1.2).
- **task2_1.py**: MapReduce program to find top 3 athletes by medal count (Task 2.1).
- **task2_2.py**: MapReduce program to find top 3 countries by gold medals (Task 2.2).
- **task2_3.py**: MapReduce program to find top 3 events by medal count per decade (Task 2.3).
- **athletes.txt**: Extracted data from Task 1.1.
- **output1_2.txt**: Sorted athlete data from Task 1.2.
- **output2_1.txt**: Output for top 3 athletes by medal count (Task 2.1).
- **output2_2.txt**: Output for top 3 countries by gold medals (Task 2.2).
- **output2_3.txt**: Output for top 3 events by medal count per decade (Task 2.3).

## Tools and Technologies
- **Python**: Primary programming language used.
- **MongoDB**: For creating databases and importing datasets.
- **Pymongo**: To connect and interact with MongoDB.
- **MrJob**: For implementing the MapReduce programs.

## Contact Information

For any questions or further information, feel free to contact me at [nafialhasan@gmail.com].

