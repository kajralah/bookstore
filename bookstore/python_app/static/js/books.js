			 function getParameter(paramName) {
                var searchString = window.location.search.substring(1), i, val, params = searchString.split("&");

                for ( i = 0; i < params.length; i++) {
                    val = params[i].split("=");
                    if (val[0] == paramName) {
                        return val[1];
                    }
                }
                return null;
            }
            function getUrlData() {
                var parameter = getParameter("title");
				return parameter;	
            }

            function getBookInfo(){
				var parameter = getUrlData();
				$.post("http://localhost:8000/showProduct",{'title':parameter},
					function(data){
						var values = data.split(',');
                        $('#th').append("Info for book : "+values[0]);
                        $('#title').append(values[0]);
                        $('#price').append(values[1]);
                        $('#author').append(values[2]);
                        $('#pages').append(values[3]);
                        $('#publisher').append(values[4]);
                        $('#description').append(values[5]);
                        $('#category').append(values[6]);  
                        $('#image').append("<img src=\"/static/img/"+values[7]+"\" width=\"250\" height=\"250\" alt=\"\" style=\"display:block;\"/>");
				        $('#the_price').append(values[1]);
                        $('#transport').append('2.50');
                        var total = parseInt(values[1])+2.50;
                        $('#total').append(total);
                        $('#price').append(' BGN');
                        $('#transport').append(' BGN');
                        $('#the_price').append(' BGN');
                        $('#total').append(' BGN');
                });
			}

            function Like(){
                var category = $('#category').html();
                var title = $('#title').html();
                $.post("http://localhost:8000/likeProduct",{'category':category,'title':title},
                    function(data){
                        if(data === 'True'){
                            $('#likeInfo').append("Thank you for liking !");
                            $('#likeInfo').append("<a href=\"index.html\"> Back to homepage!</a>");
                        }
                        else{
                            $('#likeInfo').append("You have already liked it!");
                            $('#likeInfo').append("<a href=\"index.html\"> Back to homepage!</a>");
                        }
                    });
            }

        function Buy(){
            var title = $('#title').html();
            window.open("http://localhost:8000/buyBook?title="+title);
        }

        function buyBook(){
             var parameter = getUrlData();
             $.post("http://localhost:8000/buyProduct",{'title':parameter},
                    function(data){
                       if(data=='True'){
                            $('#buyButton').hide();
                            $('#result').append("You bought the item !")
                       }
                       else{
                            $('#buyButton').hide();
                            $('#result').append("Sorry,you cannot buy now! Contact with admin!");
                       }
                    }
                );
}