odoo.define('delivery_options', function (require) {
    'use strict';

    var core = require('web.core');
    var AbstractAction =require('web.AbstractAction');

    var DeliveryOptions = AbstractAction.extend({
        _render: function () {
            console.log("Hello, world!");
        },
    });

    core.action_registry.add('delivery_options', DeliveryOptions);

    return DeliveryOptions;
});
