import { Template } from 'meteor/templating';

import { Hotels } from '../api/hotels.js';
import './hotel.html';


Router.route('/:id', function(){
  console.log(this.params.id);
  this.render('Hotel', {
    'data': () => Hotels.findOne({id: this.params.id })
  });
});


Template.Hotels.helpers({});


Template.Hotels.events({});
