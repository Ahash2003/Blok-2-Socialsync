<?php
	$firstName = $_POST['firstName'];
	$lastName = $_POST['lastName'];
	$emailadress = $_POST['emailadress'];
	$password = $_POST['password'];
	$telephonenumber = $_POST['telephonenumber'];

	// Database connection
	$conn = new mysqli('localhost','root','123456','DATABASE_BLOK_2');
	if($conn->connect_error){
		echo "$conn->connect_error";
		die("Connection Failed : ". $conn->connect_error);
	} else {
		$stmt = $conn->prepare("insert into registration(firstName, lastName, emailadress, password, telephonenumber) values(?, ?, ?, ?, ?)");
		$stmt->bind_param("ssssi", $firstName, $lastName, $emailadress, $password, $telephonenumber);
		$execval = $stmt->execute();
		echo $execval;
		echo "Registration successfully...";
		$stmt->close();
		$conn->close();
	}
?>