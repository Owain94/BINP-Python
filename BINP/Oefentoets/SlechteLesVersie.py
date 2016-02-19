speler_dict = {"Owain": 0, "Mies": 0}
speler_lijst = list(speler_dict.keys())

print(speler_lijst)

while speler_dict["Owain"] != 20:
    speler_dict["Owain"] += 1
    print(speler_dict["Owain"])