-- create a table in a given database
-- database passed as argument of command mysql
--      id = 1, name = “John”, score = 10
--      id = 2, name = “Alex”, score = 3
--      id = 3, name = “Bob”, score = 14
--      id = 4, name = “George”, score = 8
CREATE TABLE IF NOT EXISTS `second_table` (`id` INT, `name` VARCHAR(256),`score` INT);
-- add new rows into the created if not exist table
INSERT INTO `second_table` (`id`, `name`, `score`)
VALUES
	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8);
