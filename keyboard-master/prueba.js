function readTextFile(file)
		{
   		 var rawFile = new XMLHttpRequest();
    	 rawFile.open("GET", file, false);
   		 rawFile.onreadystatechange = function ()
   		 {
   	     	if(rawFile.readyState === 4)
   		     {
   	         	if(rawFile.status === 200 || rawFile.status == 0)
   	         	{
   	             var allText = rawFile.responseText;
   	             alert(allText);
   	        	 }
   	    	 }
   		 }
   		 rawFile.send(null);
		}
function main(){
		readTextFile("File:///media/saul365/1A4A-D778/keyboard/keyboard_master/keys.txt");
   }