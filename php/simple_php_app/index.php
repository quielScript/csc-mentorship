<?php
  include "config.php";

  $sql = "SELECT * FROM users";
  $result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simple PHP App</title>
</head>
<body>
  <h2>Users List</h2>

  <a href="create.php">Add New User</a>

  <hr />

  <?php while ($row = $result->fetch_assoc()): ?>
    <p>
      <?php echo $row["name"]; ?> -
      <?php echo $row["email"]; ?>
    </p>
  <?php endwhile ?>
</body>
</html>