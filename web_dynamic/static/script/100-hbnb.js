$(document).ready(init);

const HOST_API = '0.0.0.0';
const amenity_obj_arrayect = {};
const state_obj_arrayect = {};
const cityObj = {};
let obj_array = {};

function init () {
  $('.amenities .popover input').change(function () { obj_array = amenity_obj_arrayect; checkedObjects.call(this, 1); });
  $('.state_input').change(function () { obj_array = state_obj_arrayect; checkedObjects.call(this, 2); });
  $('.city_input').change(function () { obj_array = cityObj; checkedObjects.call(this, 3); });
  apiStatus();
  searchPlaces();
}

function checkedObjects (nObject) {
  if ($(this).is(':checked')) {
    obj_array[$(this).attr('data-name')] = $(this).attr('data-id');
  } else if ($(this).is(':not(:checked)')) {
    delete obj_array[$(this).attr('data-name')];
  }
  const names = Object.keys(obj_array);
  if (nObject === 1) {
    $('.amenities h4').text(names.sort().join(', '));
  } else if (nObject === 2) {
    $('.locations h4').text(names.sort().join(', '));
  }
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

function searchPlaces () {
  const PLACES_URL = `http://${HOST_API}:5001/api/v1/places_search/`;
  $.ajax({
    url: PLACES_URL,
    type: 'POST',
    headers: { 'Content-Type': 'application/json' },
    data: JSON.stringify({
      amenities: Object.values(amenity_obj_arrayect),
      states: Object.values(state_obj_arrayect),
      cities: Object.values(cityObj)
    }),
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

