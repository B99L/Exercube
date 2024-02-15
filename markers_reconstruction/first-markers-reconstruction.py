import numpy as np
from modules.markerorder import getMarkerOrder
# Marker Indizes für jede Platte
marker_order = getMarkerOrder()
platten = {
    "Platte1": [4, 5, 6, 7],
    "Platte2": [8, 9, 10, 11],
    "Platte3": [12, 13, 14, 15],
    "Platte4": [16, 17, 18, 19],
    "Platte5": [0, 1, 2, 3],  # Hinzugefügte Platte
    "LinkeFerse": [20, 21, 22, 23],  # Neue Platte für linke Fersenmarker
    "RechteFerse": [24, 25, 26, 27]  # Neue Platte für rechte Fersenmarker
}

# Referenzframe zur Berechnung der durchschnittlichen Distanzen
frame_daten = np.array([
    [-28.92438126, -100.96434021, -29.12799835, -99.06578827, 153.73579407,
     161.02684021, 144.98815918, 163.10972595, 197.6464386, 231.75596619,
     199.63873291, 232.98020935, -302.96063232, -314.46054077, -295.64874268,
     -315.68765259, -332.36361694, -359.68572998, -327.93453979, -356.78399658,
     205.08891296, 204.11219788, 242.63180542, 257.25247192, -306.29705811,
     -307.59771729, -347.47625732, -367.65414429],
    [-432.265625, -431.2244873, -463.48931885, -458.99087524, -538.6373291,
     -583.43218994, -513.05841064, -596.72479248, -456.60275269, -513.33233643,
     -454.13183594, -512.05529785, -526.5625, -589.91046143, -511.2338562,
     -595.07592773, -470.14083862, -530.32330322, -469.52786255, -530.92315674,
     -417.63684082, -421.96118164, -434.15081787, -464.53326416, -433.87335205,
     -437.80593872, -452.52706909, -489.9331665],
    [1003.50341797, 1003.2064209, 1048.52514648, 1045.20385742, 757.45129395,
     755.0065918, 686.20904541, 683.99737549, 264.14126587, 263.32070923,
     221.82746887, 219.98893738, 774.99377441, 765.42651367, 705.53588867,
     703.45617676, 267.21115112, 265.10510254, 224.41546631, 222.31968689,
     33.39823914, 65.09871674, 28.89788246, 32.05305862, 35.88646698,
     58.02891159, 27.63437843, 25.39485931]
])




def finde_ebene(p1, p2, p3):
    """ Bestimmt die Ebene, die durch drei Punkte im Raum definiert wird. """
    v1 = p3 - p1
    v2 = p2 - p1
    normalenvektor = np.cross(v1, v2)
    normalenvektor /= np.linalg.norm(normalenvektor)
    return normalenvektor

def schatze_fehlenden_marker(frame, platten, referenz_frame):
    for platte, indices in platten.items():
        fehlende_marker_indices = [i for i in indices if np.isnan(frame[:, i]).any()]
        vorhandene_marker_indices = [i for i in indices if i not in fehlende_marker_indices]

        # Rekonstruiere nur, wenn genau ein Marker in der Platte fehlt
        if len(fehlende_marker_indices) == 1 and len(vorhandene_marker_indices) == 3:
            p1, p2, p3 = [frame[:, idx] for idx in vorhandene_marker_indices]
            normalenvektor = finde_ebene(p1, p2, p3)

            fehlender_index = fehlende_marker_indices[0]
            referenz_position = referenz_frame[:, fehlender_index]
            frame[:, fehlender_index] = referenz_position

    return frame




# Hauptdatenstruktur: D (20 Trials, 3 Dimensionen, 28 Marker, 360000 Frames)
D = np.load(r"C:\Users\nevio\Downloads\Pats (1).npy")

# Rekonstruktion des gesamten D Arrays
for trial in range(D.shape[0]):
    for frame in range(D.shape[3]):
        D[trial, :, :, frame] = schatze_fehlenden_marker(D[trial, :, :, frame], platten, frame_daten)

np.save(r"C:\Users\nevio\OneDrive - ZHAW\5. Semester\Projektarbeit\pats.npy", D)

print("Rekonstruktion abgeschlossen.")


