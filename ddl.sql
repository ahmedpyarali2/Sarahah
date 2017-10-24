
-- This DDL script was written by Ahmed Pyar Ali on Oct 24, 2017
-- This script creates two tables in database.


-- user tab;e to store user info
create table user(
    user_id varchar(36) not null,
    username varchar(50) not null,
    password varchar(50) not null,
    token varchar(36) not null,
    
    primary key(user_id)
);


-- message table to store anonymous message
create table message(
    m_id varchar(36) not null,
    to_id varchar(36) not null,
    from_id varchar(36) not null,
    message varchar(100),
    
    primary key(m_id)
);