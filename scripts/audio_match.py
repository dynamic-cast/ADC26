import pickle
import glob
import heapq
from pathlib import Path
from scripts.config import *


class AudioMatch():
    def __init__(self, fp_database_path: str):
           
        fp_database = Path(fp_database_path)
        pkl_files = list(fp_database.glob("*.pkl"))

        if not pkl_files:
            raise FileNotFoundError (f".pkl file not found in {fp_database.resolve()}")

        with open(pkl_files[0], "rb") as f:
            self.master_db = pickle.load(f)

    
    def query_match(self, query_fp: dict) -> dict:

        candidate_scores = {}
        raw_align = {}

        # Check raw frequency matches
        for q_hash, q_tuple in query_fp.items():
            if q_hash in self.master_db:
                
                for q_fname, q_time in q_tuple:

                    if q_fname not in candidate_scores:
                        candidate_scores[q_fname] = {}
                        raw_align[q_fname] = {}


                    for db_fname, db_time in self.master_db[q_hash]:
                        # Check how many frequencies are in common
                        candidate_scores[q_fname][db_fname] = candidate_scores[q_fname].get(db_fname, 0) + 1

                        # Save raw alignments of frequencies- use for retrieval instead of master_db
                        if db_fname not in raw_align[q_fname]:
                            raw_align[q_fname][db_fname] = []
                        raw_align[q_fname][db_fname].append((db_time, q_time))

        result = {}

        # Offeset computation for top candidates
        for q_fname, scores in candidate_scores.items():
            top_db_candidates = heapq.nlargest(3, scores.keys(), key=lambda x: scores[x])

            hist = {}
            for db_fname in top_db_candidates:
                for db_time, q_time in raw_align[q_fname][db_fname]:
                    offset = db_time - q_time
                    hist[(db_fname, offset)] = hist.get((db_fname, offset), 0) + 1

            if not hist:
                continue

            # Find the peak of the histogram 

            sort_peaks = sorted(hist.items(), key=lambda x: x[1], reverse=True)

            top_unique_songs = []

            for (song, offset), votes in sort_peaks:
                if song not in top_unique_songs:
                    top_unique_songs.append(song)
                    
                # Stop once we have exactly 3 unique songs
                if len(top_unique_songs) == 3:
                    break
            
            result[q_fname] = top_unique_songs

        return result

