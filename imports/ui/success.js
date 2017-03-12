import { Template } from 'meteor/templating';

import './success.html';


Router.route('/:id/success', function(){
  this.render('Success');
});


Template.Success.helpers({});


Template.Success.events({});
