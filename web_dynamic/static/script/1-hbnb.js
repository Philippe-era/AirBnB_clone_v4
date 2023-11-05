$(document).ready(init);

function init () {
  const object_amenity = {};
  $('.amenities .popover input').change(function () {
    if ($(this).is(':checked')) {
      object_amenity[$(this).attr('data-name')] = $(this).attr('data-id');
    } else if ($(this).is(':not(:checked)')) {
      delete object_amenity[$(this).attr('data-name')];
    }
    const amenity_name = Object.keys(object_amenity);
    $('.amenities h4').text(amenity_name.sort().join(', '));
  });
}



