odoo.define('pos_products_gross_price.pos', function (require) {
    "use strict";

    var models = require('point_of_sale.models');
    var utils = require('web.utils');
    var round_di = utils.round_decimals;
    var round_pr = utils.round_precision;

    models.load_fields("product.product", [ "lst_price_gross" ]);

    var OrderlineModelSuper = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        set_unit_price: function (price) {
            this.order.assert_editable();
            var self = this;
            var price = round_di(parseFloat(price) || 0, 2);
            if (this.pos.config.iface_tax_included) {
                var taxes = this.get_taxes();
                var tax_amount = 0;
                _(taxes).each(function(tax) {
                    if (tax.amount_type == 'percent') {
                        tax_amount = price - price / ((100 + tax.amount) / 100);
                    }
                });

                this.price = price - tax_amount;
            }
            this.trigger('change', this);
        },
    });

});