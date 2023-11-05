$(document).ready(init);

const HOST_API = '0.0.0.0';
const amenity_object = {};

function init () {
  $('.amenities .popover input').change(function () {
    if ($(this).is(':checked')) {
      amenity_object[$(this).attr('data-name')] = $(this).attr('data-id');
    } else if ($(this).is(':not(:checked)')) {
      delete amenity_object[$(this).attr('data-name')];
    }
    const amenity_list = Object.keys(amenity_object);
    $('.amenities h4').text(amenity_list.sort().join(', '));
  });

  apiStatus();
  searchPlacesAmenities();
}

function apiStatus () {
  const URL_API = `http://${HOST_API}:5001/api/v1/status/`;
  $.get(URL_API, (data, textStatus) => {
    if (textStatus === 'success' && data.status === 'OK') {
      $('#api_status').addClass('available');
    } else {
      $('#api_status').removeClass('available');
    }
  });
}

function searchPlacesAmenities () {
  const URL_PLACE = `http://${HOST_API}:5001/api/v1/places_search/`;
  $.ajax({
    url: URL_PLACE,
    type: 'POST',
    headers: { 'Content-Type': 'application/json' },
    data: JSON.stringify({ amenities: Object.values(amenity_object) }),
    success: function (response) {
      $('SECTION.places').empty();
      for (const r of response) {
        const article = ['<article>',
          '<div class="title_box">',
        `<h2>${r.name}</h2>`,
        `<div class="price_by_night">$${r.price_by_night}</div>`,
        '</div>',
        '<div class="information">',
        `<div class="max_guest">${r.max_guest} Guest(s)</div>`,
        `<div class="number_rooms">${r.number_rooms} Bedroom(s)</div>`,
        `<div class="number_bathrooms">${r.number_bathrooms} Bathroom(s)</div>`,
        '</div>',
        '<div class="description">',
        `${r.description}`,
        '</div>',
        '</article>'];
        $('SECTION.places').append(article.join(''));
      }
    },
    error: function (error) {
      console.log(error);
    }
  });
}

