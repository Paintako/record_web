function add_request(){
   console.log("add");
   // var img = $("<a href = https://www.ptt.cc" + `${(obj[i]['href: '])}` +">").appendTo(json_pic);
   for(var i=1;i<4;i++){
      var container = $("<div class='web_container'></div>");
      var check = $("<input type='checkbox' class='checkpoint' name='ch'>");
      audio_name = '/AUDIO/'+`${i}`+'.mp3';
      var audio = $("<audio class='audio' src="+`${audio_name}`+" controls></audio>");
      var post_form = $("<form method='post'></form>");
      var inside_form = $("<input type='text' name='message' class='leavemessage'>");
      var inside_form2 = $("<input type='submit' name='submit' class='submit_btn'> value");
      var message_id = "第"+`${i}`+"則";
      var inside_form3 = $("<input type='hidden' name='message_id' value="+`${message_id}`+">");

      check.appendTo(container);
      inside_form.appendTo(post_form);
      inside_form2.appendTo(post_form);
      inside_form3.appendTo(post_form);
      audio.insertAfter(check);
      post_form.insertAfter(audio);
      $(".All_elements").before(container);
   }
   console.log("finished");
}
