odoo.define('pos_products_gross_price.pos', function (require) {
    "use strict";

    var models = require('point_of_sale.models');

    models.load_fields("product.product", [ "lst_price_gross" ]);

});