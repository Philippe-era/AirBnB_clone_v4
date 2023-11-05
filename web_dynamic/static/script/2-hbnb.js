$(document).ready(init);

const HOST_API = '0.0.0.0';

function init () {
  const amenity_object = {};
  $('.amenities .popover input').change(function () {
    if ($(this).is(':checked')) {
      amenity_object[$(this).attr('data-name')] = $(this).attr('data-id');
    } else if ($(this).is(':not(:checked)')) {
      delete amenity_object[$(this).attr('data-name')];
    }
    const names = Object.keys(amenity_object);
    $('.amenities h4').text(names.sort().join(', '));
  });

  apiStatus();
}

function apiStatus () {
  const API_URL = `http://${HOST_API}:5001/api/v1/status/`;
  $.get(API_URL, (data, textStatus) => {
    if (textStatus === 'success' && data.status === 'OK') {
      $('#api_status').addClass('available');
    } else {
      $('#api_status').removeClass('available');
    }
  });
}

