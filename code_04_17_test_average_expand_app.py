# Add input validation: student and test number can't be exceed 11, exam socre input range should be 0 to 100
# Calculate tthe average exams score of the all students
#！ Make it as streamlit web application(extra point)
#! deploy your application to the github and stream.io (extra point)

import streamlit as st
st.title("score app")

if st.button("SUBMIT"):
    num_student = int(st.number_input("How many students do you have?: "))
    while num_student >= 11 :
        st.write("The number of students must be lower than 11. Please try again.")
        num_students = int(st.number_input("How many students do you have?: "))

    num_test_scores = int(st.number_input("how many quiz are you run per students?: "))
    while num_test_scores >= 11 :
        st.write("The number of quizzes must be lower than 11. Please try again.")
        num_test_scores = int(st.number_input("how many quiz are you run per students?: "))
else:
     st.write("We are waiting your input.")
     
if st.button("Average Score"):
    # Determine each students' average test score
    for student in range(num_student):
        st.write('student number', student + 1)
        st.write('-----------------------------')
        # Initiallize an accumulator for test score
        total = 0.0
        for test_num in range(num_test_scores):
            st.write("Test number", test_num +1, end='')
            score = float(input(": "))
            while score < 0 or score > 100:
                st.write("The score cannot be negative or exceed 100. Please try again.")
                st.write("Test number", test_num +1, end='')
                score = float(input(": "))
            # Calculate the average test scores for this student
            total = total + score #total += score
        average = total / num_test_scores  
        # Display the avergae
        st.write('average of student number', student+1, 'is', average)
        #！ Calculate the average score of the  all studens' exam score
        total_average = total_average + average
    all_average = total_average / num_student
    # Dsplay the average exam score for all students
    st.write('average of all student is', all_average)
else:
     st.write("We are waiting your input.")
