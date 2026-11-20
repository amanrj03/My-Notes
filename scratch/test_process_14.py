import sys
sys.path.append("scratch")
from build_modules_14_to_18 import process_raw_notes_for_module

html = process_raw_notes_for_module(14)
idx = html.find("Important messages — revision table")
print(html[idx:idx+800])
