document.addEventListener('DOMContentLoaded', function() {
  var stats;
  getCurrentDocumentOnSelectedTab(function(dom) {
    stats = JSON.parse(dom.getElementById('hapiStats').innerHTML);
    document.getElementById('no-of-fakes').innerHTML = stats.fakeSiteLinks;
    document.getElementById('no-of-nc').innerHTML = stats.hateSpeechLinks;
  });
});

function getCurrentDocumentOnSelectedTab(callback) {
  chrome.tabs.getSelected(null, function(tab) {
    chrome.tabs.sendRequest(tab.id, {action: "getDOM"}, function(response) {
      callback(response.dom);
    });
  });
}