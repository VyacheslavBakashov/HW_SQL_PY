-- название и год выхода альбомов, вышедших в 2018 году
SELECT name_album, EXTRACT(YEAR FROM date_release) as year_release
  FROM album
 WHERE EXTRACT(YEAR FROM date_release) = 2018;

-- название и продолжительность самого длительного трека
SELECT name_track, duration
  FROM track
 WHERE duration = (SELECT MAX(duration)
				     FROM track);

  /*SELECT name_track, duration
    FROM track
ORDER BY duration DESC 
   LIMIT 1;*/

-- название треков, продолжительность которых не менее 3,5 минуты				 
SELECT name_track
  FROM track
 WHERE duration > 210;

-- названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT name_collection
  FROM collection
 WHERE EXTRACT(YEAR FROM date_release) BETWEEN 2018 AND 2020;

-- исполнители, чье имя состоит из 1 слова
SELECT name_singer
  FROM singer
 WHERE name_singer NOT LIKE '% %';

-- название треков, которые содержат слово "мой"/"my"
SELECT name_track
  FROM track
 WHERE name_track ~* 'my|мой'  /*WHERE name_track LIKE '%my%'*/;



