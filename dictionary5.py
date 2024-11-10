def students():
    stud_dict = {input('Enter student name: '):int(input('Enter student scores: ')) 
                 for _ in range(int(input('How many students you want to check?: ')))}.items()
    grader_tuple = []
    for name, scores in stud_dict:
        if scores >= 90:
          grade = 'A'  
        elif scores < 90 and scores >= 80:
           grade = 'B'
        elif scores < 80 and scores >= 70:
           grade = 'C'
        else:
           grade = 'F'
        grader_tuple.append((name, grade))
    return(grader_tuple)
print(students())