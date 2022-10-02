function add_request(){
   console.log("add");
   // var img = $("<a href = https://www.ptt.cc" + `${(obj[i]['href: '])}` +">").appendTo(json_pic);
   for(let i=1;i<4;i++){
      var container = $("<div class='audio_container'></div>");
      var check = $("<input type='checkbox' class='checkpoint' name='ch'>");
      //var audio = $("<audio class='audio' src='AUDIO/knocking_an_iron_door1.mp3' controls></audio>");
      var audio = $("<audio class='audio' src='AUDIO/"+`${i}`+".mp3 controls></audio>");
      audio.appendTo(check);
      check.appendTo(container);
      $(".web_container").append(container);
   }
   console.log("finished");
}

/*
 <p>段落11-1</p>
        <input type="checkbox" name="check1" class="checkpoint" name="ch">
        <audio class="audio" src="AUDIO/knocking_an_iron_door1.mp3" controls></audio>
        <form method="post">
            <input type="text" name="message" class="leavemessage">
            <input type="submit" name="submit1" class="submit_btn">
        </form>
*/