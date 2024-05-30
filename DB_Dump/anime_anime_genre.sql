-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: anime
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `anime_genre`
--

DROP TABLE IF EXISTS `anime_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `anime_genre` (
  `id` int NOT NULL AUTO_INCREMENT,
  `anime_id` int DEFAULT NULL,
  `genre_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `anime_id` (`anime_id`),
  CONSTRAINT `anime_genre_ibfk_1` FOREIGN KEY (`anime_id`) REFERENCES `anime` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=428 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anime_genre`
--

LOCK TABLES `anime_genre` WRITE;
/*!40000 ALTER TABLE `anime_genre` DISABLE KEYS */;
INSERT INTO `anime_genre` VALUES (1,2,1),(2,2,2),(3,2,3),(4,2,4),(5,2,5),(6,3,6),(7,3,4),(8,3,5),(9,3,7),(10,3,8),(11,2,7),(12,2,8),(13,2,9),(14,2,10),(15,2,11),(16,3,12),(17,3,10),(18,3,11),(19,3,13),(20,3,14),(21,1,7),(22,1,8),(23,1,9),(24,1,10),(25,1,11),(26,2,12),(27,2,13),(28,2,14),(29,3,15),(30,4,8),(31,4,10),(32,4,11),(33,4,16),(34,5,8),(35,5,11),(36,6,8),(37,6,9),(38,6,10),(39,6,11),(40,6,14),(41,7,9),(42,7,10),(43,7,11),(44,7,13),(45,7,14),(46,8,10),(47,8,11),(48,8,17),(49,8,13),(50,8,16),(51,9,8),(52,9,10),(53,9,11),(54,9,16),(55,10,9),(56,10,10),(57,10,11),(58,10,16),(59,11,7),(60,11,18),(61,11,10),(62,11,19),(63,11,16),(64,12,12),(65,12,9),(66,12,10),(67,12,11),(68,12,20),(69,13,7),(70,13,17),(71,14,8),(72,14,10),(73,14,11),(74,14,21),(75,14,17),(76,15,9),(77,15,10),(78,15,11),(79,15,17),(80,15,16),(81,16,15),(82,16,7),(83,16,18),(84,16,10),(85,16,22),(86,17,10),(87,17,11),(88,17,17),(89,17,23),(90,17,16),(91,18,8),(92,18,9),(93,18,24),(94,18,25),(95,19,10),(96,19,11),(97,19,17),(98,19,13),(99,19,16),(100,20,26),(101,21,7),(102,21,21),(103,21,23),(104,21,27),(105,22,7),(106,22,9),(107,22,10),(108,22,16),(109,23,8),(110,23,9),(111,23,10),(112,23,11),(113,23,16),(114,24,7),(115,24,9),(116,24,10),(117,25,8),(118,25,10),(119,25,11),(120,25,17),(121,25,16),(122,26,24),(123,26,21),(124,26,23),(125,27,7),(126,27,24),(127,27,11),(128,27,25),(129,27,28),(130,28,15),(131,28,7),(132,28,18),(133,28,29),(134,28,30),(135,29,17),(136,29,31),(137,29,27),(138,30,8),(139,30,9),(140,30,10),(141,30,11),(142,30,13),(143,31,12),(144,31,10),(145,31,11),(146,31,13),(147,31,14),(148,32,8),(149,32,11),(150,32,17),(151,33,7),(152,33,9),(153,33,10),(154,33,11),(155,33,16),(156,34,15),(157,34,7),(158,34,12),(159,35,8),(160,35,17),(161,35,31),(162,35,27),(163,36,8),(164,36,10),(165,36,11),(166,36,16),(167,37,9),(168,37,10),(169,37,11),(170,37,21),(171,37,23),(172,38,7),(173,38,17),(174,38,27),(175,38,14),(176,39,12),(177,39,9),(178,39,10),(179,39,11),(180,39,32),(181,40,15),(182,40,7),(183,40,12),(184,40,9),(185,40,10),(186,41,8),(187,41,24),(188,41,11),(189,41,33),(190,41,14),(191,42,21),(192,42,17),(193,43,12),(194,43,9),(195,43,11),(196,43,34),(197,43,14),(198,44,34),(199,44,27),(200,44,14),(201,45,7),(202,45,11),(203,45,17),(204,45,14),(205,46,8),(206,46,9),(207,46,18),(208,46,29),(209,46,11),(210,47,7),(211,47,8),(212,47,9),(213,47,24),(214,47,11),(215,48,9),(216,48,10),(217,48,11),(218,48,16),(219,48,14),(220,49,9),(221,49,10),(222,49,11),(223,49,16),(224,50,9),(225,50,10),(226,50,11),(227,50,16),(228,51,15),(229,51,7),(230,51,8),(231,51,11),(232,51,32),(233,52,9),(234,52,35),(235,52,10),(236,52,11),(237,52,19),(238,53,8),(239,53,17),(240,53,31),(241,53,27),(242,54,24),(243,54,11),(244,54,36),(245,55,9),(246,55,10),(247,55,11),(248,56,9),(249,56,35),(250,56,10),(251,56,11),(252,56,16),(253,57,8),(254,57,10),(255,57,21),(256,57,23),(257,57,16),(258,58,8),(259,58,9),(260,58,10),(261,58,17),(262,58,13),(263,59,15),(264,59,18),(265,59,29),(266,59,24),(267,59,10),(268,60,10),(269,60,11),(270,60,16),(271,60,14),(272,61,7),(273,61,18),(274,61,24),(275,61,11),(276,61,19),(277,62,7),(278,62,18),(279,62,22),(280,62,11),(281,63,8),(282,63,9),(283,63,10),(284,63,11),(285,63,13),(286,64,10),(287,64,21),(288,64,17),(289,64,16),(290,65,7),(291,65,8),(292,65,9),(293,65,10),(294,65,22),(295,66,7),(296,66,37),(297,66,14),(298,67,8),(299,67,9),(300,67,10),(301,67,11),(302,67,16),(303,68,7),(304,68,18),(305,68,17),(306,68,36),(307,69,9),(308,69,10),(309,69,11),(310,69,16),(311,70,10),(312,70,23),(313,70,16),(314,70,31),(315,71,7),(316,71,8),(317,71,10),(318,71,17),(319,71,31),(320,72,8),(321,72,35),(322,72,27),(323,73,12),(324,73,8),(325,73,10),(326,73,11),(327,73,32),(328,74,10),(329,74,11),(330,74,16),(331,75,8),(332,75,9),(333,75,10),(334,75,11),(335,75,23),(336,76,10),(337,76,11),(338,76,21),(339,76,23),(340,76,16),(341,77,15),(342,77,12),(343,77,8),(344,77,10),(345,77,11),(346,78,8),(347,78,9),(348,78,10),(349,78,11),(350,79,7),(351,79,12),(352,79,9),(353,79,11),(354,80,7),(355,80,9),(356,80,10),(357,80,11),(358,80,23),(359,81,15),(360,81,7),(361,81,24),(362,82,7),(363,82,9),(364,82,29),(365,82,10),(366,82,22),(367,83,8),(368,83,10),(369,83,11),(370,83,21),(371,83,17),(372,84,7),(373,84,8),(374,84,9),(375,84,10),(376,84,22),(377,85,8),(378,85,10),(379,85,11),(380,85,21),(381,85,16),(382,86,9),(383,86,10),(384,86,11),(385,87,24),(386,87,10),(387,87,11),(388,87,14),(389,88,8),(390,88,17),(391,88,23),(392,88,27),(393,89,10),(394,89,11),(395,89,17),(396,89,23),(397,89,16),(398,90,10),(399,90,11),(400,90,16),(401,90,27),(402,90,14),(403,91,8),(404,91,10),(405,91,13),(406,91,27),(407,91,14),(408,92,10),(409,92,11),(410,92,16),(411,93,8),(412,93,9),(413,93,10),(414,94,8),(415,94,9),(416,94,10),(417,94,11),(418,94,16),(419,95,7),(420,95,17),(421,96,8),(422,96,10),(423,96,16),(424,96,33),(425,15,7),(426,15,18),(427,15,19);
/*!40000 ALTER TABLE `anime_genre` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-30 17:59:50