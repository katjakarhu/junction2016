var props =  {
  apiBaseUrl: 'https://localhost:8000/fakenews?',
  numberOfUrlsPerRequest: 10,
  xhrTimeout: 5000
};

var hapiStats = {
  fakeSiteLinks: 0,
  hateSpeechLinks: 0
};

function startHapi() {
  var documentLinks = document.links;
  var storage =  {"linkStorage":[]};
  var chosenOnes = [];
  for (var i = 0; i < documentLinks.length; i++) {
    var currentLink = documentLinks[i];
    if (currentLink.href.startsWith('javascript') === false) {
      if (chosenOnes.length < getLimit()) {
        chosenOnes.push(currentLink);
      } else {
        storage.linkStorage.push(chosenOnes);
        chosenOnes = [];
      }
    }
  }

  alert(JSON.stringify(storage));
  sieveTheFakeAndTheHate(storage.linkStorage);
}

function getLimit() {
  return (props.numberOfUrlsPerRequest + 1);
}

function addLinksToChosenOnes(links) {
  chosenOnes.linkStorage.push(links);
}

function sieveTheFakeAndTheHate(storage) {
  for (var i = 0; i < storage.length; i++) {
    var currentStorage = storage[i];

    prepareApiCallUrl(currentStorage, function(apiCallUrl) {
      retrieveTheTruthFromTheTruthServer(apiCallUrl, function(theTruth) {
        if (!theTruth) {
          console.log("The truth.. there is none");
        } else {
          handleTheTruth(currentStorage, theTruth);
        }
      });
    });
  }
}

function retrieveTheTruthFromTheTruthServer(apiCallUrl,i, truthCall) {
  var xhr = new XMLHttpRequest();
  xhr.timeout = props.xhrTimeout;
  xhr.open('GET', apiCallUrl, true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        var theTruth = JSON.parse(xhr.responseText).response;
        truthCall(theTruth,i);
      } else {
        console.log('HapiError', xhr.statusText);
        truthCall(null,i);
      }
    }
  };
  xhr.ontimeout = function(e) {
    console.log('XMLHttpRequest timeout');
    truthCall(null,i);
  };

  xhr.send();
}

function handleTheTruth(toBeTheTruthOrNotToBe, theTruth) {
  console.log("HAHAA THE TRUUTH IS HIAR HARR HARR");
  for(var truthI = 0; truthI < theTruth.length; truthI++) {
    var currentTruth = theTruth[truthI];
    if (currentTruth.isFake === "true") {
      shameOnYouTheLink(toBeTheTruthOrNotToBe[truthI]);
    }
  }
}

function shameOnYouTheLink(shameLink) {
  console.log("LIIIES ALL LIEES: " + shameLink.href);
  var currentInnerHTML = shameLink.innerHTML
  shameLink.innerHTML = "<span class='warning'>" + currentInnerHTML + "</span>";
}

function prepareApiCallUrl(urls, callback) {
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

var callJson = {"calls":[]};

function protoHapi() {
  for (var i = 0; i < document.links.length; i++) {
    
    if (document.links[i].href.startsWith('javascript') === false) {
      var apiCallUrl = props.apiBaseUrl + "url=" + document.links[i].hostname + document.links[i].pathname;
      var insert = {"apiCallUrl": apiCallUrl, "linkIndex": i};
      callJson.calls.push(insert);
    }
  }

  alert(JSON.stringify(callJson));
  for (var i = 0; i < callJson.calls.length; i++) {
    retrieveTheTruthFromTheTruthServer(callJson.calls[i].apiCallUrl,i, function(truth,i) {
      if (truth) {
        console.log(JSON.stringify(truth));
        if (truth[0].isFake === "true") {
          console.log("Insert to index " + callJson.calls[i].linkIndex);
          var currentInnerHTML = document.links[callJson.calls[i].linkIndex].innerHTML
          document.links[callJson.calls[i].linkIndex].innerHTML = "<span class='hapi-warning'>" + currentInnerHTML + "</span>";
        }
      }
    });
  }
}

//document.body.onload = startHapi();
document.body.onload = protoHapi();