from Flask_app import app
from Flask_app.controllers import students_controller


if __name__ == '__main__':
    app.run(debug=True, port=5001)
