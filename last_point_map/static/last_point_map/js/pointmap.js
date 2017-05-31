window.addEventListener('map:init', function (e) {
    var detail = e.detail;
    var map = detail.map;

    var point_marker;
    var marker_icon = L.icon({
        iconUrl: icon_url,
        iconSize: [30, 40],
        iconAnchor: [20, 40],
        popupAnchor: []
    });
    var marker_settings = {
        draggable: false,
        icon: marker_icon
    };

    var default_coords = [51.0, 0.0];
    var default_zoom = 12;

    $.getJSON(
        '/get_recent',
        {},
        function (data) {
            var create_marker = function (latlng) {
                point_marker = new L.Marker(latlng, marker_settings);
                point_marker.addTo(map);
            };

            var point = JSON.parse(data[0].fields.point);
            console.log(point.coordinates);

            if (data && data.length > 0) {
                create_marker(point.coordinates.reverse());
                default_zoom = data[0].fields.zoom;
            } else {
                create_marker(default_coords);
            }

            map.setView(point_marker.getLatLng(), default_zoom);
        }
    );
}, false);

