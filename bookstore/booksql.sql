CREATE TABLE BOOK(
BOOK_ID NUMBER NOT NULL,
BOOK_IMG VARCHAR2(100) NOT NULL,
BOOK_TITLE VARCHAR2(100) NOT NULL,
BOOK_PRICE FLOAT NOT NULL,
BOOK_AUTHOR VARCHAR2(100) NOT NULL,
BOOK_PAGES NUMBER NOT NULL,
BOOK_PUBLISHER VARCHAR2(100) NOT NULL,
BOOK_DESCRIPTION VARCHAR(500),
CONSTRAINT BOOK_PK PRIMARY KEY(BOOK_ID)
);

CREATE TABLE USERS(
USER_ID NUMBER NOT NULL,
USERNAME VARCHAR2(20) NOT NULL,
USER_PASSWORD VARCHAR2(20) NOT NULL,
USER_EMAIL VARCHAR2(40),
USER_ADDRESS VARCHAR2(200),
USER_PHONE NUMBER NOT NULL,
IS_SUPERVISOR VARCHAR2(1),
CONSTRAINT USER_PK PRIMARY KEY(USER_ID)
);

CREATE TABLE USER_BOUGHT(
USER_ID NUMBER NOT NULL,
BOOK_ID NUMBER NOT NULL,
BUY_DATE TIMESTAMP,
CONSTRAINT USER_BOUGHT_PK PRIMARY KEY(USER_ID,BOOK_ID,BUY_DATE);

CREATE TABLE CATEGORIES(
CATEGORY_ID NUMBER NOT NULL,
CATEGORY_NAME VARCHAR2(50),
CONSTRAINT CATEGORIES_PK PRIMARY KEY(CATEGORY_ID)
);

CREATE TABLE USER_LIKED_CATEGORIES(
USER_ID NUMBER NOT NULL,
CATEGORY_ID NUMBER NOT NULL,
CONSTRAINT USER_LIKED_CATEGORIES_PK PRIMARY KEY(USER_ID,CATEGORY_ID)
);

CREATE TABLE USER_LIKED_BOOKS(
USER_ID NUMBER NOT NULL,
BOOK_ID NUMBER NOT NULL,
CONSTRAINT USER_LIKED_BOOKS_PK PRIMARY KEY(USER_ID,BOOK_ID)
);

CREATE SEQUENCE USER_SEQUENCE;
CREATE SEQUENCE PRODUCT_SEQUENCE;
CREATE SEQUENCE CATEGORY_SEQUENCE;


CREATE TRIGGER before_insert_user
BEFORE INSERT ON USERS FOR EACH ROW
BEGIN
  SELECT USER_SEQUENCE.NEXTVAL
  INTO :new.USER_ID
  FROM dual;
END;
/
CREATE TRIGGER before_insert_product
BEFORE INSERT ON BOOK FOR EACH ROW
BEGIN
  SELECT USER_SEQUENCE.NEXTVAL
  INTO :new.BOOK_ID
  FROM dual;
END;
/
CREATE TRIGGER before_insert_categories
BEFORE INSERT ON CATEGORIES FOR EACH ROW
BEGIN
  SELECT CATEGORY_SEQUENCE.NEXTVAL
  INTO :new.CATEGORY_ID
  FROM dual;
END;
/

ALTER TABLE BOOK
ADD (category_id NUMBER);

ALTER TABLE BOOK
ADD CONSTRAINT category_fk FOREIGN KEY(CATEGORY_ID) 
            REFERENCES CATEGORIES (CATEGORY_ID);

INSERT INTO USERS(USERNAME,USER_PASSWORD,USER_EMAIL,USER_PHONE)
VALUES('ADMIN','ADMIN','ADMIN@ADMIN',089669765);

INSERT INTO CATEGORIES(CATEGORY_ID,CATEGORY_NAME) VALUES (1,'ROMANCE');
