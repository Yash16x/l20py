student={
"id1": {"name": "Yash","age": 16, "roll_no": 101},
"id2": {"name": "Peter", "age": 17, "roll_no":110},
"id3": {"name": "Jordan", "age":16, "roll_no": 105},
"id4": {"name": "Med","age":17, "roll_no":109},
"id5": {"name": "Yash", "age": 16, "roll_no" : 101}
}

result={}
for key,value in student. items():
    if value not in result.values( ) :
        result[key]=value

print(result)
