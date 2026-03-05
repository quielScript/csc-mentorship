<?php
  $host = "localhost";
  $username = "";
  $password = "";
  $database = "csc-simple-php-app";

  $conn = new mysqli($host, $username, $password, $database);

  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
?>