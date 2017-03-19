window.addEventListener('map:init', function (e) {
    var detail = e.detail;
    var map = detail.map;

    var point_marker;
    var marker_icon = L.icon({
        iconUrl: icon_url,
        iconSize: [60, 70],
        iconAnchor: [34, 70],
        popupAnchor: []
    });
    var marker_settings = {
        draggable: true,
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

            if (data && data.length > 0) {
                create_marker([data[0].fields.lat, data[0].fields.lng]);
                default_zoom = data[0].fields.zoom;
            } else {
                create_marker(default_coords);
            }

            map.setView(point_marker.getLatLng(), default_zoom);
        }
    );

    map.on('click', function (f) {
        point_marker.setLatLng(f.latlng);
    })

    $('#save_pt_button').on('click', function () {
        var latlng;
        if (point_marker) {
            latlng = point_marker.getLatLng();
            $.getJSON('/submit',
                      {
                          lat: latlng.lat,
                          lng: latlng.lng,
                          zoom: map.getZoom()
                      }
                     );
            location.reload();
        }
    });

    $('#help-toggle').on('click', function () {
        $('#help').toggle({duration: 250});
    });
}, false);

