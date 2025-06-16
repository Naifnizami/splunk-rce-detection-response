<?php
$conn = new mysqli("localhost", "vulnuser", "", "vulnapp");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['username'])) {
    $user = $_POST['username'];
    $pass = $_POST['password'];

    // Vulnerable to SQL Injection (user input not sanitized)
    $query = "SELECT * FROM users WHERE username='$user' AND password='$pass'";
    echo "<p>Query: $query</p>"; // For debug/testing

    $result = $conn->query($query);

    // Log login attempts
    file_put_contents("/var/log/vulnapp.log", "Login attempt: $user / $pass\n", FILE_APPEND);

    if ($result && $result->num_rows > 0) {
        echo "<h3>Welcome, $user!</h3>";
    } else {
        echo "<h3>Login failed!</h3>";
    }
}

// Vulnerable file upload handler
if (isset($_POST['submit_upload'])) {
    $file = $_FILES['upload']['name'];
    $tmp = $_FILES['upload']['tmp_name'];
    $dest = "uploads/" . basename($file);

    // No filetype validation = RCE vulnerability
    if (move_uploaded_file($tmp, $dest)) {
        echo "<p>File uploaded to: <a href='$dest'>$dest</a></p>";
        file_put_contents("/var/log/vulnapp.log", "File uploaded: $file\n", FILE_APPEND);
    } else {
        echo "<p>Upload failed.</p>";
    }
}
?>

<!-- Login Form -->
<h3>Login</h3>
<form method="POST">
    <input name="username" placeholder="Username"><br>
    <input name="password" placeholder="Password" type="password"><br>
    <input type="submit" value="Login">
</form>

<!-- File Upload Form -->
<h3>Upload a file</h3>
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="upload"><br>
    <input type="submit" name="submit_upload" value="Upload">
</form>
