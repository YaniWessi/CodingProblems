#its photo day at the local school, and you're the photographer assigned to
# take calss photos. The class that you'll be photographing has an even number
# of students, and all these students are wearing red or blue shirts. In fact, 
# exactly half of the class is wearing red shirts, and the other half is wearing
#blue shirts. You're responsible for arranging the students in two rows before 
# taking the photo. Eahc row should contain the same number of the students and
# should contain the same number of students and should adhere to the following 
# guidlines: 
# all students wearing red shirts must be in the same row. 
# all studnets wearing blue shirts must be the same row. 
# Each student in the back row must be strictly taller than the student 
# directly in front of them in the front row. 

#You're given two input arrays: one containing the height of all the students and
# with red shirts and another one containing the heights of all the students 
# withblue shirts. These arrays will always have the same length, and each 
# height will be a positive integer. Write a function that returns whether
# or not a class photo that follows the stated guidelines canbe taken.

# Note: you can assume that each class has at least 2 students. 

def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    bigger = max(redShirtHeights, blueShirtHeights)
    small = min(redShirtHeights, blueShirtHeights)


    bigger.sort()
    small.sort()

    start = 0 

    while start <= len(bigger) -1:
        if bigger[start] <= small[start]:
            return False
        else:
            start += 1
    return True  



redS = [5, 8, 1, 3, 4]

blueS = [6, 9, 2, 4, 5]


    