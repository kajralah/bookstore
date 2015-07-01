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
				});
			}

            // NEED TO FIX
            /*function Like(){
                var title = $('#category').html();
                $.post("http://localhost:8000/likeProduct",{'category':category},
                    function(data){
                      $('#body').empty();
                      window.location.load("index.html");
                });
            }*/