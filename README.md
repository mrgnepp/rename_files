# rename_files
python script to rename files in a folder based on string matching or regex

```python
python rename_files.py -h
```
usage: rename.py [-h] [-a | -p] [-r] [-v] folder pattern replace

positional arguments:
```
folder - the folder to search through
pattern - the pattern to look for
replace - string to replace the pattern with
```
optional arguments:
```
-h, --help     show this help message and exit
-a, --append   the "replace" string will be appended to the pattern
-p, --prepend  the "replace" string will be prepended to the pattern
-r, --regex    the pattern is a regex
-v, --view     only view the potential changes, does not rename files
```
Example usage:

```bash
# In a folder with: ["text1.txt", "text 2.txt", "TEXT3 3.txt"]
python rename_files.py "C:/folder with files to rename" "text" "new_text"
# Results in: ["new_text1.txt", "new_text 2.txt", "TEXT3 3.txt"]
```

```bash
# In a folder with: ["text1.txt", "text 2.txt", "TEXT3 3.txt"]
python rename_files.py "C:/folder with files to rename" "text" "new_text" --preprend
# Results in: ["new_texttext1.txt", "new_texttext 2.txt", "TEXT3 3.txt"]
```

```bash
# In a folder with: ["text1.txt", "text 2.txt", "TEXT3.txt"]
python rename_files.py "C:/folder with files to rename" "[\d]" "5" --regex
# Results in: ["text5.txt", "text 5.txt", "TEXT5 5.txt"]
```
