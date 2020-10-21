CREATE DATABASE Manageo;
USE Manageo;

CREATE TABLE `users` (
	`user_id` INT NOT NULL AUTO_INCREMENT,
    `user_last_name` VARCHAR(50) NOT NULL,
    `user_first_name` VARCHAR(50) NOT NULL,
    `mdp_hash` CHAR(64) NOT NULL,
    `user_email` VARCHAR(320) NOT NULL,
    `user_adress` TEXT NOT NULL,
    `user_phone` VARCHAR(20) NOT NULL,
    `user_siret` INT(14) DEFAULT NULL,
    PRIMARY KEY (`user_id`)
);

CREATE TABLE `admin` (
	`admin_id` VARCHAR(10) NOT NULL,
    `admin_first_name` VARCHAR(50) NOT NULL,
    `admin_last_name` VARCHAR(50) NOT NULL,
    `admin_mdp_hash` CHAR(64) NOT NULL,
    PRIMARY KEY (`admin_id`)
);
    
CREATE TABLE `log` (
	`id` INT NOT NULL AUTO_INCREMENT,
    `log_id` INT NOT NULL,
    `log_status` ENUM('non traitée', 'en cours de traitement', 'cloturée') NOT NULL,
    `log_category` ENUM('accéder', 'modifier', 'supprimer') NOT NULL,
    `log_date` DATETIME NOT NULL,
    `log_admin_id` VARCHAR(10) NOT NULL,
    `user_id` INT NOT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `log_ibfk_1` FOREIGN KEY (`log_admin_id`) REFERENCES `admin` (`admin_id`),
    CONSTRAINT `log_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
);


    
#USE Manageo;
#SET FOREIGN_KEY_CHECKS = 0;
#ALTER TABLE users CONVERT TO CHARACTER SET utf8 COLLATE utf8_bin;
#SET FOREIGN_KEY_CHECKS = 1;

#USE Manageo;
#SET FOREIGN_KEY_CHECKS = 0;
#ALTER TABLE log CONVERT TO CHARACTER SET utf8 COLLATE utf8_bin;
#SET FOREIGN_KEY_CHECKS = 1;

#USE Manageo;
#SET FOREIGN_KEY_CHECKS = 0;
#ALTER TABLE admin CONVERT TO CHARACTER SET utf8 COLLATE utf8_bin;
#SET FOREIGN_KEY_CHECKS = 1;