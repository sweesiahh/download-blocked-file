function craftUrl(url,) {
  return `https://download-blocked-file.onrender.com/?url=${url}&password=${password}`
}

function updateLink(url) {
  theLink = document.getElementById('link')
  theLink.href = url
  theLink.innerHTML = url
}

var urlElem = document.getElementById('inputField');
var passwordElem = document.getElementById('passwordField');
urlElem.addEventListener('keypress', function(e){
  if (e.keyCode == 13) {
    url = urlElem.value
    password = document.getElementById('passwordField');
    newUrl = craftUrl(url)
    updateLink(newUrl)
  }
}); 
