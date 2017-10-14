<script src="<path_to_js_files>/gyronorm.complete.min.js"></script>

<script type="text/javascript">
    var gn = new GyroNorm();
    var a = 0;
    var b = 0;
    var lat = 0;
    var long = 0;

    gn.init().then(function(){
      gn.start(function(data){
        // Process:
        a = data.do.alpha;    // deviceorientation event alpha value
        b = data.do.beta;     // deviceorientation event beta value
      });
    }).catch(function(e){
      // Error if the browser doesn't support device orientation
    });

    function getData() {
        var xmlReq = new XMLHttpRequest();

        function processReq(e) {
            if (xmlReq.readyState == 4) {
                var message = xmlReq.responseText;
                //Do something
            }
        }

        xmlReq.addEventListener("GETupdate", processReq);
        xmlReq.open("GET", /*"https://example.com/something"*/);
        xmlReq.onreadystatechange = processReq;

    }

    setInterval(getData, 1000);

    function buttonClick() {
        getLocation();
        //TODO: Send location and orientation to server
        function sendListener() {

        }

        var sendReq = new XMLHttpRequest();
        sendReq.addEventListener("sendingLocation", sendListener);
        sendReq.open("POST", /*"https://example.com/something"*/);
        sendReq.setRequestHeader("Alpha", a);
        sendReq.setRequestHeader("Beta", b);
        sendReq.setRequestHeader("Longitude", long);
        sendReq.setRequestHeader("Latitude", lat);
        sendReq.send();


    }

    function getLocation() {
        if (navigator.geolocation) { //Tests if the object exists
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