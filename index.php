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
  $classStr="";
  if(isset($_GET["error"])){
    if(($_GET["error"]=="empty_input")){
      $errStr='Please don&#39;t leave any fields blank';
    }
    elseif(($_GET["error"]=="login_failed")){
      $errStr='Invalid Username or wrong password';
    }
    
  }
  ?>




    <header class="container-fluid text-bg-primary">
        <img src="images/White_and_Green_Minimalist_Photo_Frame_Merry_Christmas_Family_Greeting_Card__1_-removebg-preview.png" alt="logo" width="200" height="75">
    </header>
    <main class="container d-flex flex-column justify-content-center" id="mainArea">
         
        <section class="" id="mainContent">
            <h1 class="text-center">Login</h1>
        <form action="validateuser.php" method="post" class="border rounded">
            <div class="p-1 px-3 pb-2">
              <label for="" class="form-label">Username or Email</label>
              <input type="text" class="form-control" name="user" id="" aria-describedby="emailHelpId" placeholder="">
              <small id="emailHelpId" class="form-text text-muted">Help text</small>
            </div>
            <div class="p-1 px-3 pb-2">
              <label for="" class="form-label">Password</label>
              <input type="password" class="form-control" name="password" id="" placeholder="Password">
            </div>
            <div class="row m-1">
                <div class="col">
  
                </div>
                <div class="col text-end ">
                    <a href="register.php" class="link-primary">Register here</a>
                </div>
            </div>
            <div class="p-1 px-3 pb-2 d-flex flex-column justify-content-center">
                <button type="submit" name="submit" class="btn btn-primary">Login</button>
                <span class="text-danger text-center"><?php echo $errStr; ?></span>
            </div>
        </form>
        </section>   
    </main>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
  </body>
</html>
