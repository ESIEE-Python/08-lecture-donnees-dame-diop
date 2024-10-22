import random

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """Retourne le contenu du fichier <filename> sous forme d'une liste de listes d'entiers"""
    with open(filename, mode='r', encoding='utf8') as f:
        lines = f.readlines()
    data = [[int(num) for num in line.strip().split(';')] for line in lines]
    return data

def get_list_k(data, k):
    if 0 <= k < len(data):
        return data[k]
    else:
        return None  

def get_first(l):
    if l:
        return l[0]
    return None  

def get_last(l):
    if l:
        return l[-1]
    return None  

def get_max(l):
    if l:
        return max(l)
    return None  

def get_min(l):
    if l:
        return min(l)
    return None  

def get_sum(l):
    if l:
        return sum(l)
    return None  


#### Fonction principale

def main():
    data = read_data(FILENAME)
    print("Contenu du fichier:", data)
    
    k = 1
    l = get_list_k(data, k)
    print(f"Liste {k}:", l)
    
    if l:
        print("Premier élément:", get_first(l))
        print("Dernier élément:", get_last(l))
        print("Max:", get_max(l))
        print("Min:", get_min(l))
        print("Somme:", get_sum(l))
    else:
        print(f"La liste {k} n'existe pas")


if __name__ == "__main__":
    main()
