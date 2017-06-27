var awaited = 1500000000

function begin() {
	var cts_field   = document.getElementById("cts") ;
	var to_ts_field = document.getElementById("to_ts") ;

	get_date() ;

	/* doesn't run anything if it's more than a day after the event */
	if ( awaited-get_timestamp() > -86400 ) {
		countdown(cts_field, to_ts_field) ;
	}
	else 
	{
		var errmsg = "Too bad, the event ended "+
						(get_timestamp()-awaited)+
						" seconds ago" ;
		cts_field.textContent = errmsg ;
		to_ts_field.textContent = errmsg ; 
	}
}

function countdown(cts_field, to_ts_field) {
	var cntdwn = window.setInterval(function () {
        var cts     = get_timestamp() ;
		var to_ts   = awaited - cts

		cts_field.textContent = cts ;
		to_ts_field.textContent = to_ts ; 

		console.log(cts) ;
 
		if (to_ts <= 0) {
			party() ;
			clearInterval(cntdwn);
		}

	}, 500);
}

function get_date() {
	var date = new Date((get_timestamp()) * 1000) ;
	document.getElementById("date").textContent = "on "+ date ;
}

function get_timestamp() {
	return Date.now() / 1000 | 0 ;
}

function party() {
	document.body.innerHTML = '' ;

	var party_h1 = document.createElement ("h1") ;
	party_h1.textContent = "Merry Timestamp !" ;
	party_h1.setAttribute('class', 'bounce')
	document.body.appendChild (party_h1) ;
	new Audio('./party.mp3').play()
}