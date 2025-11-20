CREATE TABLE news_articles (
    newsid int,
    title varchar(255),
    url varchar(255),
    author varchar(255),
    published_at varchar(255)
);

INSERT INTO news_articles (newsid, title, url, author, published_at)
VALUES 
(1, 'AI 시대 도래', 'https://news.com/ai', '홍길동', '2025-01-01'),
(2, '경제 성장률 상승', 'https://news.com/economy', '이영희', '2025-01-05');

-- author가 "홍길동"인 데이터만 조회하는 쿼리를 작성하라
SELECT author = '홍길동'
FROM news_articles;

-- 첫 번째 뉴스 제목을 새로운 문자열로 변경하는 UPDATE문 작성
UPDATE news_articles
SET title = 'aaa'
WHERE newsid = 1;

-- 두 번째 뉴스를 삭제하는 DELETE문 작성
DELETE FROM news_articles 
WHERE newsid = 2;