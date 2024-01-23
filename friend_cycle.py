'''
Pt 1.Given employees and friendships, find all adjacencies that denote the friendship, 
A friendship is bi-directional/mutual so if 1 is friends with 2, 2 is also friends with 1.

Sample Output:
Output:
1: 2, 3
2: 1
3: 1, 4
4: 3
6: None
'''


employees = [
  "1, Bill, Engineer",
  "2, Joe, HR",
  "3, Sally, Engineer",
  "4, Richard, Business",
  "6, Tom, Engineer"
]

friendships = [
  "1, 2",
  "1, 3",
  "3, 4"
]

def friend_cycle(employees, friendships):
    emp_dict = {}
    for emp in employees:
        emp_id, emp_name, emp_dept = emp.split(', ')
        if emp_id not in emp_dict:
            emp_dict[emp_id] = {'name': emp_name , 'dept': emp_dept}
    
    friendship_dict = {}
    for friendship in friendships:
        friend_1, friend_2 = friendship.split(', ')
        if friend_1 not in friendship_dict:
            friendship_dict[friend_1] = [friend_2]
        else:
            friendship_dict[friend_1].append(friend_2)
        
        if friend_2 not in friendship_dict:
            friendship_dict[friend_2] = [friend_1]
        else:
            friendship_dict[friend_2].append(friend_1)

    # add people who are dont have any friendships but are employees
    for emp in emp_dict.keys():
        if emp not in friendship_dict:
            friendship_dict[emp] = []
    
    # print(friendship_dict)
    for k, v in friendship_dict.items():
        print(k + ': ' + ', '.join(v))
    

friend_cycle(employees, friendships)
