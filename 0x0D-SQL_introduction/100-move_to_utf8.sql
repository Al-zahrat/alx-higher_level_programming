-- alter hbtn_0c_0 database
ALTER DATABASE `hbtn_0c_0`
CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `hbtn_0c_0`;
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
ALTER TABLE `first_table`
MODIFY `name` VARCHAR(256)
CHARACTER SET utf8 COLLATE utf8_unicode_ci;
