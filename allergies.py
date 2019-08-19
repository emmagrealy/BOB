Score2Allergy = {
  1:   "eggs",
  2:   "peanuts",
  4:   "shellfish",
  8:   "strawberries",
  16:  "tomatoes",
  32:  "chocolate",
  64:  "pollen",
  128: "cats"
}

Allergy2Score = dict((y,x) for x,y in Score2Allergy.items())

class Allergies:
  def __init__(self, score):
    self.score = score
    self.lst = [ Score2Allergy[x] for x in Score2Allergy.keys() if 0 != x & self.score ]
  def allergic_to(self, allergy):
    return 0 != Allergy2Score.get(allergy,0) & self.score