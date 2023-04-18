# Table of Contents

-   [Stackunderflow](#orgf7dcbc7)
    -   [Task requirements](#orgeecc645)
        -   [General requirements](#org5720438)
        -   [DB](#org1f7cbcd)
        -   [Frontend](#org33e1453)
    -   [Stuff I did not manage to implement](#orgef59409)
    -   [Databases](#orgfaeae44)
-   [Extra's](#org97fdc00)
    -   [Blueprints](#orgdb41530)
    -   [Rich text editor](#org7690dd3)
    -   [My<sub>account</sub> page](#org206cf85)
    -   [filtering/sorting](#org7391f1f)
    -   [Hosing the app to Linode](#orgdf9e273)



<a id="orgf7dcbc7"></a>

# Stackunderflow

An app where users can ask questions and get the answers.

Can be reached from here - <http://139.162.204.223:5000/>


<a id="orgeecc645"></a>

## Task requirements


<a id="org5720438"></a>

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


<a id="org1f7cbcd"></a>

### DB

Duomenų bazė turėtų saugoti visą informaciją - klausimus, atsakymai,
vartotojus, ir bet kokią kitą informaciją kurios prireiktų.


<a id="org33e1453"></a>

### Frontend

Frontend'as neturi nustatyto dizaino vaizdo (angl. wireframes), kurį
reikia atkartoti. Tačiau jum tenka sunkesnė užduotis - patiems
sugalvoti ir sukurti puslapio dizainą. Svarbiausia išpildyti visus
funkcinius reikalavimus ir validuoti vartotojo įvestį.


<a id="orgef59409"></a>

## Stuff I did not manage to implement

-   testing
-   deleting related answers when a question is deleted(meh)
-   duckdns domain
-   pagination


<a id="orgfaeae44"></a>

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


<a id="org97fdc00"></a>

# Extra's


<a id="orgdb41530"></a>

## Blueprints

Using blueprints helped me to separate the app even more. Questions,
Answers, Auth stuff - everything separated in separate files.

Routes also separated and accessible as such:

/auth

/questions

Much cleaner and intuitive.


<a id="org7690dd3"></a>

## Rich text editor

Since this is a programmer's place to ask questions, I decided it
would be good to add syntax highlighting to the question/answer
content. I have used `ckeditor` for this task. It was very quick and
easy to implement.


<a id="org206cf85"></a>

## My<sub>account</sub> page

Added so the user can upload his/her profile image. Also could edit
his/her username. And to see the questions that the user has asked.

Pre-populating the fields with the help of these lines in `auth.py`:

    elif request.method == "GET":
        form.name.data = current_user.name
        form.email.data = current_user.email


<a id="org7391f1f"></a>

## filtering/sorting

request.args.get() is a method in Flask that allows you to retrieve
the value of a query parameter from a request. In this case, it is
used to retrieve the value of the filter parameter from the URL query
string.

When a user submits the form with either "Questions with answers" or
"Questions without answers" selected, the corresponding value of
filter (i.e. "with<sub>answers</sub>" or "without<sub>answers</sub>") is added to the URL
query string as a parameter. The request.args.get() method retrieves
this parameter value and assigns it to the filter variable, which is
then used in the filter query to filter the list of questions.

    sort = request.args.get("sort", "created_at_desc")

In the code above, the default value of sort is set to
"created<sub>at</sub><sub>desc</sub>" by providing it as the second argument to
request.args.get(). This means that if the sort parameter is not
provided in the request, the default sort order will be used.


<a id="orgdf9e273"></a>

## Hosing the app to Linode

Hiding the secrets first - [This commit](https://github.com/arvydasg/stackunderflow/commit/69cd7e6c3fca1dbb4b3d6a8fe049e7730b37a6a8).

Followed [this](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04) tutorial. Quite basic, simply connected with ssh and
launched the app. Did not have time to make it as a service, add
domain name and such.
