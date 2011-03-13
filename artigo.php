<!DOCTYPE html>
<html>
<?php

error_reporting(E_ALL);

$id = $_GET['id'];

//$feed_url = "http://portal.ufes.br/rss.xml";
//$news_feed = file_get_contents($feed_url);
//$feed_stream = new SimpleXmlElement($news_feed, NULL, TRUE);
//$entry = $feed_stream->channel->item;

    $rss = simplexml_load_file("http://portal.ufes.br/rss.xml");
    $entry = $rss->channel->item;

switch($id)
{
    case "0": 
    $current = $entry[0]; 
    break; 
    
    case "1": 
    $current = $entry[1];  
    break; 
    
    case "2": 
    $current = $entry[2];  
    break; 
    
    case "3": 
    $current = $entry[3];  
    break; 
}
?>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="user-scalable=no, width=device-width" />
<link rel="stylesheet" type="text/css" href="iphone.css" media="screen" />
<title><?php echo $current->title ?> - Ufes Mobile</title>
</head>
<body>
<div id="container">
  <div id="toolbar" class="article">
    <h1></h1>
    <a href="noticias.php" class="back long">Últimas Notícias</a></div>
  <div id="articleContent" class="fullWidth content">
    <h2 class="title"><?php echo $current->title ?></h2>
    <p><?php echo $current->description ?></a></p>
    <div id="mail" class="alignright"><a href="mailto:?subject=<?php echo $current->title ?>&body=<?php echo $current->link ?>"><input name="button" type="button" value="Envie por email" class="sendMail" id="sendMail"></a></div>
  </div>
</div>
<script type="text/javascript" src="javascript/jquery.js"></script>
<script type="text/javascript" src="javascript/iphone.js" charset="utf-8"></script>
</body>
</html>