name="anandhi"
count=0
for c in name.lower():
    if c in 'aeiou':
        print (c)
        count=count+1
print("Vowel count:", count)