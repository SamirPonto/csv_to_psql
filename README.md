Hello, everyone!
Welcome to the version 1.0.

1. Introduction
    In this script I brought a script to add a csv to postgresql to visualization.
    As a way of studying, this script gave me a headache, but it worked with my csvs.

2. How to use
    Put the script in the same folder (if you want, but you can copy the path of the file).
    After this, type it:
    python3 add_data.py -f file.csv -n nrows* -c postgresql://postgres:postgres@localhost:5432/database_name -t table_name -r r or nothing.

    2.1 Notes 
        The flag -c is not compulsory, but, if not, the script will search in .env file. If you won't put the connstring in terminal, put this in the .env like:
        DB_CONNSTRING = postgresql://postgres:postgres@localhost:5432/database_name.

        So, you need already created a database, but the table_name, if it doesn't exist, it will be created.

        *obs: nrows is the number of lines the script will execute at a time (to alleviate memory overhead).

        -r flag: If you pass "-r r" the data will replace the existent (even the column's name).

3. Feedbacks
    I will appreciate if you want to contribute ideas, fix something, write less code.