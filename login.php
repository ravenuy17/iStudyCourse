<?php
    $username = $_POST['username'];
    $password = $_POST['password'];

    //database connection
    $con = new mysqli("localhost", "root", "", "mozarella");

    if($con->connect_error){
        die("failed to connect: $con->connect_error");
    }   else    {
        $stms = $con->prepare("select*from registration where email = ?");
        $stsm->bind_param("s, $username");
        $stms->execute();
        $stms_result = $stms->get_result();
        if($stms_result->num_rows>0){
            $data=$stms_result->fetch_assoc();
            if($data["password"]===$password){
                echo "Login successfully";
            }
        }   else    {
            echo "Invalid username or password";
        }
}
?>