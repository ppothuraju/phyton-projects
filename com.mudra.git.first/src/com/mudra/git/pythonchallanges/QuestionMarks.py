'''
Take an input string parameter and determine if exactly 3 question marks exist between every pair of numbers 
that add up to 10. If so, return true, otherwise return false. Some examples test cases are below:
"arrb6???4xxbl5???eee5" => true
"acc?7??sss?3rr1??????5" => true
"5??aaaaaaaaaaaaaaaaaaa?5?5" => false
"9???1???9???1???9" => true
"aa6?9" => false
'''
def QuestionsMarks(s):
    qcount = 0
    addup = 0
    is10 = False
    for ch in s:
        if ch.isdigit():
            if int(ch) + addup == 10:
                if qcount != 3:
                    return 'false'
                is10 = True
            addup = int(ch)
            qcount = 0
        elif ch == '?':
            qcount += 1
    return 'true' if is10 else 'false'

print (QuestionsMarks('arrb6???4xxbl5???eee5'))
print (QuestionsMarks('acc?7??sss?3rr1??????5'))
print (QuestionsMarks('5??aaaaaaaaaaaaaaaaaaa?5?5')) 
print (QuestionsMarks('9???1???9???1???9'))
print (QuestionsMarks('aa6?9'))