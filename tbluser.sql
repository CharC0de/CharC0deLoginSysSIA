-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 08, 2023 at 01:52 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbactivity6`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbluser`
--

CREATE TABLE `tbluser` (
  `userid` int(10) NOT NULL,
  `username` varchar(300) NOT NULL,
  `password` varchar(300) NOT NULL,
  `email` varchar(300) NOT NULL,
  `pfp` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbluser`
--

INSERT INTO `tbluser` (`userid`, `username`, `password`, `email`, `pfp`) VALUES
(1, 'CharlieBoy', '$2y$10$KCXhuVK0xZ7P7v7fms07d.BwXjd7TTBS1KclSgWRthwSwa/Vu5G2G', 'charlesreiner@gmail.com', 'IMG_20230114_133512111.jpg'),
(2, 'MarkTahimik', '$2y$10$NVMokgrzsiZ5sTDe0F.4lefG64bZ7IRUAPyplMQBquextu9vH1O4q', 'marktanga@gmail.com', '642de60659d959.57380496.png'),
(3, 'JohnDont', '$2y$10$gMKEhA8TLd9lvW6XVLyIFuX6/5kWCn/.yVCeQoDwIpbV8I58RUVIS', 'JohnDoesnt@gmail.com', 'default.png'),
(5, 'JomarT', '$2y$10$aNWCL1yBviTl9JUAtAP.N.WzY4pgJaLvhY68QS47zbDPnGAO/Cj/y', 'jomartumahan@gmail.com', '642e25cbba1eb9.05096761.jpg'),
(18, 'Charlie', '$2y$10$wf0IOAmhkjFuZKp6klfaSugGqMiydOCzlie8V1hTNNmWuoEWv3ATS', 'charliekun@gmail.com', 'default.png'),
(23, 'KinitHarden', '$2y$10$XsxU9MbXlZIzQeSOPIm1YODmoxUE5NIsfz1CCew8ttc3YGe.RPCfW', 'KennethHard@gmail.com', '642eeabca43370.09798246.jpg'),
(25, 'CharlesMamirahay', '$2y$10$6uuS6cWoOme8doY3uHu4yeaP.nlN0wFuLnm5TdU9VBzNbWXBxrj4i', 'CharlesM@gmail.com', 'default.png'),
(27, 'MarkFoe', '$2b$12$Z9sE58nortqzOdcyA9gT9O3c7xottLmBEoEe1FbnG0rAbwzG9meGi', 'MFer@gmail.com', 'default.png'),
(28, 'JaneAlex', '$2b$12$HjDwGqb3VjcLRblK.U0udek7swEOKXZw.LelUf1q8MbRti.NC4Re2', 'Jalex@gmail.com', 'depositphotos_210207074-stock-photo-young-beautiful-woman-isolated-background.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbluser`
--
ALTER TABLE `tbluser`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbluser`
--
ALTER TABLE `tbluser`
  MODIFY `userid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
