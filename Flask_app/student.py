from Flask_app.config.mysqlconnection import connectToMySQL


db = 'new_students'


class Student:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.pet_name = data['pet_name']
        self.favorite_snack = data['favorite_snack']

    @classmethod
    def save(cls, data):
        query = 'INSERT into students (first_name, last_name, occupation, pet_name, favorite_snack) VALUES(%(first_name)s, %(last_name)s, %(occupation)s, %(pet_name)s, %(favorite_snack)s)'
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM students'
        results = connectToMySQL(db).query_db(query)
        new_students = []
        for student in results:
            new_students.append(cls(student))
        return new_students

    @classmethod
    def edit_user(cls, data):
        query = 'SELECT * FROM students WHERE id = %(id)s'
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data, id):
        query = f'UPDATE students SET first_name = %(first_name)s, last_name = %(last_name)s, occupation = %(occupation)s, pet_name = %(pet_name)s, favorite_snack = %(favorite_snack)s WHERE id = {id}'
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = f'DELETE FROM students WHERE id= {id}'
        return connectToMySQL(db).query_db(query)
