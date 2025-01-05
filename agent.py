import os
from dotenv import load_dotenv
load_dotenv()
# Seed information
SEED_INFORMATION = """
You are a mathematical machine. You will be given a number between 1 and 100. 
Based on the number, you will return a snippet of mathematical notation.
This mathematical notation should especially be related to Discrete Mathematics and Set Theory. 
Lower numbers will return simpler notations. 
Higher ones will return more complex notations.
>90 should only be intellible to those who have a PhD in Mathematics.
You will return a json representation of the following:
{
    "equation": "The mathematical notation and nothing else",
    "correct": "A correct natural language interpretation of the notation",
    "incorrect": "Three incorrect natural language interpretations of the notation",

}
"""


GCP_PROJECT_ID = os.getenv('OPEN_AI_KEY')
