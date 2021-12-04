from model import model

# Calculate probability for a given observation
probability = model.probability([
  ["none", "no", "on time", "attend"],
  ["none", "no", "on time", "miss"],
  ["none", "yes", "delayed", "attend"]
])

print(probability)
