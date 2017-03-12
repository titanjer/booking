import { Template } from 'meteor/templating';

import { Hotels } from '../api/hotels.js';
import './hotel.html';


Router.route('/:id', function(){
  const hotel = Hotels.findOne({id: this.params.id});
  console.log(hotel);

  this.render('Hotel', {
    'data': () => Hotels.findOne({id: this.params.id})
  });

  GoogleMaps.load({
    v: '3', 
    key: 'AIzaSyCP6PBwaDx7ePiSzPMCyAzh6IXMtfKQBkk', 
    libraries: 'geometry,places'
  });

  GoogleMaps.ready('souvenirs', (map) => {
    console.log('gg');
  });
});


Template.Hotel.helpers({
  souvenirsMapOptions: () => {
    if (GoogleMaps.loaded()) {
      const hotel = Template.instance().data;
      console.log(hotel.lat, hotel.lng);
      return {
        center: new google.maps.LatLng(hotel.lat, hotel.lng),
        zoom: 16
      }
    } 
  }
});


Template.Hotel.events({});
