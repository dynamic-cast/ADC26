# Audio Fingerprinting Project

This project implements an audio fingerprinting system based on Avery Wang's algorithm for Shazam. 
# Instructions: 
1. Create a virtual environment and activate
```bash
 python3 -m venv venv
 source venv/bin/activate
 ```

2. Install dependencies:

```bash 
pip install -r requirements.txt
```

3. Run the main script for end to end execution using the following command in the terminal:

```bash
python3 main.py
```

## Requirements:
1. Make sure you have Python 3.12+ installed.


## Importing files (Input Files)

The system takes .wav or .mp3 files as input for fingerprinting. Import the database recordings to the database_recordings directory.
```bash
'./data/database_recordings'
```
Import query files 
```bash
'./data/query_recordings'
```
## Project Structure


```bash
├── main.py                     # Main script for running the app
├── finger_print                # Where the fingerprint hashes are stored
    └── db_audio.pkl
├── notebooks                   # Contains plots and evaluation (F1, Precision and Recall)
    ├── evaluation.ipynb    
    └── plot.ipynb
├── scripts
    ├── __init__.py
    ├── audio_match.py          # Matching algorithm for query audio files
    ├── config.py               # Stored variables 
    ├── fingerprint_build.py    # Algorithm for building the fingerprint
├── requirements.txt            # Python dependencies for the project
├── README.md                   # Instructions
└── audio_data/                       # Folder for storing audio files 
    ├── database/    # Store database audio files
    └── query/       # Store query audio files

```
## Output files
Output files are located in output.txt 
Example:
```bash
query: 011298_query.mp3 matches: 011298.mp3, 094468.mp3, 115471_query.mp3
```

References:
[1] Wang, A. (2003). An industrial strength audio search algorithm. In Proceedings of the 4th International Conference on Music Information Retrieval (ISMIR 2003) (pp. 7–13)
[2] Defferrard, M., Benzi, K., Vandergheynst, P., & Bresson, X. (2017). FMA: A Dataset For Music Analysis [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5HW28.


