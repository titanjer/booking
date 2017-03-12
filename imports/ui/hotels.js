import { Template } from 'meteor/templating';

import { Hotels } from '../api/hotels.js';
import './hotels.html';


Router.route('/', function(){
  this.render('Hotels');
});


Template.Hotels.helpers({
  hotels() {
    return Hotels.find({});
  }
});


Template.Hotels.events({});
