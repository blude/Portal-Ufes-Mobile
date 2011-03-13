<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="user-scalable=no, width=device-width" />
<link rel="stylesheet" type="text/css" href="iphone.css" media="screen" />
<title>Últimas Notícias - Ufes Mobile</title>
</head>
<body>

<?php
        
    error_reporting(E_ALL);
    
    $rss = simplexml_load_file("http://portal.ufes.br/rss.xml");
    $entry = $rss->channel->item;

?>

<div id="container">
  <div id="toolbar" class="newsheader">
    <h1>Últimas Notícias</h1>
    <a href="index.php" class="back">Menu</a></div>
  <div id="content" class="fullWidth">
    <div class="listing" id="newsList">
      <ul>
        <?php
            $i = 0; 
            foreach ( $entry as $item ) { ?>
        <li class="arrow"><a href="artigo.php?id=<?php echo $i; ?>"><?php echo $item->title ?></a></li>
        <?php
             $i++;
             } ?>
        <li><a href="javascript:return false;" class="more">Mais notícias...</a></li>
        <li class="arrow"><a href="http://www.twitter.com/UfesOnline" target="_blank" class="twitterlink">Veja mais notícias no Twitter</a></li>
      </ul>
    </div>
  </div>
</div>
<script type="text/javascript" src="javascript/jquery.js"></script>
<script type="text/javascript" src="javascript/iphone.js" charset="utf-8"></script>
</body>
</html>