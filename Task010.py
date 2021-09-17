def common_char(str1, str2):
    empty_str = ""
    for char1 in range(len(str1)):
        for char2 in range(len(str2)):
            if str1[char1] == str2[char2]:
               empty_str += str1[char1]
    print("Common Characters: " + ", ".join(empty_str))

common_char("Rethabile", "Relebohile")
        