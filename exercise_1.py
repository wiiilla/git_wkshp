MEMBER_1 = "Tiffany"
MEMBER_2 = "Allen"
MEMBER_3 = "Ramon"

MEMBER_1_HOME = "Richmond, VA"
MEMBER_2_HOME = "Haiphong, Viet Nam"
MEMBER_3_HOME = "Monterrey, Mexico"

MEMBERS = {
    MEMBER_1:MEMBER_1_HOME,
    MEMBER_2:MEMBER_2_HOME,
    MEMBER_3:MEMBER_3_HOME,
}

for k,v in MEMBERS.items():
    print(f"{k} is from {v}")