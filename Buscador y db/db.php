﻿<?php

$mysql = new mysqli("localhost", "root", "", "rivero");

if ($mysql->connect_error){

    die("fallo la conexion");

}else{
    echo "conexion satisfactoria";
}

?>