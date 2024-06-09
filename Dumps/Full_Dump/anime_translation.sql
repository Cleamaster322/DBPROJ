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
-- Table structure for table `translation`
--

DROP TABLE IF EXISTS `translation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `translation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=274 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `translation`
--

LOCK TABLES `translation` WRITE;
/*!40000 ALTER TABLE `translation` DISABLE KEYS */;
INSERT INTO `translation` VALUES (1,'Animedia'),(2,'Shachiburi'),(3,'VoiceHub'),(4,'Persona99'),(5,'Shikoku Studio'),(6,'Studio Band'),(7,'AniDUB'),(8,'OPRUS'),(9,'2x2'),(10,'Субтитры'),(11,'AniFilm'),(12,'TVShows'),(13,'AniStar'),(14,'Amazing Dubbing'),(15,'SHIZA Project'),(16,'AniMaunt'),(17,'AniLibria'),(18,'AniBoom'),(19,'Cringedub'),(20,'MedusaSub.Subtitles'),(21,'Wakanim.Subtitles'),(22,'Crunchyroll'),(23,'Onibaku'),(24,'Shiroi Kitsune'),(25,'Inari Studio'),(26,'AnimeVost'),(27,'JAM'),(28,'Jisedai'),(29,'AniRise'),(30,'KANSAI Studio'),(31,'LE-Production'),(32,'КОМНАТА ДИДИ'),(33,'HaronMedia'),(34,'Ушастая озвучка'),(35,'DubClub'),(36,'NekoVoice'),(37,'New Land Studio'),(38,'Dream Cast'),(39,'OnWave'),(40,'youmiteru'),(41,'AniNyaTV'),(42,'AniPLague'),(43,'Anything Group'),(44,'AnimeJet'),(45,'SEKAI PROJECT'),(46,'Буханка.TV'),(47,'AniMovie'),(48,'TAKEOVER Project'),(49,'Freedub Studio'),(50,'J&N Union'),(51,'AniPlay Studio'),(52,'EVA'),(53,'Crunchyroll.Subtitles'),(54,'Ушастая озвучка.Subtitles'),(55,'AniRise.Subtitles'),(56,'СВ-Дубль'),(57,'Мега-Аниме'),(58,'2D-DUB'),(59,'KrioDub'),(60,'SENU Project'),(61,'VOX-S'),(62,'FumoDub'),(63,'Youkai Studio'),(64,'AEROChannelEkat'),(65,'Fronda Studio'),(66,'AniClub'),(67,'Kazoku Project'),(68,'MifFan'),(69,'AniJoy'),(70,'AniDorFilm'),(71,'Akame'),(72,'FaulyDub'),(73,'Head Pack Films'),(74,'Кладбище топовых релизов'),(75,'ReVoice'),(76,'FNDP'),(77,'BanderYmka'),(78,'NoNameDUB Project'),(79,'Вистерия'),(80,'DOBROVOICE'),(81,'Flarrow Films'),(82,'Невинный Кружок'),(83,'Crimson Star Voice'),(84,'BAZA Band'),(85,'LampStudio'),(86,'NoMi Dub'),(87,'AniRai'),(88,'SillyCat Studio'),(89,'AniLeague.TV'),(90,'ShadowVoice'),(91,'DUBляжники'),(92,'AniBreeze.Subtitles'),(93,'Kazoku Project.Subtitles'),(94,'FSG Sanae.Subtitles'),(95,'AniBaza'),(96,'Sergei Vasya'),(97,'Silver AniAge'),(98,'Naikō.Subtitles'),(99,'RadiantVoice'),(100,'MoonWalkers'),(101,'Brees Club'),(102,'Amber'),(103,'Оканэ'),(104,'LDA TEAM'),(105,'HeatSound'),(106,'GrandStudio'),(107,'HORIZON'),(108,'AniVi'),(109,'Ancord'),(110,'ТО Дубляжная'),(111,'IIITUKATUPKA'),(112,'ПВА ШОУ & Anton Shanteau'),(113,'AEROChannelEkat & Risha'),(114,'CelestialDub'),(115,'AniDub Online'),(116,'Onigiri'),(117,'Люб. Многоголосый'),(118,'FSG YakuSub Studio.Subtitles'),(119,'NIGHT VOICE'),(120,'AniBreeze'),(121,'ОВН'),(122,'TimaMan & Milirina'),(123,'AniDorFilm & AniDub Online'),(124,'AniFame'),(125,'Bezdari Sound'),(126,'LazDub'),(127,'ChillDub'),(128,'SoftBox'),(129,'STEPonee'),(130,'Reanimedia'),(131,'ADStudio'),(132,'3df voice'),(133,'Kalabs Studio'),(134,'MiraiDUB'),(135,'AniLane'),(136,'SAYGEX'),(137,'ArrowHell'),(138,'HDrezka Studio'),(139,'NewComers'),(140,'VOICEDUB'),(141,'Risens Team'),(142,'OBELISK Project'),(143,'KaenDub'),(144,'Dragon\'s Lair & GrandStudio'),(145,'ibadub'),(146,'VDub'),(147,'AniLauba'),(148,'RokuDub'),(149,'РуАниме / DEEP'),(150,'РуАниме / DEEP.Subtitles'),(151,'KerobTV'),(152,'Leviafilm'),(153,'Swimming Cat'),(154,'SubVost.Subtitles'),(155,'VERSO'),(156,'Дар Судьбы'),(157,'DM Project'),(158,'SovetRomantica.Subtitles'),(159,'Get Smart Group'),(160,'Studio Band & Wakanim'),(161,'ConeVoice'),(162,'AniLibria.Subtitles'),(163,'Amaivon'),(164,'AniVersal'),(165,'Творческая студия МИР'),(166,'Akame.Subtitles'),(167,'DejzDub'),(168,'Zetflix'),(169,'Netflix.Subtitles'),(170,'Anton Shanteau'),(171,'Animy'),(172,'ПВА ШОУ'),(173,'Aniharu'),(174,'Дублированный'),(175,'AlexFilm'),(176,'Люб. Двухголосый'),(177,'Мосфильм'),(178,'YouNet Translate'),(179,'FSG Younet Translate.Subtitles'),(180,'Aniraccoon'),(181,'Flavius Studio'),(182,'AniPlay'),(183,'Менталитет'),(184,'Kazuttx'),(185,'Omori'),(186,'Red Head Sound & Studio Band'),(187,'Xala.Project'),(188,'AniCosmic'),(189,'AniCrystal'),(190,'AniCosmic 18+'),(191,'Сербин'),(192,'KitsuneBox'),(193,'Milirina'),(194,'NewStation'),(195,'LightFamily'),(196,'Trina_D & Rizz_Fisher'),(197,'LostFilm'),(198,'Anything Group & DubClub'),(199,'AniLibria.TV 18+'),(200,'SHIZA Project 18+'),(201,'RuDub'),(202,'КОМНАТА ДИДИ (Альтернативная)'),(203,'AniSense'),(204,'Wakanim'),(205,'animereactor'),(206,'AniPlay.Subtitles'),(207,'OpenDub'),(208,'MC Entertainment'),(209,'The Cult Of Sound'),(210,'The Voice Company'),(211,'Animegroup'),(212,'VoiceLand'),(213,'Arlimax'),(214,'OneSound Band'),(215,'VokiDoki'),(216,'AniLot'),(217,'Sad Kit'),(218,'Light Family.Subtitles'),(219,'Alisma.Subtitles'),(220,'INSOMNIA Studio'),(221,'AniStarks'),(222,'Евгения Лурье'),(223,'AniMax'),(224,'Cuba77'),(225,'GoLTFilm'),(226,'foxwave'),(227,'Asura Project'),(228,'AlFair Studio'),(229,'AniLibria.TV'),(230,'AniBar'),(231,'AniJoy.Subtitles'),(232,'KoeKak'),(233,'Kansai'),(234,'ТО Bamboo'),(235,'AniStar Многоголосый'),(236,'AniRaid / Naoka & Sedrix'),(237,'Eladiel & Zendos'),(238,'AniHero'),(239,'Force Media'),(240,'AniPlay & Get Smart Group'),(241,'Пекарня «Папин хлеб»'),(242,'ДИК - Правильная озвучка'),(243,'Jamix'),(244,'Inter Voices'),(245,'Erlach studios'),(246,'Дубляжная'),(247,'Digga Dubbing'),(248,'GrickVoice'),(249,'Паноптикум'),(250,'AniBar & Studiinet'),(251,'KALGAZM'),(252,'SEIU CLUB'),(253,'Reanimedia.Subtitles'),(254,'ZoneVision'),(255,'Дубляжники'),(256,'RBCDub'),(257,'HotVoice 41'),(258,'Проф. Многоголосый'),(259,'AniMani.TV'),(260,'CalliopeHouse'),(261,'GoldFilm'),(262,'Важный Гусь'),(263,'Kawaii.TV'),(264,'KawaiiTV'),(265,'Yamoturo Sound'),(266,'Заговорщики'),(267,'Студия \"ПИП\"'),(268,'Persona99 & MaxDamage'),(269,'Манипулятор.Subtitles'),(270,'VF-Studio'),(271,'AniDUB Online & Ушастая озвучка'),(272,'2x2 New'),(273,'ANI.OMNIA');
/*!40000 ALTER TABLE `translation` ENABLE KEYS */;
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
