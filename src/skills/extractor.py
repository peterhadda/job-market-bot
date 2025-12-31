import re
from typing import Dict, List, Pattern, Set
from  src.skills.skill_patterns import   SKILL_ALIASES


found = set()

def build_patern():
    pattern = {}
    for skill, aliases in SKILL_ALIASES.items():
        escaped = [re.escape(a) for a in aliases]
        joined = "|".join(escaped)
        pattern_str = r"(?i)(?<![a-z0-9])(" + joined + r")(?![a-z0-9])"
        pattern[skill] = re.compile(pattern_str)
    return pattern
PATTERNS = build_patern()

def extract_skills(text: str):
    if not text:
        return []
    found = set()
    for skill, pattern in PATTERNS.items():
        if pattern.search(text):
            found.add(skill)
    return sorted(found)



