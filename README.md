#📌 Django REST Framework CRUD Operations
#This project demonstrates CRUD (Create, Read, Update, Delete) operations using Django REST Framework (DRF) with different types of views, including:

#Function-based views (@api_view)
#Class-based views (APIView)
#Mixins
#Generic views & ViewSets
#It also includes pagination, filtering, ordering (basic to advanced), and serialization (basic to nested) but does not use authentication.

📂 Apps in This Project
✅ Blogs - CRUD using various API views
✅ Employees - CRUD with function-based views and mixins
✅ Students - CRUD with APIView and class-based views
✅ API - Common API configurations

🚀 Features
✔ CRUD Operations using @api_view, APIView, Mixins, Generic Views, and ViewSets
✔ Custom & Global Pagination
✔ Filtering using query parameters
✔ Advanced Ordering (Ascending & Descending)
✔ Basic to Advanced Serialization (Nested, ForeignKey)
❌ No Authentication Used

🛠 Technologies Used
🔹 Django (Backend Framework)
🔹 Django REST Framework (API Development)
🔹 SQLite/MySQL (Database)
🔹 Git & GitHub (Version Control)

🔧 Setup Instructions
1️⃣ Clone the Repository

bash
Copy code
git clone https://github.com/AnilKumarSingh9856/django_restframework_crude_operation.git
2️⃣ Navigate to the Project Directory

bash
Copy code
cd django_restframework_crude_operation
3️⃣ Create a Virtual Environment & Activate It

bash
Copy code
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
4️⃣ Install Dependencies

bash
Copy code
pip install -r requirements.txt
5️⃣ Apply Migrations

bash
Copy code
python manage.py migrate
6️⃣ Start the Development Server

bash
Copy code
python manage.py runserver
🎯 API Endpoints
Blogs App (Function-based views using @api_view)
GET /blogs/ → List all blogs
POST /blogs/ → Create a new blog
GET /blogs/{id}/ → Retrieve a specific blog
PUT /blogs/{id}/ → Update blog details
DELETE /blogs/{id}/ → Delete a blog
Employees App (Class-based views using APIView)
GET /employees/ → List all employees
POST /employees/ → Create a new employee
GET /employees/{id}/ → Retrieve a specific employee
PUT /employees/{id}/ → Update employee details
DELETE /employees/{id}/ → Delete an employee
Students App (Mixins & Generic Views)
GET /students/ → List all students
POST /students/ → Create a new student
GET /students/{id}/ → Retrieve a specific student
PUT /students/{id}/ → Update student details
DELETE /students/{id}/ → Delete a student
🔍 Ordering & Filtering
Ordering by ID, Name, Date:
bash
Copy code
/blogs/?ordering=id
/employees/?ordering=-name
Multiple Field Ordering:
bash
Copy code
/students/?ordering=name,age
Filtering Example:
bash
Copy code
/employees/?designation=Manager
📌 Serialization (Basic to Advanced)
Django REST Framework Serializers are used to convert Python QuerySets → JSON response.

🔹 Basic Serialization (ModelSerializer)
Used for simple CRUD operations:

python
Copy code
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
🔹 Custom Serializer Fields
Adding custom fields to a serializer:

python
Copy code
class EmployeeSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'full_name', 'designation']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
🔹 Nested Serialization (ForeignKey Relationship)
Used when one model is linked to another. Example: A Blog model has a User (Author).

python
Copy code
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author']
🔹 Nested Serialization (Many-to-Many Relationship)
Example: A Student model has multiple Courses.

python
Copy code
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'courses']
🔹 Hyperlinked Serializers
python
Copy code
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'id', 'name', 'designation']
❌ No Authentication Used
This project does not include authentication. The APIs are open and can be accessed without login credentials.

🤝 Contributing
Feel free to fork this project, raise issues, or submit pull requests!

📜 License
This project is licensed under the MIT License.

