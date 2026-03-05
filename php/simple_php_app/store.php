<?php
  include "config.php";

  $name = $_POST["name"];
  $email = $_POST["email"];

  // Prepare statement
  $stmt = $conn->prepare("INSERT INTO users (name, email) VALUE(?, ?)");
  $stmt->bind_param("ss", $name, $email);

  // Execute query
  $stmt->execute();

  // Redirect user back to homepage
  header("Location: index.php");
  exit();
?>