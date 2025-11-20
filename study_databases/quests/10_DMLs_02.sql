CREATE TABLE web_links (
    numberid int,
    link_text varchar(255),
    link_url varchar(255),
    category varchar(255)
);

INSERT INTO web_links (numberid, link_text, link_url, category)
VALUES 
(1, '네이버' , 'https://naver.com', 'portal'),
(2, '구글' , 'https://google.com', 'portal'),
(3, '깃허브', '깃허브', '깃허브');


-- category가 "portal"인 링크만 조회
SELECT category = 'portal'
FROM web_links;

-- "깃허브"의 category를 "code" 로 수정
UPDATE web_links
SET category = 'aaacode'
WHERE numberid = 3;

-- "네이버" 데이터 삭제
DELETE FROM web_links 
WHERE link_text = '네이버';
