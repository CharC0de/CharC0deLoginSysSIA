<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bootstrap demo</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
  <link rel="stylesheet" href="style.css">
</head>

<body class="text-bg-dark">
  <?php
  $errStr="";
  session_start();
  if (!isset($_SESSION["userid"])) {
    header("Location: index.php");
    die();
  }
  if(isset($_GET["error"])){
    if(($_GET["error"]=="old_password_do_not_match")){
      $errStr='inputted password does not match with old password';
    }
  }
 
  
  ?>
  <header class="container-fluid text-bg-primary d-flex flex-row justify-content-between align-items-end">
    <img src="images/White_and_Green_Minimalist_Photo_Frame_Merry_Christmas_Family_Greeting_Card__1_-removebg-preview.png" alt="logo" width="200" height="75">
    <a href="sessionEnd.php" class=" btn btn-secondary m-1">Log Out</a>
  </header>
  <main>

    <h1 class="m-4">
      Dashboard
    </h1>
    <div class=" d-flex flex-row align-items-center">
      <h2>
        Current User:
      </h2>
      <img src="images/<?php echo $_SESSION["userpfp"]; ?>" alt="" id="currUserPfp" class="mx-2" width="50" height="50">
      <h3>
         <?php echo $_SESSION["username"]; ?>
      </h3>
      
    </div>
    <div class=" d-flex align-items-center ">
      <h3>
        Search User
      </h3>
      <input type="text" name="" id="searchBar" class="mx-2">
      </div>
    <p class="danger"><?php echo $errStr; ?></p>
    <section class="container-fluid">

       

        <?php


        include_once 'dbExec.php';
        $query = "SELECT * FROM tbluser WHERE userid != '".$_SESSION["userid"]."'";

        if ($result = $conn->query($query)) {
          $var = 0;
          echo '<div class="row">';
          while ($row = $result->fetch_assoc()) {
            $userid = $row["userid"];
            $username = $row["username"];
            $email = $row["email"];
            $oldPass = $row["password"];
            $pfp = $row["pfp"];
            
            echo '<div class="col">
       <form action="upload.php" method="post" id="myForm' . $var . '" enctype="multipart/form-data">
       <div class="card border text-bg-dark my-4" style="width: 20rem;">
           <img src="images/' . $pfp . '" class="card-img-top border-bottom border-primary" alt="pfp">
           <input type="file" name="file">
           <div class="card-body">
           <h5 class="card-title">#Id:' . $userid . '</h5>
             <p class="card-text d-flex align-items-center">Username: <input type="text" class="form-control text-bg-dark info" name="username" value="' . $username . '"></p>
             <p class="card-text d-flex align-items-center">Email: <input type="text" class="form-control text-bg-dark info" name="email" value="' . $email . '"></p>
             <p class="card-text">New Password <input type="password" class="form-control text-bg-dark" name="password"></p>
             <p class="card-text">Old Password <input type="password" class="form-control text-bg-dark" name="confpass"></p>
             <input type="hidden" class="form-control text-bg-dark" name="userid" value="' . $userid . '">
             <input type="hidden" class="form-control text-bg-dark" name="oldpass" value="' . $oldPass . '">
             <section class="d-flex flex-row justify-content-center">
             <button type="submit" name="submit" class="btn btn-primary">Update</button> <a href=deleteuser.php?id='.$userid.' class="btn btn-primary mx-1">Delete</a>
             </section>
           </div>
          </div>
           </form>
   </div>';
            $var++;
          }
          $result->free();
        }
        echo '</div>';
        ?>
        
    </section>
  </main>
  <script src="script.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
</body>

</html>