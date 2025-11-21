## 프롬프트
```
나는 코딩 초보자야.
아래 5문제에 대해 각각 코드를 짜야하는데.
AI에게 요청할 JSON으로 된 명령어를 만들어줘
-----------------------------------------------------------

📌 문제 1 — 테이블 생성 (PRIMARY KEY 기초)
아래 요구사항에 맞는 CREATE TABLE 문을 작성하시오.
✔ 요구사항
테이블명: students


컬럼:


id (INT, PRIMARY KEY)


name (VARCHAR(50))


age (INT)



📌 문제 2 — CREATE (INSERT) 기초
✔ 요구사항
위 students 테이블에 다음 데이터를 INSERT 하시오.
id
name
age
1
홍길동
23
2
이영희
21
3
박철수
26


📌 문제 3 — READ (SELECT) 기본 조회
다음 조건들을 만족하는 SELECT 쿼리를 작성하시오.
students 테이블의 전체 데이터를 조회


나이가 22세 이상인 학생만 조회


name 이 “홍길동”인 학생만 조회



📌 문제 4 — UPDATE 연습
✔ 요구사항
id = 2 인 학생의 나이를 25로 수정하시오.

📌 문제 5 — DELETE 연습
✔ 요구사항
id = 3 번 학생 데이터를 삭제하는 DELETE 문을 작성하시오.

📌 문제 6 — PRIMARY KEY 이해 문제
다음과 같은 테이블을 가정하시오:
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    price INT
);

아래 데이터 INSERT 시 발생할 문제를 설명하시오.
INSERT INTO books (book_id, title, price)
VALUES (1, '책 A', 10000);

INSERT INTO books (book_id, title, price)
VALUES (1, '책 B', 15000);

📌 질문:
어떤 에러가 발생하는가?


왜 발생하는가?


PRIMARY KEY 의 규칙을 쓰시오.
```
## 결과 JSON
```
{
  "request_type": "sql_code_generation_and_explanation",
  "task_description": "초보자를 위한 SQL 문제 6가지에 대한 해답(SQL 쿼리 또는 설명)을 작성해주세요.",
  "problems": [
    {
      "id": 1,
      "title": "테이블 생성 (PRIMARY KEY 기초)",
      "prompt": "테이블명: students, 컬럼: id (INT, PRIMARY KEY), name (VARCHAR(50)), age (INT) 에 맞는 CREATE TABLE 문을 작성하시오."
    },
    {
      "id": 2,
      "title": "CREATE (INSERT) 기초",
      "prompt": "students 테이블에 다음 데이터를 INSERT 하시오. (id=1, name='홍길동', age=23), (id=2, name='이영희', age=21), (id=3, name='박철수', age=26)"
    },
    {
      "id": 3,
      "title": "READ (SELECT) 기본 조회",
      "prompt": "students 테이블에 대해 다음 조건들을 만족하는 SELECT 쿼리를 각각 작성하시오. 1. 전체 데이터 조회, 2. 나이가 22세 이상인 학생만 조회, 3. name이 '홍길동'인 학생만 조회."
    },
    {
      "id": 4,
      "title": "UPDATE 연습",
      "prompt": "students 테이블에서 id = 2 인 학생의 나이를 25로 수정하는 UPDATE 쿼리를 작성하시오."
    },
    {
      "id": 5,
      "title": "DELETE 연습",
      "prompt": "students 테이블에서 id = 3 번 학생 데이터를 삭제하는 DELETE 문을 작성하시오."
    },
    {
      "id": 6,
      "title": "PRIMARY KEY 이해 문제",
      "prompt": "CREATE TABLE books (book_id INT PRIMARY KEY, title VARCHAR(100), price INT); 구문으로 생성된 테이블에 'INSERT INTO books (book_id, title, price) VALUES (1, '책 A', 10000);' 실행 후 'INSERT INTO books (book_id, title, price) VALUES (1, '책 B', 15000);' 를 실행했을 때 발생할 에러, 원인, 그리고 PRIMARY KEY의 규칙을 설명하시오."
    }
  ]
}
```






