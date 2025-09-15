# Librariancat😺📁 – lightweight console tool for file management

### Librariancat is a lightweight command-line tool for Linux systems written in Python, designed for managing files and directories.  
**Author:** \
 ![Pitsune](https://img.shields.io/badge/Pitsune🦊-purple?)

**Info📃:**\
 ![Version](https://img.shields.io/badge/version-0.1--BETA-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8%2B-yellow)
![Pip](https://img.shields.io/badge/pip-25.2%2B-red)

## Features 🔧
- **File sorting** (`-s, --sorting`) – copies all files with a given extension from one directory to another.  
- **Remove files by size** (`-r, --remove_size`) – removes files smaller (`-ssr`) or larger (`-lsr`) than the given size in bytes.  
- **Remove empty directories** (`-e, --empty_dirs`) – deletes empty directories from the given directory.  
- **Help** (`-h, --help`) – displays help.  

---

## Installation ⚙️
```bash
# Download Librariancat
cd librariancat
pipx install .
```

---

## Update ⬇️
```bash
# Get the latest version of Librariancat
cd librariancat
pipx install --force .
```

---

## Usage examples ✍️
```bash
# Show help
lcat -h

# Copy all .txt files from dir1 to dir2
lcat -s /home/user/dir1 /home/user/dir2 .txt

# Remove files smaller than 1024 bytes from /tmp
lcat -r -ssr 1024 /tmp

# Remove files larger than 5 MB from Downloads
lcat -r -lsr 5242880 ~/Downloads

# Remove empty directories from /var/log
lcat -e /var/log

# (Optional) Schedule daily empty directory cleanup at midnight
lcat --schedule -e /home/user/dir
```

---

## What's new  📅

---

## Roadmap 🛠️

|       **Version 0.2**          |
:---------------------------------:|
| Cron integration                |
| Automatic filtering             |
| Additional file filtering options |

|       **Version 0.3**          |
:---------------------------------:|
| Log file support                |
| Automatic folder cleanup        |
| Additional file deletion options |

---

## Requirements ‼️
- Linux  
- Python 3.8+  
- Pip 25.2+  

---

## Project structure 📁
```
librariancat/
├── librariancat.py             # source code
├── setup.py                    # installation configuration
└── README.md                   # documentation
```

---

## License📜
This project is licensed under the MIT License – you are free to use, modify, and distribute it.  
