window.AudioContext = window.AudioContext || window.webkitAudioContext;
navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;

var s = document.getElementById('s');
var p = document.getElementById('p');
var timer;
var context = new AudioContext();
navigator.getUserMedia({audio: true}, function(stream) {

    //把要做的事情寫在這邊

}, function(){
  console.log('error');
});

var microphone = context.createMediaStreamSource(stream);
var analyser = context.createAnalyser();
microphone.connect(analyser);
analyser.connect(context.destination);

analyser.fftSize = 2048;
var bufferLength = analyser.frequencyBinCount;
var dataArray = new Uint8Array(analyser.fftSize);
//analyser.getByteFrequencyData(dataArray);

s.onclick = function(){
  clearTimeout(timer);
};

p.onclick = function(){
  update();
};

update();

function update(){
  console.log(dataArray);
  analyser.getByteFrequencyData(dataArray);
  timer = setTimeout(update,20);
}