from rapidfuzz import fuzz
from itertools import combinations
from dateutil import parser

def normalize_dob(dob):
    try:
        # Convert any input date format into standard YYYY-MM-DD
        parsed_date = parser.parse(dob, dayfirst=True)   # Parse input
        normalized_date = parsed_date.strftime("%Y-%m-%d")  # Standard format
        return normalized_date
    except Exception as e:

        return dob

def checkMatchScore(values, tag):
    if not values:
        return 0


    if tag == "name":
        scores = [fuzz.token_set_ratio(a, b) for a, b in combinations(values, 2)]
        return sum(scores) / len(scores) if scores else 100


    elif tag == "address":
        scores = [fuzz.token_set_ratio(a, b) for a, b in combinations(values, 2)]
        return sum(scores) / len(scores) if scores else 100


    elif tag == "dob":
        normalized = [normalize_dob(v) for v in values]
        scores = [100 if a == b else 0 for a, b in combinations(normalized, 2)]
        return sum(scores) / len(scores) if scores else 100


    elif tag == "age":
        scores = [100 if a == b else 0 for a, b in combinations(values, 2)]
        return sum(scores) / len(scores) if scores else 100

    else:
        raise ValueError("Unsupported tag! Use 'name', 'address', 'dob', or 'age'.")
names = ["raju bala", "bala raju", "raju bal"]
dobs  = ["2000-12-1", "12-1-2000", "12/1/2000"]
ages  = [24, 24, 24, 25, 24]
addresses = ["123 MG Road Pune", "MG Rd Pune 123", "123, M.G. Road, Pune"]
# the cut of should be the 75 for name and address

print(checkMatchScore(names, "name"))        # ~96%
print(checkMatchScore(dobs, "dob"))          # 100%
print(checkMatchScore(ages, "age"))          # 80%
print(checkMatchScore(addresses, "address")) # ~88–95%
