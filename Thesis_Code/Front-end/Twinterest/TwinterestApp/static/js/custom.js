


function get_color(){
      $.ajax({
            type: "GET",
            url: "color/",
            data: {},
            success: function(json){
                console.log("success color");
                console.log(json);
                var name = "#brand_dropdown_"+json;
                console.log(name);
                $(name).addClass("color_menu_option");
                $(".brand_name").html(json);


                
            }
        });

}


function get_categories(){
  console.log("in get_categories");
  $.ajax({
            type: "GET",
            url: "load/",
            data: {},
            success: function(json){
                console.log("success menu");
                for (i=json.length - 1; i > -1; i--){
                    $('#menuid').prepend("<li id='brand_dropdown_"+json[i]+"'><a name='dropdown' value='"+json[i]+"'><form action = '' method='get'><button class='dropdownbutton' name = 'dropdown' value = '"+json[i]+"'><i class='fa fa-at'></i>"+json[i]+"</button></form></a>");

                };
                get_color();
            }
        });
  

}

function appendToHtml(json, string, string2){
  $(string).empty()
  for (i=0; i < json.length; i++){
                
        html_func(json[i][0], json[i][1], string, string2);
            };
}

function appendToHtmlNoBio(json, string, string2){
  console.log("in html no bio");
  $(string).empty();


  var length = json.length;
  if (length > 6){ 
    length = 6;
  }
  for (i=0; i < length; i++){
                
        html_func(json[i], null, string, string2);
  };
}

function html_func(name, description, string, string2){

  var text = '';
  if (description != null){
    text = "<h5>"+description+"</h5><small><button type='button' data-toggle='modal' data-target='#myModal"+name+"' id='id"+name+"' value="+name+">Report an error</button></small>";
    var item = "#id"+name;
    var nameofprofession = '"'+$('#actualProfessions').val()+'"';
    var nameofinterest = '"'+$('#actualInterests').val()+'"';
  }
    $(string).prepend(
      "<div id='user"+name+"'><h4><li><a target='_blank' href='http://www.twitter.com/"+name+"'><strong>"+name+"</strong></a></li></h4>"+ text + "<small style='padding-left:10px;'><button type='button' data-toggle='modal' data-target='#myModal2"+name+"' id='flag"+name+"' value="+name+">Flag User</button></small>");
                
                var item2 = "#flag"+name;
                var nameofuser = '"'+name+'"';
                
                $(string2).prepend(
                    "<div class='modal fade' id='myModal"+name+"' tabindex='-1; role='dialog' aria-labelledby='myModalLabel'>"+
                    "<div class='modal-dialog' role='document'>"+
                    "<div class='modal-content'>" +
                      "<div class='modal-header'>" +
                        "<button type='button' class='close' data-dismiss='modal' aria-label='Close'><span aria-hidden='true'>&times;</span></button>" +
                        "<h4 class='modal-title' id='myModalLabel"+name+"'>Correct the classification of "+$(item).val()+"</h4>"+
                      "</div>" +
                      "<div class='modal-body' id='myModalBody"+name+"'>"+
                       "<h5>Actual Top Interest:</h5>   <fieldset class='form-group'>"+

                        "<select class='form-control' id='actualInterests"+name+"'>"+
                          "<option value='Unknown'>Unknown</option>"+
                          "<option value='Music'>Music</option>"+
                          "<option value='Fashion/Beauty'>Fashion &amp; Beauty</option>"+
                          "<option value='Gaming'>Gaming</option>"+
                          "<option value='Food'>Food</option>"+
                          "<option value='Tech'>Technology &amp; Science</option>"+
                          "<option value='Biz'>Business &amp; Finance</option>"+
                          "<option value='Politics'>News &amp; Politics</option>"+
                          "<option value='Arts/Culture'>Arts &amp; Culture</option>"+
                          "<option value='Sports/Fitness'>Sports &amp; Fitness</option>"+

                          
                        "</select>"+
                      "</fieldset>"+
                       "<h5>Actual Influence Category:</h5> <fieldset class='form-group'>"+
                        
                        "<select class='form-control' id='actualProfessions"+name+"'>"+
                          "<option value='casual_user'>Casual User</option>"+
                          "<option value='business_expert'>Business Expert</option>"+
                          "<option value='celebrity'>Celebrity</option>"+
                          "<option value='writer'>Writer or Journalist</option>"+
                          "<option value='youtuber'>Youtuber</option>"+
                          "<option value='brand_corp'>Brand or Corporation</option>"+
                          "<option value='academic'>Academic</option>"+
                          
                        "</select>"+
                      "</fieldset>"+
                      "</div>"+
                      "<div class='modal-footer' id='myModalFooter" +name+"'>"+
                        "<button type='button' style='background-color:#302782; outline-color: #302782;' class='btn btn-primary' onclick='report(username="+nameofuser+")' value="+name+">Submit</button>"+
                      "</div>"+
                    "</div>"+
                    "</div>"+
                    "</div>"+


                    "<div class='modal fade' id='myModal2"+name+"' tabindex='-1; role='dialog' aria-labelledby='myModalLabel2'>"+
                    "<div class='modal-dialog' role='document'>"+
                    "<div class='modal-content'>" +
                      "<div class='modal-header'>" +
                        "<button type='button' class='close' data-dismiss='modal' aria-label='Close'><span aria-hidden='true'>&times;</span></button>" +
                        "<h4 class='modal-title' id='myModalLabel2"+name+"'>Flag "+$(item2).val()+" as inappropriate user?</h4>"+
                      "</div>" +
        
                      "<div class='modal-footer' id='myModalFooter2" +name+"'>"+
                        "<button type='button' class='btn btn-primary' style='background-color:#302782; outline-color: #302782;' onclick='flag(username="+nameofuser+")' value="+name+">Flag</button>"+
                        "<button type='button' class='btn btn-default' data-dismiss='modal'>Close</button>"+
                      "</div>"+
                    "</div>"+
                    "</div>"+
                    "</div>"
                    );  
              
}
function get_usernames() {
    $('#list').empty()
    $.ajax({
        type:"GET",
        url: "get_usernames/",
        data: {number: $('#num').val(), interest: $('#interests').val(), profession: $('#professions').val()},

        success: function(json){
            console.log(json);
            appendToHtml(json, "#list", "#listdiv");
            //$("#errorReport").click(function(){
            //    console.log('report submitted');
             //   console.log($('#errorReport').val())
                //report(username=, profession, interest);
            //})
                
            
            console.log(json);
            console.log("success");
        }
        
    });
    console.log("after ajax");
};

function flag(username){
    console.log("flag detected");
    console.log(username)
    $.ajax({
        type: "GET",
        url: "flag/",
        data: {name: username},

        success: function(json){
            $('#myModalLabel2' + username).html("Thank you, your response has been saved!");
            $('#myModalFooter2' + username).html("<button type='button' class='btn btn-default' data-dismiss='modal'>Close</button>");
            var userdiv = "#user"+json;
            $(userdiv).empty();
      }
    })
}

function report(username) {
    console.log("report detected");

    console.log(username);
    var realProf = $('#actualProfessions' + username).val();
    var realInt = $('#actualInterests' + username).val();

    $.ajax({
        type: "GET",
        url: "report/",
        data: {name: username, profession: realProf, interest: realInt },

        success: function(json){
            console.log("success2");
            $('#myModalLabel' + username).html("Thank You!");
            $('#myModalBody' + username).html(json);
            $('#myModalFooter' + username).html("<button type='button' class='btn btn-default' data-dismiss='modal'>Close</button>");
            var userdiv = "#user"+username;
            $(userdiv).empty();


        }

    })


};