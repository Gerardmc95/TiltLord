<?php
	//ORDEN DE CONSULTAS
	/*	
		1.- $url = 'https://la1.api.riotgames.com/lol/summoner/v3/summoners/by-name/'.$cadena.'?api_key=RGAPI-7b6b0401-1252-4228-84e4-5b213a9fcc73';
				donde cadena es el nombre del invocador y se busca el accountID

		2.- $url2 = 'https://la1.api.riotgames.com/lol/match/v3/matchlists/by-account/'.$numeroUsuario.'?api_key=RGAPI-7b6b0401-1252-4228-84e4-5b213a9fcc73'
				donde numroUsuario es la accountID del invocador y se busca el gameId mas reciente

		3.- $url3 = 'https://la1.api.riotgames.com/lol/match/v3/timelines/by-match/'.$juegoID.'?api_key=RGAPI-7b6b0401-1252-4228-84e4-5b213a9fcc73'
				donde juegoID es el gameID y la consulta trae todos los detalles de la partida.

	*/
	

	$url = 'https://la1.api.riotgames.com/lol/champion-mastery/v3/scores/by-summoner/62576?api_key=RGAPI-7b6b0401-1252-4228-84e4-5b213a9fcc73';
	$document = new DOMDocument();
  	$document->loadHTML($content);
 	$document->getElementsByTagName('demo') = curl_init($url);
 ?>