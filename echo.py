import os
import sys

if __name__ == "__main__":
    input_text = os.getenv("AICORE_PARAMETER_input_text")
    print(f"You entered: {input_text}")
