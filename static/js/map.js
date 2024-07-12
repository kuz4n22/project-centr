ymaps.ready(init);

function init() {
  let map = new ymaps.Map('map', {
    center: [59.89076256268025,30.317270338730083],
    zoom: 17,
  });

  let placemark = new ymaps.Placemark([59.89076256268025,30.317270338730083], {}, {
    iconLayout: 'default#image',
    iconImageHref: 'https://cdn-icons-png.flaticon.com/512/5817/5817225.png',
    iconImageSize: [40, 40],
    iconImageOffset: [-20, -20],
  });

  map.geoObjects.add(placemark);
}