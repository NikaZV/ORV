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

def zmanjsaj_sliko(slika: np.ndarray) -> np.ndarray: 
    # pridobimo visino, sirino originalne slike
    visina, sirina = slika.shape[:2]

    y = 1 if visina % 2 != 0 else 0
    x = 1 if sirina % 2 != 0 else 0

    obrezana_slika = slika[y:, x:]

    # izracunamo pov za vsako obmocje - sestejemo vse 4 polozaje in delimo z 4 
    nova_slika = (
        obrezana_slika[0::2, 0::2] + # zgornji levi kot
        obrezana_slika[1::2, 0::2] + # spodnji levi kot
        obrezana_slika[0::2, 1::2] + # zgornji desni kot 
        obrezana_slika[1::2, 1::2] # spodnji desni kot 
    ) /4
    
    return nova_slika

def prestej_piksle_z_barvo(slika: np.ndarray, spodnja_meja: tuple[int, int, int], zgornje_meja: tuple[int, int, int]) -> int:
    # naredimo masko -> true: znotraj meje, false: zunaj meje
    # inRnage: matrika z piksli v obmocju
    maska = cv.inRange(slika, spodnja_meja, zgornje_meja)

    stevilo_pikslov = cv.countNonZero(maska)
    return stevilo_pikslov

def zrcali_sliko_vertikalno(slika: np.ndarray, ROI: str) -> np.ndarray: