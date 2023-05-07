<?php

function emptyInputSignup($uName, $pwd, $pwdRepeat,$email)
{
    $result = true;
    if (empty($uName) || empty($pwd) || empty($pwdRepeat ||empty($email))) {
        $result = true;
    } else {
        $result = false;
    }
    return $result;
}

function invalidUid($uName)
{
    $result = true;
    if (!preg_match('/^[a-zA-Z0-9]*$/', $uName)) {
        $result = true;
    } else {
        $result = false;
    }
    return $result;
}

function invalidEmail($email){
    $result = true;
    if(!filter_var($email, FILTER_VALIDATE_EMAIL)){
        $result = true;

    }
    else {
        $result=false;
    }
    return $result;
}

function pwdMatch($pwd, $pwdRepeat)
{
    $result = true;
    if ($pwd !== $pwdRepeat) {
        $result = true;
    } else {
        $result = false;
    }
    return $result;
}
function invalidPwdMatch($confpwd,$oldpwd){
    $result= true;
    if(!password_verify($confpwd,$oldpwd)){
    $result= true;
    }
    else{
        $result= false; 
    }
    return $result;
}
function uidExists($conn, $uName,$email)
{
    $result = true;
    $sql = "SELECT*FROM `tbluser` WHERE `username` = ? OR `email` =?";
    $stmt = mysqli_stmt_init($conn);
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: register.php?error=stmt_failed");
        exit();
    }
    mysqli_stmt_bind_param($stmt, "ss", $uName,$email);
    mysqli_stmt_execute($stmt);
    $resultData = mysqli_stmt_get_result($stmt);
    if ($row = mysqli_fetch_assoc($resultData)) {
        return $row;
    } else {
        $result = false;
        return $result;
    }
    mysqli_stmt_close($stmt);
}

function createUser($conn, $uName, $pwd, $defaultPfp,$email)
{
    $sql = "INSERT INTO `tbluser` (`username`, `password`, `pfp`,`email`) VALUES (?, ?, ?,?)";
    $stmt = mysqli_stmt_init($conn);
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: register.php?error=stmt_failed");
        exit();
    }
    $hashedPwd = password_hash($pwd, PASSWORD_DEFAULT);
    mysqli_stmt_bind_param($stmt, "ssss", $uName, $hashedPwd, $defaultPfp,$email);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_close($stmt);
    header("location: register.php?error=none");
    exit();
}
###############################################################
#user Login
###############################################################
function emptyInputLogin($uName,$pwd){
    $result = true;
    if (empty($uName) || empty($pwd)) {
        $result = true;
    } else {
        $result = false;
    }
    return $result;
}
function loginUser($conn,$username,$pwd){
    $uidExists=uidExists($conn,$username,$username);
    if($uidExists===false){
        header("location: index.php?error=login_failed");
        exit();
    }
    
    $hashedPwd = $uidExists["password"];
    $checkPwd = password_verify($pwd,$hashedPwd);

    if($checkPwd===false){
        header("location: index.php?error=login_failed");
        exit();
    }
    elseif($checkPwd===true){
        session_start();
        $_SESSION["userid"]=$uidExists["userid"];
        $_SESSION["username"]=$uidExists["username"];
        $_SESSION["userpfp"]=$uidExists["pfp"];
        header("location: dashboard.php");
        exit();
    }
}
?>
