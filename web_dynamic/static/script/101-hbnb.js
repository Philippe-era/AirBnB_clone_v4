$(document).ready(init);

const HOST_aPI = '0.0.0.0';
const amenity_obj_listect = {};
const state_obj_listect = {};
const city_obj_listect = {};
let obj_list = {};

function init () {
  $('.amenities .popover input').change(function () { obj_list = amenity_obj_listect; checkedObjects.call(this, 1); });
  $('.state_input').change(function () { obj_list = state_obj_listect; checkedObjects.call(this, 2); });
  $('.city_input').change(function () { obj_list = city_obj_listect; checkedObjects.call(this, 3); });
  apiStatus();
  searchPlaces();
  showReviews();
}

function checkedObjects (nObject) {
  if ($(this).is(':checked')) {
    obj_list[$(this).attr('data-name')] = $(this).attr('data-id');
  } else if ($(this).is(':not(:checked)')) {
    delete obj_list[$(this).attr('data-name')];
  }
  const names = Object.keys(obj_list);
  if (nObject === 1) {
    $('.amenities h4').text(names.sort().join(', '));
  } else if (nObject === 2) {
    $('.locations h4').text(names.sort().join(', '));
  }
}

function apiStatus () {
  const API_URL = `http://${HOST_aPI}:5001/api/v1/status/`;
  $.get(API_URL, (data, textStatus) => {
    if (textStatus === 'success' && data.status === 'OK') {
      $('#api_status').addClass('available');
    } else {
      $('#api_status').removeClass('available');
    }
  });
}

function searchPlaces () {
  const PLACES_URL = `http://${HOST_aPI}:5001/api/v1/places_search/`;
  $.ajax({
    url: PLACES_URL,
    type: 'POST',
    headers: { 'Content-Type': 'application/json' },
    data: JSON.stringify({
      amenities: Object.values(amenity_obj_listect),
      states: Object.values(state_obj_listect),
      cities: Object.values(city_obj_listect)
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
          '<div class="reviews"><h2>',
          `<span id="${r.id}n" class="treview">Reviews</span>`,
          `<span id="${r.id}" onclick="showReviews(this)">Show</span></h2>`,
          `<ul id="${r.id}r"></ul>`,
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

function showReviews (obj_list) {
  if (obj_list === undefined) {
    return;
  }
  if (obj_list.textContent === 'Show') {
    obj_list.textContent = 'Hide';
    $.get(`http://${HOST_aPI}:5001/api/v1/places/${obj_list.id}/reviews`, (data, textStatus) => {
      if (textStatus === 'success') {
        $(`#${obj_list.id}n`).html(data.length + ' Reviews');
        for (const review of data) {
          printReview(review, obj_list);
        }
      }
    });
  } else {
    obj_list.textContent = 'Show';
    $(`#${obj_list.id}n`).html('Reviews');
    $(`#${obj_list.id}r`).empty();
  }
}

function printReview (review, obj_list) {
  const date = new Date(review.created_at);
  const month = date.toLocaleString('en', { month: 'long' });
  const day = dateOrdinal(date.getDate());

  if (review.user_id) {
    $.get(`http://${HOST_aPI}:5001/api/v1/users/${review.user_id}`, (data, textStatus) => {
      if (textStatus === 'success') {
        $(`#${obj_list.id}r`).append(
          `<li><h3>From ${data.first_name} ${data.last_name} the ${day + ' ' + month + ' ' + date.getFullYear()}</h3>
          <p>${review.text}</p>
          </li>`);
      }
    });
  }
}

function dateOrdinal (dom) {
  if (dom === 31 || dom === 21 || dom === 1) return dom + 'st';
  else if (dom === 22 || dom === 2) return dom + 'nd';
  else if (dom === 23 || dom === 3) return dom + 'rd';
  else return dom + 'th';
}

