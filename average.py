def get_grade(s1, s2, s3):
    av = s1+s2+s3
    average = av/3
    if  90<=average<=100:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    elif 0 <= average < 60:
        return "F"

print(get_grade(90,90,80))