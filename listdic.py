def test(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]
    return result

student=[['John', 'A', 'B', 'A'], ['Alice', 'C', 'B', 'B'], ['Bob', 'B', 'B', 'C']]
print("original list:")
print(student)
print("converted dictionary:")
print(test(student))