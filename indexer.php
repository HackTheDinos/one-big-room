<?php

$file = fopen("species-scraper/digimorph_species_list/dinos.json", "r");
$out_tmp = fopen("tmp.json", 'w');

$line = fgets($file);
$docs = json_decode($line);
$ind = 0;
foreach(array_slice($docs,1) as $doc) {
    $desc = isset($doc->descriptions->description) ? $doc->descriptions->description : "";
    $spec = isset($doc->species) ? $doc->species : isset($doc->SPECIES) ? $doc->SPECIES : "";

    $doc = [
        "scientific_name" => $doc->scientificName,
        "species" => $doc->species,
        "family" => $doc->family,
        "genus" => $doc->genus,
        "phylum" => $doc->phylum,
        "class" => $doc->class,
        "parent" => $doc->parent,
        "num_descendents" => $doc->numDescendants,
        "wikipedia_snippet" => "",
        "wikipedia_misc" => "",
        "gbif_snippet" => $desc,
        "gbif_misc" => "",
        "is_skrillex" => false,
    ];

    $blob = json_encode($doc);
    $bonsai_url = "https://uhxnwjp8:t3y4mdk8zo1ck366@pine-2787280.us-east-1.bonsai.io";
    $index_cmd = "curl -XPOST \"{$bonsai_url}/scans/scans_test/\" -d '{$blob}'\n";

    fwrite($out_tmp, $index_cmd);

    try {
        shell_exec($index_cmd);
    } catch (Exception $e) {
        echo $e;
    }
}

fclose($file);
fclose($out_tmp);
