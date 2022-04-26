# Solution to Task 4

book_info = (("Best Mystery & Thriller", "The Silent Patient", 68821), ("Best Horror", "The Institute", 75717),
             ("Best History & Biography", "The five", 31783), ("Best Fiction", "The Testaments", 98291))

element1, element2, element3, element4 = book_info
award_category1, book_name1, vote1 = element1
award_category2, book_name2, vote2 = element2
award_category3, book_name3, vote3 = element3
award_category4, book_name4, vote4 = element4

print(f"{book_name1} won the '{award_category1}' category with {vote1} votes")
print(f"{book_name2} won the '{award_category2}' category with {vote2} votes")
print(f"{book_name3} won the '{award_category3}' category with {vote3} votes")
print(f"{book_name4} won the '{award_category4}' category with {vote4} votes")
