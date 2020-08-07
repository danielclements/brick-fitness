        $(function() {
            var price_desc = $(".price_desc")
            var price_asc = $(".price_asc")
            var name_asc = $(".name_asc")
            var name_desc = $(".name_desc")
            var reset = $(".reset")
            var currentUrl = new URL(window.location);


            $(price_desc).click(function() {
                var sort = "price"; 
                var direction = "desc";
                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);

                window.location.replace(currentUrl);
                });
            
            $(price_asc).click(function() {
                var sort = "price";
                var direction = "asc";
                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);

                window.location.replace(currentUrl);
                });

            $(name_asc).click(function() {
                var sort = "name";
                var direction = "asc";
                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);

                window.location.replace(currentUrl);
                });

            $(name_desc).click(function() {
                var sort = "name";
                var direction = "desc";
                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);

                window.location.replace(currentUrl);
                });
            
            $(reset).click(function() {
                currentUrl.searchParams.delete("sort");
                currentUrl.searchParams.delete("direction");
                window.location.replace(currentUrl);
                });
            });

         $("#in-row-5").click(function() {
            $(this).addClass("in-row-active");
            $("#in-row-6").removeClass("in-row-active");
            $(".card-merch").addClass("card-in-row-5").removeClass("col-lg-2");
            });

        $("#in-row-6").click(function() {
            $(this).addClass("in-row-active");
            $("#in-row-5").removeClass("in-row-active");
            $(".card-merch").addClass("col-lg-2").removeClass("card-in-row-5");
            });
        
        $(function() {
            $(document).scroll(function() {
                var $nav = $(".merch-navbar");
                $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
            });
        });

        $(".color-button").click(function() {
            var color = this.id;
            var currentUrl = new URL(window.location)
            currentUrl.searchParams.set("color", color);
            window.location.replace(currentUrl);
        });