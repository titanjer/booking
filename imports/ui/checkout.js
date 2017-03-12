import { Template } from 'meteor/templating';

import { Hotels } from '../api/hotels.js';
import './checkout.html';


Router.route('/:id/checkout', function(){
  this.render('Checkout');
});


Template.Checkout.helpers({
  hotels() {
    return Hotels.find({});
  }
});


Template.Checkout.events({});
