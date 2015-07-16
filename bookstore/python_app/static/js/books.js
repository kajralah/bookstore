function get_parameter(paramName) {
    var searchString = window.location.search.substring(1), i, val, params = searchString.split("&");
    
    for (var i = 0; i < params.length; i++) {
        val = params[i].split("=");
        if (val[0] == paramName) {
            return val[1];
        }
    }
    return null;
}

function get_url_data() {
    var parameter = get_parameter("title");
    return parameter;
}

function get_book_info(){
    var parameter = get_url_data();
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
        }
    );
}

function is_user_logged(callback){
    $.post("http://localhost:8000/isLoggedUser/", {},
        function(data){
            callback(data);
        }
    );
}

function like(){            
    is_user_logged(function(data) {
        if(data ==='False'){
            alert('You\'re not logged in');
        }
        else{
            var category = $('#category').html();
            var title = $('#title').html();
            $.post("http://localhost:8000/likeProduct",{'category':category,'title':title},
                function(data){
                    if(data === 'True'){
                        $('#likeInfo').append("<div class=\"email_div\">")
                        $('#likeInfo').append("Thank you for liking !");
                        $('#likeInfo').append("Do you want to receive emails for new books in this category? ");
                        $('#likeInfo').append("<button onclick=\"enableEmails()\">Yes</button>");
                        $('#likeInfo').append("<button onclick=\"disableEmails()\">No</button>");
                        $('#likeInfo').append("</div>")
                        $('#likeInfo').append("<div class=\"result\"></div>")
                        $('#likeInfo').append("<a href=\"\index.html\"> Back to homepage!</a>");
                    }
                    else if (data==='False'){
                        $('#likeInfo').append("You have already liked it!");
                        $('#likeInfo').append("<a href=\"\index.html\"> Back to homepage!</a>");
                    }
                }
            );
        }           
    });
}

function go_to_home_page(){
    window.location.href = "/index.html";
}

function buy(){
        var title = $('#title').html();
        window.open("http://localhost:8000/buyBook?title="+title);
}

function buy_book(){
    $.post("http://localhost:8000/is_supervisor",{},
        function(data){
            if(data === 'False'){
                alert('You\'re not logged in');
                go_to_home_page();                     
            }
            else{
                buy_book_as_user();
            }
        }
    );
}

function buy_book_as_user(){
    var parameter = get_url_data();
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

function enable_emails(){
    $.post("http://localhost:8000/wantEmail",{'want_email':'T'},
        function(data){
            $('.result').append("Thanks!")
        }
    );
}

function disable_emails(){
    $.post("http://localhost:8000/wantEmail",{'want_email':'F'},
        function(data){
            $('.result').append("Thanks!")
        }     
    );
}