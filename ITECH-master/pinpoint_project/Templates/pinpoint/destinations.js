
			$(document).ready(function(){
				$("#search").on("keyup", function() {
					var value = $(this).val().toLowerCase();
					$("#destinations .card").filter(function() {
						$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
					});
				});
			});


		jQuery(document).ready(function($) {
			// <!--DROP DOWN - WORKIN-->
			$("#contselect").on('change', function() {
				var value = this.value;

				$("#destinations .card").filter(function() {
						$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
				});
			});

			// <!--TODO CLIMATE RADIO - workin (but searching all words)-->
			$(function climate() {
				$('input[name="climate"]').change(function() {
					var value = this.value;
					if (value == "none" ) {
					$("#destinations .card").toggle()
					}
					else {
					$("#destinations .card").filter(function() {
						$(this).toggle($(this).text().indexOf(value) > -1)
					});
					}
				});
			});

			// <!--BUDGET RADIO - WORKIN (had to add modifiers, so £££ techinically contains £-->
			// <!--TODO UPDATE DATABASE WITH MODIFIERS-->
			$(function budget() {
				$('input[name="budget"]').change(function() {
					var value = this.value;
					if (value == "none" ) {
					$("#destinations .card").toggle()
					}

					else {
					$("#destinations .card").filter(function() {
						$(this).toggle($(this).text().indexOf(value) > -1)
					});
					}
				});
			});

			// <!--ACTIVITIES CHECKBOX - NOT WORKIN -->
				$("#activities :checkbox").click(function() {

				   $("#activities :checkbox:checked").each(function() {
						var value = this.value;
					  $("#destinations .card").filter(function() {
						$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
						});
				   });
				});
		});

