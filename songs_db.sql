CREATE DATABASE  IF NOT EXISTS `songs_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `songs_db`;
-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: songs_db
-- ------------------------------------------------------
-- Server version	8.0.41-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `artists`
--

DROP TABLE IF EXISTS `artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artists` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `country` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artists`
--

LOCK TABLES `artists` WRITE;
/*!40000 ALTER TABLE `artists` DISABLE KEYS */;
INSERT INTO `artists` VALUES (1,'The Pop Stars','USA','2025-03-26 18:38:59','2025-03-26 18:38:59'),(2,'Rock Legends','UK','2025-03-26 18:38:59','2025-03-26 18:38:59'),(3,'Electro Beats','Germany','2025-03-26 18:38:59','2025-03-26 18:38:59'),(4,'Jazz Masters','France','2025-03-26 18:38:59','2025-03-26 18:38:59'),(5,'Country Roads','USA','2025-03-26 18:38:59','2025-03-26 18:38:59'),(6,'Taylor Swift','USA','2025-03-26 18:40:49','2025-03-26 18:40:49'),(7,'The Beatles','UK','2025-03-26 18:40:49','2025-03-26 18:40:49'),(8,'Daft Punk','France','2025-03-26 18:40:49','2025-03-26 18:40:49'),(9,'Miles Davis','USA','2025-03-26 18:40:49','2025-03-26 18:40:49'),(10,'Johnny Cash','USA','2025-03-26 18:40:49','2025-03-26 18:40:49'),(11,'Beyoncé','USA','2025-03-26 18:40:49','2025-03-26 18:40:49'),(12,'Queen','UK','2025-03-26 18:40:49','2025-03-26 18:40:49'),(13,'Kendrick Lamar','USA','2025-03-26 18:40:49','2025-03-26 18:40:49'),(14,'Adele','UK','2025-03-26 18:40:49','2025-03-26 18:40:49'),(15,'Coldplay','UK','2025-03-26 18:40:49','2025-03-26 18:40:49'),(16,'Bob Marley & The Wailers','Jamaica','2025-03-26 18:40:49','2025-03-26 18:40:49'),(17,'Ed Sheeran','UK','2025-03-26 18:53:57','2025-03-26 18:53:57'),(18,'Drake','Canada','2025-03-26 18:53:57','2025-03-26 18:53:57'),(19,'The Weeknd','Canada','2025-03-26 18:53:57','2025-03-26 18:53:57'),(20,'Imagine Dragons','USA','2025-03-26 18:53:57','2025-03-26 18:53:57'),(21,'Rihanna','Barbados','2025-03-26 18:53:57','2025-03-26 18:53:57');
/*!40000 ALTER TABLE `artists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genre`
--

DROP TABLE IF EXISTS `genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genre` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre`
--

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES (1,'Pop','2025-03-26 18:39:06'),(2,'Rock','2025-03-26 18:39:06'),(3,'Electronic','2025-03-26 18:39:06'),(4,'Jazz','2025-03-26 18:39:06'),(5,'Country','2025-03-26 18:39:06'),(6,'Pop','2025-03-26 18:40:54'),(7,'Rock','2025-03-26 18:40:54'),(8,'Electronic','2025-03-26 18:40:54'),(9,'Jazz','2025-03-26 18:40:54'),(10,'Country','2025-03-26 18:40:54'),(11,'Hip Hop','2025-03-26 18:40:54'),(12,'R&B','2025-03-26 18:40:54'),(13,'Reggae','2025-03-26 18:40:54');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `listened_logs`
--

DROP TABLE IF EXISTS `listened_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `listened_logs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `song_id` bigint NOT NULL,
  `count` int DEFAULT '1',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `song_id` (`song_id`),
  CONSTRAINT `listened_logs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `listened_logs_ibfk_2` FOREIGN KEY (`song_id`) REFERENCES `songs` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `listened_logs`
--

LOCK TABLES `listened_logs` WRITE;
/*!40000 ALTER TABLE `listened_logs` DISABLE KEYS */;
INSERT INTO `listened_logs` VALUES (1,1,1,3,'2025-03-26 18:39:22'),(2,2,2,1,'2025-03-26 18:39:22'),(3,1,3,2,'2025-03-26 18:39:22'),(4,3,4,5,'2025-03-26 18:39:22'),(5,4,5,1,'2025-03-26 18:39:22'),(6,1,2,1,'2025-03-26 18:39:22'),(7,1,1,5,'2025-03-26 18:50:31'),(8,2,2,2,'2025-03-26 18:50:31'),(9,1,3,3,'2025-03-26 18:50:31'),(10,3,4,1,'2025-03-26 18:50:31'),(11,4,5,7,'2025-03-26 18:50:31'),(12,1,6,2,'2025-03-26 18:50:31'),(13,2,7,4,'2025-03-26 18:50:31'),(14,5,8,1,'2025-03-26 18:50:31'),(15,1,9,6,'2025-03-26 18:50:31'),(16,3,10,3,'2025-03-26 18:50:31'),(17,6,11,2,'2025-03-26 18:50:31'),(18,7,23,4,'2025-03-26 18:56:00'),(19,8,24,1,'2025-03-26 18:56:00'),(20,7,25,3,'2025-03-26 18:56:00'),(21,9,26,2,'2025-03-26 18:56:00'),(22,10,27,5,'2025-03-26 18:56:00'),(23,8,28,1,'2025-03-26 18:56:00'),(24,11,29,2,'2025-03-26 18:56:00'),(25,7,30,3,'2025-03-26 18:56:00');
/*!40000 ALTER TABLE `listened_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `song_artists`
--

DROP TABLE IF EXISTS `song_artists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `song_artists` (
  `song_id` bigint NOT NULL,
  `artist_id` bigint NOT NULL,
  PRIMARY KEY (`song_id`,`artist_id`),
  KEY `artist_id` (`artist_id`),
  CONSTRAINT `song_artists_ibfk_1` FOREIGN KEY (`song_id`) REFERENCES `songs` (`id`) ON DELETE CASCADE,
  CONSTRAINT `song_artists_ibfk_2` FOREIGN KEY (`artist_id`) REFERENCES `artists` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `song_artists`
--

LOCK TABLES `song_artists` WRITE;
/*!40000 ALTER TABLE `song_artists` DISABLE KEYS */;
INSERT INTO `song_artists` VALUES (1,1),(6,1),(2,2),(7,2),(3,3),(4,4),(5,5),(8,6),(19,6),(9,7),(20,7),(10,8),(21,8),(11,9),(22,9),(12,10),(13,11),(14,12),(15,13),(16,14),(17,15),(18,16),(16,17),(21,17),(17,18),(22,18),(18,19),(23,19),(19,20),(20,21);
/*!40000 ALTER TABLE `song_artists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `song_likes`
--

DROP TABLE IF EXISTS `song_likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `song_likes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `song_id` bigint NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`song_id`),
  KEY `song_id` (`song_id`),
  CONSTRAINT `song_likes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `song_likes_ibfk_2` FOREIGN KEY (`song_id`) REFERENCES `songs` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `song_likes`
--

LOCK TABLES `song_likes` WRITE;
/*!40000 ALTER TABLE `song_likes` DISABLE KEYS */;
INSERT INTO `song_likes` VALUES (1,1,1,'2025-03-26 18:39:26'),(2,2,2,'2025-03-26 18:39:26'),(3,1,3,'2025-03-26 18:39:26'),(4,3,1,'2025-03-26 18:39:26'),(5,4,5,'2025-03-26 18:39:26'),(11,1,8,'2025-03-26 18:51:49'),(12,2,9,'2025-03-26 18:51:49'),(13,1,10,'2025-03-26 18:51:49'),(14,3,8,'2025-03-26 18:51:49'),(15,4,12,'2025-03-26 18:51:49'),(16,2,13,'2025-03-26 18:51:49'),(17,5,14,'2025-03-26 18:51:49'),(18,1,16,'2025-03-26 18:51:49'),(19,6,17,'2025-03-26 18:51:49'),(27,8,23,'2025-03-26 18:56:05'),(28,9,24,'2025-03-26 18:56:05'),(29,7,25,'2025-03-26 18:56:05'),(30,10,26,'2025-03-26 18:56:05'),(31,11,27,'2025-03-26 18:56:05'),(32,8,28,'2025-03-26 18:56:05'),(33,9,29,'2025-03-26 18:56:05');
/*!40000 ALTER TABLE `song_likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `songs`
--

DROP TABLE IF EXISTS `songs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `songs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `genre_id` bigint NOT NULL,
  `country` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `genre_id` (`genre_id`),
  CONSTRAINT `songs_ibfk_1` FOREIGN KEY (`genre_id`) REFERENCES `genre` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songs`
--

LOCK TABLES `songs` WRITE;
/*!40000 ALTER TABLE `songs` DISABLE KEYS */;
INSERT INTO `songs` VALUES (1,'Awesome Pop Hit',1,'USA','2025-03-26 18:39:12'),(2,'Classic Rock Anthem',2,'UK','2025-03-26 18:39:12'),(3,'Techno Dance Party',3,'Germany','2025-03-26 18:39:12'),(4,'Smooth Jazz Evening',4,'France','2025-03-26 18:39:12'),(5,'Heartland Ballad',5,'USA','2025-03-26 18:39:12'),(6,'Another Pop Song',1,'USA','2025-03-26 18:39:12'),(7,'Heavy Metal Mania',2,'USA','2025-03-26 18:39:12'),(8,'Shake It Off',1,'USA','2025-03-26 18:41:01'),(9,'Hey Jude',2,'UK','2025-03-26 18:41:01'),(10,'Get Lucky',3,'France','2025-03-26 18:41:01'),(11,'So What',4,'USA','2025-03-26 18:41:01'),(12,'Ring of Fire',5,'USA','2025-03-26 18:41:01'),(13,'Crazy in Love',7,'USA','2025-03-26 18:41:01'),(14,'Bohemian Rhapsody',2,'UK','2025-03-26 18:41:01'),(15,'Humble',6,'USA','2025-03-26 18:41:01'),(16,'Rolling in the Deep',1,'UK','2025-03-26 18:41:01'),(17,'Yellow',2,'UK','2025-03-26 18:41:01'),(18,'No Woman, No Cry',8,'Jamaica','2025-03-26 18:41:01'),(19,'Blank Space',1,'USA','2025-03-26 18:41:01'),(20,'Yesterday',2,'UK','2025-03-26 18:41:01'),(21,'One More Time',3,'France','2025-03-26 18:41:01'),(22,'All Blues',4,'USA','2025-03-26 18:41:01'),(23,'Shape of You',1,'UK','2025-03-26 18:54:05'),(24,'Hotline Bling',6,'Canada','2025-03-26 18:54:05'),(25,'Blinding Lights',3,'Canada','2025-03-26 18:54:05'),(26,'Believer',2,'USA','2025-03-26 18:54:05'),(27,'Umbrella',7,'Barbados','2025-03-26 18:54:05'),(28,'Thinking Out Loud',1,'UK','2025-03-26 18:54:05'),(29,'Gods Plan',6,'Canada','2025-03-26 18:54:05'),(30,'Cant Feel My Face',7,'Canada','2025-03-26 18:54:05');
/*!40000 ALTER TABLE `songs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `country` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Alice Smith','alice.smith@example.com','password123','USA','2025-03-26 18:38:53','2025-03-26 18:38:53'),(2,'Bob Johnson','bob.johnson@example.com','securePass','Canada','2025-03-26 18:38:53','2025-03-26 18:38:53'),(3,'Charlie Brown','charlie.brown@example.com','mySecret','UK','2025-03-26 18:38:53','2025-03-26 18:38:53'),(4,'Diana Miller','diana.miller@example.com','strongPwd','Australia','2025-03-26 18:38:53','2025-03-26 18:38:53'),(5,'Eve Davis','eve.davis@example.com','anotherPwd','France','2025-03-26 18:38:53','2025-03-26 18:38:53'),(6,'John Doe','john.doe@email.com','P@sswOrd123','USA','2025-03-26 18:40:44','2025-03-26 18:40:44'),(7,'Jane Smith','jane.smith@example.net','SecurePwd!','Canada','2025-03-26 18:40:44','2025-03-26 18:40:44'),(8,'Robert Williams','robert.w@mail.co.uk','MySecretKey','UK','2025-03-26 18:40:44','2025-03-26 18:40:44'),(9,'Emily Davis','emily.d@domain.com','StrongerPwd','Australia','2025-03-26 18:40:44','2025-03-26 18:40:44'),(10,'Michael Brown','michael.b@test.org','Another123','France','2025-03-26 18:40:44','2025-03-26 18:40:44'),(11,'Olivia Wilson','olivia.w@email.ca','Password1!','Canada','2025-03-26 18:40:44','2025-03-26 18:40:44'),(12,'David Lee','david.l@email.com','P@ssword1234','USA','2025-03-26 18:53:51','2025-03-26 18:53:51'),(13,'Sarah Clark','sarah.c@example.co.uk','SecurePwd!','UK','2025-03-26 18:53:51','2025-03-26 18:53:51'),(14,'Peter Green','peter.g@mail.fr','MySecretKey','France','2025-03-26 18:53:51','2025-03-26 18:53:51'),(15,'Jessica White','jessica.w@domain.au','StrongerPwd','Australia','2025-03-26 18:53:51','2025-03-26 18:53:51'),(16,'Kevin Taylor','kevin.t@test.ca','Another123','Canada','2025-03-26 18:53:51','2025-03-26 18:53:51');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-28 12:48:27
