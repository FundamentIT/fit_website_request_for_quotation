odoo.define('website_request_for_quotation.dialog', function (require) {
	'use strict';
	var ajax = require('web.ajax');

	$(document).ready(function(){
        $("body").on("click","#get_quote",function(){
		    $("#modal_get_quote").modal("show");
        });

		$('#getquote').click(function(){
            var is_public_user = $("div[id='is_public_user']").text();
            if (is_public_user == 'true'){
                console.log('public user, getquote click, is_public_user: '+is_public_user);
                var company = document.getElementById("company");
                var contact = document.getElementById("contact");
                var telephone = document.getElementById("telephone");
                var email = document.getElementById("email");
                var qty = document.getElementById("qty");
                const isValidCompany = company.checkValidity();
                const isValidContact = contact.checkValidity();
                const isValidTelephone = telephone.checkValidity();
                const isValidEmail = email.checkValidity();
                const isValidQty = qty.checkValidity();

                if (!isValidCompany || !isValidContact || !isValidTelephone || !isValidEmail || !isValidQty) {
                    console.log('Form not valid');
                    $("p[id='validation_error']").removeClass('o_hidden');
                    return false;
                }
            }
			var company = $("input[name='company']").val();
			var contact = $("input[name='contact']").val();
			var telephone = $("input[name='telephone']").val();
			var email = $("input[name='email']").val();
			var qty = $("input[name='qty']").val();
			var message = $("textarea[name='message']").val();
			var product = $("input[id=product_id]").val();
			ajax.jsonRpc('/quotation', 'call', {'company': company, 'contact': contact, 'telephone': telephone, 'email': email, 'qty': qty, 'message': message, 'product': product})
			return qty;
		});



	});
});
