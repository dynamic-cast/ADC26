# Audio Fingerprinting Project

This project implements an audio fingerprinting system based on Avery Wang's algorithm for Shazam. 

Both reference and query audio files are in 44.1kHz
# Instructions: 
1. Create a virtual environment and activate

For macOS and Linux:
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

The system takes .mp3 files as input for fingerprinting. Import the database recordings to the database_recordings directory.
```bash
'./audio_data/database'
```
Import query files 
```bash
'./audio_data/query'
```

## Input and Output 
```bash
Input: query: 011298_query.mp3 
Output: (1) 011298.mp3, (2) 094468.mp3, (3) 115471.mp3 (4) 071173.mp3 (5) 133802.mp3
```

References:
[1] Wang, A. (2003). An industrial strength audio search algorithm. In Proceedings of the 4th International Conference on Music Information Retrieval (ISMIR 2003) (pp. 7–13) <br>
[2] Defferrard, M., Benzi, K., Vandergheynst, P., & Bresson, X. (2017). FMA: A Dataset For Music Analysis [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5HW28.


