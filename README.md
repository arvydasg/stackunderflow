# Table of Contents

-   [Stackunderflow](#orgb04beb2)
    -   [Task requirements](#orgda0334b)
        -   [General requirements](#orgb021765)
        -   [DB](#org737c602)
        -   [Frontend](#org33a34e3)
    -   [Stuff I did not manage to implement](#org38b5ac6)
    -   [Databases](#orgb684737)
-   [Extra's](#org96edc5a)
    -   [Blueprints](#org86599c1)
    -   [Rich text editor](#orgf328911)
    -   [Macro for rendering form fields](#org90b477c)
    -   [My\_account page](#orgf8283a1)
    -   [filtering/sorting](#org51eb88e)
    -   [Hosing the app to Linode](#org6779dca)



<a id="orgb04beb2"></a>

# Stackunderflow

An app where users can ask questions and get the answers.

Can be reached from here - <http://139.162.204.223:5000/>


<a id="orgda0334b"></a>

## Task requirements


<a id="orgb021765"></a>

### General requirements

Final Full-Stack with Python Project ( stackoverflow )
Due April 19, 2023 5:00 PM
Closes April 19, 2023 5:00 PM

Baigiamasis projektas

Šios projekto metu reikės sukurti internetinį forumą naudojant "Flask"
ir SQLite duombaze. Forumo tikslas - leisti užduoti klausimus, į juos
atsakinėti ir žymėti patinkančius arba nepatinkančius atsakymus.
Galite įsivaizduoti kažką panašaus į
<https://stackoverflow.com/questions>, tik truputį supaprastintą
versiją.

Funkcionalumas:

-   Registruotis
-   Prisijungti
-   Užduoti naują klausimą (tik prisijungus)
-   Redaguoti užduotą klausimą (UI turi matytis, kad klausimas buvo
    redaguotas) (tik prisijungus)
-   Ištrinti klausimą (tik prisiijungus)
-   Atsakyti į užduotą klausimą (tik prisijungus)
-   Redaguoti atsakymą (taip pat turi matytis, kad atsakymas buvo
    redaguotas) (tik prisijungus)
-   Ištrinti atsakymą (tik prisijungus)
-   Žymėti/atžymėti patinkačius ir nepatinkančius atsakymus
    (like/dislike) (tik prisijungus)
-   Peržiūrėti klausimų sąrašą su gamybė rikiuoti pagal klausimo datą
    ir/arba atsakymų skaičių (didėjimo arba mažėjimo tvarka)
-   Filtruoti atsakytus arba neatsakytus klausimus
-   Peržiūrėti klausimų atsakymus


<a id="org737c602"></a>

### DB

Duomenų bazė turėtų saugoti visą informaciją - klausimus, atsakymai,
vartotojus, ir bet kokią kitą informaciją kurios prireiktų.


<a id="org33a34e3"></a>

### Frontend

Frontend'as neturi nustatyto dizaino vaizdo (angl. wireframes), kurį
reikia atkartoti. Tačiau jum tenka sunkesnė užduotis - patiems
sugalvoti ir sukurti puslapio dizainą. Svarbiausia išpildyti visus
funkcinius reikalavimus ir validuoti vartotojo įvestį.


<a id="org38b5ac6"></a>

## Stuff I did not manage to implement

-   testing
-   deleting related answers when a question is deleted(meh)
-   duckdns domain
-   pagination


<a id="orgb684737"></a>

## Databases

![img](/db.jpeg)

`Users` table: one-to-many relationship with the Question table and a
one-to-many relationship with the Answer table. This means that each
user can have multiple questions and answers associated with them.

`Question` table: one-to-many relationship with the Answer table. This
means that each question can have multiple answers associated with it.

`Answer` table: many-to-one relationship with the Users table and a
many-to-one relationship with the Question table. This means that each
answer is associated with a single user who is its author and a single
question to which it is a response.

`Action` table: many-to-many relationship between the Users and Answer
tables. This means that each user can perform multiple actions on
multiple answers, such as liking or disliking them.

Migrations really help. Got used to using them, no need to delete the
db each and every time when making changes to the models.


<a id="org96edc5a"></a>

# Extra's


<a id="org86599c1"></a>

## Blueprints

Using blueprints helped me to separate the app even more. Questions,
Answers, Auth stuff - everything separated in separate files.

Routes also separated and accessible as such:

/auth

/questions

Much cleaner and intuitive.


<a id="orgf328911"></a>

## Rich text editor

Since this is a programmer's place to ask questions, I decided it
would be good to add syntax highlighting to the question/answer
content. I have used `ckeditor` for this task. It was very quick and
easy to implement.

[How I implemented CKEditor](https://github.com/arvydasg/stackunderflow/commit/8278895e899d644b685f89c7286e2348211caa3a).


<a id="org90b477c"></a>

## Macro for rendering form fields

<https://bootstrap-flask.readthedocs.io/en/stable/macros/>

Forms can get large, especially with flask\_wtf.

Macros help with that enormously. Instead of having 20 lines of code
for a form, you can have 2-5 lines.

Describe the template for the form, use this template in teach of
your forms.


<a id="orgf8283a1"></a>

## My\_account page

Added so the user can upload his/her profile image. Also could edit
his/her username. And to see the questions that the user has asked.

Pre-populating the fields with the help of these lines in `auth.py`:

    elif request.method == "GET":
        form.name.data = current_user.name
        form.email.data = current_user.email


<a id="org51eb88e"></a>

## filtering/sorting

request.args.get() is a method in Flask that allows you to retrieve
the value of a query parameter from a request. In this case, it is
used to retrieve the value of the filter parameter from the URL query
string.

When a user submits the form with either "Questions with answers" or
"Questions without answers" selected, the corresponding value of
filter (i.e. "with\_answers" or "without\_answers") is added to the URL
query string as a parameter. The request.args.get() method retrieves
this parameter value and assigns it to the filter variable, which is
then used in the filter query to filter the list of questions.

    sort = request.args.get("sort", "created_at_desc")

In the code above, the default value of sort is set to
"created\_at\_desc" by providing it as the second argument to
request.args.get(). This means that if the sort parameter is not
provided in the request, the default sort order will be used.


<a id="org6779dca"></a>

## Hosing the app to Linode

Hiding the secrets first - [This commit](https://github.com/arvydasg/stackunderflow/commit/69cd7e6c3fca1dbb4b3d6a8fe049e7730b37a6a8).

Followed [this](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04) tutorial. Quite basic, simply connected with ssh and
launched the app. Did not have time to make it as a service, add
domain name and such.
