text = input("Please enter your text:\n")
words = text.split()  # تقسيم النص إلى كلمات
unique_words = set(words)  # إنشاء مجموعة للكلمات الفريدة
len_text = len(text)
len_words = len(words)
print(f"The number of words in the text you entered:", len_words)
print(f"and number of characters:", len_text)
print(f"Unique words in text", [word for word in unique_words])
