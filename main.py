from reportlab.pdfgen.canvas import Canvas
canvas = Canvas("resume.pdf", pagesize=(612.0, 792.0))

class Profile:
  def __init__(self, first_name, last_name, occupation):
    self.first_name = first_name
    self.last_name = last_name
    self.occupation = occupation

  def education(secondary, year, primary=None, degree):
    self.secondary = secondary
    self.year = year
    if degree == "2":
      self.degree = "Associates"
    elif degree == "4":
      self.degree == "Bachelors"
    elif degree == "6":
      self.degree == "Masters"
    self.primary = primary
    self.primary_year = year - 4

  def skills
