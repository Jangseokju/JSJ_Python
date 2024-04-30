-- Active: 1712576325728@@127.0.0.1@3306@joeun
CREATE TABLE Address_book (
    -- 컬럼명 데이터타입 NULL여부 기본값 제약조건
    번호 INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    이름 VARCHAR(100) NOT NULL,
    전화번호 VARCHAR(100) NOT NULL,
    주소 VARCHAR(100) NOT NULL,
    등록일자 TIMESTAMP DEFAULT now(),
    수정일자 TIMESTAMP DEFAULT now()
) COMMENT = '어드레스 북 테이블';