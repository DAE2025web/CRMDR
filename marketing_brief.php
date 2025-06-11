<?php
// Simple CLI script to generate a marketing brief for an immigration law firm

echo "Bienvenido al generador de Brief de Marketing para Bufetes de Abogados\n";

function prompt($text) {
    echo $text . ": ";
    return trim(fgets(STDIN));
}

$nombre = prompt("Nombre del bufete");
$mision = prompt("Misión o eslogan");
$colores = prompt("Colores corporativos deseados");
$tipografia = prompt("Tipografías preferidas");
$objetivos = prompt("Objetivos de marketing digital");
$audiencia = prompt("Público objetivo");
$objetivo_web = prompt("Objetivo principal del sitio web");

$brief = "\n==== BRIEF DE MARKETING ====\n";
$brief .= "Bufete: $nombre\n";
$brief .= "Eslogan: $mision\n";
$brief .= "Identidad Visual:\n";
$brief .= "  Colores: $colores\n";
$brief .= "  Tipografía: $tipografia\n";
$brief .= "Marketing Digital:\n";
$brief .= "  Objetivos: $objetivos\n";
$brief .= "  Audiencia: $audiencia\n";
$brief .= "Sitio Web:\n";
$brief .= "  Objetivo: $objetivo_web\n";
$brief .= "==========================\n";

file_put_contents("brief_$nombre.txt", $brief);

echo "Brief generado en brief_$nombre.txt\n";
?>
