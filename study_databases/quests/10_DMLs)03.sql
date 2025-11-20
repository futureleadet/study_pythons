
CREATE TABLE scraping_html_results (
    pageid int,
    page_title varchar(255),
    page_url varchar(255),
    html_length int,
    status_code int
);

INSERT INTO scraping_html_results (pageid, page_title, page_url, html_length, status_code)
VALUES
(1, '홈페이지', 'https://site.com', 15700, 200),
(2, '블로그', 'https://blog.com', 9800, 200),
(3, '404 페이지', 'https://site.com/notfound', 0, 404);

-- status_code가 200인 페이지만 조회
SELECT status_code = '200'
FROM scraping_html_results

-- "블로그"의 html_length를 12000으로 수정
UPDATE scraping_html_results
SET html_length = 12000
WHERE page_title = '블로그'

-- status_code가 404인 데이터 삭제
