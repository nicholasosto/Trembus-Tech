from google.appengine.api import users

import webapp2
import pprint


f = open("test.html",'r')

webpage = "<!DOCTYPE html>
<html>
  <head>
    <title>Geolocation</title>
    <meta name=\"viewport\" content=\"initial-scale=1.0, user-scalable=no\">
    <meta charset=\"utf-8\">
    <style>
      html, body, #map-canvas {
        height: 100%;
        margin: 30px;
        padding: 20px
      }
    </style>
    <script src=\"https://maps.googleapis.com/maps/api/js?v=3.exp\"></script>

    <script>
// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see a blank space instead of the map, this
// is probably because you have denied permission for location sharing.

var map;

function initialize() {
  var mapOptions = {
    zoom: 6
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  // Try HTML5 geolocation
  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = new google.maps.LatLng(position.coords.latitude,
                                       position.coords.longitude);

      var infowindow = new google.maps.InfoWindow({
        map: map,
        position: pos,
        content: 'Lt: '+position.coords.latitude.toString().substring(0,4)+' Ln:'+position.coords.longitude.toString().substring(0, 6)
      });

      map.setCenter(pos);
    }, function() {
      handleNoGeolocation(true);
    });
  } else {
    // Browser doesn't support Geolocation
    handleNoGeolocation(false);
  }
}

function handleNoGeolocation(errorFlag) {
  if (errorFlag) {
    var content = 'Error: The Geolocation service failed.';
  } else {
    var content = 'Error: Your browser doesn\'t support geolocation.';
  }

  var options = {
    map: map,
    position: new google.maps.LatLng(60, 105),
    content: content
  };

  var infowindow = new google.maps.InfoWindow(options);
  map.setCenter(options.position);
}

google.maps.event.addDomListener(window, 'load', initialize);

    </script>
  </head>
  <body>
    <div id=\"map-canvas\"></div>
  </body>
</html>"

class MainPage(webapp2.RequestHandler):

    def get(self):
        # [START get_current_user]
        # Checks for active Google account session
        user = users.get_current_user()
        
        client_addy = self.response.body_file
        
        self.response.headers['HTTP_X_FORWARDED_FOR'] = 't-nine'
        # [END get_current_user]

        # [START if_user]
        if user:
        
            self.response.headers['Content-Type'] = 'text/HTML'

            self.response.write(f.read())
           # self.response.write(test.)
            
            #if user.nickname() == 'nicholas.osto':
            	
            	#self.response.write(f.read())
            	
            #else:
            
            	#self.response.write(f.read())
            
        # [END if_user]
        # [START if_not_user]
        
        else:
            self.redirect(users.create_login_url(self.request.uri))
        # [END if_not_user]
        
    def post(self):
	    self.response.write(self.response.headerlist)
    


application = webapp2.WSGIApplication([
    ('/', MainPage),('/pizzle', MainPage)
], debug=True)