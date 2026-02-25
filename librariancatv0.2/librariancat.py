#!/usr/bin/env python3
import sys
import subprocess


# ====================================================STAlE====================================================


# ==========================
# COLOR
# ==========================


red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"


# ==========================
# TEXT MODIFICATION
# ==========================


bold = "\033[1m"
darken = "\033[2m"
italic = "\033[3m"
underline = "\033[4m"
colorInvert = "\033[7m"
fade = "\033[8m" 
deletion = "\033[9m"


reset = "\033[0m"


# ====================================================FUNKCJA MAIN==================================================== 


def main():
    if len(sys.argv) < 2:
        print(f'{red}No option provided. Use "-h" or "--help" for usage.{reset}')
        sys.exit(1)


# ==========================
# KOPIOWANIE PO ROSZERZENIU
# ==========================


    if sys.argv[1] == "-c"  or sys.argv[1] == "--copying":
         if len(sys.argv) == 5:
            od = sys.argv[2]
            do = sys.argv[3]
            ros = sys.argv[4]
            if subprocess.run(["test", "-d", od]).returncode != 0 or subprocess.run(["test", "-d", do]).returncode != 0 :
                print(f"{red}Directory {italic}'{od}'{reset}{red} or {italic}'{do}'{reset}{red} does not exist.{reset}")
                sys.exit(1)

            kopiowanie(od, do, ros)
         else:
              print(f"{red}Invalid number of arguments for -c. Use -h for help.{reset}")
              sys.exit(1)


# ==========================
# HELP
# ==========================


    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        pomoc()


# ==========================
# USUWANIE PLIKÓW ROZMIAR
# ==========================


    elif sys.argv[1] == "-r" or sys.argv[1] == "--remove_size":
        if len(sys.argv) == 5:
            wi = sys.argv[2]
            mb = sys.argv[3]
            zk = sys.argv[4]
            if subprocess.run(["test", "-d", zk]).returncode != 0:
                print(f"{red}Directory{italic} '{zk}'{reset}{red} does not exist.{reset}")
                sys.exit(1)
            usuwanieRozmiar(wi, mb, zk)
        else:
              print(f"{red}Invalid number of arguments for -r. Use -h for help.{reset}")
              sys.exit(1)
             

# ==========================
# USUWANIE PUSTYCH FOLDERÓW
# ==========================


    elif sys.argv[1] == "-e" or sys.argv[1] == "--empty_dir":
        if len(sys.argv) == 3:
            fol = sys.argv[2]
            if subprocess.run(["test", "-d", fol]).returncode != 0:
                print(f"{red}Directory{italic} '{fol}'{reset}{red} does not exist.{reset}")
                sys.exit(1)
            usuwaniePustychFolderow(fol)
        else:
              print(f"{red}Invalid number of arguments for -e. Use -h for help.{reset}")
              sys.exit(1)


# ==========================
# WERSJA
# ==========================


    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        version()         


# ==========================
# PRZENOSZENIE PO ROSZEZENIU
# ==========================


    elif sys.argv[1] == "-m"  or sys.argv[1] == "--move":
         if len(sys.argv) == 5:
            od = sys.argv[2]
            do = sys.argv[3]
            ros = sys.argv[4]
            if subprocess.run(["test", "-d", od]).returncode != 0 or subprocess.run(["test", "-d", do]).returncode != 0 :
                print(f"{red}Directory{italic} '{od}'{reset}{red} or{italic} '{do}'{reset}{red} does not exist.{reset}")
                sys.exit(1)

            przenoszenie(od, do, ros)
         else:
              print(f"{red}Invalid number of arguments for -m. Use -h for help.{reset}")
              sys.exit(1)


# ==========================
# USUWANIE DUPLIKATOW
# ==========================

    elif sys.argv[1] == "-d" or sys.argv[1] == "--deduplicate":
         if len(sys.argv) == 3:
            dir_path = sys.argv[2]
            if subprocess.run(["test", "-d", dir_path]).returncode != 0:
                print(f"{red}Directory {italic}'{dir_path}'{reset}{red} does not exist.{reset}")
                sys.exit(1)
            usuwanieDuplikatow(dir_path)
         else:
              print(f"{red}Invalid number of arguments for -d. Use -h for help.{reset}")
              sys.exit(1)




# ==========================
# NIEZNALEZIONO OPCJI
# ==========================


    else:
        print(f'{red}Unknown option: {sys.argv[1]}. If you need help, type "-h" or "--help".{reset}')
        sys.exit(1)
    sys.exit(0) 


# ====================================================Funkcje====================================================


# ==========================
# HELP
# ==========================


def pomoc():
    help_text = """
║Main options║
  -h, --help
      Display this help message.

  -v, --version
      Displays program versions.

  -c, --copying <source_dir> <dest_dir> <extension>
      Copy all files with the given extension from one directory to another.
      Example:
        lcat -c /home/user/dir1 /home/user/dir2 .txt

  -m, --move <source_dir> <dest_dir> <extension>
      Moves all files with the given extension from one directory to another.
      Example:
        lcat -m /home/user/dir1 /home/user/dir2 .txt

  -r, --remove_size <mode> <size> <dir>
      Remove files from the given directory that are smaller (-ssr) or larger (-lsr)
      than the specified size (in bytes).
      Examples:
        lcat -r -ssr 1024 /home/user/dir   # remove files < 1024 bytes
        lcat -r -lsr 2048 /home/user/dir   # remove files > 2048 bytes

  -e, --empty_dir <dir>
      Remove all empty directories inside the given directory.
      Example:
        lcat -e /home/user/dir
  -d, --deduplicate <dir>
      Remove all duplicates inside the given directory.
      Example:
        lcat -d /home/user/dir
"""
    print(help_text)


# ==========================
# WERSJA
# ==========================


def version(): 
    print("Librariancat version: 0.2 \n ≽^•⩊•^≼ ")
                   

# ==========================
# KOPIOWANIE PO ROSZERZENIU
# ==========================


def kopiowanie(od, do, ros):
     wynik = subprocess.run( ["find", od, "-maxdepth", "1", "-type", "f", "-name", f"*{ros}"], capture_output=True, text=True )
     pliki = wynik.stdout.strip().split("\n") if wynik.stdout.strip() else []
     for file_path in pliki:
            subprocess.run(["cp", file_path, do])
            
     print(f"{green}Copy {len(pliki)} files from directory '{od}' to directory '{do}'.{reset}")


# ==========================
# USUWANIE PLIKÓW ROZMIAR
# ==========================


def usuwanieRozmiar(wi, mb, zk):
    if wi == "-lsr":
        flaga_rozmiaru = f"+{mb}c"  
    elif wi == "-ssr":
        flaga_rozmiaru = f"-{mb}c"  
    else:
       print(f"{red}Option must be '-lsr' or '-ssr'.{reset}")
       sys.exit(1)

   
    wynik = subprocess.run(
        ["find", zk, "-maxdepth", "1", "-type", "f", "-size", flaga_rozmiaru],
        capture_output=True,
        text=True
    )

    pliki_usuniencie = wynik.stdout.strip().split("\n") if wynik.stdout.strip() else []

    for file_path in pliki_usuniencie:
        subprocess.run(["rm", "-f", file_path])

    print(f"{green}Removed {len(pliki_usuniencie)} files from folder '{zk}'.{reset}")


# ==========================
# USUWANIE PUSTYCH FOLDERÓW
# ==========================


def usuwaniePustychFolderow(fol):
    
    result = subprocess.run(
        ["find", fol, "-maxdepth", "1", "-type", "d", "-empty"],
        capture_output=True,
        text=True
    )

    puste_foldery = result.stdout.strip().split("\n") if result.stdout.strip() else []

  
    puste_foldery = [d for d in puste_foldery if d != fol]

    for dir_path in puste_foldery:
        subprocess.run(["rmdir", dir_path])  

    print(f"{green}Removed {len(puste_foldery)} empty directories in '{fol}'.{reset}")


# ==========================
# PRZENOSZENIE PO ROSZEZENIU
# ==========================


def przenoszenie(od, do, ros):
     wynik = subprocess.run( ["find", od, "-maxdepth", "1", "-type", "f", "-name", f"*{ros}"], capture_output=True, text=True )
     pliki = wynik.stdout.strip().split("\n") if wynik.stdout.strip() else []
     for file_path in pliki:
            subprocess.run(["mv", file_path, do])
            
     print(f"{green}Moved {len(pliki)} files from directory '{od}' to directory '{do}'.{reset}")


# ==========================
# USUWANIE DUPLIKATOW
# ==========================


def usuwanieDuplikatow(dir_path):
    
    wynik = subprocess.run(
        ["find", dir_path, "-type", "f", "-exec", "sha256sum", "{}", "+"], capture_output=True, text=True)

    lines = wynik.stdout.strip().split("\n")
    hashes = {}
    duplicates = []

    for line in lines:
        if not line.strip():
            continue
        file_hash, file_path = line.split(maxsplit=1)
        
        if file_hash in hashes:
            duplicates.append(file_path)
            subprocess.run(["rm", "-f", file_path])  
        else:
            hashes[file_hash] = file_path

    print(f"{green}Removed {len(duplicates)} duplicate files in '{dir_path}'.{reset}")
    if duplicates:
        for d in duplicates:
            print(f"{green}Duplicate removed: {d}{reset}")




if __name__ == "__main__":
    main()



