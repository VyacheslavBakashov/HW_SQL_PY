-- 1 количество исполнителей в каждом жанре
  SELECT name_genre, COUNT(singer_id) AS num
    FROM genre AS g
	     JOIN genre_singer AS gs
	     ON (g.genre_id = gs.genre_id)
   GROUP BY name_genre
   ORDER BY num DESC;

-- 2 количество треков, вошедших в альбомы 2019-2020 годов
SELECT COUNT(t.name_track) AS quantity
  FROM track AS t 
	   JOIN album AS a 
	   USING (album_id)
 WHERE EXTRACT(YEAR FROM a.date_release) IN (2019, 2020);

-- 3 средняя продолжительность треков по каждому альбому
  SELECT a.name_album, ROUND(AVG(t.duration)) AS track_avg_duration
    FROM album  AS a
	     JOIN track AS t
	     USING(album_id)
   GROUP BY album_id
   ORDER BY track_avg_duration;

-- 4 все исполнители, которые не выпустили альбомы в 2020 году
 				    
SELECT name_singer
FROM singer s 
WHERE s.singer_id NOT IN (SELECT sa.singer_id
							FROM singer_album AS sa	     
	 							 JOIN album AS a USING(album_id)
						    WHERE EXTRACT(YEAR FROM date_release) = 2020
						  );

-- 5 названия сборников, в которых присутствует конкретный исполнитель
  SELECT c.name_collection
    FROM collection AS c
		 JOIN collection_track AS ct USING(collection_id)
		 JOIN track AS t USING(track_id)
		 JOIN singer_album AS sa USING(album_id)
		 JOIN singer AS s USING(singer_id)
   WHERE s.name_singer = 'Eminem';

-- 6 название альбомов, в которых присутствуют исполнители более 1 жанра
SELECT name_album
  FROM (SELECT COUNT(ga.genre_id), a.name_album
	      FROM singer_album
			   JOIN genre_singer AS ga USING(singer_id)
			   JOIN album AS a USING(album_id)
	     GROUP BY a.name_album
	    HAVING COUNT(ga.genre_id) > 1
	  ) query;
 
-- 7 наименование треков, которые не входят в сборники
SELECT name_track
  FROM track
 WHERE track_id NOT IN (SELECT track_id 
 						  FROM collection_track
 					   );

-- 8 исполнителя(-ей), написавшего самый короткий по продолжительности трек 
  SELECT name_singer
    FROM singer 
		 JOIN singer_album USING(singer_id)
		 JOIN track USING(album_id)
   GROUP BY name_singer, duration
  HAVING duration = (SELECT MIN(duration) AS min_duration 
 					   FROM track
 					);

-- 9  название альбомов, содержащих наименьшее количество треков

SELECT album.name_album, COUNT(track.name_track) AS track_count FROM album 
JOIN track USING(album_id)
GROUP BY album.name_album
HAVING COUNT(track.name_track) = (  
	SELECT COUNT(track.name_track) FROM album
	JOIN track USING(album_id)
	GROUP BY album.name_album
	ORDER BY COUNT(track.name_track)
	LIMIT 1);				
 				
 				
 				
/*SELECT name_album
  FROM album 
	   JOIN (SELECT album_id, COUNT(*) AS num
		       FROM track
		   GROUP BY album_id
		     ) AS query_1
	   USING(album_id)
 WHERE num = (SELECT MIN(num)
			    FROM (SELECT album_id, COUNT(*) AS num
				        FROM track
				    GROUP BY album_id
			          ) AS query_2
			  );*/

