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


    if tag == "name" or tag=='pan' or tag=='maddhar'or tag=='phone':
        scores = [fuzz.token_set_ratio(a.lower(), b.lower()) for a, b in combinations(values, 2)]
        return sum(scores) / len(scores) if scores else 100


    elif tag == "address":
        scores = [fuzz.token_set_ratio(a.lower(), b.lower()) for a, b in combinations(values, 2)]
        return sum(scores) / len(scores) if scores else 100


    elif tag == "dob":
        normalized = [normalize_dob(v) for v in values]
        scores = [100 if a == b else 0 for a, b in combinations(normalized, 2)]
        return sum(scores) / len(scores) if scores else 100


    elif tag == "age":
        scores = [100 if a == b else 0 for a, b in combinations(values, 2)]
        return sum(scores) / len(scores) if scores else 100


    elif tag == "gender":
        normalized = []
        for i in values:
            val = i.lower().strip()
            if val in ["m", "male"]:
                normalized.append("male")
            elif val in ["f", "female"]:
                normalized.append("female")
            else:
                normalized.append(val)
        return 100 if len(set(normalized)) == 1 else 0



    else:
        raise ValueError("Unsupported tag! Use 'name', 'address', 'dob', or 'age'.")
names1 = ['IRSAD ALI SAIYAD', 'IRSAD ALI SAIYAD', "Irsad Ali Saiyad"]
names2=['Durga Singh','DURGA SINGH', "DURGA SINGH"]
names2wihtbank=['Durga Singh','DURGA SINGH', "DURGA SINGH","Vijay Singh"]
dobs1  = ["1/10/1995", '1995-01-10', '1995-01-10']
dobs2=['4/22/1986','1986-04-22', "1986-04-22"]
ages  = [30,30]
addresses = ["'line_1': '', 'line_2': '', 'street_name': '', 'zip': '', 'city': '', 'state': '', 'country': '', 'full': ''", "'line_1': 'jelai', 'line_2': 'amar pura khalsa(kheroda) vallabh nagar', 'street_name': 'UDAIPUR', 'zip': '313602', 'city': 'UDAIPUR', 'state': 'Rajasthan', 'country': 'INDIA', 'full': 'jelai amar pura khalsa(kheroda) vallabh nagar UDAIPUR UDAIPUR Rajasthan 313602'"]
gender=['male','M']
madhar=['XXXXXXXX1212','XXXX1212']
numb=[ '7426018956','7426018956']
# the cut of should be the 75 for name and address

print(checkMatchScore(names1, "name")) # 100%
print(checkMatchScore(names2, "name")) # 100%
print(checkMatchScore(names2wihtbank, "name")) # 81.81818181818181
print(checkMatchScore(dobs1, "dob")) # 100%
print(checkMatchScore(dobs2, "dob"))  # 100%
print(checkMatchScore(ages, "age"))   # 100%
print(checkMatchScore(addresses, "address")) # ~88–95%
print(checkMatchScore(gender, "gender"))
print(checkMatchScore(madhar, "maddhar"))
print(checkMatchScore(numb,'phone'))