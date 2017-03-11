import { Template } from 'meteor/templating';

import { Hotels } from '../api/hotels.js';
 
import './hotel.js';

import './body.html';


Template.body.helpers({
  hotels() {
    return Hotels.find({});
  }
});


Template.body.events({});
