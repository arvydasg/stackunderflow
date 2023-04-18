# Table of Contents

-   [Stackunderflow](#org72df02f)
-   [The requirements](#org5e2219f)
        -   [General requirements](#orgef0a474)
        -   [Duomenų bazė](#org2e6c711)
        -   [Frontend'as](#orgebdf2a6)
-   [Stuff I did not manage to implement](#org6221a80)
-   [Databases](#orgbfaf525)



<a id="org72df02f"></a>

# Stackunderflow

An app where users can ask questions and get the answers.


<a id="org5e2219f"></a>

# The requirements


<a id="orgef0a474"></a>

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


<a id="org2e6c711"></a>

### Duomenų bazė

Duomenų bazė turėtų saugoti visą informaciją - klausimus, atsakymai,
vartotojus, ir bet kokią kitą informaciją kurios prireiktų.


<a id="orgebdf2a6"></a>

### Frontend'as

Frontend'as neturi nustatyto dizaino vaizdo (angl. wireframes), kurį
reikia atkartoti. Tačiau jum tenka sunkesnė užduotis - patiems
sugalvoti ir sukurti puslapio dizainą. Svarbiausia išpildyti visus
funkcinius reikalavimus ir validuoti vartotojo įvestį.


<a id="org6221a80"></a>

# Stuff I did not manage to implement

-   testing
-   deleting related answers when a question is deleted(meh)
-   duckdns domain
-   pagination


<a id="orgbfaf525"></a>

# Databases

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
