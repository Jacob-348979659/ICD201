QUESTIONS: dict[tuple[int, str], list[tuple[int, str]]] = {
(1, "Question 1"): [(1, "Option A"), (2, "Option B"), (3, "Option C"), (4, "Option D")],
(2, "Question 2"): [(1, "Option A"), (2, "Option B"), (3, "Option C"), (4, "Option D")],
(3, "Question 3"): [(1, "Option A"), (2, "Option B"), (3, "Option C"), (4, "Option D")],
(4, "Question 4"): [(1, "Option A"), (2, "Option B"), (3, "Option C"), (4, "Option D")],
(5, "Question 5"): [(1, "Option A"), (2, "Option B"), (3, "Option C"), (4, "Option D")]
}

def border(c: str = "=", w: int = 50) -> str: # Create a border line of a given character and width
    return c * w

for question, options in QUESTIONS.items():
    print(f"{border()}\n{question[1]}")
    for num, s in options:
        print(f"{num}: {s}")
    answer = input("\nInput the correct answer: ")

    if (answer is question[0]):
        print(f"Correct")
    else:
        print(f"Incorrect, the correct answer was {question[0]}")
    print(f"\n{border()}\n")
