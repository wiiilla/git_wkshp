MEMBER_1 = "Willa"
MEMBER_2 = "Elham"
MEMBER_3 = "Ramon"

MEMBER_1_HOME = "Shanghai, China"
MEMBER_2_HOME = "Tehran, Iran"
MEMBER_3_HOME = "Monterrey, Mexico"

MEMBERS = {
    MEMBER_1:MEMBER_1_HOME,
    MEMBER_2:MEMBER_2_HOME,
    MEMBER_3:MEMBER_3_HOME,
}

for k,v in MEMBERS.items():
    print(f"{k} is from {v}")
