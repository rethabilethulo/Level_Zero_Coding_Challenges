def vowels(string):
    vowels = "AaEeIiOoUu"
    new_string = set(string)
    new_vowels = set (vowels)
    word_list = (new_string & new_vowels)         
    vowel_string = " , ".join(word_list).lower()
    return "Vowels: " + vowel_string

print(vowels("ReAthabile"))   
