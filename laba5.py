"""
#1
import re
def match_a_b_zero_or_more(text):
    return bool(re.fullmatch(r'ab*', text))

print(match_a_b_zero_or_more("a"))       
print(match_a_b_zero_or_more("abbb"))     
print(match_a_b_zero_or_more("ac"))      

"""
"""
import re
# 2
def match_a_two_to_three_b(text):
    return bool(re.fullmatch(r'ab{2,3}', text))

print(match_a_two_to_three_b("abb"))     
print(match_a_two_to_three_b("abbbb"))   

"""
"""
import re
# 3
def find_lowercase_underscore(text):
    return re.findall(r'[a-z]+_[a-z]+', text)

print(find_lowercase_underscore("one_two three_four fiveSix"))  # ['one_two', 'three_four']

""" 
"""
import re
# 4
def find_upper_by_lower(text):
    return re.findall(r'[A-Z][a-z]+', text)

print(find_upper_by_lower("KbtuSite ALgaTolebi"))  # ['Kbtu', 'Site', 'ALga', 'Tolebi']

"""
"""
import re
# 5
def match(text):
    return bool(re.fullmatch(r'a.*b', text))

print(match("acb"))   
print(match("a123b"))
print(match("ab"))    
print(match("a-b"))   
"""
"""
import re
# 6
def replace_with(text):
    return re.sub(r'[ ,\.]+', ':', text)

print(replace_with("Hscdj, ef. eteht mpqfrjc"))  

"""
"""
import re 
# 7
def snake(text):
    return ''.join(word.capitalize() for word in text.split('_'))

print(snake("python_labka")) 
"""
"""
import re
# 8
def splituppercase(text):
    return re.findall(r'[A-Z][^A-Z]*', text)

print(splituppercase("PythonLabkaIsHard"))  # ['Python', 'Labka', 'Is', 'Hard']

"""
"""
import re
# 9
def insert_spaces(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

print(insert_spaces("KasKEleNsiLA)) 
 
"""
"""
import re
# 10
def camel(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

print(camel("KasKeLensILa))  
"""