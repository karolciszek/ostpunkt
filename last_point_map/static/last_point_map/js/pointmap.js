window.addEventListener('map:init', function (e) {
    var detail = e.detail;
    var map = detail.map;

    var point_marker;
    var marker_settings = {
        draggable: true
    };

    var default_coords = [51.0, 0.0];
    var default_zoom = 13;

    var create_marker = function (latlng) {
        point_marker = new L.Marker(latlng, marker_settings);
    };

    $.getJSON(
        '/get_recent',
        {},
        function (data) {
            if (data && data.length > 0) {
                create_marker([data[0].fields.lat, data[0].fields.lng]);
            } else {
                create_marker(default_coords);
            }
            point_marker.addTo(map);
        }
    );
}, false);

