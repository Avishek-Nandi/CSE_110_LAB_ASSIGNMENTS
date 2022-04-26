# Solution to Task 3

book_info = (("Best Mystery & Thriller", "The Silent Patient", 68, 821), ("Best Horror", "The Institute", 75, 717),
             ("Best History & Biography", "The five", 31, 783), ("Best Fiction", "The Testaments", 98, 291))

print(f"Size of the tuple is {len(book_info)}")

# without for loop
print(*book_info, sep="\n")

# with for loop [Please uncomment to check]
for element in book_info:
    print(element, end="\n")
