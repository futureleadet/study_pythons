-- CREATE TABLE students (
--     id INT PRIMARY KEY,
--     name VARCHAR(50),
--     age INT
-- );

-- INSERT INTO students (id, name, age) VALUES (1, '홍길동', 23);
-- INSERT INTO students (id, name, age) VALUES (2, '이영희', 21);
-- INSERT INTO students (id, name, age) VALUES (3, '박철수', 26);

-- UPDATE students SET age = 25 WHERE id = 2;

-- DELETE FROM students WHERE id = 3;

-- 문제 6: PRIMARY KEY 이해 문제
-- 어떤 에러가 발생하는가?

-- Duplicate entry 또는 Primary Key violation 에러가 발생합니다. (정확한 메시지는 DBMS에 따라 다를 수 있습니다.)

-- 왜 발생하는가?

-- book_id 컬럼이 PRIMARY KEY로 지정되어 있기 때문에, 이미 **book_id = 1**인 레코드가 첫 번째 INSERT 문으로 삽입되었습니다. 두 번째 INSERT 문에서 다시 **book_id = 1**을 삽입하려고 시도하면 PRIMARY KEY의 고유성(Unique) 규칙을 위반하게 되어 에러가 발생합니다.

-- PRIMARY KEY 의 규칙을 쓰시오.

-- 고유성(Unique): 테이블 내의 모든 레코드를 고유하게 식별할 수 있어야 합니다. 즉, 중복된 값을 가질 수 없습니다.

-- NOT NULL: NULL 값, 즉 빈 값을 가질 수 없습니다.