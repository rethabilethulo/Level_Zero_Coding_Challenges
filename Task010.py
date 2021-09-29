def common_char(str1, str2):
    empty_str = ""
    for character in str1.lower():
        for character in str2.lower():
            if character in empty_str:
                    continue
            empty_str += character
    print("Common Characters: " + ", ".join(empty_str))

common_char("Dear", "Ear")
        