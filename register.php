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
    <header class="container-fluid text-bg-primary mb-4">
        <img src="images/White_and_Green_Minimalist_Photo_Frame_Merry_Christmas_Family_Greeting_Card__1_-removebg-preview.png" alt="logo" width="200" height="75">
    </header>
<?php
  $errStr="";
  $classStr="";
  if(isset($_GET["error"])){
    if(($_GET["error"]=="empty_input")){
      $classStr="text-danger";
      $errStr='Please don&#39;t leave any fields blank';
    }
    elseif(($_GET["error"]=="invalid_uid")){
      $classStr="text-danger";
      $errStr='Username should have no spaces or any special character';
    }
    elseif(($_GET["error"]=="invald_email")){
      $classStr="text-danger";
      $errStr='Inputted email is invalid';
    }
    elseif(($_GET["error"]=="passwords_do_not_match")){
      $classStr="text-danger";
      $errStr='Passwords do not match please try again';
    }
    elseif(($_GET["error"]=="username_taken")){
      $classStr="text-danger";
      $errStr='Username is already taken';
    }
    elseif(($_GET["error"]=="stmt_failed")){
      $classStr="text-danger";
      $errStr='<p>Something went wrong please contact website admin for more details</p>';
    }
    elseif(($_GET["error"]=="none")){
      $classStr="text-success";
      $errStr='<strong>You&#39;ve signed up successfully!</strong>';
    }
  }
?>
    <main class="container d-flex flex-column" id="mainArea">
        <section class="" id="mainContent">
            <h1 class="text-center">Register Account</h1>
        <form action="insertuser.php" method="post" class="border rounded">
            <div class="p-1 px-3 pb-1 mt-1">
              <label for="" class="form-label">Username</label>
              <input type="text" class="form-control" name="username" id="" aria-describedby="emailHelpId" placeholder="Username">
              <small id="emailHelpId" class="form-text text-muted">Help text</small>
            </div>
            <div class="p-1 px-3 pb-1">
              <label for="" class="form-label">Email</label>
              <input type="email" class="form-control" name="email" id="" aria-describedby="emailHelpId" placeholder="abc@mail.com">
              <small id="emailHelpId" class="form-text text-muted">Help text</small>
            </div>
            <div class="p-1 px-3 pb-4">
              <label for="" class="form-label">Password</label>
              <input type="password" class="form-control" name="password" id="" placeholder="Password">
            </div>
            <div class="p-1 px-3 py-3">
              <label for="" class="form-label">Confirm Password</label>
              <input type="password" class="form-control" name="confpass" id="" placeholder="Confirm password">
            </div>
            <div class="p-1 px-3 pb-2 d-flex flex-column justify-content-center">
            <span class="<?php echo $classStr; ?> text-center"><?php echo $errStr; ?></span>
            </div>
            <div class="row m-1">
              <div class="col">
              </div>
              <div class="col text-end ">
                  <a href="index.php" class="link-primary">Back to Login</a>
              </div>
          </div>
            <div class="p-1 px-3 py-2 d-flex flex-column justify-content-center">
                <button type="submit" name="submit" class="btn btn-primary">Submit</button>
            </div>
        </form>
        </section>   
    </main>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
  </body>
</html>
