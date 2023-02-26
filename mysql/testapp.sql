CREATE TABLE songs(

    id int auto_increment primary key not null,
    title text not null,
    artist text not null,
    album text not null,
    songFile longblob not null
);
