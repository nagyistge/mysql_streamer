CREATE TABLE `business` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `acxiom_id` int(11) DEFAULT NULL,
  `name` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address1` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address2` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address3` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL,
  `city` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `county` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `state` varchar(3) COLLATE utf8_unicode_ci DEFAULT NULL,
  `country` varchar(2) COLLATE utf8_unicode_ci DEFAULT NULL,
  `zip` varchar(12) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `fax` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `url` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `flags` int(11) NOT NULL DEFAULT '0',
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `accuracy` double DEFAULT NULL,
  `time_created` int(11) NOT NULL DEFAULT '0',
  `score` double DEFAULT NULL,
  `rating` double DEFAULT NULL,
  `review_count` int(11) NOT NULL DEFAULT '0',
  `photo_id` int(11) DEFAULT NULL,
  `alias` varchar(96) COLLATE utf8_unicode_ci DEFAULT NULL,
  `geoquad` int(10) unsigned DEFAULT NULL,
  `data_source_type` tinyint(3) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `zip` (`zip`,`phone`),
  KEY `longitude` (`longitude`,`latitude`),
  KEY `phone` (`phone`),
  KEY `review_count` (`review_count`),
  KEY `geoquad` (`geoquad`)
) ENGINE=InnoDB AUTO_INCREMENT=31854197 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;