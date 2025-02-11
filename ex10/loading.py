import sys
import time

def ft_progress(listy):
    total = len(listy)
    start = time.time()

    for i, elem in enumerate(listy):
        # Elapsed time
        end = time.time()
        elapsed = end - start

        # Progression %
        percentage = (i / total) * 100  # Calcul correct du pourcentage

        # Progession Bar
        bar_length = 50  # Longueur de la barre
        filled_length = int(bar_length * i // total)
        bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length)  # Barre dynamique

        # Calculate ETA
        eta = (elapsed / (i + 1)) * (total - (i + 1))

        # Print the line
        sys.stdout.write(f"\r ETA: {eta:.2f}s [{percentage:.2f}%] [{bar}] {i}/{total} | elapsed time : {elapsed:.2f}s")
        sys.stdout.flush()  # Force l'affichage immédiatement

        yield elem

# ft_progress | ETA: 8.67s [ 23%][=====> ] 233/1000 | elapsed time 2.33s
# Nothing     | ...
# RET         | 2000 

# Main
if __name__ == "__main__" :
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print("...")
    print(ret)