<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Add Users</title>
</head>
<body>
  <h2>Add new User</h2>
  <form action="store.php" method="post">
    <label for="name">Name:</label>
    <input type="text" name="name" id="name" required>
    <br /><br />
    <label for="email">Email:</label>
    <input type="email" name="email" id="email">
    <br /><br />
    <button type="submit">Save</button>
  </form>
</body>
</html>