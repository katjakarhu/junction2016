document.addEventListener('DOMContentLoaded', function() {
  var stats;
  getCurrentDocumentOnSelectedTab(function(dom) {
    stats = JSON.parse(dom.getElementById('hapiStats').innerHTML);
  });
});

function getCurrentDocumentOnSelectedTab(callback) {
  chrome.tabs.getSelected(null, function(tab) {
    chrome.tabs.sendRequest(tab.id, {action: "getDOM"}, function(response) {
      callback(response.dom);
    });
  });
}