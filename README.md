
# Django_test(Vehicle Rental API)

Don't bother about UIs, we're here for APIs,
Here you need to identify the schema/model fields by observing the UIs, The goal of this assignment is to build **_API_** for a **Vehicle Rental** site in which you are free to play with as much as possible your sample data.

<img src="car_rental1.png" />
<img src="car_rental2.png" />

---

<hr>

### API Features:

1. User login for renter and car owner.

2. Vehicle owner

- owner can add,update multiples vehicles (fields= car_model,colour,fuel_type,car images,price per hour, is_available etc) 
- owner can update and view only his vehicles(use permissions)
- owner can accept or reject renter request( in case any renter choose his vehicle for rent).
- owner can check all rent history for his vehicles.

3. Renter(user) <br>

- user can see all vehicles with details(e.g price,image,fuel_type etc)  .
- user can request for any car that he choose.
-user can check his rent history 

4. Authentication

- Login (mandatory)
- Logout(optional)
- Signup (optional)

5.Create Logs
 -whenever any user login , a log should be generate in login_logs table(model) (fields=user,user_type,login_at )<br>
 <b>Note: Use signals to create logs</b>
<hr>

### Coding Guidelines

- Please fork current problem repository or use it as template and, add [@divyansh420](https://github.com/divyansh420) ,[@nitesh5695smilebots](https://github.com/nitesh5695smilebots) as collaborator while intializing repository in github. And follow the given timeline instructions from your mail.
- The changes/commits will not be considered after timeline mentioned in your mail.
- Please avoid any frameworks and libraries except **_Django REST framework_**.
- Focus more on the **_Django REST framework_** side of the problem.
- You need to add requirements.txt file in project
- Add a readme.md file and add all details about your APIs.
- You will be evaluated on a **WORKING PROJECT** for:
  - Modularity of Code
  - Security
  - Data Structures used
  - Model serialization
  - Database designing
  - Logic and cleanliness of code.
  - Completeness.
- Please ask us for any hurdle in your problem assignment.

<b>Note: <b> please use sqlite database and tables should be related to other tables.
