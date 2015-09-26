<?php
$valor = $_POST['valor'];
exec('sudo python /var/www/pi/motor_paso/horizontal.py');
echo 'retorno: '.$valor;
?>
