<script src="<path_to_js_files>/gyronorm.complete.min.js"></script>

<script type="text/javascript">
    var gn = new GyroNorm();
    var a = 0;
    var b = 0;

    gn.init().then(function(){
      gn.start(function(data){
        // Process:
        data.do.alpha;    // deviceorientation event alpha value
        data.do.beta;     // deviceorientation event beta value
      });
    }).catch(function(e){
      // Error if the browser doesn't support device orientation
    });

</script>