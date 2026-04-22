n, x = map(int, input().split())
subject_scores = []
for _ in range(x):
    subject_scores.append(list(map(float, input().split())))
for student_marks in zip(*subject_scores):
    print(sum(student_marks) / x)
