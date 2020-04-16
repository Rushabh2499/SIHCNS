-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 16, 2020 at 09:11 AM
-- Server version: 5.7.26
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cns1`
--

-- --------------------------------------------------------

--
-- Table structure for table `airport`
--

DROP TABLE IF EXISTS `airport`;
CREATE TABLE IF NOT EXISTS `airport` (
  `a_id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `altitude` int(6) DEFAULT NULL,
  `area` float DEFAULT NULL,
  `dgm_id` int(5) DEFAULT NULL,
  `longitude` varchar(10) DEFAULT NULL,
  `latitude` varchar(10) DEFAULT NULL,
  `code` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`a_id`),
  UNIQUE KEY `dm_id` (`dgm_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `airport`
--

INSERT INTO `airport` (`a_id`, `name`, `altitude`, `area`, `dgm_id`, `longitude`, `latitude`, `code`) VALUES
(1, 'Vadodara', 129, 149, 2102, '22.3325', '73.2171', 'BDQ'),
(2, 'Dabolim', 132, 121, NULL, '15.3803', '73.8350', 'GOI'),
(3, 'Sahar', 142, 125, NULL, '19.0896', '72.8656', 'BOM'),
(4, 'Delhi', 151, 120, NULL, '28.5562', '77.1000', 'DEL');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=181 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add airport', 1, 'add_airport'),
(2, 'Can change airport', 1, 'change_airport'),
(3, 'Can delete airport', 1, 'delete_airport'),
(4, 'Can view airport', 1, 'view_airport'),
(5, 'Can add cdvordaily', 2, 'add_cdvordaily'),
(6, 'Can change cdvordaily', 2, 'change_cdvordaily'),
(7, 'Can delete cdvordaily', 2, 'delete_cdvordaily'),
(8, 'Can view cdvordaily', 2, 'view_cdvordaily'),
(9, 'Can add cdvormonthly', 3, 'add_cdvormonthly'),
(10, 'Can change cdvormonthly', 3, 'change_cdvormonthly'),
(11, 'Can delete cdvormonthly', 3, 'delete_cdvormonthly'),
(12, 'Can view cdvormonthly', 3, 'view_cdvormonthly'),
(13, 'Can add cdvorweekly', 4, 'add_cdvorweekly'),
(14, 'Can change cdvorweekly', 4, 'change_cdvorweekly'),
(15, 'Can delete cdvorweekly', 4, 'delete_cdvorweekly'),
(16, 'Can view cdvorweekly', 4, 'view_cdvorweekly'),
(17, 'Can add communication', 5, 'add_communication'),
(18, 'Can change communication', 5, 'change_communication'),
(19, 'Can delete communication', 5, 'delete_communication'),
(20, 'Can view communication', 5, 'view_communication'),
(21, 'Can add datisdaily', 6, 'add_datisdaily'),
(22, 'Can change datisdaily', 6, 'change_datisdaily'),
(23, 'Can delete datisdaily', 6, 'delete_datisdaily'),
(24, 'Can view datisdaily', 6, 'view_datisdaily'),
(25, 'Can add datisweekly', 7, 'add_datisweekly'),
(26, 'Can change datisweekly', 7, 'change_datisweekly'),
(27, 'Can delete datisweekly', 7, 'delete_datisweekly'),
(28, 'Can view datisweekly', 7, 'view_datisweekly'),
(29, 'Can add dgm', 8, 'add_dgm'),
(30, 'Can change dgm', 8, 'change_dgm'),
(31, 'Can delete dgm', 8, 'delete_dgm'),
(32, 'Can view dgm', 8, 'view_dgm'),
(33, 'Can add dmedaily', 9, 'add_dmedaily'),
(34, 'Can change dmedaily', 9, 'change_dmedaily'),
(35, 'Can delete dmedaily', 9, 'delete_dmedaily'),
(36, 'Can view dmedaily', 9, 'view_dmedaily'),
(37, 'Can add dmemonthly', 10, 'add_dmemonthly'),
(38, 'Can change dmemonthly', 10, 'change_dmemonthly'),
(39, 'Can delete dmemonthly', 10, 'delete_dmemonthly'),
(40, 'Can view dmemonthly', 10, 'view_dmemonthly'),
(41, 'Can add dmeweekly', 11, 'add_dmeweekly'),
(42, 'Can change dmeweekly', 11, 'change_dmeweekly'),
(43, 'Can delete dmeweekly', 11, 'delete_dmeweekly'),
(44, 'Can view dmeweekly', 11, 'view_dmeweekly'),
(45, 'Can add dscndaily', 12, 'add_dscndaily'),
(46, 'Can change dscndaily', 12, 'change_dscndaily'),
(47, 'Can delete dscndaily', 12, 'delete_dscndaily'),
(48, 'Can view dscndaily', 12, 'view_dscndaily'),
(49, 'Can add dscnmonthly', 13, 'add_dscnmonthly'),
(50, 'Can change dscnmonthly', 13, 'change_dscnmonthly'),
(51, 'Can delete dscnmonthly', 13, 'delete_dscnmonthly'),
(52, 'Can view dscnmonthly', 13, 'view_dscnmonthly'),
(53, 'Can add dscnweekly', 14, 'add_dscnweekly'),
(54, 'Can change dscnweekly', 14, 'change_dscnweekly'),
(55, 'Can delete dscnweekly', 14, 'delete_dscnweekly'),
(56, 'Can view dscnweekly', 14, 'view_dscnweekly'),
(57, 'Can add engineer', 15, 'add_engineer'),
(58, 'Can change engineer', 15, 'change_engineer'),
(59, 'Can delete engineer', 15, 'delete_engineer'),
(60, 'Can view engineer', 15, 'view_engineer'),
(61, 'Can add head', 16, 'add_head'),
(62, 'Can change head', 16, 'change_head'),
(63, 'Can delete head', 16, 'delete_head'),
(64, 'Can view head', 16, 'view_head'),
(65, 'Can add issues', 17, 'add_issues'),
(66, 'Can change issues', 17, 'change_issues'),
(67, 'Can delete issues', 17, 'delete_issues'),
(68, 'Can view issues', 17, 'view_issues'),
(69, 'Can add navigation', 18, 'add_navigation'),
(70, 'Can change navigation', 18, 'change_navigation'),
(71, 'Can delete navigation', 18, 'delete_navigation'),
(72, 'Can view navigation', 18, 'view_navigation'),
(73, 'Can add ndbdaily', 19, 'add_ndbdaily'),
(74, 'Can change ndbdaily', 19, 'change_ndbdaily'),
(75, 'Can delete ndbdaily', 19, 'delete_ndbdaily'),
(76, 'Can view ndbdaily', 19, 'view_ndbdaily'),
(77, 'Can add ndbmonthly', 20, 'add_ndbmonthly'),
(78, 'Can change ndbmonthly', 20, 'change_ndbmonthly'),
(79, 'Can delete ndbmonthly', 20, 'delete_ndbmonthly'),
(80, 'Can view ndbmonthly', 20, 'view_ndbmonthly'),
(81, 'Can add ndbweekly', 21, 'add_ndbweekly'),
(82, 'Can change ndbweekly', 21, 'change_ndbweekly'),
(83, 'Can delete ndbweekly', 21, 'delete_ndbweekly'),
(84, 'Can view ndbweekly', 21, 'view_ndbweekly'),
(85, 'Can add scctvdaily', 22, 'add_scctvdaily'),
(86, 'Can change scctvdaily', 22, 'change_scctvdaily'),
(87, 'Can delete scctvdaily', 22, 'delete_scctvdaily'),
(88, 'Can view scctvdaily', 22, 'view_scctvdaily'),
(89, 'Can add scctvmonthly', 23, 'add_scctvmonthly'),
(90, 'Can change scctvmonthly', 23, 'change_scctvmonthly'),
(91, 'Can delete scctvmonthly', 23, 'delete_scctvmonthly'),
(92, 'Can view scctvmonthly', 23, 'view_scctvmonthly'),
(93, 'Can add scctvweekly', 24, 'add_scctvweekly'),
(94, 'Can change scctvweekly', 24, 'change_scctvweekly'),
(95, 'Can delete scctvweekly', 24, 'delete_scctvweekly'),
(96, 'Can view scctvweekly', 24, 'view_scctvweekly'),
(97, 'Can add supervisor', 25, 'add_supervisor'),
(98, 'Can change supervisor', 25, 'change_supervisor'),
(99, 'Can delete supervisor', 25, 'delete_supervisor'),
(100, 'Can view supervisor', 25, 'view_supervisor'),
(101, 'Can add surveillance', 26, 'add_surveillance'),
(102, 'Can change surveillance', 26, 'change_surveillance'),
(103, 'Can delete surveillance', 26, 'delete_surveillance'),
(104, 'Can view surveillance', 26, 'view_surveillance'),
(105, 'Can add vhfdaily', 27, 'add_vhfdaily'),
(106, 'Can change vhfdaily', 27, 'change_vhfdaily'),
(107, 'Can delete vhfdaily', 27, 'delete_vhfdaily'),
(108, 'Can view vhfdaily', 27, 'view_vhfdaily'),
(109, 'Can add vhfmonthly', 28, 'add_vhfmonthly'),
(110, 'Can change vhfmonthly', 28, 'change_vhfmonthly'),
(111, 'Can delete vhfmonthly', 28, 'delete_vhfmonthly'),
(112, 'Can view vhfmonthly', 28, 'view_vhfmonthly'),
(113, 'Can add vhfyearly', 29, 'add_vhfyearly'),
(114, 'Can change vhfyearly', 29, 'change_vhfyearly'),
(115, 'Can delete vhfyearly', 29, 'delete_vhfyearly'),
(116, 'Can view vhfyearly', 29, 'view_vhfyearly'),
(117, 'Can add log entry', 30, 'add_logentry'),
(118, 'Can change log entry', 30, 'change_logentry'),
(119, 'Can delete log entry', 30, 'delete_logentry'),
(120, 'Can view log entry', 30, 'view_logentry'),
(121, 'Can add permission', 31, 'add_permission'),
(122, 'Can change permission', 31, 'change_permission'),
(123, 'Can delete permission', 31, 'delete_permission'),
(124, 'Can view permission', 31, 'view_permission'),
(125, 'Can add group', 32, 'add_group'),
(126, 'Can change group', 32, 'change_group'),
(127, 'Can delete group', 32, 'delete_group'),
(128, 'Can view group', 32, 'view_group'),
(129, 'Can add user', 33, 'add_user'),
(130, 'Can change user', 33, 'change_user'),
(131, 'Can delete user', 33, 'delete_user'),
(132, 'Can view user', 33, 'view_user'),
(133, 'Can add content type', 34, 'add_contenttype'),
(134, 'Can change content type', 34, 'change_contenttype'),
(135, 'Can delete content type', 34, 'delete_contenttype'),
(136, 'Can view content type', 34, 'view_contenttype'),
(137, 'Can add session', 35, 'add_session'),
(138, 'Can change session', 35, 'change_session'),
(139, 'Can delete session', 35, 'delete_session'),
(140, 'Can view session', 35, 'view_session'),
(141, 'Can add auth group', 36, 'add_authgroup'),
(142, 'Can change auth group', 36, 'change_authgroup'),
(143, 'Can delete auth group', 36, 'delete_authgroup'),
(144, 'Can view auth group', 36, 'view_authgroup'),
(145, 'Can add auth group permissions', 37, 'add_authgrouppermissions'),
(146, 'Can change auth group permissions', 37, 'change_authgrouppermissions'),
(147, 'Can delete auth group permissions', 37, 'delete_authgrouppermissions'),
(148, 'Can view auth group permissions', 37, 'view_authgrouppermissions'),
(149, 'Can add auth permission', 38, 'add_authpermission'),
(150, 'Can change auth permission', 38, 'change_authpermission'),
(151, 'Can delete auth permission', 38, 'delete_authpermission'),
(152, 'Can view auth permission', 38, 'view_authpermission'),
(153, 'Can add auth user', 39, 'add_authuser'),
(154, 'Can change auth user', 39, 'change_authuser'),
(155, 'Can delete auth user', 39, 'delete_authuser'),
(156, 'Can view auth user', 39, 'view_authuser'),
(157, 'Can add auth user groups', 40, 'add_authusergroups'),
(158, 'Can change auth user groups', 40, 'change_authusergroups'),
(159, 'Can delete auth user groups', 40, 'delete_authusergroups'),
(160, 'Can view auth user groups', 40, 'view_authusergroups'),
(161, 'Can add auth user user permissions', 41, 'add_authuseruserpermissions'),
(162, 'Can change auth user user permissions', 41, 'change_authuseruserpermissions'),
(163, 'Can delete auth user user permissions', 41, 'delete_authuseruserpermissions'),
(164, 'Can view auth user user permissions', 41, 'view_authuseruserpermissions'),
(165, 'Can add django admin log', 42, 'add_djangoadminlog'),
(166, 'Can change django admin log', 42, 'change_djangoadminlog'),
(167, 'Can delete django admin log', 42, 'delete_djangoadminlog'),
(168, 'Can view django admin log', 42, 'view_djangoadminlog'),
(169, 'Can add django content type', 43, 'add_djangocontenttype'),
(170, 'Can change django content type', 43, 'change_djangocontenttype'),
(171, 'Can delete django content type', 43, 'delete_djangocontenttype'),
(172, 'Can view django content type', 43, 'view_djangocontenttype'),
(173, 'Can add django migrations', 44, 'add_djangomigrations'),
(174, 'Can change django migrations', 44, 'change_djangomigrations'),
(175, 'Can delete django migrations', 44, 'delete_djangomigrations'),
(176, 'Can view django migrations', 44, 'view_djangomigrations'),
(177, 'Can add django session', 45, 'add_djangosession'),
(178, 'Can change django session', 45, 'change_djangosession'),
(179, 'Can delete django session', 45, 'delete_djangosession'),
(180, 'Can view django session', 45, 'view_djangosession');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` int(11) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `cdvordaily`
--

DROP TABLE IF EXISTS `cdvordaily`;
CREATE TABLE IF NOT EXISTS `cdvordaily` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `Azimuth_angle` int(11) DEFAULT NULL,
  `30Hz_modulation` int(11) DEFAULT NULL,
  `9960Hz_modulation` int(11) DEFAULT NULL,
  `9960Hz_deviation` int(11) DEFAULT NULL,
  `field_intensity` int(11) DEFAULT NULL,
  `ident_modulation` int(11) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  KEY `emp_id` (`emp_id`),
  KEY `CDVORDaily_ibfk_1` (`a_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cdvordaily`
--

INSERT INTO `cdvordaily` (`date`, `a_id`, `emp_id`, `Azimuth_angle`, `30Hz_modulation`, `9960Hz_modulation`, `9960Hz_deviation`, `field_intensity`, `ident_modulation`, `REMARKS`, `Unit_incharge_approval`, `f_id`, `p_id`, `s_verify`, `status`) VALUES
('2020-04-12 12:33:14', 1, 4121, 24, 30, 30, 16, 0, 10, NULL, 'YES', '1', 1, NULL, ''),
('2020-04-12 12:33:15', 1, 4123, 23, 28, 32, 17, 1, 11, NULL, 'YES', '2', 2, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `cdvormonthly`
--

DROP TABLE IF EXISTS `cdvormonthly`;
CREATE TABLE IF NOT EXISTS `cdvormonthly` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  `measured_bearing_1` float DEFAULT NULL,
  `bearing_deviation_1` float DEFAULT NULL,
  `measured_bearing_2` float DEFAULT NULL,
  `bearing_deviation_2` float DEFAULT NULL,
  `measured_bearing_3` float DEFAULT NULL,
  `bearing_deviation_3` float DEFAULT NULL,
  `measured_deviation_4` float DEFAULT NULL,
  `bearing_deviation_4` float DEFAULT NULL,
  `measured_deviation_5` float DEFAULT NULL,
  `bearing_deviation_5` float DEFAULT NULL,
  `error_spread` float DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  KEY `emp_id` (`emp_id`),
  KEY `VHFMaily_ibfk_1` (`a_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cdvormonthly`
--

INSERT INTO `cdvormonthly` (`date`, `a_id`, `emp_id`, `f_id`, `p_id`, `s_verify`, `status`, `measured_bearing_1`, `bearing_deviation_1`, `measured_bearing_2`, `bearing_deviation_2`, `measured_bearing_3`, `bearing_deviation_3`, `measured_deviation_4`, `bearing_deviation_4`, `measured_deviation_5`, `bearing_deviation_5`, `error_spread`, `REMARKS`, `Unit_incharge_approval`) VALUES
('2020-04-12 12:33:46', 1, 4123, '1', 1, NULL, '', 0, 0, 7.5, 0, 15, 0, 22.5, 0, 37.5, 0, 0, NULL, 'YES'),
('2020-04-12 12:33:46', 1, 4121, '2', 2, NULL, '', 0, 0, 8, 0.5, 16, 1, 22.5, 0, 37.8, 0.3, 1.8, 'Error spread found of 1.8, which is nominal.', 'YES');

-- --------------------------------------------------------

--
-- Table structure for table `cdvorweekly`
--

DROP TABLE IF EXISTS `cdvorweekly`;
CREATE TABLE IF NOT EXISTS `cdvorweekly` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  `PS_5V` int(11) DEFAULT NULL,
  `PS_12V` int(11) DEFAULT NULL,
  `PS_negative_12V` int(11) DEFAULT NULL,
  `PS_28V` int(11) DEFAULT NULL,
  `PS_48V` int(11) DEFAULT NULL,
  `outside_temp` int(11) DEFAULT NULL,
  `TX1_temp` int(11) DEFAULT NULL,
  `TX2_temp` int(11) DEFAULT NULL,
  `Out_temp_enabled` varchar(10) DEFAULT NULL,
  `AM` int(11) DEFAULT NULL,
  `FM` int(11) DEFAULT NULL,
  `sideband_frequency` int(11) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `date` (`date`,`a_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cdvorweekly`
--

INSERT INTO `cdvorweekly` (`date`, `a_id`, `emp_id`, `f_id`, `p_id`, `s_verify`, `status`, `PS_5V`, `PS_12V`, `PS_negative_12V`, `PS_28V`, `PS_48V`, `outside_temp`, `TX1_temp`, `TX2_temp`, `Out_temp_enabled`, `AM`, `FM`, `sideband_frequency`, `REMARKS`, `Unit_incharge_approval`) VALUES
('2020-04-12 12:34:23', 1, 4129, '1', 1, NULL, '', 3, 10, -13, 29, 41, 79, 44, 49, 'FALSE', 30, 30, 10001, 'PS 5V,PS 12V,PS -12V, reading deviating too much. Issue no 519', 'NO'),
('2020-04-12 12:34:23', 1, 4156, '2', 2, NULL, '', 5, 5, 3, 56, 67, 45, 456, 67, '234', 546, 435, 345, 'xcg cgbxbvc', 'YES');

-- --------------------------------------------------------

--
-- Table structure for table `communication`
--

DROP TABLE IF EXISTS `communication`;
CREATE TABLE IF NOT EXISTS `communication` (
  `f_id` int(11) NOT NULL,
  `a_id` int(11) NOT NULL,
  `facility` varchar(20) DEFAULT NULL,
  `make` varchar(20) DEFAULT NULL,
  `model` varchar(20) DEFAULT NULL,
  `power` int(11) DEFAULT NULL,
  `DOI` date DEFAULT NULL,
  `DOC` date DEFAULT NULL,
  `location` varchar(20) DEFAULT NULL,
  `emp_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`f_id`,`a_id`),
  UNIQUE KEY `f_id` (`f_id`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `communication`
--

INSERT INTO `communication` (`f_id`, `a_id`, `facility`, `make`, `model`, `power`, `DOI`, `DOC`, `location`, `emp_id`) VALUES
(1, 1, 'VHF TX/RX', 'PAE', 'T6T', 50, '2009-06-15', '2009-06-20', 'E/ROOM', 4144),
(2, 1, 'DATIS', 'TERMA', '50209', NULL, '2008-11-01', '2009-01-01', 'E/ROOM', 4156),
(3, 1, 'DSCN', 'MEMOTEC', 'CX 800', NULL, '2020-01-07', '2020-02-29', 'COM CENTRE', 4169);

-- --------------------------------------------------------

--
-- Table structure for table `datisdaily`
--

DROP TABLE IF EXISTS `datisdaily`;
CREATE TABLE IF NOT EXISTS `datisdaily` (
  `p_id` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time DEFAULT NULL,
  `a_id` int(11) DEFAULT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `Status` varchar(40) NOT NULL,
  `f_id` int(11) DEFAULT NULL,
  `room_temp` int(11) DEFAULT NULL,
  `status_of_AC` varchar(10) DEFAULT NULL,
  `status_of_UPS` varchar(10) DEFAULT NULL,
  `status_of_serverA` varchar(10) DEFAULT NULL,
  `status_of_serverB` varchar(10) DEFAULT NULL,
  `datetime_of_servers_wrt_GPS_CLK` varchar(10) DEFAULT NULL,
  `status_of_Disk_array` varchar(10) DEFAULT NULL,
  `VHFTX_ATIS_status` varchar(10) DEFAULT NULL,
  `VHFRX_ATIS_status` varchar(10) DEFAULT NULL,
  `DATIS_update` varchar(10) DEFAULT NULL,
  `Audio_quality` varchar(10) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `test` varchar(30) DEFAULT NULL,
  `s_verify` int(30) DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `f_id` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `datisdaily`
--

INSERT INTO `datisdaily` (`p_id`, `date`, `time`, `a_id`, `emp_id`, `Status`, `f_id`, `room_temp`, `status_of_AC`, `status_of_UPS`, `status_of_serverA`, `status_of_serverB`, `datetime_of_servers_wrt_GPS_CLK`, `status_of_Disk_array`, `VHFTX_ATIS_status`, `VHFRX_ATIS_status`, `DATIS_update`, `Audio_quality`, `REMARKS`, `Unit_incharge_approval`, `test`, `s_verify`) VALUES
(1, '2020-03-24', '15:14:07', 1, 4169, 'PENDING', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', 'CORRECT', 'OK', 'ON LINE', 'ON LINE', 'OK', 'GOOD', NULL, 'YES', 'PASS', 3112),
(2, '2020-03-25', '15:08:08', 1, 4156, 'COMPLETED', 2, 23, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', 'CORRECT', 'OK', 'ON LINE', 'ON LINE', 'OK', 'GOOD', NULL, 'YES', 'PASS', 3112),
(3, '2020-03-26', '14:05:02', 1, 4156, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', 'CORRECT', 'OK', 'ON LINE', 'ON LINE', 'OK', 'GOOD', NULL, 'YES', 'PASS', 3112),
(4, '2020-03-27', '16:28:16', 1, 4156, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', 'CORRECT', 'OK', 'ON LINE', 'OM LINE', 'OK', 'GOOD', NULL, 'YES', 'PASS', 3112),
(5, '2020-03-28', '14:01:01', 1, 4144, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', 'CORRECT', 'OK', 'ON LINE', 'ON LINE', 'OK', 'GOOD', NULL, 'YES', 'PASS', 3112),
(6, '2020-03-29', '23:35:25', 1, 4144, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3112),
(7, '2020-03-30', '11:57:01', 1, 4156, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3112),
(8, '2020-03-31', '16:41:26', 1, 4156, 'PENDING', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3112),
(9, '2020-04-01', '01:10:31', 1, 4144, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3112),
(10, '2020-04-06', '19:06:51', 1, 4144, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3112),
(19, '2020-04-07', '22:52:02', 1, 4156, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3112),
(31, '2020-04-08', '16:45:06', 1, 4156, 'COMPLETED', 2, 26, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(32, '2020-04-13', '15:14:07', 1, 4156, 'PENDING', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', 'CORRECT', 'OK', 'ON LINE', 'ON LINE', 'OK', 'GOOD', NULL, 'YES', 'PASS', NULL),
(37, '2020-04-14', NULL, NULL, 4156, 'COMPLETED', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(38, '2020-04-15', '00:34:52', 1, 4156, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'STANDBY', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3112);

-- --------------------------------------------------------

--
-- Table structure for table `datisdlogs`
--

DROP TABLE IF EXISTS `datisdlogs`;
CREATE TABLE IF NOT EXISTS `datisdlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `value` varchar(30) NOT NULL,
  `Remarks` varchar(100) NOT NULL,
  `Date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`),
  KEY `p_id` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `datisdlogs`
--

INSERT INTO `datisdlogs` (`log_id`, `emp_id`, `p_id`, `value`, `Remarks`, `Date`, `time`) VALUES
(1, 4169, 1, '25', 'Temperature exceeds 24 degrees', '2020-03-24', '14:01:01'),
(2, 4169, 1, 'HIGH', 'Status of ups not NORMAL', '2020-03-24', '14:01:01'),
(3, 4169, 1, 'NOT MAINS', 'Status of ServerB is not MAINS', '2020-03-24', '14:01:01'),
(4, 4169, 1, '26', 'Temperature not normal(update)', '2020-03-24', '14:01:11'),
(5, 4169, 1, 'All parameters NORMAL', 'Parameter/s fixed', '2020-03-24', '14:01:11'),
(6, 4156, 3, '25', 'Temperature exceeds 24 degrees', '2020-03-26', '11:57:01'),
(7, 4156, 3, 'NOT NORMAL', 'Status of ups not NORMAL', '2020-03-26', '11:57:01'),
(8, 4156, 3, 'NOT NORMAL', 'Status of ups not NORMAL(update)', '2020-03-26', '12:26:47'),
(9, 4156, 3, '25', 'Temperature not normal(update)', '2020-03-26', '12:26:57'),
(10, 4156, 3, 'NOT NORMAL', 'Status of ups not NORMAL(update)', '2020-03-26', '12:27:05'),
(11, 4156, 3, 'All parameters NORMAL', 'Parameter/s fixed', '2020-03-26', '12:27:30'),
(12, 4144, 10, 'MAIN', 'Status of ServerA is not MAINS', '2020-04-01', '19:06:51'),
(13, 4144, 10, 'MAIN', 'Status of ServerA is not MAINS(update)', '2020-04-01', '19:06:58'),
(14, 4144, 10, 'All parameters NORMAL', 'Parameter/s fixed', '2020-04-01', '19:15:15'),
(28, 4156, 10, '24', 'Status of ups not NORMAL', '2020-04-07', '22:52:02'),
(29, 4156, 19, '24', 'Parameter/s fixed', '2020-04-07', '22:52:19'),
(62, 4156, 19, '26', 'Temperature exceeds 24 degrees', '2020-04-08', '16:45:06'),
(63, 4156, 31, 'Final submit with errors', 'OOPS', '2020-04-08', '16:45:36'),
(71, 4156, 38, 'Final submit with errors', 'OK', '2020-04-15', '20:18:00'),
(72, 4156, 38, '24', 'Parameter/s fixed and also-', '2020-04-15', '20:28:50');

-- --------------------------------------------------------

--
-- Table structure for table `datisweekly`
--

DROP TABLE IF EXISTS `datisweekly`;
CREATE TABLE IF NOT EXISTS `datisweekly` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time DEFAULT NULL,
  `a_id` int(11) DEFAULT NULL,
  `f_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `Status` varchar(40) NOT NULL,
  `serverAorB` varchar(1) DEFAULT NULL,
  `UPS_ip` int(11) DEFAULT NULL,
  `UPS_op` int(11) DEFAULT NULL,
  `Dust_free` varchar(10) DEFAULT NULL,
  `LAN_status` varchar(10) DEFAULT NULL,
  `time_sync` varchar(5) DEFAULT NULL,
  `Audio_quality` varchar(5) DEFAULT NULL,
  `ptt_off_interval_seconds` int(11) DEFAULT NULL,
  `main_to_standby_changeover` varchar(5) DEFAULT NULL,
  `status_of_ROP` varchar(5) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `s_verify` int(30) DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `f_id` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `datisweekly`
--

INSERT INTO `datisweekly` (`p_id`, `date`, `time`, `a_id`, `f_id`, `emp_id`, `Status`, `serverAorB`, `UPS_ip`, `UPS_op`, `Dust_free`, `LAN_status`, `time_sync`, `Audio_quality`, `ptt_off_interval_seconds`, `main_to_standby_changeover`, `status_of_ROP`, `REMARKS`, `Unit_incharge_approval`, `s_verify`) VALUES
(1, '2020-03-11', '11:08:08', 1, 2, 4156, 'PENDING', 'B', 210, 230, 'OK', 'OK', 'OK', 'GOOD', 15, 'OK', 'OK', 'Residual dust was found on the system. Cleaning was performed.', 'YES', NULL),
(2, '2020-03-18', '10:05:05', 1, 2, 4169, 'COMPLETED', 'A', 230, 230, 'OK', 'OK', 'OK', 'GOOD', 15, 'OK', 'OK', NULL, NULL, NULL),
(3, '2020-03-25', '15:00:46', 1, 2, 4144, 'COMPLETED', 'A', 200, 230, 'OK', 'OK', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 3112),
(4, '2020-03-30', '13:13:10', 1, 2, 4144, 'COMPLETED', 'A', 230, 230, 'OK', 'OK', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(10, '2020-04-07', '22:43:40', 1, 2, 4156, 'COMPLETED', 'A', 220, 230, 'OK', 'OK', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(12, '2020-04-09', '17:16:01', 1, 2, 4156, 'COMPLETED', 'A', 224, 230, 'NOT OK', 'OK', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `datiswlogs`
--

DROP TABLE IF EXISTS `datiswlogs`;
CREATE TABLE IF NOT EXISTS `datiswlogs` (
  `logs_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `Remarks` varchar(100) NOT NULL,
  `value` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`logs_id`),
  KEY `emp_id` (`emp_id`),
  KEY `p_id` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `datiswlogs`
--

INSERT INTO `datiswlogs` (`logs_id`, `emp_id`, `p_id`, `Remarks`, `value`, `date`, `time`) VALUES
(1, 4144, 3, 'UPS_ip not in corrent range', '190', '2020-03-25', '15:00:46'),
(2, 4144, 3, 'Not Dustfree', 'NOT OK', '2020-03-25', '15:00:46'),
(3, 4144, 3, 'Parameter/s fixed', 'All parameters NORMAL', '2020-03-25', '15:01:04'),
(8, 4144, 4, 'UPS_op value not normal', '220', '2020-04-02', '13:13:10'),
(9, 4144, 4, 'Lan status not OK', 'NOT OK', '2020-04-02', '13:13:10'),
(10, 4144, 4, 'Parameter/s fixed', 'All parameters NORMAL', '2020-04-02', '13:13:18'),
(24, 4156, 10, 'UPS_op value not normal', '220', '2020-04-07', '22:43:40'),
(25, 4156, 10, 'Parameter/s fixed', 'A', '2020-04-07', '22:51:22'),
(29, 4156, 12, 'Not Dustfree', 'NOT OK', '2020-04-08', '17:16:01'),
(30, 4156, 12, 'Not Dustfree(update)', 'A', '2020-04-08', '17:16:13'),
(31, 4156, 12, 'OOPS', 'Final submit with errors', '2020-04-08', '17:16:23');

-- --------------------------------------------------------

--
-- Table structure for table `dgm`
--

DROP TABLE IF EXISTS `dgm`;
CREATE TABLE IF NOT EXISTS `dgm` (
  `dgm_id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `designation` varchar(10) DEFAULT NULL,
  `a_id` int(11) DEFAULT NULL,
  `contact` int(11) DEFAULT NULL,
  `password` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `head_id` int(11) DEFAULT NULL,
  `email` varchar(30) NOT NULL,
  PRIMARY KEY (`dgm_id`),
  KEY `a_id` (`a_id`),
  KEY `head_id` (`head_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dgm`
--

INSERT INTO `dgm` (`dgm_id`, `name`, `designation`, `a_id`, `contact`, `password`, `head_id`, `email`) VALUES
(2102, 'Linus Torvaldas', 'DGM', 1, 904471123, 'pbkdf2_sha256$180000$7LqYYghTlDpY$lXlFwMM4SieeCYZgavDkqEp+I2djxOpf3wqQO8xXC5Q=', 1101, 'yes@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'login', 'airport'),
(2, 'login', 'cdvordaily'),
(3, 'login', 'cdvormonthly'),
(4, 'login', 'cdvorweekly'),
(5, 'login', 'communication'),
(6, 'login', 'datisdaily'),
(7, 'login', 'datisweekly'),
(8, 'login', 'dgm'),
(9, 'login', 'dmedaily'),
(10, 'login', 'dmemonthly'),
(11, 'login', 'dmeweekly'),
(12, 'login', 'dscndaily'),
(13, 'login', 'dscnmonthly'),
(14, 'login', 'dscnweekly'),
(15, 'login', 'engineer'),
(16, 'login', 'head'),
(17, 'login', 'issues'),
(18, 'login', 'navigation'),
(19, 'login', 'ndbdaily'),
(20, 'login', 'ndbmonthly'),
(21, 'login', 'ndbweekly'),
(22, 'login', 'scctvdaily'),
(23, 'login', 'scctvmonthly'),
(24, 'login', 'scctvweekly'),
(25, 'login', 'supervisor'),
(26, 'login', 'surveillance'),
(27, 'login', 'vhfdaily'),
(28, 'login', 'vhfmonthly'),
(29, 'login', 'vhfyearly'),
(30, 'admin', 'logentry'),
(31, 'auth', 'permission'),
(32, 'auth', 'group'),
(33, 'auth', 'user'),
(34, 'contenttypes', 'contenttype'),
(35, 'sessions', 'session'),
(36, 'login', 'authgroup'),
(37, 'login', 'authgrouppermissions'),
(38, 'login', 'authpermission'),
(39, 'login', 'authuser'),
(40, 'login', 'authusergroups'),
(41, 'login', 'authuseruserpermissions'),
(42, 'login', 'djangoadminlog'),
(43, 'login', 'djangocontenttype'),
(44, 'login', 'djangomigrations'),
(45, 'login', 'djangosession');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-03-20 18:42:09.840064'),
(2, 'auth', '0001_initial', '2020-03-20 18:42:10.412917'),
(3, 'admin', '0001_initial', '2020-03-20 18:42:12.079254'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-03-20 18:42:12.386207'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-03-20 18:42:12.408521'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-03-20 18:42:12.577563'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-03-20 18:42:12.703945'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-03-20 18:42:12.785416'),
(9, 'auth', '0004_alter_user_username_opts', '2020-03-20 18:42:12.822220'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-03-20 18:42:12.901993'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-03-20 18:42:12.907018'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-03-20 18:42:12.917989'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-03-20 18:42:13.006949'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-03-20 18:42:13.101602'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-03-20 18:42:13.171220'),
(16, 'auth', '0011_update_proxy_permissions', '2020-03-20 18:42:13.182230'),
(17, 'login', '0001_initial', '2020-03-20 18:42:13.378825'),
(18, 'login', '0002_delete_manors', '2020-03-20 18:42:13.407074'),
(19, 'sessions', '0001_initial', '2020-03-20 18:42:13.839124'),
(20, 'login', '0003_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django', '2020-03-20 18:52:30.753958');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('f16zxlu1ladwiuvfm2ub06o6huh7ge81', 'MzFhZWNmYzgzODA0YmYxZmY2ZTY0MmFiZTFiNzBhNTY2ZDU0NWVjZTp7InR5cGUiOiJzIn0=', '2020-04-08 15:04:14.663004'),
('6gqolw8tsefvj34isl1r12cfn8eoy6vv', 'M2RmYjdiNzkyY2I4ZjRkMjhlMThhOWFmZWI1ZDUyYTIyMWU4OWY4MTp7InVpZCI6IjQxNTYifQ==', '2020-04-22 11:45:51.966277'),
('od5fv1s70gugpn8jzfto4p0f9a2uhu1i', 'MTRkYTJhODc5ZDhiYzg4N2FiOTQ2YjMzYzIzZjE0YzY5ODM0NWM1Yjp7InVpZCI6IiJ9', '2020-04-14 19:12:25.234777'),
('w9py0nuxsyxsmqubmtnshhgdhqgisnig', 'ZGRiYmU1MDc0NmJlYzU5YzJiOGNhMzIxYzJlYWU3ODUxNWQ1NDE4ODp7InR5cGUiOiJzIiwidWlkIjoiMzExMiIsInBpZCI6MSwibmFtZSI6ImRhdGlzZGFpbHkiLCJwYXNzdyI6IjEyMyJ9', '2020-04-28 13:04:30.502482'),
('3hdaipxur7b7fh5s1z9qv2uv7uj07hje', 'NjhmN2RiMTJlYjJjNGU1NTA2NzNkM2Y0NjVjMTY2YTVkNTNhMzUwYzp7InR5cGUiOiJzIiwidWlkIjoiMzExMiIsInBhc3N3IjoiMTIzIn0=', '2020-04-28 18:32:06.381492'),
('3ep01jkgcwgcwnbrhxdh3b6g6uob0gec', 'M2RmYjdiNzkyY2I4ZjRkMjhlMThhOWFmZWI1ZDUyYTIyMWU4OWY4MTp7InVpZCI6IjQxNTYifQ==', '2020-04-30 08:51:22.985964');

-- --------------------------------------------------------

--
-- Table structure for table `dmedaily`
--

DROP TABLE IF EXISTS `dmedaily`;
CREATE TABLE IF NOT EXISTS `dmedaily` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `eqpt_shelter_cleanliness` varchar(10) DEFAULT NULL,
  `Battery_room_cleanliness` varchar(10) DEFAULT NULL,
  `AC_status` varchar(20) DEFAULT NULL,
  `eqpt_shelter_temperature` float DEFAULT NULL,
  `mains_power_supply` int(11) DEFAULT NULL,
  `stabiliser_output` int(11) DEFAULT NULL,
  `batterybank_voltage` int(11) DEFAULT NULL,
  `status_of_monitor` varchar(10) DEFAULT NULL,
  `unusual_noise` varchar(10) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `p_id` int(30) NOT NULL,
  `s_verify` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dmedaily`
--

INSERT INTO `dmedaily` (`date`, `a_id`, `emp_id`, `f_id`, `eqpt_shelter_cleanliness`, `Battery_room_cleanliness`, `AC_status`, `eqpt_shelter_temperature`, `mains_power_supply`, `stabiliser_output`, `batterybank_voltage`, `status_of_monitor`, `unusual_noise`, `REMARKS`, `Unit_incharge_approval`, `p_id`, `s_verify`) VALUES
('2020-04-12 11:51:12', 1, 4123, '2', 'DUST FREE', 'NOT CLEAN', 'SERVICABLE', 24, 215, 221, 24, 'OK', 'YES', 'Battery room found not clean. Noise was audible from the DME.Issue no. 520', 'NO', 10, NULL),
('2020-04-12 11:51:27', 1, 4129, '2', 'DUST FREE', 'DUST FREE', 'SERVICABLE', 22, 221, 219, 24, 'OK', 'NO', NULL, 'YES', 11, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `dmemonthly`
--

DROP TABLE IF EXISTS `dmemonthly`;
CREATE TABLE IF NOT EXISTS `dmemonthly` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `SGDNF_pulse_width` float DEFAULT NULL,
  `SGDNF_amplitude` float DEFAULT NULL,
  `Squitter_rate_of_inhibit_interrogation` float DEFAULT NULL,
  `max_reply_rate_KHz` float DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `p_id` int(30) NOT NULL,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dmemonthly`
--

INSERT INTO `dmemonthly` (`date`, `a_id`, `emp_id`, `f_id`, `SGDNF_pulse_width`, `SGDNF_amplitude`, `Squitter_rate_of_inhibit_interrogation`, `max_reply_rate_KHz`, `REMARKS`, `Unit_incharge_approval`, `p_id`, `s_verify`, `status`) VALUES
('2020-04-12 12:30:49', 1, 4123, '2', 6, 12, 0.94, 2.7, NULL, 'YES', 0, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `dmeweekly`
--

DROP TABLE IF EXISTS `dmeweekly`;
CREATE TABLE IF NOT EXISTS `dmeweekly` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `test_interrogation_module` int(11) DEFAULT NULL,
  `RX_video_module` int(11) DEFAULT NULL,
  `100W_module` int(11) DEFAULT NULL,
  `Monitor_module` int(11) DEFAULT NULL,
  `AC_regulator_ip` int(11) DEFAULT NULL,
  `AC_regulator_op` int(11) DEFAULT NULL,
  `system_delay` float DEFAULT NULL,
  `pulse_pair_spacing_SEPN` float DEFAULT NULL,
  `reply_efficiency_percent` float DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(30) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dmeweekly`
--

INSERT INTO `dmeweekly` (`date`, `a_id`, `emp_id`, `f_id`, `test_interrogation_module`, `RX_video_module`, `100W_module`, `Monitor_module`, `AC_regulator_ip`, `AC_regulator_op`, `system_delay`, `pulse_pair_spacing_SEPN`, `reply_efficiency_percent`, `REMARKS`, `Unit_incharge_approval`, `p_id`, `s_verify`, `status`) VALUES
('2020-04-12 12:30:06', 1, 4129, '2', 16, 15, 15, 15, 248, 230, 50, 12, 74, NULL, 'YES', 1, NULL, ''),
('2020-04-12 12:30:20', 1, 4121, '2', 15, 15, 15, 15, 240, 230, 50.8, 12.25, 89, NULL, 'YES', 2, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `dscndaily`
--

DROP TABLE IF EXISTS `dscndaily`;
CREATE TABLE IF NOT EXISTS `dscndaily` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(30) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `a_id` int(11) NOT NULL,
  `f_id` int(11) NOT NULL DEFAULT '3',
  `emp_id` int(11) DEFAULT NULL,
  `SAT_LED` varchar(10) DEFAULT NULL,
  `ODU_LED` varchar(10) DEFAULT NULL,
  `IO_LED` varchar(10) DEFAULT NULL,
  `Alarm_LED` varchar(10) DEFAULT NULL,
  `Power_LED` varchar(10) DEFAULT NULL,
  `V35_LED` varchar(20) DEFAULT NULL,
  `IP_Voltage` int(11) DEFAULT NULL,
  `OP_voltage` int(11) DEFAULT NULL,
  `Battery_Voltage` int(11) DEFAULT NULL,
  `CorO_function` varchar(5) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `dscndaily_ibfk_3` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dscndaily`
--

INSERT INTO `dscndaily` (`p_id`, `s_verify`, `status`, `date`, `time`, `a_id`, `f_id`, `emp_id`, `SAT_LED`, `ODU_LED`, `IO_LED`, `Alarm_LED`, `Power_LED`, `V35_LED`, `IP_Voltage`, `OP_voltage`, `Battery_Voltage`, `CorO_function`, `REMARKS`, `Unit_incharge_approval`) VALUES
(1, NULL, '', '2020-03-30', '13:14:06', 1, 3, 4169, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'OFF', 'STEADY ON', 'RX/TX BLINKING', 230, 220, 210, 'OK', NULL, 'YES'),
(2, NULL, '', '2020-03-31', '16:05:04', 1, 3, 4169, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'OFF', 'STEADY ON', 'RX/TX BLINKING', 230, 230, 190, 'OK', 'Alarm LED found ON.\r\nLess voltage generated at the output side of the UPS. This giving rise to even lesser and insufficient battery voltage of 170V.\r\nIssue no 518. Issue was solved on the same day.', 'YES'),
(3, NULL, '', '2020-04-01', '23:50:12', 1, 3, 4169, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'OFF', 'STEADY ON', 'RX/TX BLINKING', 230, 230, 195, 'OK', 'UPS I/P,O/P very low. ', 'YES'),
(4, NULL, '', '2020-04-02', '01:13:31', 1, 3, 4169, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'OFF', 'STEADY ON', 'RX/TX BLINKING', 230, 230, 200, 'OK', 'Alarm LED is ON. it was tuned off successfully', 'YES'),
(5, NULL, '', '2020-04-07', '17:29:54', 1, 3, 4156, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'OFF', 'STEADY ON', 'RX/TX BLINKING', 230, 220, 210, 'OK', 'Every parameters are normal', 'YES');

-- --------------------------------------------------------

--
-- Table structure for table `dscndlogs`
--

DROP TABLE IF EXISTS `dscndlogs`;
CREATE TABLE IF NOT EXISTS `dscndlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `value` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dscndlogs`
--

INSERT INTO `dscndlogs` (`log_id`, `emp_id`, `remarks`, `value`, `date`, `time`) VALUES
(1, 4144, 'Alarm LED was turned ON', 'ON', '2020-03-28', '23:50:12'),
(2, 4144, 'UPS I/P Voltage exceeding normal voltage', '210', '2020-03-28', '23:50:12'),
(3, 4144, 'UPS O/P Voltage exceeding normal voltage', '210', '2020-03-28', '23:50:12'),
(4, 4144, 'UPS Battery Voltage exceeding normal voltage', '170', '2020-03-28', '23:50:12'),
(5, 4144, 'Alarm LED was turned ON(update)', 'ON', '2020-03-28', '23:51:19'),
(6, 4144, 'Parameter/s fixed', 'All parameters NORMAL', '2020-03-28', '23:52:09'),
(7, 4169, 'Alarm LED was turned ON', 'ON', '2020-03-29', '01:13:31'),
(8, 4144, 'Parameter/s fixed', 'All parameters NORMAL', '2020-03-29', '01:13:51');

-- --------------------------------------------------------

--
-- Table structure for table `dscnmonthly`
--

DROP TABLE IF EXISTS `dscnmonthly`;
CREATE TABLE IF NOT EXISTS `dscnmonthly` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` int(11) DEFAULT NULL,
  `Cleaning_DSCN_associated_eqpt` tinytext,
  `Battery_backup_time_of_UPS1nUPS2` tinytext,
  `UPS_battery_voltage_on_load` tinytext,
  `Antenna_n_cable_check` tinytext,
  `Earth_resistance` tinytext,
  `EorN_voltage` int(11) DEFAULT NULL,
  `eqpt_status_after_check` varchar(5) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `s_verify` int(30) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dscnmonthly`
--

INSERT INTO `dscnmonthly` (`p_id`, `date`, `time`, `a_id`, `emp_id`, `f_id`, `Cleaning_DSCN_associated_eqpt`, `Battery_backup_time_of_UPS1nUPS2`, `UPS_battery_voltage_on_load`, `Antenna_n_cable_check`, `Earth_resistance`, `EorN_voltage`, `eqpt_status_after_check`, `REMARKS`, `Unit_incharge_approval`, `s_verify`, `status`) VALUES
(1, '2020-04-03', '10:05:06', 1, 4156, 3, 'Cleaning performed.', '15hrs ', 'Can withstand load ', 'All antennas and cables properly connected.', 'All connections are maintained.', 25, 'GOOD', NULL, 'YES', NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `dscnweekly`
--

DROP TABLE IF EXISTS `dscnweekly`;
CREATE TABLE IF NOT EXISTS `dscnweekly` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` int(11) NOT NULL,
  `Air_conditioning_check` tinytext,
  `Cleaning_DSCN_associated_eqpt` tinytext,
  `UPS1_UPS2_battery_backup` tinytext,
  `UPS_battery_voltage_on_load` tinytext,
  `Antenna_n_Cable_check` tinytext,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `f_id` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dscnweekly`
--

INSERT INTO `dscnweekly` (`p_id`, `date`, `time`, `a_id`, `emp_id`, `f_id`, `Air_conditioning_check`, `Cleaning_DSCN_associated_eqpt`, `UPS1_UPS2_battery_backup`, `UPS_battery_voltage_on_load`, `Antenna_n_Cable_check`, `REMARKS`, `Unit_incharge_approval`, `s_verify`, `status`) VALUES
(1, '2020-03-26', '14:06:03', 1, 4156, 3, 'ALL installed AC\'s working.', 'ALL DSCN related equipments were cleaned.', 'UPS1 & UPS2 battery backup maintained.', 'Can withstand load', 'All cables and Antenna properly connected', NULL, 'YES', NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE IF NOT EXISTS `employee` (
  `emp_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `designation` varchar(10) NOT NULL,
  `a_id` int(11) NOT NULL,
  PRIMARY KEY (`emp_id`) USING BTREE,
  KEY `a_id` (`a_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`emp_id`, `name`, `designation`, `a_id`) VALUES
(1101, 'Hannibal Lecter', 'ED CNS', 1),
(2102, 'Linus Torvaldas', 'DGM', 1),
(3112, 'BP Singh', 'AGM CT', 1),
(3181, 'Mahesh Gotawandi', 'AGM SR', 1),
(3193, 'Corey Schrafer', 'AGM CE', 1),
(4121, 'Umesh Yadav', 'MGR CT', 1),
(4123, 'Ketan Hackerman', 'AM', 1),
(4129, 'Ramesh Sharma', 'JET', 1),
(4131, 'Chandresh Reddy', 'MGR SR', 1),
(4132, 'Suresh Kelkar', 'AM', 1),
(4133, 'Thon Thangal', 'JET', 1),
(4144, 'Hudson Odoi', 'AM', 1),
(4156, 'Mason Mount', 'JET', 1),
(4169, 'Varun Naik', 'MGR CE', 1);

-- --------------------------------------------------------

--
-- Table structure for table `engineer`
--

DROP TABLE IF EXISTS `engineer`;
CREATE TABLE IF NOT EXISTS `engineer` (
  `emp_id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `designation` varchar(10) DEFAULT NULL,
  `a_id` int(11) DEFAULT NULL,
  `dept` varchar(1) DEFAULT NULL,
  `contact` int(11) DEFAULT NULL,
  `password` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `supervisor_id` int(11) DEFAULT NULL,
  `email` varchar(30) NOT NULL DEFAULT 'bro@gmail.com',
  PRIMARY KEY (`emp_id`),
  KEY `a_id` (`a_id`),
  KEY `supervisor_id` (`supervisor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `engineer`
--

INSERT INTO `engineer` (`emp_id`, `name`, `designation`, `a_id`, `dept`, `contact`, `password`, `supervisor_id`, `email`) VALUES
(4121, 'Umesh Yadav', 'MGR CT', 1, 'N', 213112, 'pbkdf2_sha256$180000$Kj8R19kacWs5$72QHE97Jv6lEBHE7+BTdxvvSq3F9Wde8dA5lzwbGDqY=', 3112, 'bro@gmail.com'),
(4123, 'Ketan Hackerman', 'AM', 1, 'N', 21343, 'pbkdf2_sha256$180000$JAMo3q70IL9k$IpOIzvv+SQgd8ZQG2rzmkWDBfJTJGudEfmxj1sV4YQc=', 3112, 'bro@gmail.com'),
(4129, 'Ramesh Sharma', 'JET', 1, 'N', 32412, 'pbkdf2_sha256$180000$diZOk8Rzg1jx$hs/Io2JxPemTz/XiP1p/1ZNseMjMDi87l8hmWF/nmcI=', 3112, 'bro@gmail.com'),
(4131, 'Chandresh Reddy', 'MGR SR', 1, 'S', 21315, 'pbkdf2_sha256$180000$KqlhlXzv8Mjd$Jz3b0MbUJiah//q+7bR17PzYMZarf0/bjtSY2m3Im5E=', 3181, 'bro@gmail.com'),
(4132, 'Suresh Kelkar', 'AM', 1, 'S', 12312, 'pbkdf2_sha256$180000$TyI6a1BHImPz$T138jiTOLZO5K4cIoLP4HTS/Ips0oyFJX4XmF/rvp6Y=', 3181, 'bro@gmail.com'),
(4133, 'bobby', 'JET', 1, 'N', 44499, 'pbkdf2_sha256$180000$3mDUpcCefGhT$ISSBIRA6W4A34bfUm/5Q36geKPDs5LhGl5decyPhLTA=', 3112, 'bro@gmail.com'),
(4144, 'Hudson Odoi', 'AM', 1, 'C', 23231, 'pbkdf2_sha256$180000$0gx6UouLSNhm$reJqcqeiPkGZncq2y/Xbw/BdkhnaQoA08Lo7AepAEJE=', 3193, 'bro@gmail.com'),
(4156, 'Mason Mount', 'JET', 1, 'C', 231123, 'pbkdf2_sha256$180000$jSyJMRXoC0OR$WRh6O+2VZnlicZqvopk6Iz6NPzj1tcv+OrkGa71r/bA=', 3193, 'bro@gmail.com'),
(4169, 'Varun Naik', 'MGR CE', 1, 'C', 866651, 'pbkdf2_sha256$180000$u14lkS5xAW9g$N4A5ZRz8byVghDGCYfIfZKi8mbd2+oS45clKoeOKHJQ=', 3193, 'bro@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `head`
--

DROP TABLE IF EXISTS `head`;
CREATE TABLE IF NOT EXISTS `head` (
  `head_id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `designation` varchar(10) DEFAULT NULL,
  `contact` int(11) DEFAULT NULL,
  `password` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  PRIMARY KEY (`head_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `head`
--

INSERT INTO `head` (`head_id`, `name`, `designation`, `contact`, `password`) VALUES
(1101, 'Hannibal Lecter', 'ED CNS', 95187238, 'pbkdf2_sha256$180000$etVquvJaLhJ9$eL823OLaqGzqVY+2TI+vS0LFatJ280UlOWm9Ns63bdU=');

-- --------------------------------------------------------

--
-- Table structure for table `issues`
--

DROP TABLE IF EXISTS `issues`;
CREATE TABLE IF NOT EXISTS `issues` (
  `issue_no` int(11) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `Topic` varchar(30) NOT NULL,
  `desgn` varchar(10) DEFAULT NULL,
  `dept` varchar(1) DEFAULT NULL,
  `facility_affected` varchar(20) DEFAULT NULL,
  `observations` tinytext,
  `actions_taken` tinytext,
  `approved_by` int(11) DEFAULT NULL,
  PRIMARY KEY (`issue_no`,`date`,`a_id`),
  UNIQUE KEY `issue_no` (`issue_no`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `approved_by` (`approved_by`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `issues`
--

INSERT INTO `issues` (`issue_no`, `date`, `a_id`, `emp_id`, `Topic`, `desgn`, `dept`, `facility_affected`, `observations`, `actions_taken`, `approved_by`) VALUES
(503, '2020-03-24 10:48:19', 1, 4144, 'BIT TEST FAILURE', 'AM', 'C', 'VHF RX (PAE)', 'Bit test failure was observed. This lead to non availability of the instrument.', 'Switched to standby receiver from VCS operator position for tower main frequency i.e. 118.65 MHz.', 3193),
(504, '2020-03-24 10:48:35', 1, 4156, 'SQUELCH DEFEAT', 'JET', 'C', 'VHF RX (PAE)', 'Ready signal not found to be Standard. Squelch defeat was observed to be ON. Squelch threshold varying more than usual. ', 'ATCO switched to alternate frequency', 3193),
(517, '2020-03-24 10:48:55', 1, 4169, 'BIT TEST FAILURE', 'MGR CE', 'C', 'VHF RX (PAE)', 'Bit test failure and abnormal AC to DC changeover observed. Referred to AGM-CE.\r\n', 'Emergency frequency utilised as per standard operating procedure from standard transmitter at EMERGENCY frequency of 121.5 MHz.', 2102),
(518, '2020-03-24 10:49:12', 1, 4169, 'UPS FAULTS', 'MGR CE', 'C', 'DSCN', 'Less voltage generated at the output side of the UPS. This giving rise to even lesser and insufficient battery voltage of 170V.\r\n', 'Class B surge diverter was found producing anomalies. Standby replacement was used on MGR CE\'s recommendation.', 3193),
(519, '2020-03-24 10:49:41', 1, 4129, 'SURGE DIVERTER FAULTS', 'JET', 'N', 'DVOR', 'PS 5V,PS 12V,PS -12V, reading deviating too much. This caused temperature to rise beyond the threshold of 70 degrees, recording 79 degrees.\r\nClass C surge diverter found faulty.', 'Class C surge diverter sent for repairing. Facility suspended till further notice.', 3112),
(520, '2020-03-24 10:49:56', 1, 4123, 'CLEANLINESS', 'AM', 'N', 'DME (HP)', 'Battery room not clean. This led to less voltage generation as per recommendation. This further lead to the sound produced by the DME due to low power supply.', 'Room was cleaned and the connections were thoroughly checked.', 3112),
(521, '2020-03-24 10:50:10', 1, 4129, 'UPS FAULTS', 'JET', 'N', 'NDB', 'Forward power observed to be very less (80W) as compared to (100W). This has led to decrease in reflected power.\r\n', 'Fault in UPS 1(Master) power supply. No spares available. This particular NDB is suspended until further notice. Spare NDB from Udaipur station has been called out. ', 2102);

-- --------------------------------------------------------

--
-- Table structure for table `mcdo`
--

DROP TABLE IF EXISTS `mcdo`;
CREATE TABLE IF NOT EXISTS `mcdo` (
  `emp_id` int(11) NOT NULL,
  `a_id` int(11) NOT NULL,
  `topic` varchar(50) NOT NULL,
  `DOP` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `content` tinytext NOT NULL,
  `DOA` timestamp NULL DEFAULT NULL,
  `approved_by` int(11) DEFAULT NULL,
  PRIMARY KEY (`emp_id`,`a_id`),
  KEY `a_id` (`a_id`),
  KEY `approved_by` (`approved_by`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mcdo`
--

INSERT INTO `mcdo` (`emp_id`, `a_id`, `topic`, `DOP`, `content`, `DOA`, `approved_by`) VALUES
(4131, 1, 'Enhancement of Surveillance Facilities', '2020-03-30 11:06:33', '1. Drone based surveillance pioneer.\r\n2. Zero faults return in scheduled maintenance for a period of 2 months.', '2020-04-02 11:06:33', 3181);

-- --------------------------------------------------------

--
-- Table structure for table `navigation`
--

DROP TABLE IF EXISTS `navigation`;
CREATE TABLE IF NOT EXISTS `navigation` (
  `f_id` varchar(10) NOT NULL,
  `a_id` int(11) NOT NULL,
  `facility` varchar(20) DEFAULT NULL,
  `frequency` int(11) DEFAULT NULL,
  `power` int(11) DEFAULT NULL,
  `IDNT` varchar(10) DEFAULT NULL,
  `coordinateN` varchar(11) DEFAULT NULL,
  `coordinateE` varchar(11) DEFAULT NULL,
  `eqpt` varchar(20) DEFAULT NULL,
  `DOI` date DEFAULT NULL,
  `DOC` date DEFAULT NULL,
  `emp_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`f_id`,`a_id`),
  UNIQUE KEY `f_id` (`f_id`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `navigation`
--

INSERT INTO `navigation` (`f_id`, `a_id`, `facility`, `frequency`, `power`, `IDNT`, `coordinateN`, `coordinateE`, `eqpt`, `DOI`, `DOC`, `emp_id`) VALUES
('1', 1, 'DVOR', 117, 100, 'QQZ', '22 19\'58.2', '73 13\'30.5', 'AMS 1150', '2001-09-11', '2001-09-18', 4129),
('2', 1, 'DME (HP)', 1144, 1000, 'QQZ', '22 19\'58.2', '73 13\'30.5', 'GCEL 753', '2001-10-19', '2001-10-28', 4121),
('3', 1, 'NDB', 0, 100, 'QZ', '22 20\'5.2', '73 12\'33.6', 'SAC-100', '2019-07-22', '2019-11-07', 4123);

-- --------------------------------------------------------

--
-- Table structure for table `ndbdaily`
--

DROP TABLE IF EXISTS `ndbdaily`;
CREATE TABLE IF NOT EXISTS `ndbdaily` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `room_temp` int(11) DEFAULT NULL,
  `ac_mains_voltage_50Hz` int(11) DEFAULT NULL,
  `battery_voltage` int(11) DEFAULT NULL,
  `reflected_power` int(11) DEFAULT NULL,
  `forward_power` int(11) DEFAULT NULL,
  `modulation` int(11) DEFAULT NULL,
  `system_status_LED` varchar(3) DEFAULT NULL,
  `Primary_TX_LED` varchar(3) DEFAULT NULL,
  `TX_power_ON_LED` varchar(3) DEFAULT NULL,
  `remote_ctrl_link_LED` varchar(20) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ndbdaily`
--

INSERT INTO `ndbdaily` (`date`, `a_id`, `emp_id`, `f_id`, `room_temp`, `ac_mains_voltage_50Hz`, `battery_voltage`, `reflected_power`, `forward_power`, `modulation`, `system_status_LED`, `Primary_TX_LED`, `TX_power_ON_LED`, `remote_ctrl_link_LED`, `REMARKS`, `Unit_incharge_approval`, `p_id`, `s_verify`, `status`) VALUES
('2020-03-24 10:37:54', 1, 4121, '3', 20, 230, 21, 18, 100, 90, 'ON', 'ON', 'ON', 'BLINKING', NULL, 'YES', 1, NULL, ''),
('2020-03-24 10:37:57', 1, 4121, '3', 20, 225, 24, 18, 100, 87, 'ON', 'ON', 'ON', 'BLINKING', NULL, 'YES', 2, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `ndbmonthly`
--

DROP TABLE IF EXISTS `ndbmonthly`;
CREATE TABLE IF NOT EXISTS `ndbmonthly` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `frwd_power_modulation_OFF` int(11) DEFAULT NULL,
  `reflected_power` int(11) DEFAULT NULL,
  `modulation_depth_check` int(11) DEFAULT NULL,
  `ident_code_check` varchar(10) DEFAULT NULL,
  `antenna_n_ACU_check` varchar(20) DEFAULT NULL,
  `NDB_eqpt_n_ACU_cleaning` varchar(10) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ndbmonthly`
--

INSERT INTO `ndbmonthly` (`date`, `a_id`, `emp_id`, `f_id`, `frwd_power_modulation_OFF`, `reflected_power`, `modulation_depth_check`, `ident_code_check`, `antenna_n_ACU_check`, `NDB_eqpt_n_ACU_cleaning`, `REMARKS`, `Unit_incharge_approval`, `p_id`, `s_verify`, `status`) VALUES
('2020-03-24 10:38:26', 1, 4121, '3', 100, 15, 92, 'VALID', 'GOOD', 'DONE', NULL, 'YES', 1, NULL, ''),
('2020-03-24 10:38:29', 1, 4129, '3', 80, 10, 82, 'VALID', 'GOOD', 'DONE', 'Forward power observed to be very less (80W) as compared to (100W). This has led to decrease in reflected power.\r\nReferred to AGM-CT. Issue no. 521.', 'NO', 2, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `ndbweekly`
--

DROP TABLE IF EXISTS `ndbweekly`;
CREATE TABLE IF NOT EXISTS `ndbweekly` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `mains_pwr_supply_check` tinytext,
  `battery_terminals_check` tinytext,
  `battery_sealed` varchar(3) DEFAULT NULL,
  `specific_gravity` float DEFAULT NULL,
  `antenna_site_condition` tinytext,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ndbweekly`
--

INSERT INTO `ndbweekly` (`date`, `a_id`, `emp_id`, `f_id`, `mains_pwr_supply_check`, `battery_terminals_check`, `battery_sealed`, `specific_gravity`, `antenna_site_condition`, `REMARKS`, `Unit_incharge_approval`, `p_id`, `s_verify`, `status`) VALUES
('2020-03-24 10:38:48', 1, 4123, '3', 'OK', 'OK', 'YES', 12.3, 'OK', NULL, 'YES', 1, NULL, ''),
('2020-03-24 10:38:51', 1, 4129, '3', 'OK', 'OK', 'NO', 12, 'OK', NULL, 'YES', 2, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `scctvdaily`
--

DROP TABLE IF EXISTS `scctvdaily`;
CREATE TABLE IF NOT EXISTS `scctvdaily` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `UPS_battery_indication` varchar(20) DEFAULT NULL,
  `Servers_ON_condition` varchar(10) DEFAULT NULL,
  `NAS_status_in_VMSorVRM` varchar(10) DEFAULT NULL,
  `recording_active_status_VRS_server` int(11) DEFAULT NULL,
  `recording_active_status_RRS_server` varchar(20) DEFAULT NULL,
  `database_status_VMS` varchar(10) DEFAULT NULL,
  `cameras_IVMS` varchar(10) DEFAULT NULL,
  `eqpt_cleaning` varchar(20) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `scctvdaily`
--

INSERT INTO `scctvdaily` (`date`, `a_id`, `emp_id`, `f_id`, `UPS_battery_indication`, `Servers_ON_condition`, `NAS_status_in_VMSorVRM`, `recording_active_status_VRS_server`, `recording_active_status_RRS_server`, `database_status_VMS`, `cameras_IVMS`, `eqpt_cleaning`, `REMARKS`, `Unit_incharge_approval`, `p_id`, `s_verify`, `status`) VALUES
('2020-03-24 10:41:57', 1, 4132, '3', 'FULL', 'OK', 'OK', 32, 'PAUSE', 'OK', 'OK', 'OK', NULL, 'YES', 1, NULL, ''),
('2020-03-24 10:42:00', 1, 4133, '3', 'FULL', 'OK', 'OK', 32, 'PAUSE', 'OK', 'OK', 'CARRIED OUT', NULL, 'YES', 2, NULL, ''),
('2020-03-24 10:42:03', 1, 4131, '3', 'FULL', 'OK', 'OK', 32, 'PAUSE', 'OK', 'OK', 'OK', NULL, 'YES', 3, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `scctvmonthly`
--

DROP TABLE IF EXISTS `scctvmonthly`;
CREATE TABLE IF NOT EXISTS `scctvmonthly` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `ups_ip_voltage` int(11) DEFAULT NULL,
  `ups_op_voltage` int(11) DEFAULT NULL,
  `ups_battery_op_voltage_ACpwrON` int(11) DEFAULT NULL,
  `ups_battery_op_voltage_ACpwrOFF` int(11) DEFAULT NULL,
  `ups_battery_op_voltage_after15min_ACpwrOFF` int(11) DEFAULT NULL,
  `server_status` varchar(5) DEFAULT NULL,
  `cameras_in_VRS_server` varchar(20) DEFAULT NULL,
  `NAS_free_capacity` float DEFAULT NULL,
  `OFClinkto_L2L3_switches` varchar(20) DEFAULT NULL,
  `cleaning_camera_eqpt` varchar(20) DEFAULT NULL,
  `user_rights_check` varchar(10) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `scctvmonthly`
--

INSERT INTO `scctvmonthly` (`date`, `a_id`, `emp_id`, `f_id`, `ups_ip_voltage`, `ups_op_voltage`, `ups_battery_op_voltage_ACpwrON`, `ups_battery_op_voltage_ACpwrOFF`, `ups_battery_op_voltage_after15min_ACpwrOFF`, `server_status`, `cameras_in_VRS_server`, `NAS_free_capacity`, `OFClinkto_L2L3_switches`, `cleaning_camera_eqpt`, `user_rights_check`, `REMARKS`, `Unit_incharge_approval`, `p_id`, `s_verify`, `status`) VALUES
('2020-03-24 10:42:17', 1, 4133, '3', 235, 225, 203, 191, 176, 'ON', 'ACCESSIBLE', 1.24, 'BLINKING GREEN', 'CARRIED OUT', 'OK', NULL, 'YES', 1, NULL, ''),
('2020-03-24 10:42:19', 1, 4132, '3', 230, 225, 208, 186, 176, 'ON', 'OK', 9.2, 'BLINKING GREEN', 'CARRIED OUT', 'OK', NULL, 'YES', 2, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `scctvweekly`
--

DROP TABLE IF EXISTS `scctvweekly`;
CREATE TABLE IF NOT EXISTS `scctvweekly` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `ups_ip_voltage` int(11) DEFAULT NULL,
  `ups_op_voltage` int(11) DEFAULT NULL,
  `ups_battery_status` varchar(10) DEFAULT NULL,
  `server_status` varchar(5) DEFAULT NULL,
  `camera_NAS_status_in_VRS` varchar(10) DEFAULT NULL,
  `workstns_n_client_softw_check` varchar(10) DEFAULT NULL,
  `cameras_client_IVMS_softw` varchar(10) DEFAULT NULL,
  `NAS_free_capacity` float DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `scctvweekly`
--

INSERT INTO `scctvweekly` (`date`, `a_id`, `emp_id`, `f_id`, `ups_ip_voltage`, `ups_op_voltage`, `ups_battery_status`, `server_status`, `camera_NAS_status_in_VRS`, `workstns_n_client_softw_check`, `cameras_client_IVMS_softw`, `NAS_free_capacity`, `REMARKS`, `Unit_incharge_approval`, `p_id`, `s_verify`, `status`) VALUES
('2020-03-24 10:42:34', 1, 4131, '3', 230, 225, 'FULL', 'OK', 'OK', 'OK', 'OK', 1.23, 'NAS_free_capacity not to be equal to 0.', 'YES', 1, NULL, ''),
('2020-03-24 10:42:37', 1, 4132, '3', 225, 220, 'FULL', 'OK', 'OK', 'OK', 'OK', 1.34, NULL, 'YES', 2, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `supervisor`
--

DROP TABLE IF EXISTS `supervisor`;
CREATE TABLE IF NOT EXISTS `supervisor` (
  `supervisor_id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `designation` varchar(10) DEFAULT NULL,
  `a_id` int(11) DEFAULT NULL,
  `dept` varchar(1) DEFAULT NULL,
  `contact` int(11) DEFAULT NULL,
  `password` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `dgm_id` int(11) DEFAULT NULL,
  `email` varchar(30) NOT NULL DEFAULT 'hello@gmail.com',
  PRIMARY KEY (`supervisor_id`),
  KEY `a_id` (`a_id`),
  KEY `dgm_id` (`dgm_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `supervisor`
--

INSERT INTO `supervisor` (`supervisor_id`, `name`, `designation`, `a_id`, `dept`, `contact`, `password`, `dgm_id`, `email`) VALUES
(3112, 'BP Singh', 'AGM CT', 1, 'N', 1122121, 'pbkdf2_sha256$180000$olWqd4mSQKuK$vfdND+Nh6wKyerQ5VnlHKd3F/qw4z23QnDULN52vxn0=', 2102, 'hello@gmail.com'),
(3181, 'Mahesh Gotawandi', 'AGM SR', 1, 'S', 3211122, 'pbkdf2_sha256$180000$emnVA6NyWm1x$wpwILWSGgc2CLasfATRPm0vYinsPg4LWpdQvlIJBv0M=', 2102, 'hello@gmail.com'),
(3193, 'Corey Schrafer', 'AGM CE', 1, 'C', 121212, 'pbkdf2_sha256$180000$IcWsycUfGh6U$pAnm3Se2RLkiSCnsM4xV/NAqYDMB58sPxshHXSS40ro=', 2102, 'hello@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `surveillance`
--

DROP TABLE IF EXISTS `surveillance`;
CREATE TABLE IF NOT EXISTS `surveillance` (
  `f_id` int(11) NOT NULL,
  `a_id` int(11) NOT NULL,
  `facility` varchar(20) DEFAULT NULL,
  `eqpt` varchar(20) DEFAULT NULL,
  `DOI` date DEFAULT NULL,
  `DOC` date DEFAULT NULL,
  `emp_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`f_id`,`a_id`),
  UNIQUE KEY `f_id` (`f_id`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `surveillance`
--

INSERT INTO `surveillance` (`f_id`, `a_id`, `facility`, `eqpt`, `DOI`, `DOC`, `emp_id`) VALUES
(1, 1, 'X-BIS', 'H.S.6040i', '2007-12-10', '2008-01-19', 4131),
(2, 1, 'ETD', '500 T', '2000-08-09', '0200-08-18', 4131),
(3, 1, 'SCCTV', 'INFINOVA', '1999-09-08', '1999-10-11', 4133);

-- --------------------------------------------------------

--
-- Table structure for table `vhfdaily`
--

DROP TABLE IF EXISTS `vhfdaily`;
CREATE TABLE IF NOT EXISTS `vhfdaily` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(11) DEFAULT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `status` varchar(40) NOT NULL,
  `f_id` int(11) NOT NULL DEFAULT '1',
  `a_id` int(11) NOT NULL,
  `RX_no` int(11) DEFAULT NULL,
  `frequency_MHz` int(11) DEFAULT NULL,
  `bit_test` varchar(10) DEFAULT NULL,
  `vstatus` varchar(10) DEFAULT NULL,
  `RXN_check` varchar(10) DEFAULT NULL,
  `ACorDC_CorO` varchar(10) DEFAULT NULL,
  `SQ_threshold` int(11) DEFAULT NULL,
  `Remarks` tinytext,
  `Unit_Incharge_Approval` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `f_id` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vhfdaily`
--

INSERT INTO `vhfdaily` (`p_id`, `s_verify`, `date`, `time`, `emp_id`, `status`, `f_id`, `a_id`, `RX_no`, `frequency_MHz`, `bit_test`, `vstatus`, `RXN_check`, `ACorDC_CorO`, `SQ_threshold`, `Remarks`, `Unit_Incharge_Approval`) VALUES
(1, NULL, '2020-03-27', '11:04:05', 4144, '', 1, 1, 1, 120, 'PASS', 'READY', 'RXN NORMAL', 'C/O NORMAL', -85, 'SQ threshold < -80 DBm as expected.\r\nMaintenance carried out for VHF RX for model type of PAE.', 'YES'),
(2, NULL, '2020-03-28', '12:04:07', 4144, '', 1, 1, 1, 122, 'PASS', 'READY', 'RXN NORMAL', 'C/O NORMAL', -81, 'Pass', 'YES'),
(3, NULL, '2020-03-29', '15:06:06', 4156, '', 1, 1, 1, 119, 'PASS', 'READY', 'RXN NORMAL', 'C/O NORMAL', -82, NULL, 'YES'),
(4, NULL, '2020-03-30', '22:37:04', 4144, '', 1, 1, 1, 123, 'PASS', 'READY', 'RXN NORMAL', NULL, -82, NULL, 'YES'),
(5, NULL, '2020-03-31', '11:02:13', 4169, '', 1, 1, 1, 120, 'PASS', 'READY', 'RXN NORMAL', NULL, -83, NULL, 'YES'),
(6, NULL, '2020-04-01', '12:40:49', 4156, '', 1, 1, 1, 123, 'PASS', 'READY', 'RXN NORMAL', NULL, -83, NULL, 'YES'),
(7, NULL, '2020-04-02', '13:12:52', 4144, '', 1, 1, 1, 120, 'PASS', 'READY', 'RXN NORMAL', NULL, -82, NULL, 'YES'),
(8, NULL, '2020-04-07', '17:28:28', 4156, 'COMPLETED', 1, 1, 1, 120, 'PASS', 'READY', 'RXN NORMAL', NULL, -82, NULL, 'YES'),
(9, NULL, '2020-04-14', '21:40:49', 4156, 'COMPLETED', 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL),
(10, NULL, '2020-04-15', '00:24:04', 4156, '', 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `vhfdlogs`
--

DROP TABLE IF EXISTS `vhfdlogs`;
CREATE TABLE IF NOT EXISTS `vhfdlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `value` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vhfdlogs`
--

INSERT INTO `vhfdlogs` (`log_id`, `emp_id`, `remarks`, `value`, `date`, `time`) VALUES
(1, 4144, 'Bit test failed', 'FAIL', '2020-03-27', '22:37:04'),
(2, 4144, 'Not Ready', 'NOT READY', '2020-03-27', '22:37:04'),
(3, 4144, 'SQ Threshold above -80 Db', '-82', '2020-03-27', '22:37:04'),
(4, 4144, 'Not Ready(update)', 'NOT READY', '2020-03-27', '22:37:39'),
(5, 4144, 'SQ Threshold above -80 Db(update)', '-82', '2020-03-27', '22:37:39'),
(6, 4144, 'SQ Threshold above -80 Db(update)', '-82', '2020-03-27', '22:37:57'),
(7, 4144, 'Parameter/s fixed', 'All parameters NORMAL', '2020-03-27', '22:37:57'),
(8, 4144, 'Bit test failed', 'READY', '2020-03-28', '11:02:13'),
(9, 4144, 'Not Ready', 'OK', '2020-03-28', '11:02:13'),
(10, 4144, 'SQ Threshold above -80 Db', '-83', '2020-03-28', '11:02:13'),
(11, 4144, 'SQ Threshold above -80 Db(update)', '-83', '2020-03-28', '11:02:29'),
(12, 4144, 'Parameter/s fixed', 'All parameters NORMAL', '2020-03-28', '11:02:29'),
(13, 4156, 'SQ Threshold above -80 Db', '-83', '2020-04-01', '12:40:49'),
(14, 4144, 'SQ Threshold above -80 Db', '-82', '2020-04-02', '13:12:52'),
(15, 4156, 'SQ Threshold above -80 Db', '-82', '2020-04-03', '17:28:28');

-- --------------------------------------------------------

--
-- Table structure for table `vhfmlogs`
--

DROP TABLE IF EXISTS `vhfmlogs`;
CREATE TABLE IF NOT EXISTS `vhfmlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `value` varchar(30) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vhfmlogs`
--

INSERT INTO `vhfmlogs` (`log_id`, `emp_id`, `value`, `remarks`, `date`, `time`) VALUES
(1, 4144, '-116', 'Squelch Threshold not normal ', '2020-03-28', '01:32:06'),
(2, 4144, 'ON', 'Squelch carrier Override is not off', '2020-03-28', '01:32:06'),
(3, 4144, 'ST', 'SQUELCH O/P FACILITIES not standard', '2020-03-28', '01:32:06'),
(4, 4144, 'ON', 'Squelch carrier Override is not off(update)', '2020-03-28', '01:32:11'),
(5, 4144, 'ST', 'SQUELCH O/P FACILITIES not standard(update)', '2020-03-28', '01:32:11'),
(6, 4144, 'All parameters NORMAL', 'Parameter/s fixed', '2020-03-28', '01:32:19');

-- --------------------------------------------------------

--
-- Table structure for table `vhfmonthly`
--

DROP TABLE IF EXISTS `vhfmonthly`;
CREATE TABLE IF NOT EXISTS `vhfmonthly` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` int(11) NOT NULL DEFAULT '1',
  `a_id` int(11) NOT NULL,
  `modulation_mode` varchar(10) DEFAULT NULL,
  `line_op` int(11) DEFAULT NULL,
  `squelch_defeat` varchar(3) DEFAULT NULL,
  `squelch_threshold` int(11) DEFAULT NULL,
  `squelch_carrier_override` varchar(3) DEFAULT NULL,
  `RF_pre_ATTN` varchar(3) DEFAULT NULL,
  `AGC` varchar(3) DEFAULT NULL,
  `Ready_signal` varchar(5) DEFAULT NULL,
  `Squelch_op_marc` varchar(5) DEFAULT NULL,
  `Squelch_op_facilities` varchar(5) DEFAULT NULL,
  `Squelch_op_phantom` varchar(5) DEFAULT NULL,
  `Squelch_defeat_ip` varchar(5) DEFAULT NULL,
  `bit_test` varchar(10) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  UNIQUE KEY `date_2` (`date`),
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `f_id` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vhfmonthly`
--

INSERT INTO `vhfmonthly` (`p_id`, `date`, `time`, `emp_id`, `f_id`, `a_id`, `modulation_mode`, `line_op`, `squelch_defeat`, `squelch_threshold`, `squelch_carrier_override`, `RF_pre_ATTN`, `AGC`, `Ready_signal`, `Squelch_op_marc`, `Squelch_op_facilities`, `Squelch_op_phantom`, `Squelch_defeat_ip`, `bit_test`, `REMARKS`, `Unit_incharge_approval`, `s_verify`, `status`) VALUES
(1, '2020-01-27', '11:24:47', 4169, 1, 1, 'AM-Voice', 12, 'OFF', -107, 'OFF', 'OFF', 'ON', 'STD', 'STD', 'STD', 'STD', 'STD', 'OK', NULL, 'YES', NULL, ''),
(2, '2020-02-26', '11:24:57', 4156, 1, 1, 'AM-Voice', 11, 'OFF', -103, 'OFF', 'OFF', 'ON', 'STD', 'STD', 'STD', 'STD', 'STD', 'OK', '', 'YES', NULL, ''),
(3, '2020-03-28', '01:32:06', 4144, 1, 1, 'AM-Voice', 11, 'OFF', -113, 'OFF', 'OFF', 'ON', 'STD', 'STD', 'STD', 'STD', 'STD', 'OK', NULL, 'YES', NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `vhfyearly`
--

DROP TABLE IF EXISTS `vhfyearly`;
CREATE TABLE IF NOT EXISTS `vhfyearly` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` int(11) NOT NULL DEFAULT '1',
  `a_id` int(11) NOT NULL,
  `RX_no` int(11) DEFAULT '1',
  `frequency_MHz` float DEFAULT NULL,
  `reference_freq` float DEFAULT NULL,
  `power` int(11) DEFAULT NULL,
  `bit_test` varchar(5) DEFAULT NULL,
  `AC_DC_changeover` varchar(20) DEFAULT NULL,
  `Remarks` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `f_id` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vhfyearly`
--

INSERT INTO `vhfyearly` (`p_id`, `date`, `time`, `emp_id`, `f_id`, `a_id`, `RX_no`, `frequency_MHz`, `reference_freq`, `power`, `bit_test`, `AC_DC_changeover`, `Remarks`, `Unit_incharge_approval`, `s_verify`, `status`) VALUES
(1, '2018-03-29', '15:20:34', 4156, 1, 1, 1, 119, 20.95, 43, 'PASS', 'NORMAL(DC)', 'Every parameter was observed to be normal.', 'YES', NULL, ''),
(2, '2019-03-29', '11:40:12', 4169, 1, 1, 1, 120, 20.95, 26, 'PASS', 'NORMAL(DC)', NULL, 'YES', NULL, ''),
(3, '2020-03-28', '13:56:08', 4144, 1, 1, 1, 120, 20.95, 39, 'PASS', 'NORMAL(DC)', 'Parameter/s fixed', 'YES', NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `vhfylogs`
--

DROP TABLE IF EXISTS `vhfylogs`;
CREATE TABLE IF NOT EXISTS `vhfylogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `value` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vhfylogs`
--

INSERT INTO `vhfylogs` (`log_id`, `emp_id`, `remarks`, `value`, `date`, `time`) VALUES
(1, 4144, 'Bit Test failed', 'FAIL', '2020-03-28', '13:56:08'),
(2, 4144, 'Parameter/s fixed', 'All parameters NORMAL', '2020-03-28', '13:58:27'),
(3, 4144, 'Parameter/s fixed', 'All parameters NORMAL', '2020-03-28', '13:59:04');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `airport`
--
ALTER TABLE `airport`
  ADD CONSTRAINT `airport_ibfk_1` FOREIGN KEY (`dgm_id`) REFERENCES `dgm` (`dgm_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD CONSTRAINT `auth_user_ibfk_1` FOREIGN KEY (`username`) REFERENCES `dgm` (`dgm_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `auth_user_ibfk_2` FOREIGN KEY (`username`) REFERENCES `engineer` (`emp_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `auth_user_ibfk_3` FOREIGN KEY (`username`) REFERENCES `head` (`head_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `auth_user_ibfk_4` FOREIGN KEY (`username`) REFERENCES `supervisor` (`supervisor_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `cdvordaily`
--
ALTER TABLE `cdvordaily`
  ADD CONSTRAINT `CDVORDaily_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `cdvordaily_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `cdvormonthly`
--
ALTER TABLE `cdvormonthly`
  ADD CONSTRAINT `cdvormonthly_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `cdvormonthly_ibfk_2` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `cdvorweekly`
--
ALTER TABLE `cdvorweekly`
  ADD CONSTRAINT `CDVORWeekly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `cdvorweekly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `communication`
--
ALTER TABLE `communication`
  ADD CONSTRAINT `communication_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `communication_ibfk_3` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `datisdaily`
--
ALTER TABLE `datisdaily`
  ADD CONSTRAINT `datisdaily_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `datisdaily_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `datisdaily_ibfk_3` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `datisdlogs`
--
ALTER TABLE `datisdlogs`
  ADD CONSTRAINT `datisdlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `datisdlogs_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `datisdaily` (`p_id`) ON UPDATE CASCADE;

--
-- Constraints for table `datisweekly`
--
ALTER TABLE `datisweekly`
  ADD CONSTRAINT `datisweekly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `datisweekly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `datisweekly_ibfk_3` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `datiswlogs`
--
ALTER TABLE `datiswlogs`
  ADD CONSTRAINT `datiswlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `datiswlogs_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `datisweekly` (`p_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dgm`
--
ALTER TABLE `dgm`
  ADD CONSTRAINT `dgm_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `dgm_ibfk_2` FOREIGN KEY (`head_id`) REFERENCES `head` (`head_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `dmedaily`
--
ALTER TABLE `dmedaily`
  ADD CONSTRAINT `DMEDaily_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `dmedaily_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dmemonthly`
--
ALTER TABLE `dmemonthly`
  ADD CONSTRAINT `DMEMonthly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `dmemonthly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dmeweekly`
--
ALTER TABLE `dmeweekly`
  ADD CONSTRAINT `DMEWeekly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `dmeweekly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dscndaily`
--
ALTER TABLE `dscndaily`
  ADD CONSTRAINT `DSCNDaily_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `dscndaily_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `dscndaily_ibfk_3` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dscndlogs`
--
ALTER TABLE `dscndlogs`
  ADD CONSTRAINT `dscndlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dscnmonthly`
--
ALTER TABLE `dscnmonthly`
  ADD CONSTRAINT `DSCNMonthly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `dscnmonthly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dscnweekly`
--
ALTER TABLE `dscnweekly`
  ADD CONSTRAINT `DSCNWeekly_ibfk_3` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `dscnweekly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `dscnweekly_ibfk_2` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `engineer`
--
ALTER TABLE `engineer`
  ADD CONSTRAINT `engineer_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `engineer_ibfk_2` FOREIGN KEY (`supervisor_id`) REFERENCES `supervisor` (`supervisor_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `issues`
--
ALTER TABLE `issues`
  ADD CONSTRAINT `Issues_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `gaand_karta_chedeycha` FOREIGN KEY (`approved_by`) REFERENCES `employee` (`emp_id`),
  ADD CONSTRAINT `issues_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `mcdo`
--
ALTER TABLE `mcdo`
  ADD CONSTRAINT `mcdo_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `mcdo_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `employee` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `mcdo_ibfk_3` FOREIGN KEY (`approved_by`) REFERENCES `employee` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `navigation`
--
ALTER TABLE `navigation`
  ADD CONSTRAINT `navigation_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `navigation_ibfk_3` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `ndbdaily`
--
ALTER TABLE `ndbdaily`
  ADD CONSTRAINT `NDBDaily_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `ndbdaily_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `ndbmonthly`
--
ALTER TABLE `ndbmonthly`
  ADD CONSTRAINT `NDBMonthly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `ndbmonthly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `ndbweekly`
--
ALTER TABLE `ndbweekly`
  ADD CONSTRAINT `NDBWeekly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `ndbweekly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `scctvdaily`
--
ALTER TABLE `scctvdaily`
  ADD CONSTRAINT `SCCTVDaily_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `scctvdaily_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `scctvmonthly`
--
ALTER TABLE `scctvmonthly`
  ADD CONSTRAINT `SCCTVMonthly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `scctvmonthly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `scctvweekly`
--
ALTER TABLE `scctvweekly`
  ADD CONSTRAINT `SCCTVWeekly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `scctvweekly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `supervisor`
--
ALTER TABLE `supervisor`
  ADD CONSTRAINT `supervisor_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `supervisor_ibfk_2` FOREIGN KEY (`dgm_id`) REFERENCES `dgm` (`dgm_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `surveillance`
--
ALTER TABLE `surveillance`
  ADD CONSTRAINT `surveillance_ibfk_3` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `surveillance_ibfk_4` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `vhfdaily`
--
ALTER TABLE `vhfdaily`
  ADD CONSTRAINT `VHFDaily_ibfk_3` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `vhfdaily_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `vhfdaily_ibfk_2` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `vhfdlogs`
--
ALTER TABLE `vhfdlogs`
  ADD CONSTRAINT `vhfdlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE;

--
-- Constraints for table `vhfmonthly`
--
ALTER TABLE `vhfmonthly`
  ADD CONSTRAINT `VHFMonthly_ibfk_3` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `vhfmonthly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `vhfmonthly_ibfk_2` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `vhfyearly`
--
ALTER TABLE `vhfyearly`
  ADD CONSTRAINT `VHFYearly_ibfk_3` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `vhfyearly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `vhfyearly_ibfk_2` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `vhfylogs`
--
ALTER TABLE `vhfylogs`
  ADD CONSTRAINT `vhfylogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
