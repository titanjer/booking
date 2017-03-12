import { Template } from 'meteor/templating';

import { Hotels } from '../api/hotels.js';
import './hotel.html';


Router.route('/:id', function(){
  const hotel = Hotels.findOne({id: this.params.id});

  this.render('Hotel', {
    'data': () => Hotels.findOne({id: this.params.id})
  });

  GoogleMaps.load({
    v: '3', 
    key: 'AIzaSyCP6PBwaDx7ePiSzPMCyAzh6IXMtfKQBkk', 
    libraries: 'geometry,places'
  });

  GoogleMaps.ready('souvenirs', (map) => {
    const marker = new google.maps.Marker({
      position: map.options.center,
      map: map.instance
    });
  });
});


Template.Hotel.helpers({
  souvenirsMapOptions: () => {
    if (GoogleMaps.loaded()) {
      const hotel = Template.instance().data;
      return {
        center: new google.maps.LatLng(hotel.lat, hotel.lng),
        zoom: 15
      }
    } 
  }
});


Template.Hotel.events({});
