"""This method creates a list of teachers given the unabridged (no manual 
changes) excel file"""
def initTeachers():
    book = xlrd.open_workbook("/Users/Will/Downloads/list_of_faculty.xlsx")
    first_sheet = book.sheet_by_index(0)
    teachers = []
    for i in range(4, 31):
        teachers.append(Teacher(first_sheet.row_slice(rowx=i, start_colx = 0, end_colx = 7)))
    return teachers
