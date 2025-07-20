# Question no 14: 

# Percentage of Correct Answers Input total questions and correct answers, and calculate the percentage score.

total_ques = int(input("Enter total no of question :"))
correct_ans = int(input("Enter total no of correct answers :"))

percentage =  (correct_ans/total_ques) * 100
print("You score = " , percentage , "%")