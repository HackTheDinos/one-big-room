<?php

$file = fopen("species-scraper/digimorph_species_list/dinos.json", "r");
$out_tmp = fopen("tmp.json", 'w');

$line = fgets($file);
$docs = json_decode($line);
$ind = 0;
foreach($docs as $doc) {
    $desc = isset($doc->descriptions->description) ? $doc->descriptions->description : "";
    $spec = isset($doc->species) ? $doc->species : isset($doc->SPECIES) ? $doc->SPECIES : "";
    $vernacular_name = isset($doc->vernacularNames->vernacularName) ? $doc->vernacularNames->vernacularName : "";
    $url = "http://digimorph.org/specimens/$spec";

    $doc = [
        "specimen_url" => $url,
        "scientific_name" => $doc->scientificName,
        "vernacular_name" => $vernacular_name,
        "phylum" => $doc->phylum,
        "class" => $doc->class,
        "order" => $doc->order,
        "family" => $doc->family,
        "genus" => $doc->genus,
        "species" => $doc->species,
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
