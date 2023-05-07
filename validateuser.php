<?php
if (isset($_POST["submit"])){
    $uName = $_POST["user"];
    $pwd =$_POST["password"];
    
    require_once "dbExec.php";
    require_once "functions.php";
    
    if(emptyInputLogin($uName,$pwd)!== false){
        header("location: index.php?error=empty_input");
        exit();
    }

    loginUser($conn,$uName,$pwd);
}
else{
    header("location: index.php");
    exit();
}