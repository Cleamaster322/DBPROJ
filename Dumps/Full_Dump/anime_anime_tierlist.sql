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
-- Table structure for table `anime_tierlist`
--

DROP TABLE IF EXISTS `anime_tierlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `anime_tierlist` (
  `id` int NOT NULL AUTO_INCREMENT,
  `anime_id` int DEFAULT NULL,
  `ratingSiteOne` int DEFAULT NULL,
  `ratingSiteTwo` int DEFAULT NULL,
  `ratingSiteThree` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `anime_id` (`anime_id`),
  CONSTRAINT `anime_tierlist_ibfk_1` FOREIGN KEY (`anime_id`) REFERENCES `anime` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=258 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anime_tierlist`
--

LOCK TABLES `anime_tierlist` WRITE;
/*!40000 ALTER TABLE `anime_tierlist` DISABLE KEYS */;
INSERT INTO `anime_tierlist` VALUES (1,1,1,58,87),(2,2,2,4,NULL),(3,3,3,6,NULL),(4,4,4,3,NULL),(5,5,5,NULL,NULL),(6,6,6,93,NULL),(7,7,7,NULL,NULL),(8,8,8,NULL,NULL),(9,9,9,96,NULL),(10,10,10,NULL,NULL),(11,11,11,51,1),(12,12,12,14,NULL),(13,13,13,NULL,NULL),(14,14,14,NULL,NULL),(15,15,15,19,NULL),(16,16,16,86,NULL),(17,17,17,18,NULL),(18,18,18,NULL,NULL),(19,19,19,NULL,NULL),(20,20,20,37,NULL),(21,21,21,NULL,NULL),(22,22,22,NULL,NULL),(23,23,23,60,NULL),(24,24,24,39,71),(25,25,25,32,NULL),(26,26,26,NULL,NULL),(27,27,27,NULL,NULL),(28,28,28,NULL,NULL),(29,29,29,NULL,NULL),(30,30,30,NULL,NULL),(31,31,31,NULL,NULL),(32,32,32,NULL,NULL),(33,33,33,NULL,NULL),(34,34,34,NULL,NULL),(35,35,35,23,NULL),(36,36,36,97,3),(37,37,37,NULL,NULL),(38,38,38,NULL,NULL),(39,39,39,NULL,NULL),(40,40,40,NULL,NULL),(41,41,41,NULL,NULL),(42,42,42,NULL,NULL),(43,43,43,NULL,NULL),(44,44,44,5,NULL),(45,45,45,NULL,NULL),(46,46,46,13,NULL),(47,47,47,NULL,NULL),(48,48,48,NULL,NULL),(49,49,49,NULL,NULL),(50,50,50,NULL,NULL),(51,51,51,8,NULL),(52,52,52,NULL,NULL),(53,53,53,NULL,NULL),(54,54,54,NULL,NULL),(55,55,55,NULL,NULL),(56,56,56,NULL,NULL),(57,57,57,NULL,NULL),(58,58,58,NULL,NULL),(59,59,59,NULL,NULL),(60,60,60,NULL,NULL),(61,61,61,NULL,NULL),(62,62,62,NULL,NULL),(63,63,63,NULL,NULL),(64,64,64,NULL,NULL),(65,65,65,NULL,NULL),(66,66,66,NULL,NULL),(67,67,67,NULL,NULL),(68,68,68,NULL,NULL),(69,69,69,NULL,NULL),(70,70,70,NULL,NULL),(71,71,71,NULL,22),(72,72,72,NULL,NULL),(73,73,73,90,NULL),(74,74,74,NULL,NULL),(75,75,75,NULL,NULL),(76,76,76,NULL,NULL),(77,77,77,NULL,NULL),(78,78,78,NULL,NULL),(79,79,79,NULL,NULL),(80,80,80,99,NULL),(81,81,81,NULL,NULL),(82,82,82,NULL,NULL),(83,83,83,17,NULL),(84,84,84,NULL,NULL),(85,85,85,NULL,NULL),(86,86,86,NULL,NULL),(87,87,87,NULL,NULL),(88,88,88,66,NULL),(89,89,89,NULL,NULL),(90,90,90,94,NULL),(91,91,91,NULL,NULL),(92,92,92,NULL,NULL),(93,93,93,NULL,NULL),(94,94,94,NULL,NULL),(95,95,95,NULL,NULL),(96,96,96,NULL,NULL),(97,97,97,NULL,NULL),(98,98,98,NULL,NULL),(99,99,99,NULL,41),(100,100,100,NULL,NULL),(101,101,101,NULL,NULL),(102,102,102,NULL,NULL),(103,103,NULL,1,NULL),(104,104,NULL,2,15),(105,105,NULL,7,NULL),(106,106,NULL,9,NULL),(107,107,NULL,10,NULL),(108,108,NULL,11,NULL),(109,109,NULL,12,NULL),(110,110,NULL,15,NULL),(111,111,NULL,16,19),(112,112,NULL,20,NULL),(113,113,NULL,21,NULL),(114,114,NULL,22,NULL),(115,115,NULL,24,NULL),(116,116,NULL,25,NULL),(117,117,NULL,26,NULL),(118,118,NULL,27,NULL),(119,119,NULL,28,NULL),(120,120,NULL,29,26),(121,121,NULL,30,NULL),(122,122,NULL,31,NULL),(123,123,NULL,33,NULL),(124,124,NULL,34,NULL),(125,125,NULL,35,NULL),(126,126,NULL,36,NULL),(127,127,NULL,38,NULL),(128,128,NULL,40,NULL),(129,129,NULL,41,NULL),(130,130,NULL,42,NULL),(131,131,NULL,43,NULL),(132,132,NULL,44,NULL),(133,133,NULL,45,NULL),(134,134,NULL,46,NULL),(135,135,NULL,47,NULL),(136,136,NULL,48,14),(137,137,NULL,49,NULL),(138,138,NULL,50,NULL),(139,139,NULL,52,NULL),(140,140,NULL,53,NULL),(141,141,NULL,54,2),(142,142,NULL,55,NULL),(143,143,NULL,56,NULL),(144,144,NULL,57,NULL),(145,145,NULL,59,NULL),(146,146,NULL,61,28),(147,147,NULL,62,NULL),(148,148,NULL,63,NULL),(149,149,NULL,64,NULL),(150,150,NULL,65,65),(151,151,NULL,67,NULL),(152,152,NULL,68,NULL),(153,153,NULL,69,NULL),(154,154,NULL,70,NULL),(155,155,NULL,71,4),(156,156,NULL,72,NULL),(157,157,NULL,73,NULL),(158,158,NULL,74,NULL),(159,159,NULL,75,36),(160,160,NULL,76,NULL),(161,161,NULL,77,NULL),(162,162,NULL,78,NULL),(163,163,NULL,79,NULL),(164,164,NULL,80,5),(165,165,NULL,81,NULL),(166,166,NULL,82,NULL),(167,167,NULL,83,NULL),(168,168,NULL,84,96),(169,169,NULL,85,NULL),(170,170,NULL,87,NULL),(171,171,NULL,88,16),(172,172,NULL,89,NULL),(173,173,NULL,91,NULL),(174,174,NULL,92,NULL),(175,175,NULL,95,29),(176,176,NULL,98,NULL),(177,177,NULL,100,8),(178,178,NULL,NULL,6),(179,179,NULL,NULL,7),(180,180,NULL,NULL,9),(181,181,NULL,NULL,10),(182,182,NULL,NULL,11),(183,183,NULL,NULL,12),(184,184,NULL,NULL,13),(185,185,NULL,NULL,17),(186,186,NULL,NULL,18),(187,187,NULL,NULL,20),(188,188,NULL,NULL,21),(189,189,NULL,NULL,23),(190,190,NULL,NULL,24),(191,191,NULL,NULL,25),(192,192,NULL,NULL,27),(193,193,NULL,NULL,30),(194,194,NULL,NULL,31),(195,195,NULL,NULL,32),(196,196,NULL,NULL,33),(197,197,NULL,NULL,34),(198,198,NULL,NULL,35),(199,199,NULL,NULL,37),(200,200,NULL,NULL,38),(201,201,NULL,NULL,39),(202,202,NULL,NULL,40),(203,203,NULL,NULL,42),(204,204,NULL,NULL,43),(205,205,NULL,NULL,44),(206,206,NULL,NULL,45),(207,207,NULL,NULL,46),(208,208,NULL,NULL,47),(209,209,NULL,NULL,48),(210,210,NULL,NULL,49),(211,211,NULL,NULL,50),(212,212,NULL,NULL,51),(213,213,NULL,NULL,52),(214,214,NULL,NULL,53),(215,215,NULL,NULL,54),(216,216,NULL,NULL,55),(217,217,NULL,NULL,56),(218,218,NULL,NULL,57),(219,219,NULL,NULL,58),(220,220,NULL,NULL,59),(221,221,NULL,NULL,60),(222,222,NULL,NULL,61),(223,223,NULL,NULL,62),(224,224,NULL,NULL,63),(225,225,NULL,NULL,64),(226,226,NULL,NULL,66),(227,227,NULL,NULL,67),(228,228,NULL,NULL,68),(229,229,NULL,NULL,69),(230,230,NULL,NULL,70),(231,231,NULL,NULL,72),(232,232,NULL,NULL,73),(233,233,NULL,NULL,74),(234,234,NULL,NULL,75),(235,235,NULL,NULL,76),(236,236,NULL,NULL,77),(237,237,NULL,NULL,78),(238,238,NULL,NULL,79),(239,239,NULL,NULL,80),(240,240,NULL,NULL,81),(241,241,NULL,NULL,82),(242,242,NULL,NULL,83),(243,243,NULL,NULL,84),(244,244,NULL,NULL,85),(245,245,NULL,NULL,86),(246,246,NULL,NULL,88),(247,247,NULL,NULL,89),(248,248,NULL,NULL,90),(249,249,NULL,NULL,91),(250,250,NULL,NULL,92),(251,251,NULL,NULL,93),(252,252,NULL,NULL,94),(253,253,NULL,NULL,95),(254,254,NULL,NULL,97),(255,255,NULL,NULL,98),(256,256,NULL,NULL,99),(257,257,NULL,NULL,100);
/*!40000 ALTER TABLE `anime_tierlist` ENABLE KEYS */;
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