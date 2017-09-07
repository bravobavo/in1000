<?php
//Session start
session_start()

//Session start
require 'database/connect.php';

//Get required functions and class
require 'core/functions/general.php';
require 'core/class/class.php'

$User = new User($conn)
