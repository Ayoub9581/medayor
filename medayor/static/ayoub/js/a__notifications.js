$(document).ready(function () {

	$('.form-contact').on('submit', function () {
		var form = $(this);
		fd = new FormData(form[0]);
		$.ajax({
		//	console.log(' here ')
			url: form.attr('acion'),
			data: fd,
			type: form.attr('method'),
			dataType: 'json',
			processData: false,
			contentType: false,
			success: function (data) {
				if (data.form_is_valid) {
				      console.log('True');
				} else {
					console.log('False');
				}
			}
		})
		return false;
	}
});
