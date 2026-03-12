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

def povecaj_sliko(slika: np.ndarray) -> np.ndarray: 
    # pridobimo visino, sirino originalne slike
    visina, sirina = slika.shape[:2]

    if slika.ndim == 3: #barvna slika
        nova_slika = np.zeros((visina * 2, sirina * 2, slika.shape[2]), dtype=slika.dtype)
    else: # sivinska slika 
        nova_slika = np.zeros((visina * 2, sirina * 2), dtype=slika.dtype)

    nova_slika[0::2, 0::2] = slika # zgornji levi kot
    nova_slika[1::2, 0::2] = slika # spodnji levi kot
    nova_slika[0::2, 1::2] = slika # zgornji desni kot 
    nova_slika[1::2, 1::2] = slika # spodnji desni kot 

    return nova_slika