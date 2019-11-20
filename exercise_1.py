MEMBER_1 = "Vanessa"
MEMBER_2 = "Steve"
MEMBER_3 = "Dwight"

MEMBER_1_FOOD = "pumpkin"
MEMBER_2_FOOD = "stuffing"
MEMBER_3_FOOD = "carrots"

MEMBERS = [f"MEMBER_{i}" for i in range(1,4)]

for i in MEMBERS:
    print(f"{i} doesn't like {MEMBER_1_FOOD}")