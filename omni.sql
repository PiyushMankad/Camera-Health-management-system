-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 14, 2018 at 02:02 PM
-- Server version: 10.1.32-MariaDB
-- PHP Version: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `omni`
--

-- --------------------------------------------------------

--
-- Table structure for table `advanceanalyticsdb`
--

CREATE TABLE `advanceanalyticsdb` (
  `EntryID` int(11) NOT NULL,
  `InfoCode` char(255) NOT NULL,
  `NumberOfPeople` int(11) DEFAULT NULL,
  `NumberOfAnimals` int(11) DEFAULT NULL,
  `NumberOfVehicles` int(11) DEFAULT NULL,
  `TimeStamp` datetime DEFAULT NULL,
  `CameraID` char(255) DEFAULT NULL,
  `CameraStatus` char(255) DEFAULT NULL,
  `ActionPending` char(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `advanceanalyticsdb`
--

INSERT INTO `advanceanalyticsdb` (`EntryID`, `InfoCode`, `NumberOfPeople`, `NumberOfAnimals`, `NumberOfVehicles`, `TimeStamp`, `CameraID`, `CameraStatus`, `ActionPending`) VALUES
(1, '0x0100', 1, 0, 0, '2018-06-12 13:24:01', '192.168.1.233', 'ACTIVE:', 'None'),
(2, '0x0100', 1, 0, 0, '2018-06-12 13:24:06', '192.168.1.233', 'ACTIVE:', 'None'),
(3, '0x0100', 0, 0, 0, '2018-06-12 13:24:12', '192.168.1.233', 'ACTIVE:', 'None'),
(4, '0x0100', 0, 0, 0, '2018-06-12 13:24:17', '192.168.1.233', 'ACTIVE:', 'None'),
(5, '0x0100', 0, 0, 0, '2018-06-12 13:24:23', '192.168.1.233', 'ACTIVE:', 'None'),
(6, '0x0100', 0, 0, 0, '2018-06-12 13:24:28', '192.168.1.233', 'ACTIVE:', 'None'),
(7, '0x0100', 1, 0, 0, '2018-06-12 13:24:33', '192.168.1.233', 'ACTIVE:', 'None'),
(8, '0x0100', 1, 0, 0, '2018-06-13 12:51:58', '192.168.1.233', 'ACTIVE:', 'None'),
(9, '0x0100', 0, 0, 0, '2018-06-13 12:52:04', '192.168.1.233', 'ACTIVE:', 'None'),
(10, '0x0100', 0, 0, 0, '2018-06-13 12:52:09', '192.168.1.233', 'ACTIVE:', 'None'),
(11, '0x0100', 0, 0, 0, '2018-06-13 12:52:14', '192.168.1.233', 'ACTIVE:', 'None'),
(12, '0x0100', 1, 0, 0, '2018-06-13 12:52:20', '192.168.1.233', 'ACTIVE:', 'None');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add permission', 3, 'add_permission'),
(8, 'Can change permission', 3, 'change_permission'),
(9, 'Can delete permission', 3, 'delete_permission'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add cameradb', 7, 'add_cameradb'),
(20, 'Can change cameradb', 7, 'change_cameradb'),
(21, 'Can delete cameradb', 7, 'delete_cameradb');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$36000$yCOUB0yKSQaE$qw2UaEwcHC5u3gl5KJTMQEos2fNbiEnmfIjChgUgsIo=', '2018-06-08 07:14:26.613000', 1, 'charu96', '', '', '', 1, 1, '2018-06-08 07:13:42.376000'),
(2, 'pbkdf2_sha256$36000$fm4VR1jAXiGL$bJvFILp93v4SgpL/TFOw+PMUiltVZEBlDh9Oxtu6g3s=', '2018-06-08 10:09:17.280000', 1, 'piyush', '', '', 'p@gmail.com', 1, 1, '2018-06-08 10:09:07.947000'),
(3, 'pbkdf2_sha256$36000$uVMnh06FZFva$u8+ToDVPOPWMQpEHSxZidWKR7SjXkDWEK3t37WigwTY=', '2018-06-12 06:17:12.032000', 1, 'omni', '', '', 'p@gmail.com', 1, 1, '2018-06-12 06:14:03.528000'),
(4, 'pbkdf2_sha256$36000$kaEi4SBRhqaJ$+rH0dexRFlMzFXDQ/pnjCnETrmBPSXkTgg8b/4fCpyI=', '2018-06-12 06:58:52.158000', 1, 'qw', '', '', '', 1, 1, '2018-06-12 06:58:34.556000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `cameradb`
--

CREATE TABLE `cameradb` (
  `EntryID` int(11) NOT NULL,
  `InfoCode` char(255) NOT NULL,
  `InfoType` char(255) DEFAULT NULL,
  `TimeStamp` datetime DEFAULT NULL,
  `CameraID` char(255) DEFAULT NULL,
  `CameraStatus` char(255) DEFAULT NULL,
  `ActionPending` char(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cameradb`
--

INSERT INTO `cameradb` (`EntryID`, `InfoCode`, `InfoType`, `TimeStamp`, `CameraID`, `CameraStatus`, `ActionPending`) VALUES
(1, '0x0011', 'INFO: New ROI Selected', '2018-06-12 10:53:40', '192.168.1.233', 'ACTIVE:', 'None'),
(2, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:02', '192.168.1.233', 'ACTIVE:', 'None'),
(3, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:02', '192.168.1.233', 'ACTIVE:', 'None'),
(4, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:02', '192.168.1.233', 'ACTIVE:', 'None'),
(5, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:03', '192.168.1.233', 'ACTIVE:', 'None'),
(6, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:03', '192.168.1.233', 'ACTIVE:', 'None'),
(7, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:03', '192.168.1.233', 'ACTIVE:', 'None'),
(8, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:03', '192.168.1.233', 'ACTIVE:', 'None'),
(9, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:03', '192.168.1.233', 'ACTIVE:', 'None'),
(10, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:03', '192.168.1.233', 'ACTIVE:', 'None'),
(11, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:15', '192.168.1.233', 'ACTIVE:', 'None'),
(12, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:15', '192.168.1.233', 'ACTIVE:', 'None'),
(13, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:15', '192.168.1.233', 'ACTIVE:', 'None'),
(14, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:15', '192.168.1.233', 'ACTIVE:', 'None'),
(15, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:16', '192.168.1.233', 'ACTIVE:', 'None'),
(16, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:16', '192.168.1.233', 'ACTIVE:', 'None'),
(17, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:16', '192.168.1.233', 'ACTIVE:', 'None'),
(18, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:16', '192.168.1.233', 'ACTIVE:', 'None'),
(19, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:16', '192.168.1.233', 'ACTIVE:', 'None'),
(20, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:25', '192.168.1.233', 'ACTIVE:', 'None'),
(21, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:25', '192.168.1.233', 'ACTIVE:', 'None'),
(22, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:25', '192.168.1.233', 'ACTIVE:', 'None'),
(23, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:25', '192.168.1.233', 'ACTIVE:', 'None'),
(24, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:25', '192.168.1.233', 'ACTIVE:', 'None'),
(25, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:26', '192.168.1.233', 'ACTIVE:', 'None'),
(26, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:26', '192.168.1.233', 'ACTIVE:', 'None'),
(27, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:26', '192.168.1.233', 'ACTIVE:', 'None'),
(28, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:54:26', '192.168.1.233', 'ACTIVE:', 'None'),
(29, '0x0011', 'INFO: New ROI Selected', '2018-06-12 10:55:46', '192.168.1.233', 'ACTIVE:', 'None'),
(30, '0w0010', 'Warning: Suspicious Activity', '2018-06-12 10:55:51', '192.168.1.233', 'ACTIVE:', 'None'),
(31, '0w0010', 'Warning: Suspicious Activity', '2018-06-12 10:55:51', '192.168.1.233', 'ACTIVE:', 'None'),
(32, '0w0010', 'Warning: Suspicious Activity', '2018-06-12 10:55:51', '192.168.1.233', 'ACTIVE:', 'None'),
(33, '0c0010', 'Critical: Camera Moved', '2018-06-12 10:55:52', '192.168.1.233', 'INACTIVE:', 'Reset Camera'),
(34, '0x0010', 'INFO: Camera Reset Done', '2018-06-12 10:57:26', '192.168.1.233', 'ACTIVE:', 'None'),
(35, '0x0011', 'INFO: New ROI Selected', '2018-06-12 10:57:33', '192.168.1.233', 'ACTIVE:', 'None'),
(36, '0w0010', 'Warning: Suspicious Activity', '2018-06-12 10:58:15', '192.168.1.233', 'ACTIVE:', 'None'),
(37, '0w0010', 'Warning: Suspicious Activity', '2018-06-12 10:58:15', '192.168.1.233', 'ACTIVE:', 'None'),
(38, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:58:18', '192.168.1.233', 'ACTIVE:', 'None'),
(39, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:58:18', '192.168.1.233', 'ACTIVE:', 'None'),
(40, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:58:18', '192.168.1.233', 'ACTIVE:', 'None'),
(41, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:58:20', '192.168.1.233', 'ACTIVE:', 'None'),
(42, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:58:20', '192.168.1.233', 'ACTIVE:', 'None'),
(43, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:58:20', '192.168.1.233', 'ACTIVE:', 'None'),
(44, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:58:20', '192.168.1.233', 'ACTIVE:', 'None'),
(45, '0w0010', 'Warning: Suspicious Activity', '2018-06-12 10:58:20', '192.168.1.233', 'ACTIVE:', 'None'),
(46, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:58:20', '192.168.1.233', 'ACTIVE:', 'None'),
(47, '0w0010', 'Warning: Suspicious Activity', '2018-06-12 10:58:21', '192.168.1.233', 'ACTIVE:', 'None'),
(48, '0w0001', 'Warning: ROI Activity', '2018-06-12 10:58:21', '192.168.1.233', 'ACTIVE:', 'None'),
(49, '0w0010', 'Warning: Suspicious Activity', '2018-06-12 10:58:21', '192.168.1.233', 'ACTIVE:', 'None'),
(50, '0c0001', 'Critical: Camera Blocked', '2018-06-12 10:58:21', '192.168.1.233', 'INACTIVE:', 'Reset Camera');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'group'),
(3, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'log', 'cameradb'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-06-08 07:09:12.904000'),
(2, 'auth', '0001_initial', '2018-06-08 07:09:26.986000'),
(3, 'admin', '0001_initial', '2018-06-08 07:09:29.767000'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-06-08 07:09:30.532000'),
(5, 'contenttypes', '0002_remove_content_type_name', '2018-06-08 07:09:32.451000'),
(6, 'auth', '0002_alter_permission_name_max_length', '2018-06-08 07:09:33.474000'),
(7, 'auth', '0003_alter_user_email_max_length', '2018-06-08 07:09:34.426000'),
(8, 'auth', '0004_alter_user_username_opts', '2018-06-08 07:09:34.539000'),
(9, 'auth', '0005_alter_user_last_login_null', '2018-06-08 07:09:35.320000'),
(10, 'auth', '0006_require_contenttypes_0002', '2018-06-08 07:09:35.380000'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2018-06-08 07:09:35.467000'),
(12, 'auth', '0008_alter_user_username_max_length', '2018-06-08 07:09:36.652000'),
(13, 'sessions', '0001_initial', '2018-06-08 07:09:38.082000'),
(14, 'log', '0001_initial', '2018-06-12 07:52:11.979000');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('3svke5ijg12fvama20ozl07odhaz17vi', 'ZDEyYmQ3NTIyYTcyZDBmNDBlYjg2YzAxY2EyMWMwMmQ2MWE4MzNhMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImZiM2FjYTE1NTJiNWI3MDk4NWFiZWNiYzAxZTAxMGFmODE5NDFiZDkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2018-06-22 07:14:26.656000'),
('ch2ic84pa53fdav7xbghrxeh55al9jr2', 'ZGQyMGQ5YjJjN2Y5YjA0YTRkNTdlN2JhZTcwNmY2ZTY5YTZkMjc3Mjp7Il9hdXRoX3VzZXJfaGFzaCI6IjM2NDBlZGRkMzE1OTJhMmY5YWJhYmM2ZjBlZWIzZjQyNDEzODEyM2MiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=', '2018-06-22 10:09:17.336000'),
('ixgpfr7qvvs9nni0kygw8t9iz865pw2v', 'ZWYyYWViMTY0ZjJkOWQ0OTc5ZTlmMDRiZGNlZTc3Yjc0N2VhOGRkMjp7Il9hdXRoX3VzZXJfaGFzaCI6IjY3YWQ0YTllMDNjNzRkMmRjOWIwN2Y3NjAwNWJiYjBlNmFiN2IxYmUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=', '2018-06-26 06:17:12.067000'),
('qmmy4wun88429pwsj5zqcu2c0qksh8bm', 'ZjQ5OGM3YjM3NjQ4Y2RhNjEzYTI0NDM0MWNkNDg1ODNhMjZiMjZiMjp7Il9hdXRoX3VzZXJfaGFzaCI6IjU0YzQ5OWE0ZTRhYTRiMDRjMTRhZDZjMGY3OTBiZmQ0MzZhY2ZmMjciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI0In0=', '2018-06-26 06:58:52.251000');

-- --------------------------------------------------------

--
-- Table structure for table `log_cameradb`
--

CREATE TABLE `log_cameradb` (
  `id` int(11) NOT NULL,
  `EntryID` varchar(30) NOT NULL,
  `InfoCode` varchar(30) NOT NULL,
  `InfoType` varchar(50) NOT NULL,
  `TimeStamp` date NOT NULL,
  `CameraID` varchar(20) NOT NULL,
  `CameraStatus` varchar(50) NOT NULL,
  `Action` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `advanceanalyticsdb`
--
ALTER TABLE `advanceanalyticsdb`
  ADD PRIMARY KEY (`EntryID`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `cameradb`
--
ALTER TABLE `cameradb`
  ADD PRIMARY KEY (`EntryID`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `log_cameradb`
--
ALTER TABLE `log_cameradb`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `advanceanalyticsdb`
--
ALTER TABLE `advanceanalyticsdb`
  MODIFY `EntryID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cameradb`
--
ALTER TABLE `cameradb`
  MODIFY `EntryID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `log_cameradb`
--
ALTER TABLE `log_cameradb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
