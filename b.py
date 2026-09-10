"""Destructively scrub threejs names from source, based on competition version"""

from a import a
a={v: k for k, v in a.items()}
from pathlib import Path
import re

p = Path(__file__).parent / "z.js"
with p.open() as f:
    r=f.read()
def f(s):
    m = re.search(r'THREE\.(\w+)', s)
    return s[:m.start(0)] + a[m[1]] + f(s[m.end(0):]) if m else s
r=f(r)
r=re.sub(r'new (\w+)\(', r'a(\1,',r)
with p.open('w') as f:
    f.write(r)
