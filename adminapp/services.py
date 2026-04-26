from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_faculties():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_faculty""")
        faculties = dictfetchall(cursor)
        return faculties


def get_groups():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT adminapp_group.id, adminapp_group.name, adminapp_faculty.name as faculty
         from adminapp_group left join adminapp_faculty on adminapp_group.faculty_id = adminapp_faculty.id
         """)
        groups = dictfetchall(cursor)
        return groups


def get_kafedra():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_kafedra""")
        kafedra = dictfetchall(cursor)
        return kafedra


def get_subject():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from adminapp_subject""")
        subjects = dictfetchall(cursor)
        return subjects


def get_teacher():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT adminapp_teacher.id, adminapp_teacher.first_name, adminapp_teacher.last_name,
        adminapp_teacher.specialization, adminapp_teacher.position from adminapp_teacher""")
        teachers = dictfetchall(cursor)
        return teachers


def get_student():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT adminapp_student.id, adminapp_student.first_name, adminapp_student.last_name,
        adminapp_student.phone, adminapp_student.address, adminapp_student.image from adminapp_student""")
        student = dictfetchall(cursor)
        return student


def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT adminapp_product.*, adminapp_category.name as category_name 
        FROM adminapp_product 
        LEFT JOIN adminapp_category ON adminapp_product.category_id = adminapp_category.id
        WHERE adminapp_product.available = 1""")
        return dictfetchall(cursor)


def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT * FROM adminapp_category")
        return dictfetchall(cursor)
