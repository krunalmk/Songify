# Songify

Import mysql from `mysql/testapp.sql`

## Project setup

* Install all libraries from requirements.txt using
    ```
    pip install -r requirements.txt
    ```

* Once installed, open terminal ( console) in the directory where you stored Songify. Then execute 
    ```
    cd Songify
    ```

* Grant permissions to files:
    ```
    chmod -x app.py
    chmod a+x create-table.py
    ```

* To setup the SQLite3 db, you need to execute a python script:
    ```
    python create-table.py
    ```

* This will create file, `musicDB.db`. You can open it using `sqlitebrowser`.
* If you don't have sqlitebrpwser, follow the steps to download this by [clicking here](https://sqlitebrowser.org/dl/)

* Once the db is created you can run the server using following command:
    ```
    python app.py
    ```

* *Open the project in web browser using*
    
    http://127.0.0.1:5000/

## Homepage
![Home]()


## Edit product
![View]()
