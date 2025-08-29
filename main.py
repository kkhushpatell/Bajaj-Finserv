# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

# Input model
class DataInput(BaseModel):
    data: List[str]

def alternate_caps(s: str) -> str:
    res = ""
    upper = True
    for ch in s:
        res += ch.upper() if upper else ch.lower()
        upper = not upper
    return res

@app.post("/bfhl")
async def process_data(input_data: DataInput):
    try:
        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0

        for item in input_data.data:
            if item.isdigit():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                total_sum += num
            elif item.isalpha():
                alphabets.append(item.upper())
            else:
                special_characters.append(item)

        # Concatenation in reverse order with alternating caps
        concat_str = alternate_caps("".join(alphabets)[::-1])

        response = {
            "is_success": True,
            "user_id": "khush_patel_12092003",  # Replace with your details
            "email": "khush.patel2022@vitstudent.ac.in",  # Replace with your email
            "roll_number": "22BCE3178",  # Replace with your roll no
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_str
        }
        return response

    except Exception as e:
        return {"is_success": False, "message": str(e)}

@app.get("/")
async def root():
    return {"message": "Full Stack API is running!"}