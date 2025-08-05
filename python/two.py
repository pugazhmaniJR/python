with open("demofile.txt", "a") as f:
  f.write("name : pugazhmani")
  f.write("born : 20/05/2005")

with open("demofile.txt") as f:
  print(f.read())

  