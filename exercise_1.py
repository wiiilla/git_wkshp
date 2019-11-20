MEMBER_1 = "Abigail"
MEMBER_2 = "Allen"
MEMBER_3 = "Ramon"

MEMBER_1_FOOD = "cheese"
MEMBER_2_FOOD = "pickles"
MEMBER_3_FOOD = "corn"

MEMBERS = {
    MEMBER_1:MEMBER_1_FOOD,
    MEMBER_2:MEMBER_2_FOOD,
    MEMBER_3:MEMBER_3_FOOD,
}

for k,v in MEMBERS.items():
    print(f"{k} doesn't like {v}")