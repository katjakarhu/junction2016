var props =  {
  apiBaseUrl: 'http://localhost:8000/',
  numberOfUrlsPerRequest: 10,
  xhrTimeout: 5000
};

var hapiStats = {
  fakeSiteLinks: 0,
  hateSpeechLinks: 0
};

function startHapi() {
  var links = document.links;
  var urlsToBeChecked = [];
  for (var i = 0; i < links.length; i++) {

    if (urlsToBeChecked.length < 11) {
      urlsToBeChecked.push(links[i]);
      continue;
    }

    checkUrls(urlsToBeChecked, function (data) {
      response = JSON.parse(data);
      urlsToBeChecked = [];
      // Handle data from api
    });

    // var currentInnerHTML = links[i].innerHTML
    // links[i].innerHTML = "<span class='warning'>" + currentInnerHTML + "</span>";
  }
}

function checkUrls(urls, callback) {
  var xhr = new XMLHttpRequest();
  xhr.timeout = props.xhrTimeout;

  var apiCallUrl;
  prepareUrlParameters(urls, function(data) {
    apiCallUrl = data;

    xhr.open('GET', apiCallUrl, true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          var response = xhr.responseText;
          callback(response);
        } else {
          console.log('HapiError', xhr.statusText);
        }
      }
    };
    xhr.ontimeout = function(e) {
      console.log('XMLHttpRequest timeout');
    };

    xhr.send();
  }); 
}

function prepareUrlParameters(urls, callback) {
  var url = props.apiBaseUrl;

  for (var i = 0; i < urls.length; i++) {
    var hostName = urls[i].hostname;
    var pathName = urls[i].pathname;

    if (i != 0)
      url = url + "&";
    
    url = url + "url=" + hostName + pathName;
  }
  callback(url);
}

function insertStats() {
  var statsDiv = document.createElement('div');
  statsDiv.attr('id','hapiStats');
  statsDic.style.display = 'none';
  statsDiv.innerHTML = JSON.stringify(hapiStats);
  document.appendChild(statsDiv);
}

startHapi();