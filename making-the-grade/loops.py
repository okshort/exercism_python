def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    rounded_scores=[]
    for score in student_scores:
        rounded_scores.append(round(score))

    return rounded_scores


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    failed_students_count=0
    for score in student_scores:
        if (score <= 40):
            failed_students_count+=1

    return failed_students_count


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    best_students=[]
    for score in student_scores:
        if (score >= threshold):
            best_students.append(score)

    return best_students


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """

    thresholds_list=[]
    interval=round((highest-40)/4)
    for num in range(41, highest, interval):
        thresholds_list.append(num)

    return thresholds_list


def student_ranking(student_scores, student_names):
    """
    :param student_scores: list of scores in descending order.
    :param student_names: list of names in descending order by exam score.
    :return: list of strings in format ["<rank>. <student name>: <score>"].
    """

    string_list=[]

    for index, score in enumerate(student_scores):
        string_list.append(f"{index+1}. {student_names[index]}: {score}")

    return string_list


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    """
    for index, student in enumerate(student_info):
        if (student_info[index][1] == 100):
            return student_info[index]

    return "No perfect score."
