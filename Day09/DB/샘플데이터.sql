-- Active: 1712576325728@@127.0.0.1@3306@joeun
-- 계정 생성
DROP USER IF EXISTS 'joeun'@'%';
CREATE USER 'joeun'@'%' IDENTIFIED BY '123456';


-- 모든 권한 부여
GRANT ALL PRIVILEGES ON *.* TO 'joeun'@'%';

 -- 스키마 생성
DROP DATABASE IF EXISTS joeun;
CREATE DATABASE joeun;

DROP TABLE IF EXISTS `joeun`.`학생`;
 -- 학생 테이블 생성
 CREATE TABLE `joeun`.`학생` (
  `no` int NOT NULL AUTO_INCREMENT,
  `std_id` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `tel` varchar(100) DEFAULT NULL,
  `reg_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `upd_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`no`),
  UNIQUE KEY `std_id_UNIQUE` (`std_id`)
) COMMENT='학생';


-- 데이터 추가
INSERT INTO `joeun`.`학생` ( std_id, name, tel ) VALUES ('A2401', '김조은', '010-1234-1234');
INSERT INTO `joeun`.`학생` ( std_id, name, tel ) VALUES ('A2402', '박조은', '010-2222-3333');
INSERT INTO `joeun`.`학생` ( std_id, name, tel ) VALUES ('A2403', '황조은', '010-3333-5555');