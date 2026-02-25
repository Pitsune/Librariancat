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
- **File copying by extension** (`-c, --copying`) – copies all files with a given extension from the source directory to the destination directory.
- **File moving by extension** (`-m, --move`) – moves all files with a given extension from the source directory to the destination directory.
- **Duplicate file removal** (`-d, --deduplicate`) – removes duplicate files based on SHA-256 checksums.
- **Remove files by size** (`-r, --remove_size`) – removes files smaller (`-ssr`) or larger (`-lsr`) than the given size in bytes.
- **Remove empty directories** (`-e, --empty_dirs`) – deletes empty directories inside the given directory.
- **Version information** (`-v, --version`) – displays the program version.
- **Help** (`-h, --help`) – displays usage information and available options.
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
**New Features**

- Added file copying by extension (-c, --copying)

- Added file moving by extension (-m, --move)

- Added duplicate file removal based on SHA-256 checksums (-d, --deduplicate)

- Added program version display (-v, --version)

**Interface Changes**

- Colored terminal output

- Improved error and feedback messages

**Technical Improvements**

- Refactored sorting logic into separate modes: copying and moving

- Improved code organization (functional sections)

- Prepared the project for further versioning
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

