-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLE
-- DE REQUETES MYSQL
-- Database: sabani_eltion_expi1a_dump_i164

-- Destruction de la BD si elle existe.
-- Pour être certain d'avoir la dernière version des données

DROP DATABASE IF EXISTS sabani_eltion_expi1a_dump_i164;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS sabani_eltion_expi1a_dump_i164;

-- Utilisation de cette base de donnée

USE sabani_eltion_expi1a_dump_i164;

-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.30 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour sabani_eltion_expi1a_dump_i164
DROP DATABASE IF EXISTS `sabani_eltion_expi1a_dump_i164`;
CREATE DATABASE IF NOT EXISTS `sabani_eltion_expi1a_dump_i164` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `sabani_eltion_expi1a_dump_i164`;

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_budget
DROP TABLE IF EXISTS `t_budget`;
CREATE TABLE IF NOT EXISTS `t_budget` (
  `ID_Budget` int NOT NULL AUTO_INCREMENT,
  `Montant_total` decimal(20,6) DEFAULT NULL,
  `Depense` decimal(20,6) DEFAULT NULL,
  `Montant_restant` decimal(20,6) DEFAULT NULL,
  `FK_chantier` int DEFAULT NULL,
  PRIMARY KEY (`ID_Budget`),
  KEY `FK_chantier` (`FK_chantier`),
  CONSTRAINT `FK_t_budget_t_chantier` FOREIGN KEY (`FK_chantier`) REFERENCES `t_chantier` (`ID_Chantier`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_budget : ~5 rows (environ)
INSERT INTO `t_budget` (`ID_Budget`, `Montant_total`, `Depense`, `Montant_restant`, `FK_chantier`) VALUES
	(1, 12500.000000, 2500.000000, 10000.000000, 1),
	(2, 20000.000000, 5500.000000, 14500.000000, 3),
	(3, 5000.000000, 3000.000000, 2000.000000, 5),
	(4, 30000.000000, 25000.000000, 5000.000000, 2),
	(5, 15000.000000, 7500.000000, 7500.000000, 4);

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_chantier
DROP TABLE IF EXISTS `t_chantier`;
CREATE TABLE IF NOT EXISTS `t_chantier` (
  `ID_Chantier` int NOT NULL AUTO_INCREMENT,
  `Rue` varchar(30) DEFAULT NULL,
  `Cp` mediumint DEFAULT NULL,
  `Ville` varchar(85) DEFAULT NULL,
  `Etage` tinyint DEFAULT NULL,
  `Pays` varchar(30) DEFAULT NULL,
  `Date_debut` date DEFAULT NULL,
  `Date_fin` date DEFAULT NULL,
  `Statut` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`ID_Chantier`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_chantier : ~5 rows (environ)
INSERT INTO `t_chantier` (`ID_Chantier`, `Rue`, `Cp`, `Ville`, `Etage`, `Pays`, `Date_debut`, `Date_fin`, `Statut`) VALUES
	(1, 'Route du Bois 23', 1024, 'ecublens', 3, 'Suisse', '2024-03-01', '2025-05-11', 'En cours'),
	(2, 'Chemin de la fôret 5', 1024, 'Ecublens', 1, 'Suisse', '2023-12-01', '2024-01-07', 'Termine'),
	(3, 'Avenue de Sévelin 18', 1004, 'Lausanne', 5, 'Suisse', '2024-05-22', '2024-06-14', 'En attente'),
	(4, 'Route de Lully 5c', 1131, 'Tolochenaz', 1, 'Suisse', '2024-04-12', '2024-05-05', 'Termine'),
	(5, 'Route de Genève 22', 1033, 'Cheseaux-sur-lausanne', 4, 'Suisse', '2024-02-21', '2024-06-05', 'En cours');

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_chantier_materiel
DROP TABLE IF EXISTS `t_chantier_materiel`;
CREATE TABLE IF NOT EXISTS `t_chantier_materiel` (
  `ID_chantier_materiel` int NOT NULL AUTO_INCREMENT,
  `FK_chantier_materiel` int DEFAULT NULL,
  `FK_materiel_chantier` int DEFAULT NULL,
  PRIMARY KEY (`ID_chantier_materiel`),
  KEY `FK_chantier_materiel` (`FK_chantier_materiel`),
  KEY `FK_materiel_chantier` (`FK_materiel_chantier`),
  CONSTRAINT `FK_t_chantier_materiel_t_chantier` FOREIGN KEY (`FK_chantier_materiel`) REFERENCES `t_chantier` (`ID_Chantier`),
  CONSTRAINT `FK_t_chantier_materiel_t_materiel` FOREIGN KEY (`FK_materiel_chantier`) REFERENCES `t_materiel` (`ID_Materiel`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_chantier_materiel : ~9 rows (environ)
INSERT INTO `t_chantier_materiel` (`ID_chantier_materiel`, `FK_chantier_materiel`, `FK_materiel_chantier`) VALUES
	(1, 1, 1),
	(2, 1, 3),
	(3, 2, 3),
	(4, 2, 4),
	(5, 3, 6),
	(7, 4, 2),
	(8, 4, 5),
	(9, 5, 2),
	(10, 5, 4);

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_chantier_tache
DROP TABLE IF EXISTS `t_chantier_tache`;
CREATE TABLE IF NOT EXISTS `t_chantier_tache` (
  `ID_chantier_tache` int NOT NULL AUTO_INCREMENT,
  `FK_chantier_tache` int DEFAULT NULL,
  `FK_tache_chantier` int DEFAULT NULL,
  PRIMARY KEY (`ID_chantier_tache`),
  KEY `FK_chantier_tache` (`FK_chantier_tache`),
  KEY `FK_tache_chantier` (`FK_tache_chantier`),
  CONSTRAINT `FK_t_chantier_tache_t_chantier` FOREIGN KEY (`FK_chantier_tache`) REFERENCES `t_chantier` (`ID_Chantier`),
  CONSTRAINT `FK_t_chantier_tache_t_tache` FOREIGN KEY (`FK_tache_chantier`) REFERENCES `t_tache` (`ID_Tache`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_chantier_tache : ~5 rows (environ)
INSERT INTO `t_chantier_tache` (`ID_chantier_tache`, `FK_chantier_tache`, `FK_tache_chantier`) VALUES
	(1, 3, 1),
	(2, 2, 2),
	(3, 4, 5),
	(4, 1, 4),
	(5, 5, 3);

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_employe
DROP TABLE IF EXISTS `t_employe`;
CREATE TABLE IF NOT EXISTS `t_employe` (
  `ID_Employe` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(90) DEFAULT NULL,
  `Prenom` varchar(40) DEFAULT NULL,
  `Date_de_naissance` date DEFAULT NULL,
  `Numero_AVS` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Notoriete` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`ID_Employe`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_employe : ~10 rows (environ)
INSERT INTO `t_employe` (`ID_Employe`, `Nom`, `Prenom`, `Date_de_naissance`, `Numero_AVS`, `Notoriete`) VALUES
	(1, 'Dupont', 'Lucas', '1978-05-15', '999.6238.8216.63', 'Chef d\'equipe'),
	(2, 'Araha', 'Sophie', '1998-08-21', '999.4637.6832.98', 'Ouvrier'),
	(3, 'sheini', 'Max', '1976-11-06', '999.2775.9206.83', 'Chef d\'equipe'),
	(4, 'Fischer', 'Emma', '1991-07-27', '999.7665.9811.32', 'Ouvrier'),
	(5, 'Meier', 'David', '1983-04-09', '999.3319.4165.10', 'Chef d\'equipe'),
	(6, 'Mansour', 'rihra', '1982-03-08', '999.1574.5709.99', 'Ouvrier'),
	(7, 'Aretou', 'Albion', '1979-06-28', '999.3163.1404.26', 'Chef d\'equipe'),
	(8, 'Bonkari', 'Luk', '1969-03-01', '999.8575.8571.54', 'Ouvrier'),
	(9, 'Marah', 'Kaelle', '1989-11-29', '999.4897.1613.98', 'Chef d\'equipe'),
	(10, 'Boyka', 'Abigaelle', '1971-08-19', '999.6123.5693.92', 'Ouvrier');

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_employe_chantier
DROP TABLE IF EXISTS `t_employe_chantier`;
CREATE TABLE IF NOT EXISTS `t_employe_chantier` (
  `ID_employe_chantier` int NOT NULL AUTO_INCREMENT,
  `FK_employe_chantier` int DEFAULT NULL,
  `FK_chantier_employe` int DEFAULT NULL,
  PRIMARY KEY (`ID_employe_chantier`) USING BTREE,
  KEY `FK_chantier_ouvrier` (`FK_chantier_employe`) USING BTREE,
  KEY `FK_ouvrier_chantier` (`FK_employe_chantier`) USING BTREE,
  CONSTRAINT `FK_t_chantier_employe_t_chantier` FOREIGN KEY (`FK_chantier_employe`) REFERENCES `t_chantier` (`ID_Chantier`),
  CONSTRAINT `FK_t_chantier_employe_t_employe` FOREIGN KEY (`FK_employe_chantier`) REFERENCES `t_employe` (`ID_Employe`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_employe_chantier : ~10 rows (environ)
INSERT INTO `t_employe_chantier` (`ID_employe_chantier`, `FK_employe_chantier`, `FK_chantier_employe`) VALUES
	(1, 1, 1),
	(2, 2, 1),
	(3, 3, 2),
	(4, 4, 2),
	(5, 5, 3),
	(6, 6, 3),
	(7, 7, 4),
	(8, 8, 4),
	(9, 9, 5),
	(10, 10, 5);

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_employe_mail
DROP TABLE IF EXISTS `t_employe_mail`;
CREATE TABLE IF NOT EXISTS `t_employe_mail` (
  `ID_employe_mail` int NOT NULL AUTO_INCREMENT,
  `FK_employe_mail` int DEFAULT NULL,
  `FK_mail_employe` int DEFAULT NULL,
  `FK_type_mail` int DEFAULT NULL,
  PRIMARY KEY (`ID_employe_mail`),
  KEY `employe_mail` (`FK_employe_mail`),
  KEY `mail_employe` (`FK_mail_employe`),
  KEY `FK_type_mail` (`FK_type_mail`),
  CONSTRAINT `FK_t_employe_mail_t_employe` FOREIGN KEY (`FK_employe_mail`) REFERENCES `t_employe` (`ID_Employe`),
  CONSTRAINT `FK_t_employe_mail_t_mail` FOREIGN KEY (`FK_mail_employe`) REFERENCES `t_mail` (`ID_Mail`),
  CONSTRAINT `FK_t_employe_mail_t_type_mail` FOREIGN KEY (`FK_type_mail`) REFERENCES `t_type_mail` (`ID_type_mail`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_employe_mail : ~20 rows (environ)
INSERT INTO `t_employe_mail` (`ID_employe_mail`, `FK_employe_mail`, `FK_mail_employe`, `FK_type_mail`) VALUES
	(1, 1, 1, 1),
	(2, 1, 2, 2),
	(3, 2, 3, 1),
	(4, 2, 4, 2),
	(5, 3, 5, 1),
	(6, 3, 6, 2),
	(7, 4, 7, 1),
	(8, 4, 8, 2),
	(9, 5, 9, 1),
	(10, 5, 10, 2),
	(11, 6, 11, 1),
	(12, 6, 12, 2),
	(13, 7, 13, 1),
	(14, 7, 14, 2),
	(15, 8, 15, 1),
	(16, 8, 16, 2),
	(17, 9, 17, 1),
	(18, 9, 18, 2),
	(19, 10, 19, 1),
	(20, 10, 20, 2);

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_employe_numero
DROP TABLE IF EXISTS `t_employe_numero`;
CREATE TABLE IF NOT EXISTS `t_employe_numero` (
  `ID_employe_numero` int NOT NULL AUTO_INCREMENT,
  `FK_employe_numero` int DEFAULT NULL,
  `FK_numero_employe` int DEFAULT NULL,
  `FK_type_numero` int DEFAULT NULL,
  PRIMARY KEY (`ID_employe_numero`),
  KEY `FK_employe_numero` (`FK_employe_numero`),
  KEY `FK_numero_employe` (`FK_numero_employe`),
  KEY `FK_type_numero` (`FK_type_numero`),
  CONSTRAINT `FK_t_employe_numero_t_employe` FOREIGN KEY (`FK_employe_numero`) REFERENCES `t_employe` (`ID_Employe`),
  CONSTRAINT `FK_t_employe_numero_t_numero_telephone` FOREIGN KEY (`FK_numero_employe`) REFERENCES `t_numero_telephone` (`ID_Numero_telephone`),
  CONSTRAINT `FK_t_employe_numero_t_type_numero` FOREIGN KEY (`FK_type_numero`) REFERENCES `t_type_numero` (`ID_type_numero`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_employe_numero : ~20 rows (environ)
INSERT INTO `t_employe_numero` (`ID_employe_numero`, `FK_employe_numero`, `FK_numero_employe`, `FK_type_numero`) VALUES
	(1, 1, 1, 1),
	(2, 1, 2, 2),
	(3, 2, 3, 1),
	(4, 2, 4, 2),
	(5, 3, 5, 1),
	(6, 3, 6, 2),
	(7, 4, 7, 1),
	(8, 4, 8, 2),
	(9, 5, 9, 1),
	(10, 5, 10, 2),
	(11, 6, 11, 1),
	(12, 6, 12, 2),
	(13, 7, 13, 1),
	(14, 7, 14, 2),
	(15, 8, 15, 1),
	(16, 8, 16, 2),
	(17, 9, 17, 1),
	(18, 9, 18, 2),
	(19, 10, 19, 1),
	(20, 10, 20, 2);

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_employe_tache
DROP TABLE IF EXISTS `t_employe_tache`;
CREATE TABLE IF NOT EXISTS `t_employe_tache` (
  `ID_employe_tache` int NOT NULL AUTO_INCREMENT,
  `FK_employe_tache` int DEFAULT NULL,
  `FK_tache_employe` int DEFAULT NULL,
  PRIMARY KEY (`ID_employe_tache`) USING BTREE,
  KEY `FK_ouvrier_tache` (`FK_employe_tache`) USING BTREE,
  KEY `FK_tache_ouvrier` (`FK_tache_employe`) USING BTREE,
  CONSTRAINT `FK_t_employe_tache_t_employe` FOREIGN KEY (`FK_employe_tache`) REFERENCES `t_employe` (`ID_Employe`),
  CONSTRAINT `FK_t_employe_tache_t_tache` FOREIGN KEY (`FK_tache_employe`) REFERENCES `t_tache` (`ID_Tache`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_employe_tache : ~5 rows (environ)
INSERT INTO `t_employe_tache` (`ID_employe_tache`, `FK_employe_tache`, `FK_tache_employe`) VALUES
	(1, 1, 4),
	(2, 3, 2),
	(3, 5, 1),
	(4, 7, 5),
	(5, 9, 3);

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_fournisseur
DROP TABLE IF EXISTS `t_fournisseur`;
CREATE TABLE IF NOT EXISTS `t_fournisseur` (
  `ID_Fournisseur` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(90) DEFAULT NULL,
  `Prenom` varchar(40) DEFAULT NULL,
  `Numero_AVS` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Mail_professionnel` varchar(320) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Telephone_professionnel` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`ID_Fournisseur`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_fournisseur : ~5 rows (environ)
INSERT INTO `t_fournisseur` (`ID_Fournisseur`, `Nom`, `Prenom`, `Numero_AVS`, `Mail_professionnel`, `Telephone_professionnel`) VALUES
	(1, 'Charteau', 'Jacob', '999.5248.8317.54', 'charteau.jacob@entreprise.com', '+41 88 894 77 80'),
	(2, 'Porac', 'Foueda', '999.6245.7459.61', 'porac.foueda@entreprise.com', '+41 37 303 35 95'),
	(3, 'Roli', 'Alissia', '999.8709.8542.12', 'roli.alissia@entreprise.com', '+41 32 938 77 45'),
	(4, 'Zeqiri', 'Artiola', '999.5620.4875.45', 'zeqiri.artiola@entreprise.com', '+41 21 811 52 37'),
	(5, 'Sarbacan', 'Xhem', '999.0953.1501.34', 'sarbacan.xhem@entreprise.com', '+41 68 302 23 79');

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_mail
DROP TABLE IF EXISTS `t_mail`;
CREATE TABLE IF NOT EXISTS `t_mail` (
  `ID_Mail` int NOT NULL AUTO_INCREMENT,
  `Mail` varchar(320) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`ID_Mail`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=189 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_mail : ~20 rows (environ)
INSERT INTO `t_mail` (`ID_Mail`, `Mail`) VALUES
	(1, 'lucas.dupont@entreprise.com'),
	(2, 'lucasdupont@hotmail.com'),
	(3, 'sophie.araha@entreprise.com'),
	(4, 'sophiearaha@hotmail.com'),
	(5, 'max.sheini@entreprise.com'),
	(6, 'maxsheini@hotmail.com'),
	(7, 'emma.fischer@entreprise.com'),
	(8, 'emmafischer@hotmail.com'),
	(9, 'david.meier@entreprise.com'),
	(10, 'davidmeier@hotmail.com'),
	(11, 'rihra.mansour@entreprise.com'),
	(12, 'rihramansour@hotmail.com'),
	(13, 'albion.aretou@entreprise.com'),
	(14, 'albionaretou@hotmail.com'),
	(15, 'luk.bonkari@entreprise.com'),
	(16, 'lukbonkari@hotmail.com'),
	(17, 'kaelle.marah@entreprise.com'),
	(18, 'kaellemarah@hotmail.com'),
	(19, 'abigaelle.boyka@entreprise.com'),
	(20, 'abigaelleboyka@hotmail.com');

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_materiel
DROP TABLE IF EXISTS `t_materiel`;
CREATE TABLE IF NOT EXISTS `t_materiel` (
  `ID_Materiel` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(36) DEFAULT NULL,
  `Quantite_disponible` smallint DEFAULT NULL,
  PRIMARY KEY (`ID_Materiel`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_materiel : ~6 rows (environ)
INSERT INTO `t_materiel` (`ID_Materiel`, `Nom`, `Quantite_disponible`) VALUES
	(1, 'Disjoncteur', 15),
	(2, 'Generateur', 6),
	(3, 'Marteau de macon', 57),
	(4, 'Fusible', 22),
	(5, 'Marteau de menusier', 46),
	(6, 'Led', 146);

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_materiel_fournisseur
DROP TABLE IF EXISTS `t_materiel_fournisseur`;
CREATE TABLE IF NOT EXISTS `t_materiel_fournisseur` (
  `ID_materiel_fournisseur` int NOT NULL AUTO_INCREMENT,
  `FK_fournisseur_materiel` int DEFAULT NULL,
  `FK_materiel_fournisseur` int DEFAULT NULL,
  PRIMARY KEY (`ID_materiel_fournisseur`),
  KEY `FK_fournisseur_materiel` (`FK_fournisseur_materiel`),
  KEY `FK_materiel_fournisseur` (`FK_materiel_fournisseur`),
  CONSTRAINT `FK_t_materiel_fournisseur_t_fournisseur` FOREIGN KEY (`FK_fournisseur_materiel`) REFERENCES `t_fournisseur` (`ID_Fournisseur`),
  CONSTRAINT `FK_t_materiel_fournisseur_t_materiel` FOREIGN KEY (`FK_materiel_fournisseur`) REFERENCES `t_materiel` (`ID_Materiel`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_materiel_fournisseur : ~5 rows (environ)
INSERT INTO `t_materiel_fournisseur` (`ID_materiel_fournisseur`, `FK_fournisseur_materiel`, `FK_materiel_fournisseur`) VALUES
	(1, 1, 1),
	(2, 2, 2),
	(3, 3, 3),
	(4, 4, 4),
	(5, 5, 5);

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_numero_telephone
DROP TABLE IF EXISTS `t_numero_telephone`;
CREATE TABLE IF NOT EXISTS `t_numero_telephone` (
  `ID_Numero_telephone` int NOT NULL AUTO_INCREMENT,
  `Numero_telephone` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`ID_Numero_telephone`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_numero_telephone : ~20 rows (environ)
INSERT INTO `t_numero_telephone` (`ID_Numero_telephone`, `Numero_telephone`) VALUES
	(1, '077 621 17 65'),
	(2, '078 174 88 90'),
	(3, '077 645 78 34'),
	(4, '079 365 73 22'),
	(5, '077 547 89 92'),
	(6, '079 288 67 54'),
	(7, '077 676 54 34'),
	(8, '076 431 60 44'),
	(9, '077 743 81 78'),
	(10, '078 747 64 53'),
	(11, '077 532 15 64'),
	(12, '079 654 34 43'),
	(13, '077 780 89 63'),
	(14, '079 213 36 53'),
	(15, '077 923 35 69'),
	(16, '076 354 64 78'),
	(17, '077 245 85 98'),
	(18, '076 456 63 56'),
	(19, '077 675 34 98'),
	(20, '079 444 63 35');

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_tache
DROP TABLE IF EXISTS `t_tache`;
CREATE TABLE IF NOT EXISTS `t_tache` (
  `ID_Tache` int NOT NULL AUTO_INCREMENT,
  `Description` varchar(1000) DEFAULT NULL,
  `Date_debut` date DEFAULT NULL,
  `Date_fin` date DEFAULT NULL,
  PRIMARY KEY (`ID_Tache`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_tache : ~5 rows (environ)
INSERT INTO `t_tache` (`ID_Tache`, `Description`, `Date_debut`, `Date_fin`) VALUES
	(1, 'Changer la led de la chambre 02', '2024-05-22', '2024-06-14'),
	(2, 'Installation éléctrique de la cuisine', '2023-12-01', '2024-01-07'),
	(3, 'Raccordement des appareils éléctriques', '2024-02-21', '2024-04-04'),
	(4, 'Tracage des lignes d\'éclairage avec laser', '2024-03-01', '2024-05-11'),
	(5, 'Raccordement d\'un tableau éléctrique', '2024-04-12', '2024-05-05');

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_type_mail
DROP TABLE IF EXISTS `t_type_mail`;
CREATE TABLE IF NOT EXISTS `t_type_mail` (
  `ID_type_mail` int NOT NULL AUTO_INCREMENT,
  `Type_mail` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`ID_type_mail`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_type_mail : ~2 rows (environ)
INSERT INTO `t_type_mail` (`ID_type_mail`, `Type_mail`) VALUES
	(1, 'Professionnel'),
	(2, 'Prive');

-- Listage de la structure de table sabani_eltion_expi1a_dump_i164. t_type_numero
DROP TABLE IF EXISTS `t_type_numero`;
CREATE TABLE IF NOT EXISTS `t_type_numero` (
  `ID_type_numero` int NOT NULL AUTO_INCREMENT,
  `Type_numero` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`ID_type_numero`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table sabani_eltion_expi1a_dump_i164.t_type_numero : ~2 rows (environ)
INSERT INTO `t_type_numero` (`ID_type_numero`, `Type_numero`) VALUES
	(1, 'Professionel'),
	(2, 'Prive');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
