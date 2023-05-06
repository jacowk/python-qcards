-- MySQL dump 10.19  Distrib 10.3.38-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: qcards
-- ------------------------------------------------------
-- Server version	10.3.38-MariaDB-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_bookmark`
--

DROP TABLE IF EXISTS `t_bookmark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_bookmark` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `stack_id` int(6) DEFAULT NULL,
  `card_id` int(6) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `create_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `last_modified_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_bookmark`
--

LOCK TABLES `t_bookmark` WRITE;
/*!40000 ALTER TABLE `t_bookmark` DISABLE KEYS */;
INSERT INTO `t_bookmark` VALUES (1,1,-1,0,'2023-04-17 16:28:05','2023-04-17 16:28:05'),(2,-1,4,1,'2023-04-17 16:31:09','2023-04-17 16:31:09'),(3,-1,9,1,'2023-04-17 16:30:39','2023-04-17 16:30:39');
/*!40000 ALTER TABLE `t_bookmark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_card`
--

DROP TABLE IF EXISTS `t_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_card` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `summary` varchar(100) DEFAULT NULL,
  `front_content` varchar(200) DEFAULT NULL,
  `back_content` varchar(1000) DEFAULT NULL,
  `stack_id` int(6) DEFAULT NULL,
  `view_count` int(6) DEFAULT NULL,
  `group_cd` int(6) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `last_view_date` timestamp NULL DEFAULT NULL,
  `create_date` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `last_modified_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_card`
--

LOCK TABLES `t_card` WRITE;
/*!40000 ALTER TABLE `t_card` DISABLE KEYS */;
INSERT INTO `t_card` VALUES (1,'Creational Patterns','Abstract Factory Pattern (87)','Provide an interface from creating families of related or dependent objects without specifying their concrete classes.\n',1,0,1,1,NULL,'2023-05-05 21:59:21','2023-05-05 22:00:42'),(2,'Creational Patterns','Factory Method Pattern (107)','Define an interface for creating an object, but let subclasses decide which class to instantiate. Defer instantiation to subclasses.\n',1,0,1,1,NULL,'2023-05-05 21:59:21','2023-05-05 22:00:51'),(3,'Creational Patterns','Builder Pattern (97)','Separate the construction of a complex object from its representation so that the same construction process can create different representations.\n',1,0,1,1,NULL,'2023-05-05 21:59:21','2023-05-05 22:01:15'),(4,'Creational Patterns','Prototype Pattern (117)','Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.\n',1,0,1,1,NULL,'2023-05-05 21:59:21','2023-05-05 22:01:22'),(5,'Creational Patterns','Singleton Pattern (127)','Ensure a class only has one instance, and provide a global point of access to it.\n',1,0,1,1,NULL,'2023-05-05 21:59:21','2023-05-05 22:01:28'),(6,'Structural Patterns','Adapter Pattern (139)','Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn\'t otherwise, because of incompatible interfaces',2,0,1,1,NULL,'2023-05-05 21:59:44','2023-05-05 21:59:44'),(7,'Structural Patterns','Bridge Pattern (151)','Decouple an abstraction from it\'s implementation so that the two can vary independently',2,0,1,1,NULL,'2023-05-05 21:59:44','2023-05-05 21:59:44'),(8,'Structural Patterns','Composite Pattern (163)','Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.',2,0,1,1,NULL,'2023-05-05 21:59:44','2023-05-05 21:59:44'),(9,'Structural Patterns','Decorator Pattern (175)','Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.',2,0,1,1,NULL,'2023-05-05 21:59:44','2023-05-05 21:59:44'),(10,'Structural Patterns','Facade Pattern (185)','Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.',2,0,1,1,NULL,'2023-05-05 21:59:44','2023-05-05 21:59:44'),(11,'Structural Patterns','Flyweight Pattern (195)','Use sharing to support large numbers of fine-grained objects efficiently.',2,0,1,1,NULL,'2023-05-05 21:59:44','2023-05-05 21:59:44'),(12,'Structural Patterns','Proxy Pattern (207)','Provide a surrogate or placeholder for another object to control access to it.',2,0,1,1,NULL,'2023-05-05 21:59:45','2023-05-05 21:59:45'),(13,'Behavioral Patterns','Chain of Responsibility (223)','Avoid coupling the sender of a request to it\'s receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.',3,0,1,1,NULL,'2023-05-05 22:00:00','2023-05-05 22:00:00'),(14,'Behavioral Patterns','Command (233)','Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.',3,0,1,1,NULL,'2023-05-05 22:00:00','2023-05-05 22:00:00'),(15,'Behavioral Patterns','Interpreter (243)','Given a language, define a representation for it\'s grammar along with an interpreter that uses the representation to interpret sentences in the language.',3,0,1,1,NULL,'2023-05-05 22:00:00','2023-05-05 22:00:00'),(16,'Behavioral Patterns','Iterator (257)','Provide a way to access the elements of an aggregate object sequentially without exposing it\'s underlying representation.',3,0,1,1,NULL,'2023-05-05 22:00:00','2023-05-05 22:00:00'),(17,'Behavioral Patterns','Mediator (273)','Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and lets you vary their interaction independently.',3,0,1,1,NULL,'2023-05-05 22:00:00','2023-05-05 22:00:00'),(18,'Behavioral Patterns','Memento (283)','Without violating encapsulation, capture and externalize an object\'s internal state, so that the object can be restored to this state later.',3,0,1,1,NULL,'2023-05-05 22:00:00','2023-05-05 22:00:00'),(19,'Behavioral Patterns','Observer (293)','Define a one-to-many dependency between objects so that when one object changes state, all it\'s dependents are notified and updated automatically.',3,0,1,1,NULL,'2023-05-05 22:00:00','2023-05-05 22:00:00'),(20,'Behavioral Patterns','State (305)','Allow an object to alter it\'s behaviour when it\'s internal state changes. The object will appear to change it\'s class.',3,0,1,1,NULL,'2023-05-05 22:00:00','2023-05-05 22:00:00'),(21,'Behavioral Patterns','Stragety (315)','Define a family of algorithms, encapsulate each one, and make them interchangeable. Stragegy lets the algorithm vary independently from clients tha use it.',3,0,1,1,NULL,'2023-05-05 22:00:00','2023-05-05 22:00:00'),(22,'Behavioral Patterns','Template Method (325)','Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template method lets subclasses redefine certain steps of an algorithm, without changing the algorithm\'s stucture.',3,0,1,1,NULL,'2023-05-05 22:00:00','2023-05-05 22:00:00'),(23,'Behavioral Patterns','Visitor (331)','Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation, without changing the classes of the elements on which it operates.',3,0,1,1,NULL,'2023-05-05 22:00:01','2023-05-05 22:00:01'),(24,'Gateway Definition','Gateway (466)','An object that encapsulates access to an external system or resource.',4,0,1,1,NULL,'2023-05-06 09:36:46','2023-05-06 09:36:46'),(25,'Mapper Definition','Mapper (473)','An object that sets up a communication between two independent objects.',4,0,1,1,NULL,'2023-05-06 09:36:46','2023-05-06 09:36:46'),(26,'Layer Supertype Definition','Layer Supertype (475)','A type that acts as the supertype for all types in its layer.',4,0,1,1,NULL,'2023-05-06 09:36:46','2023-05-06 09:36:46'),(27,'Separated Interface Definition','Separated Interface (476)','Defines an interface in a separate package from its implementation.',4,0,1,1,NULL,'2023-05-06 09:36:46','2023-05-06 09:36:46'),(28,'Registry Definition','Registry (480)','A well-known object that other objects can use to find common objects and services.',4,0,1,1,NULL,'2023-05-06 09:36:46','2023-05-06 09:36:46'),(29,'Value Object Definition','Value Object (486)','A small simple object, like money or a date range, whose equality isn\'t based on identity.',4,0,1,1,NULL,'2023-05-06 09:36:46','2023-05-06 09:36:46'),(30,'Money Definition','Money (488)','Represents a monetary value.',4,0,1,1,NULL,'2023-05-06 09:36:46','2023-05-06 09:36:46'),(31,'Special Case Definition','Special Case (496)','A subclass that provides special behavior for particular cases.',4,0,1,1,NULL,'2023-05-06 09:36:46','2023-05-06 09:36:46'),(32,'Plugin Definition','Plugin (499)','Links classes during configuration rather than compilation.',4,0,1,1,NULL,'2023-05-06 09:36:46','2023-05-06 09:36:46'),(33,'Service Stub Definition','Service Stub (504)','Removes dependence upon problematic services during testing. WSDL',4,0,1,1,NULL,'2023-05-06 09:36:46','2023-05-06 09:36:46'),(34,'Record Set Definition','Record Set (508)','An in-memory representation of tabular data.',4,0,1,1,NULL,'2023-05-06 09:36:46','2023-05-06 09:36:46'),(35,'Table Data Gateway Definition','Table Data Gateway (144)','An object that acts as a Gateway (466) to a database table. One instance handles all the rows in the table.',6,0,1,1,NULL,'2023-05-06 09:38:02','2023-05-06 09:38:02'),(36,'Row Data Gateway Definition','Row Data Gateway (152)','An object that acts as a Gateway (466) to a single record in a data source. There is one instance per row.',6,0,1,1,NULL,'2023-05-06 09:38:02','2023-05-06 09:38:02'),(37,'Active Record Definition','Active Record (160)','An object that wraps a row in a database table or view, encapsulates the database access, and adds domain logic on that data.',6,0,1,1,NULL,'2023-05-06 09:38:02','2023-05-06 09:38:02'),(38,'Data Mapper Definition','Data Mapper (165)','A layer of Mappers (473) that moves data between objects and a database while keeping them independent of each other and the mapper itself.',6,0,1,1,NULL,'2023-05-06 09:38:02','2023-05-06 09:38:02'),(39,'Remote Facade Definition','Remote Facade (388)','Provides a coarse-grained facade on fine-grained objects to improve efficiency over a network.',11,0,1,1,NULL,'2023-05-06 09:39:19','2023-05-06 09:39:19'),(40,'Data Transfer Object Definition','Data Transfer Object (401)','An object that carries data between processes in order to reduce the number of method calls.',11,0,1,1,NULL,'2023-05-06 09:39:19','2023-05-06 09:39:19'),(41,'Transaction Script Definition','Transaction Script (110)','Organizes business logic by procedures where each procedure handles a single request from the presentation.',5,0,1,1,NULL,'2023-05-06 09:39:37','2023-05-06 09:39:37'),(42,'Domain Model Definition','Domain Model (116)','An object model of the domain that incorporates both behavior and data.',5,0,1,1,NULL,'2023-05-06 09:39:37','2023-05-06 09:39:37'),(43,'Table Module Definition','Table Module (125)','A single instance that handles the business logic for all rows in a database table or view.',5,0,1,1,NULL,'2023-05-06 09:39:37','2023-05-06 09:39:37'),(44,'Service Layer Definition','Service Layer (133)','Defines an application\'s boundary with a layer of services that establishes a set of available operations and coordinates the application\'s response in each operation.',5,0,1,1,NULL,'2023-05-06 09:39:37','2023-05-06 09:39:37'),(45,'Unit of Work Definition','Unit of Work (184)','Maintains a list of objects affected by a business transaction and coordinates the writing out of changes and the resolution of concurrency problems.',7,0,1,1,NULL,'2023-05-06 09:41:30','2023-05-06 09:41:30'),(46,'Identity Map Definition','Identity Map (195)','Ensures that each object gets loaded only once by keeping every loaded object in a map. Looks up objects using the map when referring to them.',7,0,1,1,NULL,'2023-05-06 09:41:30','2023-05-06 09:41:30'),(47,'Lazy Load Definition','Lazy Load (200)','An object that doesn\'t contain all of the data you need but knows how to get it.',7,0,1,1,NULL,'2023-05-06 09:41:30','2023-05-06 09:41:30'),(48,'Metadata Mapping Definition','Metadata Mapping (306)','Holds details of object-relational mapping in metadata.',9,0,1,1,NULL,'2023-05-06 09:42:24','2023-05-06 09:42:24'),(49,'Query Object Definition','Query Object (316)','An object that represents a database query.',9,0,1,1,NULL,'2023-05-06 09:42:24','2023-05-06 09:42:24'),(50,'Repository Definition','Repository (322)','Mediates between the domain and data mapping layers using a collection-like interface for accessing domain objects.',9,0,1,1,NULL,'2023-05-06 09:42:24','2023-05-06 09:42:24'),(51,'Identity Field Definition','Identity Field (216)','Saves a database ID field in an object to maintain identity between an in-memory object and a database row.',8,0,1,1,NULL,'2023-05-06 09:42:42','2023-05-06 09:42:42'),(52,'Foreign Key Mapping Definition','Foreign Key Mapping (236)','Maps an association between objects to a foreign key reference between tables.',8,0,1,1,NULL,'2023-05-06 09:42:42','2023-05-06 09:42:42'),(53,'Association Table Mapping Definition','Association Table Mapping (248)','Saves an association as a table with foreign keys to the tables that are linked by the association.',8,0,1,1,NULL,'2023-05-06 09:42:42','2023-05-06 09:42:42'),(54,'Dependent Mapping Definition','Dependent Mapping (262)','Has one class perform the database mapping for a child class.',8,0,1,1,NULL,'2023-05-06 09:42:42','2023-05-06 09:42:42'),(55,'Embedded Value Definition','Embedded Value (268)','Maps an object into several fields of another object\'s table.',8,0,1,1,NULL,'2023-05-06 09:42:42','2023-05-06 09:42:42'),(56,'Serialized LOB Definition','Serialized LOB (272)','Saves a graph of objects by serializing them into a single large object (LOB), which it stores in a database field.',8,0,1,1,NULL,'2023-05-06 09:42:42','2023-05-06 09:42:42'),(57,'Single Table Inheritance Definition','Single Table Inheritance (278)','Represents an inheritance hierarchy of classes as a single table that has columns for all the fields of the various classes.',8,0,1,1,NULL,'2023-05-06 09:42:42','2023-05-06 09:42:42'),(58,'Class Table Inheritance Definition','Class Table Inheritance (285)','Represents an inheritance hierarchy of classes with one table for each class.',8,0,1,1,NULL,'2023-05-06 09:42:42','2023-05-06 09:42:42'),(59,'Concrete Table Inheritance Definition','Concrete Table Inheritance (293)','Represents an inheritance hierarchy of classes with one table per concrete class in the hierarchy.',8,0,1,1,NULL,'2023-05-06 09:42:42','2023-05-06 09:42:42'),(60,'Inheritance Mappers Definition','Inheritance Mappers (302)','A structure to organize database mappers that handle inheritance hierarchies.',8,0,1,1,NULL,'2023-05-06 09:42:43','2023-05-06 09:42:43'),(61,'Optimistic Offline Lock Definition','Optimistic Offline Lock (416)','Prevents conflicts between concurrent business transactions by detecting a conflict and rolling back the transaction.',12,0,1,1,NULL,'2023-05-06 09:43:02','2023-05-06 09:43:02'),(62,'Pessimistic Offline Lock Definition','Pessimistic Offline Lock (426)','Prevents conflicts between concurrent business transactions by allowing only one business transaction at a time to access data.',12,0,1,1,NULL,'2023-05-06 09:43:02','2023-05-06 09:43:02'),(63,'Coarse Grained Lock Definition','Coarse Grained Lock (438)','Locks a set of related objects with a single lock.',12,0,1,1,NULL,'2023-05-06 09:43:02','2023-05-06 09:43:02'),(64,'Implicit Lock Definition','Implicit Lock (449)','Allows framework or layer supertype code to acquire offline locks.',12,0,1,1,NULL,'2023-05-06 09:43:02','2023-05-06 09:43:02'),(65,'Client Session State Definition','Client Session State (456)','Stores session state on the client.',13,0,1,1,NULL,'2023-05-06 09:43:26','2023-05-06 09:43:26'),(66,'Server Session State Definition','Server Session State (458)','Keeps the session state on a server system in a serialized form',13,0,1,1,NULL,'2023-05-06 09:43:26','2023-05-06 09:43:26'),(67,'Database Session State Definition','Database Session State (462)','Stores session data as committed data in the database.',13,0,1,1,NULL,'2023-05-06 09:43:26','2023-05-06 09:43:26'),(68,'Model View Controller Definition','Model View Controller (330)','Splits user interface interaction into three distinct roles.',10,0,1,1,NULL,'2023-05-06 09:43:54','2023-05-06 09:43:54'),(69,'Page Controller Definition','Page Controller (333)','An object that handles a request for a specific page or action on a Web site.',10,0,1,1,NULL,'2023-05-06 09:43:54','2023-05-06 09:43:54'),(70,'Front Controller Definition','Front Controller (344)','A controller that handles all requests for a Web site.',10,0,1,1,NULL,'2023-05-06 09:43:54','2023-05-06 09:43:54'),(71,'Template View Definition','Template View (350)','Renders information into HTML by embedding markers in an HTML page.',10,0,1,1,NULL,'2023-05-06 09:43:54','2023-05-06 09:43:54'),(72,'Transform View Definition','Transform View (361)','A view that processes domain data element by element and transforms it into HTML.',10,0,1,1,NULL,'2023-05-06 09:43:54','2023-05-06 09:43:54'),(73,'Two-Step View Definition','Two-Step View (365)','Turns domain data into HTML in two steps: first by forming some kind of logical page, then rendering the logical page into HTML.',10,0,1,1,NULL,'2023-05-06 09:43:54','2023-05-06 09:43:54'),(74,'Application Controller Definition','Application Controller (379)','A centralized point for handling screen navigation and the flow of an application.',10,0,1,1,NULL,'2023-05-06 09:43:54','2023-05-06 09:43:54'),(75,'File Transfer','How can I integrate multiple applications so that they work together and can exchange information?','Have each application produce files containing information that other applications need to consume. Integrators take the responsibility of transforming files into different formats. Produce the files at regular intervals according to the nature of the business.',14,0,1,1,NULL,'2023-05-06 09:56:52','2023-05-06 09:56:52'),(76,'Shared Database','How can I integrate multiple applications so that they work together and can exchange information?','Integrate applications by having them store their data in a single Shared Database.',14,0,1,1,NULL,'2023-05-06 09:56:52','2023-05-06 09:56:52'),(77,'Remote Procedure Invocation','How can I integrate multiple applications so that they work together and can exchange information?','Develop each application as a large-scale object or component with encapsulated data. Provide an interface to allow other applications to interact with the running application.',14,0,1,1,NULL,'2023-05-06 09:56:52','2023-05-06 09:56:52'),(78,'Messaging','How can I integrate multiple applications so that they work together and can exchange information?','Use Messaging to transfer packets of data frequently, immediately, reliably, and asynchronously, using customizable formats.',14,0,1,1,NULL,'2023-05-06 09:56:52','2023-05-06 09:56:52');
/*!40000 ALTER TABLE `t_card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_category`
--

DROP TABLE IF EXISTS `t_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_category` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  `parent_id` int(6) DEFAULT NULL,
  `active` tinyint(4) DEFAULT NULL,
  `create_date` timestamp NULL DEFAULT NULL,
  `last_modified_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_category`
--

LOCK TABLES `t_category` WRITE;
/*!40000 ALTER TABLE `t_category` DISABLE KEYS */;
INSERT INTO `t_category` VALUES (1,'Software Development',NULL,1,'2023-05-05 21:51:42','2023-05-05 21:51:42'),(2,'Design Patterns',1,1,'2023-05-05 21:52:04','2023-05-05 21:52:04'),(3,'Gang of Four Design Patterns',2,1,'2023-05-05 21:52:37','2023-05-05 21:52:37'),(4,'Patterns of Enterprise Application Architecture',NULL,1,'2023-05-06 09:28:10','2023-05-06 09:28:10'),(5,'EAA Definitions',4,1,'2023-05-06 09:30:06','2023-05-06 09:30:06'),(6,'Enterprise Integration Patterns',NULL,1,'2023-05-06 09:49:58','2023-05-06 09:49:58'),(7,'EIP Definitions',6,1,'2023-05-06 09:50:14','2023-05-06 09:50:14');
/*!40000 ALTER TABLE `t_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_lookup_group`
--

DROP TABLE IF EXISTS `t_lookup_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_lookup_group` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_lookup_group`
--

LOCK TABLES `t_lookup_group` WRITE;
/*!40000 ALTER TABLE `t_lookup_group` DISABLE KEYS */;
INSERT INTO `t_lookup_group` VALUES (1,'Front'),(2,'Middle'),(3,'Back');
/*!40000 ALTER TABLE `t_lookup_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_lookup_odd_even`
--

DROP TABLE IF EXISTS `t_lookup_odd_even`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_lookup_odd_even` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_lookup_odd_even`
--

LOCK TABLES `t_lookup_odd_even` WRITE;
/*!40000 ALTER TABLE `t_lookup_odd_even` DISABLE KEYS */;
INSERT INTO `t_lookup_odd_even` VALUES (1,'Odd'),(2,'Even');
/*!40000 ALTER TABLE `t_lookup_odd_even` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_lookup_review_stage`
--

DROP TABLE IF EXISTS `t_lookup_review_stage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_lookup_review_stage` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_lookup_review_stage`
--

LOCK TABLES `t_lookup_review_stage` WRITE;
/*!40000 ALTER TABLE `t_lookup_review_stage` DISABLE KEYS */;
INSERT INTO `t_lookup_review_stage` VALUES (1,'Daily'),(2,'Every other day'),(3,'Weekly'),(4,'Monthly');
/*!40000 ALTER TABLE `t_lookup_review_stage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_lookup_weekday`
--

DROP TABLE IF EXISTS `t_lookup_weekday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_lookup_weekday` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_lookup_weekday`
--

LOCK TABLES `t_lookup_weekday` WRITE;
/*!40000 ALTER TABLE `t_lookup_weekday` DISABLE KEYS */;
INSERT INTO `t_lookup_weekday` VALUES (1,'Monday'),(2,'Tuesday'),(3,'Wednesday'),(4,'Thursday'),(5,'Friday'),(6,'Saturday'),(7,'Sunday');
/*!40000 ALTER TABLE `t_lookup_weekday` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_review_stage`
--

DROP TABLE IF EXISTS `t_review_stage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_review_stage` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `stack_id` int(6) DEFAULT NULL,
  `review_stage_cd` int(6) DEFAULT NULL,
  `odd_even_cd` int(6) DEFAULT NULL,
  `weekday_cd` int(6) DEFAULT NULL,
  `week_count` int(6) DEFAULT NULL,
  `calendar_day` int(6) DEFAULT NULL,
  `month_count` int(6) DEFAULT NULL,
  `create_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `last_modified_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_review_stage`
--

LOCK TABLES `t_review_stage` WRITE;
/*!40000 ALTER TABLE `t_review_stage` DISABLE KEYS */;
INSERT INTO `t_review_stage` VALUES (1,1,1,-1,-1,-1,-1,-1,'2023-05-05 22:03:08','2023-05-05 22:03:08'),(2,2,1,-1,-1,-1,-1,-1,'2023-05-05 22:03:11','2023-05-05 22:03:11'),(3,3,1,-1,-1,-1,-1,-1,'2023-05-05 22:03:14','2023-05-05 22:03:14');
/*!40000 ALTER TABLE `t_review_stage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_stack`
--

DROP TABLE IF EXISTS `t_stack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_stack` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `description` varchar(100) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `source` varchar(300) DEFAULT NULL,
  `category_id` int(6) DEFAULT NULL,
  `next_view_date` date DEFAULT NULL,
  `create_date` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `last_modified_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_stack`
--

LOCK TABLES `t_stack` WRITE;
/*!40000 ALTER TABLE `t_stack` DISABLE KEYS */;
INSERT INTO `t_stack` VALUES (1,'Creational Patterns',1,'Gang of Four Design Patterns book',3,NULL,'2023-05-05 21:53:40','2023-05-05 21:57:22'),(2,'Structural Patterns',1,'Gang of Four Design Patterns book',3,NULL,'2023-05-05 21:54:16','2023-05-05 21:57:30'),(3,'Behavioural Design Patterns',1,'Gang of Four Design Patterns book',3,NULL,'2023-05-05 21:54:43','2023-05-05 21:57:11'),(4,'Base Patterns',0,'https://martinfowler.com/eaaCatalog/',5,NULL,'2023-05-06 09:30:52','2023-05-06 09:30:52'),(5,'Domain Logic Patterns',0,'https://martinfowler.com/eaaCatalog/',5,NULL,'2023-05-06 09:31:46','2023-05-06 09:31:46'),(6,'Data Source Architectural Patterns',0,'https://martinfowler.com/eaaCatalog/',5,NULL,'2023-05-06 09:32:31','2023-05-06 09:32:31'),(7,'Object-Relational Behavioral Patterns',0,'https://martinfowler.com/eaaCatalog/',5,NULL,'2023-05-06 09:33:05','2023-05-06 09:33:05'),(8,'Object-Relational Structural Patterns',0,'https://martinfowler.com/eaaCatalog/',5,NULL,'2023-05-06 09:33:26','2023-05-06 09:33:26'),(9,'Object-Relational Metadata Mapping Patterns',0,'https://martinfowler.com/eaaCatalog/',5,NULL,'2023-05-06 09:33:49','2023-05-06 09:33:49'),(10,'Web Presentation Patterns',0,'https://martinfowler.com/eaaCatalog/',5,NULL,'2023-05-06 09:35:18','2023-05-06 09:35:18'),(11,'Distribution Patterns',0,'https://martinfowler.com/eaaCatalog/',5,NULL,'2023-05-06 09:35:34','2023-05-06 09:35:34'),(12,'Offline Concurrency Patterns',0,'https://martinfowler.com/eaaCatalog/',5,NULL,'2023-05-06 09:35:51','2023-05-06 09:35:51'),(13,'Session State Patterns',0,'https://martinfowler.com/eaaCatalog/',5,NULL,'2023-05-06 09:36:12','2023-05-06 09:36:12'),(14,'Integration Styles',0,'https://www.enterpriseintegrationpatterns.com/',7,NULL,'2023-05-06 09:50:40','2023-05-06 09:50:40'),(15,'Messaging Systems',0,'https://www.enterpriseintegrationpatterns.com/',7,NULL,'2023-05-06 09:51:03','2023-05-06 09:51:03'),(16,'Messaging Channels',0,'https://www.enterpriseintegrationpatterns.com/',7,NULL,'2023-05-06 09:51:23','2023-05-06 09:51:23'),(17,'Message Construction',0,'https://www.enterpriseintegrationpatterns.com/',7,NULL,'2023-05-06 09:51:40','2023-05-06 09:51:40'),(18,'Message Routing',0,'https://www.enterpriseintegrationpatterns.com/',7,NULL,'2023-05-06 09:52:01','2023-05-06 09:52:01'),(19,'Message Transformation',0,'https://www.enterpriseintegrationpatterns.com/',7,NULL,'2023-05-06 09:52:18','2023-05-06 09:52:18'),(20,'Messaging Endpoints',0,'https://www.enterpriseintegrationpatterns.com/',7,NULL,'2023-05-06 09:52:35','2023-05-06 09:52:35'),(21,'System Management',0,'https://www.enterpriseintegrationpatterns.com/',7,NULL,'2023-05-06 09:52:58','2023-05-06 09:52:58');
/*!40000 ALTER TABLE `t_stack` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-06 12:05:13
