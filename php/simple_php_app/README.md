# Simple PHP App

Skeleton application that let users store user name and email with MySQL

### Database setup

1. Create database in MySQL

```js
  CREATE DATABASE csc-simple-php-app;
```

2. Verify

```js
SHOW DATABASES;
```

You should see:
`csc-simple-php-app`

3. Use the database

```js
USE csc-simple-php-app
```

4. Create `users` table

```js
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);
```
