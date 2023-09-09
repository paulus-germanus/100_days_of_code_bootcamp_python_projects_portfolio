#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"Input\Names\invited_names.txt") as names:
    invited_names = [x.strip("\n") for x in names.readlines()]

for x in invited_names:
    with open(r"Input\Letters\starting_letter.txt") as letter:
        addressed_letter = [y.replace("[name]", x) for y in letter.readlines()]
        with open(f"Output\ReadyToSend\Letter_to_{x}.txt", "w") as final_letter:
            final_letter.write("".join(addressed_letter))
