function hideURLbar() { 
	window.scrollTo(0,1);
}
addEventListener("load", function() { 
	setTimeout(hideURLbar, 0); 
}, false);

/////// -- Switch Magic -- ///////

$('a#switch').click(function() {
// ask first
	var answer = confirm("Ir para o site completo?");
	if (answer) {
		$("a#switch").toggleClass("offimg");
		setTimeout('switch_delayer()', 1350); 
	}
	return false;
});

function switch_delayer() {
	window.location = "http://www.ufes.br/";
}

