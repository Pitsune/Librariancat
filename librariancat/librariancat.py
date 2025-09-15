#!/usr/bin/env python3
import sys
import subprocess


def main():
    if len(sys.argv) < 2:
        print('No option provided. Use "-h" or "--help" for usage.')
        sys.exit(1)

    if sys.argv[1] == "-s"  or sys.argv[1] == "--sorting":
         if len(sys.argv) == 5:
            od = sys.argv[2]
            do = sys.argv[3]
            ros = sys.argv[4]
            if subprocess.run(["test", "-d", od]).returncode != 0 or subprocess.run(["test", "-d", do]).returncode != 0 :
                print(f"Directory '{do}' or '{od}' does not exist.")
                sys.exit(1)

            sortowanie(od, do, ros)
         else:
              print("Invalid number of arguments for -s. Use -h for help.")
              sys.exit(1)


    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        pomoc()


    elif sys.argv[1] == "-r" or sys.argv[1] == "--remove_size":
        if len(sys.argv) == 5:
            wi = sys.argv[2]
            mb = sys.argv[3]
            zk = sys.argv[4]
            if subprocess.run(["test", "-d", zk]).returncode != 0:
                print(f"Directory '{zk}' does not exist.")
                sys.exit(1)
            usuwanieRozmiar(wi, mb, zk)
        else:
              print("Invalid number of arguments for -r. Use -h for help.")
              sys.exit(1)
             

    elif sys.argv[1] == "-e" or sys.argv[1] == "--empty_dir":
        if len(sys.argv) == 3:
            fol = sys.argv[2]
            if subprocess.run(["test", "-d", fol]).returncode != 0:
                print(f"Directory '{fol}' does not exist.")
                sys.exit(1)
            usuwaniePustychFolderow(fol)
        else:
              print("Invalid number of arguments for -e. Use -h for help.")
              sys.exit(1)
             
    else:
        print(f'Unknown option: {sys.argv[1]}. If you need help, type "-h" or "--help".')
        sys.exit(1)
    sys.exit(0) 


# ==========================
# HELP
# ==========================



def pomoc():
    help_text = """
║Main options║
  -h, --help
      Display this help message.

  -s, --sorting <source_dir> <dest_dir> <extension>
      Copy all files with the given extension from one directory to another.
      Example:
        lcat -s /home/user/dir1 /home/user/dir2 .txt

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
"""
    print(help_text)


# ==========================
# SORTOWANIE PLIKOW
# ==========================


def sortowanie(od, do, ros):
     wynik = subprocess.run( ["find", od, "-maxdepth", "1", "-type", "f", "-name", f"*{ros}"], capture_output=True, text=True )
     pliki = wynik.stdout.strip().split("\n") if wynik.stdout.strip() else []
     for file_path in pliki:
            subprocess.run(["cp", file_path, do])
     print(f"Moved {len(pliki)} files from directory '{od}' to directory '{do}'.")





# ==========================
# USUWANIE PLIKÓW ROZMIAR
# ==========================




def usuwanieRozmiar(wi, mb, zk):
    if wi == "-lsr":
        flaga_rozmiaru = f"+{mb}c"  
    elif wi == "-ssr":
        flaga_rozmiaru = f"-{mb}c"  
    else:
       print("Option must be '-lsr' or '-ssr'")
       sys.exit(1)

   
    wynik = subprocess.run(
        ["find", zk, "-maxdepth", "1", "-type", "f", "-size", flaga_rozmiaru],
        capture_output=True,
        text=True
    )

    pliki_usuniencie = wynik.stdout.strip().split("\n") if wynik.stdout.strip() else []

    for file_path in pliki_usuniencie:
        subprocess.run(["rm", "-f", file_path])

    print(f"Removed {len(pliki_usuniencie)} files from folder '{zk}'.")



# ==========================
# Usuwanie Pustych Folderow
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

    print(f"Removed {len(puste_foldery)} empty directories in '{fol}'.")

if __name__ == "__main__":
    main()



