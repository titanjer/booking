import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';

import { Hotels } from '../api/hotels.js';
import './checkout.html';


Router.route('/:id/checkout', function(){
  this.render('Checkout', {
    'data': { 
      'hotel': Hotels.findOne({id: this.params.id}),
      'state': new ReactiveDict()
    }
  });
});


Template.Checkout.helpers({
  shops() {
    if (Template.instance().data.hotel) {
      const hotel = Template.instance().data.hotel;
      let shops = []
      hotel.goods.forEach(function(good, index){
        let c = Template.instance().data.state.get(index.toString());
        if (c) {
          shops.push({name: good.name, counter: c});
        }
      });
      return shops;
    }
  }
});


Template.Checkout.events({
  'click .add-good'(event, instance) {
    let c = instance.data.state.get(event.target.id.toString());
    console.log(c);
    if (c == undefined)
      c = 0;
    instance.data.state.set(event.target.id.toString(), c + 1);
  }
});
