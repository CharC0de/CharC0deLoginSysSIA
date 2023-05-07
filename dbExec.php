<?php

$serverName = "localhost";
$dBUsername = "root";
$dBPass = "";
$dBName= "dbactivity6";

$conn = mysqli_connect($serverName,$dBUsername,$dBPass,$dBName);

if(!$conn){
    die("Connection failed" . mysqli_connect_error());
    header("location: register.php?error=db_access_error");
    exit();
}