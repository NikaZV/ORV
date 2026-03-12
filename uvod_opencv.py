import cv2 as cv
from pathlib import Path
import numpy as np
BASE = Path(__file__).parent
UTILS = BASE / ".utils"

def razrezi_sliko(slika: np.ndarray, sirina_ps: int, visina_ps: int) -> list[np.ndarray]: