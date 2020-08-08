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

        $(".sort-button").click(function() {
            var id = this.id;
            var currentUrl = new URL(window.location)
            if( id == "price_desc"){
                var sort = "price";
                var direction = "desc";
            } else if( id == "price_asc"){
                var sort = "price";
                var direction = "asc";
            } else if( id == "name_desc"){
                var sort = "name";
                var direction = "desc";
            } else{
                var sort = "name";
                var direction = "asc";
            };
            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);
            window.location.replace(currentUrl);
        });
         $("#reset").click(function() {
                var currentUrl = new URL(window.location)
                currentUrl.searchParams.delete("sort");
                currentUrl.searchParams.delete("direction");
                window.location.replace(currentUrl);
                });