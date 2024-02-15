import numpy as np

def ersetze_nan_mit_mittelwerten(D, max_erweiterung=120):
    num_trials, num_dims, num_markers, num_frames = D.shape
    num_blocks = num_frames // 120

    for trial in range(num_trials):
        for dim in range(num_dims):
            for marker in range(num_markers):
                for i in range(num_blocks):
                    start_index = i * 120
                    end_index = (i + 1) * 120
                    block = D[trial, dim, marker, start_index:end_index]

                    # Erweitere den Block, wenn nur NaN-Werte vorhanden sind
                    erweiterung = 0
                    while np.isnan(block).all() and erweiterung <= max_erweiterung:
                        erweiterung += 60
                        erweiterte_start = max(0, start_index - erweiterung)
                        erweiterte_end = min(num_frames, end_index + erweiterung)
                        block = D[trial, dim, marker, erweiterte_start:erweiterte_end]

                    # Ersetze NaN-Werte im ursprünglichen Block durch den Mittelwert des (erweiterten) Blocks
                    mittelwert = np.nanmean(block)
                    nan_indices = np.isnan(D[trial, dim, marker, start_index:end_index])
                    D[trial, dim, marker, start_index:end_index][nan_indices] = mittelwert

    return D

# Daten laden und Funktion anwenden
D = np.load(r"C:\Users\nevio\OneDrive - ZHAW\5. Semester\Projektarbeit\pats.npy")

D = ersetze_nan_mit_mittelwerten(D)
np.save(r"C:\Users\nevio\OneDrive - ZHAW\5. Semester\Projektarbeit\pats.npy", D)
