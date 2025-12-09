
# Problem 5: Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.

import sys
import os
import urllib.request

if len(sys.argv) !=2:
    print("python wget.py <URL>")
    sys.exit(1)
url=sys.argv[1]
basename=os.path.basename(url)
if basename=="":
    basename="index.html"
try:
    print(f"Downloading {url}")
    urllib.request.urlretrieve(url,basename)
    print(f"Save as {basename}")
except Exception as e:
    print("Error downloading URL:",{e})