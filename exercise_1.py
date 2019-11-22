MEMBER_1 = "Willa"
MEMBER_2 = "Elhamiiiii"
MEMBER_3 = "Morteza"

MEMBER_1_HOME = "Shanghai, China"
MEMBER_2_HOME = "Tehran, Iran"
MEMBER_3_HOME = "Vancouver, BC"

MEMBERS = {
    MEMBER_1:MEMBER_1_HOME,
    MEMBER_2:MEMBER_2_HOME,
    MEMBER_3:MEMBER_3_HOME,
}

for k,v in MEMBERS.items():
    print(f"{k} is from {v}")
