function load_book(){
	var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('?');
    alert(sURLVariables[0]);
}