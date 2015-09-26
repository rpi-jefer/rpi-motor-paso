<?php
$valor = $_POST['valor'];
exec('sudo python /var/www/pi/motor_paso/vertical.py');
echo 'retorno: '.$valor;
?>
