<?php
include("conexion.php");


if(isset($_POST['mandar'])){
    if(strlen($_POST['nombre']) >= 1 && strlen($_POST['apellido']) >=   1 && strlen($_POST['email']) >= 1 && strlen($_POST['usuario']) >= 1 && strlen($_POST['contraseña']) >= 1 && strlen($_POST['Confircontraseña']) >= 1){
      
       
        $nom     = $_POST['nombre'];
        $ap      = $_POST['apellido'];
        $email   = $_POST['email'];
        $usu     = $_POST['usuario'];
        $contra  = $_POST['contraseña'];
        $confircontraseña = $_POST['confircontraseña'];

        

        
    }
   

}




?>