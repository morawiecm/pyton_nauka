from sys import argv

script, user_name = argv
prompt = '> '

print(f"Czesc {user_name}, jestem skyptem {script}")
print("Chcialbym Ci zadac kilka pytan.")
print(f"Lubisz mnie {user_name}")
likes = input(prompt)

print(f"Gdzie mieszkasz {user_name}? ")
lives = input(prompt)

print("Jaki masz komputer?")
computer = input(prompt)

print(f"""
Ok, gdy zapytalem, czy mnie Lubisz odpowiedziales ze {likes},
mieszkasz w {lives}, Nie jestem pewien gdzie to jest.
I masz komputer {computer}. Fajnie
""")
