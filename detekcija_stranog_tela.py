import cv2
import numpy as np

matricaHE = np.loadtxt('HE_csv', delimiter=',')
matricaLE = np.loadtxt('LE.csv', delimiter=',')

tolerancija = 1e-3 * 2**9

srednja_vrednost_HE = np.average(matricaHE)*tolerancija
srednja_vrednost_LE = np.average(matricaLE)*tolerancija

uslovHE = matricaHE > srednja_vrednost_HE
uslovLE = matricaLE > srednja_vrednost_LE

slika = np.uint8(~(uslovHE & uslovLE)) * 2**8-1

cv2.imshow('Slika sa obojenim pikselima', slika)
cv2.imwrite("SlikaSaObojenimPikselima.tif", slika)
cv2.waitKey(0)
cv2.destroyAllWindows()