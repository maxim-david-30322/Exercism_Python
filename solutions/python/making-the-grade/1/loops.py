
def round_scores(student_scores):

    list=[]
    for index ,score in enumerate(student_scores):
        list.append(round(score))

    return list    

    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    pass


def count_failed_students(student_scores):

    return sum(score<=40 for score in student_scores)
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    pass


def above_threshold(student_scores, threshold):
    list1=[]

    for score in student_scores:
        if (score >= threshold):
            list1.append(score)

    return list1
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    pass


def letter_grades(highest):
    i=0
    interval=(highest-40) //4
    
    return [41+i*interval for i in range(4)]
        
    

    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    pass


def student_ranking(student_scores, student_names):

    list1=[]
    for  index,name in enumerate(student_names):

        list1.append( f"{index+1}. {name}: {student_scores[index]}" )

    return list1
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    pass


def perfect_score(student_info):
    i=0
    for  score in student_info:

        if score[1]==100:
            i=1
            return score
        else:
            continue
    if i==0:
        return []
    
    
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    pass
