# chacking for vowel
vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
text = 'hello world'
for i in vowel:
    if i in text:
        print(i)
# chacking for vowel 02

vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
character = input()
if character in vowel:
    print(f"The character '{character}' is a vowel!")
else:
    print(f"The character '{character}' is not a vowel!")
