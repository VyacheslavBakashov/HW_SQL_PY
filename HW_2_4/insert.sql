INSERT INTO genre (name_genre)
VALUES 
	('pop'),
    ('rock'),
    ('drum & bass'),
    ('hip hop'),
    ('electronic'),
    ('R&B');

INSERT INTO singer (name_singer)
VALUES 
	('Drake'),
	('Eminem'),
	('Rihanna'),
	('Camila Cabello'),
	('Руки Вверх'),
	('Полина Гагаина'),
	('System of a Down'),
	('Slipknot'),
	('Swedish House Mafia'),
	('Second Nature'),
	('Snitch');

INSERT INTO genre_singer (genre_id, singer_id)
VALUES
	(1, 1),
	(1, 3),
	(1, 4),
	(1, 5),
	(1, 6),
	(2, 7),
	(2, 8),
	(3, 11),
	(3, 10),
	(4, 1),
	(4, 2),
	(4, 3),
	(5, 9),
	(6, 1),
	(6, 3),
	(6, 4);


INSERT INTO album (name_album, date_release)
VALUES
	('Scorpion', '2018-06-29'),
	('Care Package', '2019-07-31'),
	('Music to Be Murdered By', '2020-01-16'),
	('ANTI', '2019-10-07'),
	('Camila', '2018-01-11'),
	('Сделай Погромче!', '2018-06-07'),
	('Попроси у облаков ', '2018-02-08'),
	('Protect the Land / Genocidal Humanoidz', '2020-11-05'),
	('We Are Not Your Kind', '2019-08-08'),
	('Lost In The Virus', '2018-02-13'),
	('Moth to a Flame', '2022-02-04'),
	('Second Nature', '2019-06-14'),
	('Contract From Below', '2019-04-04');

INSERT INTO singer_album (singer_id, album_id)
VALUES
	(1, 1),
	(1, 2),
	(2, 3),
	(3, 4),
	(4, 5),
	(5, 6),
	(6, 7),
	(7, 8),
	(8, 9),
	(8, 10),
	(9, 11),
	(10, 12),
	(11, 13);

INSERT INTO track (name_track, duration, album_id)
VALUES
	('Survival', 136, 1),
	('Nonstop', 239, 1),
	('I am Upset', 199, 1),
	('In My Feelings', 217, 1),
	('Emotionless', 302, 1),
	('Dreams Money Can Buy', 253, 2),
	('The Motion', 244, 2),
	('How Bout Now', 282, 2),
	('Premonition', 174, 3),
	('In Too Deep', 194, 3),
	('Stepdad', 213, 3),
	('Consideration', 215, 4),
	('Work', 211, 4),
	('Needed Me', 194, 4),
	('Never Be the Same', 226, 5),
	('She Loves Control', 177, 5),
	('Real Friends', 214, 5),
	('Песенка', 182, 6),
	('Лишь о тебе мечтая', 243, 6),
	('Я твоя', 164, 7),
	('Я тебя не прощу никогда', 254, 7),
	('Time Stop', 249, 7),
	('Protect the Land', 307, 8),
	('Genocidal Humanoidz', 155, 8),
	('Unsainted', 260, 9),
	('Nero Forte', 315, 9),
	('Remember me', 172, 10),
	('Bodies', 189, 10),
	('Moth to a Flame (with The Weeknd)', 236, 11),
	('Late', 148, 12),
	('Wallet', 138, 12),
	('Contract From Below (Original Mix)', 347, 13),
	('Bolts (Original Mix)', 379, 13);

INSERT INTO collection (name_collection, date_release)
VALUES
	('mixed_collection_1', '2020-01-05'),
	('mixed_collection_2', '2019-11-21'),
	('mixed_collection_3', '2018-02-07'),
	('mixed_collection_4', '2018-07-21'),
	('mixed_collection_5', '2019-08-09'),
	('mixed_collection_6', '2021-05-09'),
	('mixed_collection_7', '2019-10-11'),
	('mixed_collection_8', '2021-01-01');


INSERT INTO collection_track (collection_id, track_id)
VALUES
	(1, 1),
	(1, 4),
	(1, 5),
	(1, 6),
	(1, 7),
	(1, 10),
	(2, 30),
	(2, 31),
	(2, 32),
	(2, 33),
	(3, 13),
	(3, 29),
	(4, 22),
	(4, 23),
	(4, 27),
	(4, 28),
	(5, 24),
	(5, 25),
	(5, 26),
	(6, 12),
	(6, 14),
	(6, 15),
	(6, 16),
	(6, 17),
	(7, 18),
	(7, 19),
	(7, 20),
	(7, 21),
	(8, 2),
	(8, 3),
	(8, 8),
	(8, 9);
