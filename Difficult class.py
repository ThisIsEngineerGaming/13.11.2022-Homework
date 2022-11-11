
class Human:
    height = 170
    satiety = 50
class Local_man(Human):
    satiety = 0
class Local_woman(Human):
    satiety = 100
Local_toilet_showerer = Local_woman
Local_shower_crapper = Local_man
print("Local toilet showerers height =", Local_toilet_showerer.height)
print("Local shower crapper height =", Local_shower_crapper.height)
print("Hoomanz not hungry meter = ", Human.satiety, "level")
print("Local woman hungry meter = ",Local_woman.satiety, "level")
print("Local man hungry meter = ",Local_man.satiety, "level")

