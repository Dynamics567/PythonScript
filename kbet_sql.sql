-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 28, 2020 at 09:53 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.2.14
CREATE SEQUENCE kbet_id_seq;
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */
;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */
;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */
;
/*!40101 SET NAMES utf8mb4 */
;
--
-- Database: `Testdb`
--
-- --------------------------------------------------------
--
-- Table structure for table `kbet`
--
CREATE TABLE kbet
(
    ItemID varchar (255) NOT NULL,
    OddType varchar(255) NOT NULL,
    OddName varchar (255) NOT NULL,
    OddOutcome varchar (255) NOT NULL,
    MatchOddID varchar (255) NOT NULL



);
--
--
