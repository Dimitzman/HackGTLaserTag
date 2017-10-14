<script src="<path_to_js_files>/gyronorm.complete.min.js"></script>

<script type="text/javascript">
    var gn = new GyroNorm();
    var a = 0;
    var b = 0;
    var lat = 0;
    var long = 0;
    var xhr = new XMLHttpRequest(); // use this later

    gn.init().then(function(){
      gn.start(function(data){
        // Process:
        data.do.alpha;    // deviceorientation event alpha value
        data.do.beta;     // deviceorientation event beta value
      });
    }).catch(function(e){
      // Error if the browser doesn't support device orientation
    });

    function buttonClick() {
        getLocation();
        //TODO: Send location and orientation to server
    }

    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPostion(setPosition);
        } else {
            alert("Geolocation services not suppported by this browser version");
        }
    }

    function setPosition(position) {
        lat = position.coords.latitude;
        long = position.coords.longitude;
    }


</script>