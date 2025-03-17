import datetime

def is_common_mpin(mpin):
    """Checks if a 4 or 6-digit MPIN is commonly used."""
    common_mpins_4 = [
        "1234", "0000", "1111", "2580", "1212", "7777", "1004", "2000", "4444", "2222",
        "6969", "9999", "3333", "5555", "6666", "0852", "1998", "2001", "2002", "2003",
        "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "0123",
        "9876", "1122", "1230", "1990", "1991", "1992", "1993", "1994", "1995", "1996"
       
    ]
    common_mpins_6 = [
        "123456", "000000", "111111", "654321", "121212", "777777", "100400", "200000",
        "444444", "222222", "696969", "999999", "333333", "555555", "666666", "085208",
        "199819", "200120", "200220", "200320", "200420", "200520", "200620", "200720",
        "200820", "200920", "201020", "201120", "201220", "012345", "987654"
    ]

    if len(mpin) == 4:
        return mpin in common_mpins_4
    elif len(mpin) == 6:
        return mpin in common_mpins_6
    else:
        return False

def check_mpin_strength(mpin, year_self=None, year_spouse=None, year_anniversary=None):
    """Checks MPIN strength and provides reasons for weakness."""
    reasons = []
    strength = "STRONG"

    if is_common_mpin(mpin):
        strength = "WEAK"
        reasons.append("COMMONLY_USED")

    if year_self:
        year_self_str = str(year_self)[2:] #last two digits
        year_self_full_str = str(year_self)

        if year_self_str in mpin or year_self_full_str in mpin:
            strength = "WEAK"
            reasons.append("DEMOGRAPHIC_DOB_SELF")

    if year_spouse:
        year_spouse_str = str(year_spouse)[2:]
        year_spouse_full_str = str(year_spouse)

        if year_spouse_str in mpin or year_spouse_full_str in mpin:
            strength = "WEAK"
            reasons.append("DEMOGRAPHIC_DOB_SPOUSE")

    if year_anniversary:
        year_anniversary_str = str(year_anniversary)[2:]
        year_anniversary_full_str = str(year_anniversary)

        if year_anniversary_str in mpin or year_anniversary_full_str in mpin:
            strength = "WEAK"
            reasons.append("DEMOGRAPHIC_ANNIVERSARY")

    return {"strength": strength, "reasons": reasons}

def run_tests():
    test_cases = [
        {"mpin": "1234", "year_self": None, "year_spouse": None, "year_anniversary": None, "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED"]},
        {"mpin": "5678", "year_self": None, "year_spouse": None, "year_anniversary": None, "expected_strength": "STRONG", "expected_reasons": []},
        {"mpin": "1998", "year_self": 1998, "year_spouse": None, "year_anniversary": None, "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED", "DEMOGRAPHIC_DOB_SELF"]},
        {"mpin": "2000", "year_self": None, "year_spouse": 2000, "year_anniversary": None, "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED", "DEMOGRAPHIC_DOB_SPOUSE"]},
        {"mpin": "1990", "year_self": None, "year_spouse": None, "year_anniversary": 1990, "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED", "DEMOGRAPHIC_ANNIVERSARY"]},
        {"mpin": "4321", "year_self": 1985, "year_spouse": 1990, "year_anniversary": 2010, "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED"]},
        {"mpin": "9876", "year_self": 1985, "year_spouse": 1990, "year_anniversary": 2010, "expected_strength": "STRONG", "expected_reasons": []},
        {"mpin": "1122", "year_self": 1122, "year_spouse": None, "year_anniversary": None, "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED","DEMOGRAPHIC_DOB_SELF"]},
        {"mpin": "1230", "year_self": None, "year_spouse": 1230, "year_anniversary": None, "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED","DEMOGRAPHIC_DOB_SPOUSE"]},
        {"mpin": "1999", "year_self": None, "year_spouse": None, "year_anniversary": 1999, "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED","DEMOGRAPHIC_ANNIVERSARY"]},
        {"mpin": "1985", "year_self": 1985, "year_spouse": 1990, "year_anniversary": 2010, "expected_strength": "WEAK", "expected_reasons": ["DEMOGRAPHIC_DOB_SELF"]},
        {"mpin": "1990", "year_self": 1985, "year_spouse": 1990, "year_anniversary": 2010, "expected_strength": "WEAK", "expected_reasons": ["DEMOGRAPHIC_DOB_SPOUSE"]},
        {"mpin": "2010", "year_self": 1985, "year_spouse": 1990, "year_anniversary": 2010, "expected_strength": "WEAK", "expected_reasons": ["DEMOGRAPHIC_ANNIVERSARY"]},
        {"mpin": "123456", "year_self": None, "year_spouse": None, "year_anniversary": None, "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED"]},
        {"mpin": "654321", "year_self": 2001, "year_spouse": None, "year_anniversary": None, "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED"]},
        {"mpin": "200120", "year_self": 2001, "year_spouse": None, "year_anniversary": None, "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED", "DEMOGRAPHIC_DOB_SELF"]},
        {"mpin": "999999", "year_self": None, "year_spouse": 1999, "year_anniversary": None, "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED"]},
        {"mpin": "199819", "year_self": 1998, "year_spouse": 1999, "year_anniversary": 2000, "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED","DEMOGRAPHIC_DOB_SELF"]},
        {"mpin": "200020", "year_self": 1998, "year_spouse": 2000, "year_anniversary": 2001, "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED","DEMOGRAPHIC_DOB_SPOUSE"]},
        {"mpin": "200121", "year_self": 1998, "year_spouse": 2000, "year_anniversary": 2001, "expected_strength": "WEAK", "expected_reasons": ["DEMOGRAPHIC_ANNIVERSARY"]}
    ]

    for i, test_case in enumerate(test_cases):
        result = check_mpin_strength(test_case["mpin"], test_case["year_self"], test_case["year_spouse"], test_case["year_anniversary"])
        if result["strength"] == test_case["expected_strength"] and result["reasons"] == test_case["expected_reasons"]:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed. Expected: {test_case['expected_strength']}, {test_case['expected_reasons']}. Got: {result['strength']}, {result['reasons']}")

run_tests()