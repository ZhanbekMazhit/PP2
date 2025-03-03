def polindrom(soilem, teris_soilem):
    return soilem == teris_soilem  
sentence = input("Enter a sentence: ")  
soilem_reverse = sentence[::-1]  
print(polindrom(sentence, soilem_reverse))  
