<?php

if (isset($_POST["submit"])){
    
    $uName = $_POST["username"];
    $pwd =$_POST["password"];
    $pwdRepeat =$_POST["confpass"];
    $defaultPfp ="default.png";
    $email=$_POST["email"];

    require_once "dbExec.php";
    require_once "functions.php";

    if(emptyInputSignup($uName,$pwd,$pwdRepeat,$email)!== false){
        header("location: register.php?error=empty_input");
        exit();
    }
    if(invalidUid($uName)!== false){
        header("location: register.php?error=invalid_uid");
        exit();
    }
    if (invalidEmail($email)!==false) {
        header("location: register.php?error=invalid_email");
        exit();
    }
    if(pwdMatch($pwd,$pwdRepeat)!== false){
        header("location: register.php?error=passwords_do_not_match");
        exit();
    }
    if(uidExists($conn,$uName,$email)!== false){
        header("location: register.php?error=username_taken");
        exit();
    }

    
    createUser($conn,$uName,$pwd,$defaultPfp,$email);
}
else{
    header("location: register.php");
    exit();
}
