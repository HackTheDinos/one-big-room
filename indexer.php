<?php

function normalize($str) {
    return preg_replace('/[^ A-Za-z0-9\-]/', '', $str);
}

$file = fopen($argv[1], 'r');
$intro_file = fopen("species-scraper/intros.json", 'r');
$url_file = fopen("url_map.json", 'r');
$out_tmp = fopen("tmp.json", 'w');
$slice_file = fopen("slice_data.json", 'r');

$line = fgets($file);
$docs = json_decode($line);
$iline = fgets($intro_file);
$intros = json_decode($iline);

// build a bear
$species = [];
while ($uline = fgets($url_file)) {
    $url_data = json_decode($uline, true);
    $species = array_merge($species, $url_data);
}

$slice_data = json_decode(fgets($slice_file), true);

$ind = 0;
foreach($docs as $doc) {
    $desc = "";
    if (isset($doc->descriptions)) {
        foreach($doc->descriptions as $description) {
            $desc .= normalize($description->description);
        }
    }
    $spec = isset($doc->species) ? $doc->species : (isset($doc->SPECIES) ? $doc->SPECIES : "");

    if (isset($intros->$spec)) {
        $intro = normalize($intros->$spec);
    }

    $vernacular_name = isset($doc->vernacularNames->vernacularName) ? $doc->vernacularNames->vernacularName : "";

    if (isset($species[$spec])) {
        $urls = $species[$spec]["urls"];
        $group = $species[$spec]["group"];

        foreach($urls as $url) {

            $sc = isset($slice_data[$url]) ? $slice_data[$url]["slice_count"] : 0;
            $zp = isset($slice_data[$url]) ? $slice_data[$url]["zero_padding"] : 0;

            $doc = [
                "specimen_url" => $url,
                "group" => $group,
                "scientific_name" => $doc->scientificName,
                "vernacular_name" => $vernacular_name,
                "phylum" => $doc->phylum,
                "class" => $doc->class,
                "order" => $doc->order,
                "family" => $doc->family,
                "genus" => $doc->genus,
                "species" => $spec,
                "parent" => $doc->parent,
                "num_descendents" => $doc->numDescendants,
                "wikipedia_snippet" => $intro,
                "wikipedia_misc" => "",
                "gbif_snippet" => $desc,
                "gbif_misc" => "",
                "is_skrillex" => false,
                "slice_count" => $sc,
                "zero_padding" => $zp,
            ];

            $blob = json_encode($doc);
            $bonsai_url = "https://uhxnwjp8:t3y4mdk8zo1ck366@pine-2787280.us-east-1.bonsai.io";
            $index_cmd = "curl -XPOST \"{$bonsai_url}/scans2/scans_test/\" -d '{$blob}'\n";

            fwrite($out_tmp, $index_cmd);

            try {
                shell_exec($index_cmd);
            } catch (Exception $e) {
                echo $e;
            }
        }
    }
}

fclose($file);
fclose($out_tmp);
fclose($url_file);
fclose($intro_file);
fclose($slice_file);
