<?php



$conn = mysqli_connect("localhost", "root", "", "dbactivity6");

if($conn===false){
    die("ERROR: Could connect" . mysqli_connect_error());
}
$sql = "DELETE FROM tbluser WHERE userid='" . $_GET["id"] . "'";
if (mysqli_query($conn, $sql)) {
    echo "Record deleted successfully";
} else {
    echo "Error deleting record: " . mysqli_error($conn);
}

mysqli_close($conn);
header("Location: dashboard.php?success=deletion_successful");
die();
?>