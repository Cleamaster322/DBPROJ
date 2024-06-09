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
-- Table structure for table `anime_licensed`
--

DROP TABLE IF EXISTS `anime_licensed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `anime_licensed` (
  `id` int NOT NULL AUTO_INCREMENT,
  `anime_id` int DEFAULT NULL,
  `licensed_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `anime_id` (`anime_id`),
  CONSTRAINT `anime_licensed_ibfk_1` FOREIGN KEY (`anime_id`) REFERENCES `anime` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anime_licensed`
--

LOCK TABLES `anime_licensed` WRITE;
/*!40000 ALTER TABLE `anime_licensed` DISABLE KEYS */;
INSERT INTO `anime_licensed` VALUES (1,1,1),(2,1,2),(3,1,3),(4,2,2),(5,2,4),(6,2,3),(7,3,3),(8,4,3),(9,5,3),(10,6,4),(11,6,1),(12,8,3),(13,8,2),(14,12,3),(15,12,1),(16,14,5),(17,17,2),(18,17,3),(19,17,1),(20,18,3),(21,19,3),(22,20,3),(23,25,6),(24,28,3),(25,29,3),(26,31,2),(27,31,3),(28,33,2),(29,33,3),(30,34,4),(31,35,3),(32,37,3),(33,40,6),(34,40,1),(35,41,7),(36,41,1),(37,43,1),(38,45,4),(39,46,2),(40,46,3),(41,48,3),(42,50,4),(43,51,4),(44,52,3),(45,53,3),(46,54,4),(47,55,8),(48,56,2),(49,56,3),(50,57,4),(51,58,6),(52,59,2),(53,59,4),(54,59,1),(55,62,2),(56,63,2),(57,63,4),(58,64,9),(59,64,4),(60,64,1),(61,65,6),(62,66,6),(63,68,4),(64,68,8),(65,72,3),(66,74,2),(67,74,3),(68,78,6),(69,83,10),(70,83,4),(71,83,1),(72,87,9),(73,87,1),(74,89,11),(75,89,4),(76,89,1),(77,89,8),(78,92,2),(79,92,3),(80,93,3),(81,93,2),(82,100,3),(83,102,12);
/*!40000 ALTER TABLE `anime_licensed` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-09 14:56:49
