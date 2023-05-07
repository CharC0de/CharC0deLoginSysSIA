<?php


if (isset($_POST["submit"])) {
    require_once "functions.php";
    $userid=$_POST["userid"];
    $username=$_POST["username"];
    $email=$_POST["email"];
    $newPass=$_POST["password"];
    $confpass=$_POST["confpass"];
    $oldpass=$_POST["oldpass"];
    $hashedPass = "";

       

   
    
    $file = $_FILES['file'];
    $fileName = $file['name'];
    $fileTmp = $file['tmp_name'];
    $fileError = $file['error'];
    $fileSize = $file['size'];

    $fileExtArr=explode(".",$fileName);
    $fileExt = strtolower(end($fileExtArr));
    $allowedExt= array("jpg", "jpeg", "png","pdf");

    if(empty($fileName)){
        include_once "dbExec.php";
        if (!empty($newPass)){
            if(invalidPwdMatch($confpass,$oldpass)!== false){
                header("location: dashboard.php?error=old_password_do_not_match");
                exit();
            }
            else{
                $hashedPass = password_hash($newPass,PASSWORD_DEFAULT);
            }
            $sql ="UPDATE `tbluser` SET`username`=?, `email`=?, `password`=? WHERE `tbluser`.`userid` = ?";
            $stmt = mysqli_stmt_init($conn);
            if (!mysqli_stmt_prepare($stmt, $sql)) {
                header("location: ../profile.php?error=stmt_failed");
                exit();
            }
            mysqli_stmt_bind_param($stmt, "ssss",$username,$email,$hashedPass, $userid);
            mysqli_stmt_execute($stmt);
            mysqli_stmt_close($stmt);
        }
        else{
            $sql ="UPDATE `tbluser` SET`username`=?, `email`=? WHERE `tbluser`.`userid` = ?";
                $stmt = mysqli_stmt_init($conn);
                if (!mysqli_stmt_prepare($stmt, $sql)) {
                    header("location: ../profile.php?error=stmt_failed");
                    exit();
                }
                mysqli_stmt_bind_param($stmt, "sss",$username,$email, $userid);
                mysqli_stmt_execute($stmt);
                mysqli_stmt_close($stmt);
        }
    }
    if (in_array($fileExt,$allowedExt)) {
        if($fileError===0){
            if ($fileSize<5000000) {
            include_once "dbExec.php";
            $fileNameNew=uniqid('',true).".".$fileExt;
            $fileDestination = 'images/'.$fileNameNew;
            move_uploaded_file($fileTmp,$fileDestination);
            if (!empty($newPass)){
                if(invalidPwdMatch($confpass,$oldpass)!== false){
                    header("location: dashboard.php?error=old_password_do_not_match");
                    exit();
                }
                else{
                    $hashedPass = password_hash($newPass,PASSWORD_DEFAULT);
                }
                $sql ="UPDATE `tbluser` SET`username`=?, `email`=?, `password`=?, `pfp` = ? WHERE `tbluser`.`userid` = ?";
                $stmt = mysqli_stmt_init($conn);
                if (!mysqli_stmt_prepare($stmt, $sql)) {
                    header("location: ../profile.php?error=stmt_failed");
                    exit();
                }
                mysqli_stmt_bind_param($stmt, "sssss",$username,$email,$hashedPass, $fileNameNew, $userid);
                mysqli_stmt_execute($stmt);
                mysqli_stmt_close($stmt);
            }
            else{
                $sql ="UPDATE `tbluser` SET`username`=?, `email`=?, `pfp` = ? WHERE `tbluser`.`userid` = ?";
                $stmt = mysqli_stmt_init($conn);
                if (!mysqli_stmt_prepare($stmt, $sql)) {
                    header("location: ../profile.php?error=stmt_failed");
                    exit();
                }
                mysqli_stmt_bind_param($stmt, "ssss",$username,$email, $fileNameNew, $userid);
                mysqli_stmt_execute($stmt);
                mysqli_stmt_close($stmt);
            }
            header("location: dashboard.php?success=upload_success");
            }
            else{
                header("location: dashboard.php?error=file_too_large");
            }
        }
        else{
            header("location: dashboard.php?error=upload_error");
        }
    }
    else{
        header("location: dashboard.php?error=invalid_extension");  
    }

}
else{
    header("location: ../index.php");
    exit();
}