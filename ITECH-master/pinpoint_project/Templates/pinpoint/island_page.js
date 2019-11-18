src="//www.powr.io/powr.js?external-type=html"
src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"


    function ReturnIsland(number) {

        var island = 'noIsland';

        if (number  <= 13) {

            island = 'iceland';



        } else if (number  > 13 && number <= 16) {

            island = 'svalbard';



        } else if (number > 16 && number <= 19) {

            island = 'galapagos';



        } else if (number  > 19 && number <= 22) {

            island = 'mauritius';



        } else if (number  > 22 && number <= 25) {

            island = 'iceland';



        } else if (number  > 25 && number <= 28) {

            island = 'raja-ampat';



        } else if (number  > 28 && number <= 31) {

            island = 'st-lucia';



        } else if (number  > 31 && number <= 34) {

            island = 'sri-lanka';



        } else if (number  > 34 && number <= 37) {

            island = 'malta';



        } else if (number  > 37) {

            island = 'hong-kong';



        }

        var url = 'http://aisd9561.pythonanywhere.com/pinpoint/island_page/'+island;
        window.location.href = (url);
        return island;

    }




       function CheckIfFilled()

       {

           var music = document.querySelector("input[name=music ]:checked");

           var day = document.querySelector("input[name=day ]:checked");

           var sns = document.querySelector("input[name= sns]:checked");

           var food = document.querySelector("input[name=food ]:checked");

           var style = document.querySelector("input[name=style ]:checked");

           var movie = document.querySelector("input[name=movie ]:checked");

           var coffee = document.querySelector("input[name=coffee ]:checked");

           var animal = document.querySelector("input[name=animal ]:checked");

           var season = document.querySelector("input[name=season ]:checked");

           var date = document.querySelector("input[name=date ]:checked");



           if(music && day && sns && food && style && movie && coffee && animal && season && date) {

              $('button').click(function(){

                    var total =0;

                    $.each($("input[type = radio ]:checked"), function(){

                        total += parseFloat($(this).val());

                    });



                    ReturnIsland(total);

                });

           } else {

               alert("You missed a question! Please select an answer.");

           }



        }





