-- alter hbtn_0c_0 database
ALTER DATABASE htbn_0c_0
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE htbn_0c_0;
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table
MODIFY name VARCHAR(256)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
