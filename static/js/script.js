$(document).ready(function () {
    // Sidebar and Submenu Toggle
    $(".menu > ul > li > a").click(function (e) {
        var $parentLi = $(this).parent(); // Get the parent li of the clicked link
        var hasSubMenu = $parentLi.find("ul").length > 0;

        // If there's a submenu, prevent default only for the submenu toggle
        if (hasSubMenu) {
            e.preventDefault(); // Prevent the default link behavior
            // Remove 'active' from all other sibling menu items
            $parentLi.siblings().removeClass("active").find("ul").slideUp();

            // Toggle 'active' on clicked item
            $parentLi.toggleClass("active");

            // Slide toggle the sub-menu if it exists
            $parentLi.find("ul").stop(true, true).slideToggle();

            // Close other sub-menus if any open
            $parentLi.siblings().find("ul").slideUp();
        }
    });

    // Sidebar Toggle Button
    $(".menu-btn").click(function () {
        $(".sidebar").toggleClass("active");
        $(".container").toggleClass("active");
    });

    // Auto-collapse the sidebar based on screen size
    function adjustSidebar() {
        if (window.innerWidth <= 768) {
            $(".sidebar").addClass("active");
            $(".container").addClass("active");
        } else {
            $(".sidebar").removeClass("active");
            $(".container").removeClass("active");
        }
    }

    // Call the function on page load
    adjustSidebar();

    // Adjust the sidebar on window resize
    $(window).resize(function () {
        adjustSidebar();
    });
});
$(".menu-btn").click(function () {
    $(".container").toggleClass("active");
});
