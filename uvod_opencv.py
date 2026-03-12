import cv2 as cv
from pathlib import Path
import numpy as np
BASE = Path(__file__).parent
UTILS = BASE / ".utils"

def razrezi_sliko(slika: np.ndarray, sirina_ps: int, visina_ps: int) -> list[np.ndarray]:
    visina_slike, sirina_slike = slika.shape[:2]
    podslike = []

    for y in range(0, visina_slike, visina_ps):
        for x in range(0, sirina_slike, sirina_ps): 
            podslika = slika[y:y+visina_ps, x:x+sirina_ps]
            podslike.append(podslika)

    return podslike