import os
os.environ["USE_TE"] = "0"

from evo2 import Evo2

# Load the 7B model
model = Evo2('evo2_7b')

# Run a test generation
output = model.generate(
    prompt="ATGCGATCGATCGATCG",
    max_new_tokens=100,
    temperature=0.7
)
print("Generated DNA Output:\n", output)
