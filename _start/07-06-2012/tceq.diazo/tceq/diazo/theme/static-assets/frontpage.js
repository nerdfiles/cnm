// JavaScript Document

<!-- for banner tabbed navigation menus -->
sfHover = function() {
var sfEls = document.getElementById("bannertabs").getElementsByTagName("LI");
  for (var i=0; i<sfEls.length; i++) {
  sfEls[i].onmouseover=function() {
  this.className+=" sfhover";
}
  sfEls[i].onmouseout=function() {
  this.className=this.className.replace(new RegExp(" sfhover\\b"), "");
 }
}
}
if (window.attachEvent) window.attachEvent("onload", sfHover);

<!-- for top navigation menus -->
sfHover = function() {
var sfEls = document.getElementById("navtoplinks").getElementsByTagName("LI");
  for (var i=0; i<sfEls.length; i++) {
  sfEls[i].onmouseover=function() {
  this.className+=" sfhover";
}
  sfEls[i].onmouseout=function() {
  this.className=this.className.replace(new RegExp(" sfhover\\b"), "");
 }
}
}
if (window.attachEvent) window.attachEvent("onload", sfHover);

<!-- for middle navigation menus -->
sfHover = function() {
var sfEls = document.getElementById("navmiddlelinks").getElementsByTagName("LI");
  for (var i=0; i<sfEls.length; i++) {
  sfEls[i].onmouseover=function() {
  this.className+=" sfhover";
}
  sfEls[i].onmouseout=function() {
  this.className=this.className.replace(new RegExp(" sfhover\\b"), "");
 }
}
}
if (window.attachEvent) window.attachEvent("onload", sfHover);
