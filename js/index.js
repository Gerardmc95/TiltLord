

document.getElementById('buscarInv').addEventListener("click",hacerQuery());


function hacerQuery(){
	console.log("Se ha consultado");
	var actualiza = "demo";
	var direccion = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/RiotSchmick?api_key=RGAPI-07831add-584d-40b5-bd2e-cc6c7475bb1b";
	/*
	var url = "../consultar.php";

	 var xmlhttp = new XMLHttpRequest();
	 xmlhttp.response = function() {
            if (this.readyState == 4 && this.status == 200) {
            	console.log("PAso alfo");
                document.getElementById("actualiza").innerHTML = this.responseText;
            }else
            	console.log("No paso nada");
        };
        xmlhttp.open("GET", "", true);
    	xmlhttp.send();
    */
    $.ajax({
type: "POST",
url: "curl 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/RiotSchmick?api_key=RGAPI-7b6b0401-1252-4228-84e4-5b213a9fcc73'",
dataType: "json",
success: function(data) {
console.log("ALGO",data);
}, error: function(error){
	console.log("ERROR AQUI",error);
}

});



        $.ajax({
            type:'GET',
            crossDomain: true,
            url: direccion,
            "headers":{
            	'Access-Control-Allow-Origin': 'http://localhost/lol/index.html',
            	'Access-Control-Allow-Methods': 'GET',
            	'Access-Control-Allow-Headers': '*',
            },
            success: function(data){
            	console.log("Success",data);
            },error: function (argument) {
            	console.log("Error",argument);
            }
        });


   console.log("Se ha termino consultado");
}


